import json,subprocess,time,datetime as dt
def wins(s,e,hours):
  W=[]
  while s<e:
    t=s+dt.timedelta(minutes=int(hours*60))-dt.timedelta(seconds=1)
    W.append(f"{s:%Y-%m-%dT%H:%M:%S}Z..{t:%Y-%m-%dT%H:%M:%S}Z"); s+=dt.timedelta(minutes=int(hours*60))
  return W
E=dt.datetime(2026,10,26,1,0,0)
M=[("Opus 5.5",0.5,dt.datetime(2026,10,24,20,0,0)),("Sonnet 5.5",3,dt.datetime(2026,10,24,1)),("gpt-6.1-sol",6,dt.datetime(2026,10,24,1)),("GPT-6 Astra",6,dt.datetime(2026,10,24,1)),("Claude Fable",6,dt.datetime(2026,10,24,1)),("Gemini 4 Argon",6,dt.datetime(2026,10,24,1)),("Gemini 4",6,dt.datetime(2026,10,24,1))]
out=open('commit-searches.jsonl','a');log=[]
for m,h,s in M:
  for w in wins(s,E,h):
    q=f'"{m}" game committer-date:{w}'
    total=0;n=0
    for page in ((1,2) if m=='Opus 5.5' else (1,2,3)):
      for attempt in range(4):
        r=subprocess.run(['gh','api','-X','GET','search/commits','-f',f'q={q}','-f','per_page=100','-f',f'page={page}'],capture_output=True,text=True)
        if r.returncode==0: break
        print('ERR',q,page,r.stderr[:150],flush=True)
        if 'suspended' in r.stderr or 'Bad credentials' in r.stderr: raise SystemExit('AUTH FAIL')
        time.sleep(45)
      if r.returncode: break
      d=json.loads(r.stdout); total=d['total_count']
      for it in d['items']:
        n+=1; out.write(json.dumps(dict(q=q,repo=it['repository']['full_name'],fork=it['repository']['fork'],sha=it['sha'],msg=it['commit']['message'][:600]))+'\n')
      time.sleep(2.3)
      if n>=total or len(d['items'])<100: break
    log.append(dict(query=q,hits=total,fetched=n,capped=total>n))
    out.flush(); json.dump(log,open('commit-query-log.json','w'),indent=1); print(q,total,n,flush=True)
json.dump(log,open('commit-query-log.json','w'),indent=1)
print('DONE')
