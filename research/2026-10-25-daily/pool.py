import json,subprocess
known={g['github_url'].casefold().rstrip('/') for g in json.load(open('../../games.json'))}
prev=set()
for d in ('2026-10-16-daily','2026-10-17-daily','2026-10-21-daily','2026-10-23-daily'):
  p=json.load(open(f'../{d}/candidate-decisions.json'))
  prev|={k.lower() for k in list(p['held'])+list(p['rejected'])+p['accepted']}
pool={}
for l in [x for f in ('commit-searches.jsonl',) for x in open(f)]:
  try: d=json.loads(l)
  except Exception: continue
  if d['fork']: continue
  pool.setdefault(d['repo'],[]).append(d)
for l in [x for f in ('repo-searches.jsonl',) for x in open(f)]:
  try: d=json.loads(l)
  except Exception: continue
  if d['fork']: continue
  pool.setdefault(d['full_name'],[]).append(dict(q=d['q'],sha=None,msg=(d['desc'] or '')))
repos=[r for r in pool if ('https://github.com/'+r).casefold() not in known and r.lower() not in prev and not r.startswith('TheClockwyrks/')]
print('pool',len(pool),'unknown',len(repos))
meta={}
for i in range(0,len(repos),50):
  chunk=repos[i:i+50]; parts=[]
  for j,r in enumerate(chunk):
    o,n=r.split('/',1)
    parts.append(f'r{j}: repository(owner:{json.dumps(o)}, name:{json.dumps(n)}){{nameWithOwner createdAt isFork description homepageUrl databaseId stargazerCount primaryLanguage{{name}} defaultBranchRef{{name}}}}')
  q='query{'+' '.join(parts)+'}'
  res=subprocess.run(['gh','api','graphql','-f',f'query={q}'],capture_output=True,text=True)
  d=json.loads(res.stdout or '{}').get('data') or {}
  for j,r in enumerate(chunk):
    v=d.get(f'r{j}')
    if v: meta[r]=v
json.dump(meta,open('commit-pool-meta.json','w'),indent=1)
fresh={r:v for r,v in meta.items() if v['createdAt']>='2026-10-22T01:00:00Z' and not v['isFork']}
json.dump({r:dict(meta=fresh[r],commits=[dict(sha=c['sha'],msg=c['msg'][:300],q=c['q']) for c in pool[r]]) for r in fresh},open('commit-pool-fresh.json','w'),indent=1)
open('pool-fresh.txt','w').write('\n'.join(sorted(fresh,key=lambda r:fresh[r]['createdAt'])))
print('fresh',len(fresh))
