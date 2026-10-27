# Fresh commit + repo search 2026-10-26T07:00Z..2026-10-27T01:00Z via gh-read (since the previous pass ended at 07:00Z).
import json,datetime as dt,time
from urllib.parse import quote
from ghr import get
def wins(s,e,h):
  W=[]
  while s<e:
    t=s+dt.timedelta(minutes=int(h*60))-dt.timedelta(seconds=1); W.append(f"{s:%Y-%m-%dT%H:%M:%S}Z..{t:%Y-%m-%dT%H:%M:%S}Z"); s+=dt.timedelta(minutes=int(h*60))
  return W
S=dt.datetime(2026,10,26,7); E=dt.datetime(2026,10,27,1)
M=[("Opus 5.5",0.5),("Sonnet 5.5",2),("gpt-6.1-sol",6),("GPT-6.1 Sol",6),("GPT-6 Astra",6),("Claude Fable",6),("Fable 5.1",6),("Gemini 4 Argon",6),("Gemini 4",6)]
import threading,os
from concurrent.futures import ThreadPoolExecutor
done={}
if os.path.exists('commit-searches.jsonl'):
  for l in open('commit-searches.jsonl'): done.setdefault(json.loads(l)['q'],0); done[json.loads(l)['q']]+=1
out=open('commit-searches.jsonl','a'); log=[]; L=threading.Lock()
def run(q):
  total=0; n=0; rows=[]
  for page in (1,2,3):
    d=get(f'/search/commits?q={quote(q)}&per_page=100&page={page}')
    if not d or 'items' not in d: print('ERR',q,page,flush=True); break
    total=d['total_count']
    for it in d['items']:
      n+=1; rows.append(json.dumps(dict(q=q,repo=it['repository']['full_name'],fork=it['repository']['fork'],sha=it['sha'],msg=it['commit']['message'][:600])))
    if n>=total or len(d['items'])<100 or n>=1000: break
  with L:
    for x in rows: out.write(x+'\n')
    out.flush(); log.append(dict(query=q,hits=total,fetched=n,capped=total>n)); print(q,total,n,flush=True)
Q=[f'"{m}" game committer-date:{w}' for m,h in M for w in wins(S,E,h)]
Q=[q for q in Q if q not in done]
with ThreadPoolExecutor(6) as ex: list(ex.map(run,Q))
json.dump(log,open('commit-query-log.json','w'),indent=1)
PH=["Claude Opus 5.5","Opus 5.5","Claude Sonnet 5.5","Sonnet 5.5","GPT-6.1 Sol","GPT-6 Astra","Claude Fable","Gemini 4 Argon","Fable 5","made with Claude"]
ro=open('repo-searches.jsonl','w'); rl=[]
for ph in PH:
  q=f'"{ph}" created:2026-10-26T07:00:00Z..2026-10-27T01:00:00Z'
  d=get(f'/search/repositories?q={quote(q)}&per_page=100') or {}
  items=d.get('items',[]); total=d.get('total_count',0)
  rl.append(dict(query=q,hits=total,fetched=len(items),capped=total>len(items)))
  for it in items: ro.write(json.dumps(dict(q=q,full_name=it['full_name'],desc=it['description'],created=it['created_at'],fork=it['fork']))+'\n')
  print(q,total,flush=True)
json.dump(rl,open('repo-query-log.json','w'),indent=1); print('DONE')
