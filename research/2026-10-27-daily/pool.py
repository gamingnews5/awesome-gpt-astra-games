# Build today's fresh pool: commit+repo search hits, non-fork, minus games.json and every earlier decision.
import json,glob
games={g['github_url'].lower().replace('https://github.com/','') for g in json.load(open('../../games.json'))}
prev=set()
for f in glob.glob('../*/manual-decisions.json')+glob.glob('../*/*/manual-decisions.json')+glob.glob('../*/auto-rejects.json')+glob.glob('../*/*/auto-rejects.json')+glob.glob('../*/candidate-decisions.json'):
  try: d=json.load(open(f))
  except Exception: continue
  ks=d.keys() if isinstance(d,dict) else [x.get('repo') or x.get('full_name') or x.get('repository') for x in d if isinstance(x,dict)]
  prev|={str(k).lower().replace('https://github.com/','') for k in ks if k}
seen=[];S=set()
for l in open('commit-searches.jsonl'):
  x=json.loads(l)
  if x['fork']: continue
  r=x['repo']
  if r.lower() not in S: S.add(r.lower()); seen.append(r)
for l in open('repo-searches.jsonl'):
  x=json.loads(l)
  if x['fork']: continue
  r=x['full_name']
  if r.lower() not in S: S.add(r.lower()); seen.append(r)
pool=[r for r in seen if r.lower() not in games and r.lower() not in prev and r.lower()!='gamingnews5/awesome-opus-5.5-games' and not r.lower().startswith(('gamingnews5/','aigamedevs/','agentsloop/','grootbot-dev/','searchdot1/','denaidark/'))]
open('fresh-pool.txt','w').write('\n'.join(pool)+'\n'); print('unique',len(seen),'pool',len(pool),'prev',len(prev))
