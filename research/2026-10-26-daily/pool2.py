import json,subprocess,glob,os
known={g['github_url'].casefold().rstrip('/') for g in json.load(open('../../games.json'))}
prev=set()
for f in glob.glob('../*/candidate-decisions.json'):
  try: p=json.load(open(f))
  except Exception: continue
  for k in ('held','rejected','accepted'):
    v=p.get(k) or []
    prev|={x.lower() for x in (v if isinstance(v,list) else v.keys())}
for f in ('../2026-10-25-daily/inspect.json','../2026-10-25-daily/manual-decisions.json','../2026-10-25-daily/auto-rejects.json'):
  prev|={k.lower() for k in json.load(open(f))}
pool={}
for l in open('commit-searches.jsonl'):
  try: d=json.loads(l)
  except Exception: continue
  if d['fork']: continue
  pool.setdefault(d['repo'],[]).append(d)
for l in open('repo-searches.jsonl'):
  try: d=json.loads(l)
  except Exception: continue
  if d['fork']: continue
  pool.setdefault(d['full_name'],[]).append(dict(q=d['q'],sha=None,msg=(d['desc'] or '')))
import re
PAT=re.compile(r'(?i)claude[ -]opus[ -]5\.5|opus[ -]5\.5|sonnet[ -]5\.5|fable[ -]5|claude[ -]fable|gpt-?6\.1[ -]?sol|gpt-?6[ -]astra|gemini[ -]4[ -]argon')
def tr(cs): return any(c['sha'] is None or any(l.strip().lower().startswith('co-authored-by') and PAT.search(l) for l in c['msg'].splitlines()) for c in cs)
repos=[r for r in pool if tr(pool[r]) and ('https://github.com/'+r).casefold() not in known and r.lower() not in prev]
print('pool',len(pool),'unknown',len(repos))
meta={}
def job(i):
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
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(6) as ex: list(ex.map(job,range(0,len(repos),50)))
json.dump(meta,open('commit-pool-meta.json','w'),indent=1)
fresh={r:v for r,v in meta.items() if v['createdAt']>='2026-10-23T01:00:00Z' and not v['isFork']}
json.dump({r:dict(meta=fresh[r],commits=[dict(sha=c['sha'],msg=c['msg'][:300],q=c['q']) for c in pool[r]]) for r in fresh},open('commit-pool-fresh.json','w'),indent=1)
open('pool-fresh.txt','w').write('\n'.join(sorted(fresh,key=lambda r:fresh[r]['createdAt'])))
print('fresh',len(fresh))
