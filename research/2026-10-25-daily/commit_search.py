import json,subprocess,time
def wins(hours):
  import datetime as dt
  s=dt.datetime(2026,10,24,1,0,0); e=dt.datetime(2026,10,25,1,0,0); W=[]
  while s<e:
    t=s+dt.timedelta(minutes=int(hours*60))-dt.timedelta(seconds=1)
    W.append(f"{s:%Y-%m-%dT%H:%M:%S}Z..{t:%Y-%m-%dT%H:%M:%S}Z"); s+=dt.timedelta(minutes=int(hours*60))
  return W
M=[("Opus 5.5",0.5),("Sonnet 5.5",3),("gpt-6.1-sol",6),("GPT-6 Astra",6),("Claude Fable",6),("Gemini 4 Argon",6),("Gemini 4",6)]
out=open('commit-searches.jsonl','w');log=[]
for m,h in M:
  for w in wins(h):
    q=f'"{m}" game committer-date:{w}'
    total=0;n=0
    for page in ((1,2) if m=='Opus 5.5' else (1,2,3)):
      for attempt in range(4):
        r=subprocess.run(['gh','api','-X','GET','search/commits','-f',f'q={q}','-f','per_page=100','-f',f'page={page}'],capture_output=True,text=True)
        if r.returncode==0: break
        print('ERR',q,page,r.stderr[:150],flush=True); time.sleep(45)
      if r.returncode: break
      d=json.loads(r.stdout); total=d['total_count']
      for it in d['items']:
        n+=1; out.write(json.dumps(dict(q=q,repo=it['repository']['full_name'],fork=it['repository']['fork'],sha=it['sha'],msg=it['commit']['message'][:600]))+'\n')
      time.sleep(2.3)
      if n>=total or len(d['items'])<100: break
    log.append(dict(query=q,hits=total,fetched=n,capped=total>n))
    out.flush(); print(q,total,n,flush=True)
json.dump(log,open('commit-query-log.json','w'),indent=1)
