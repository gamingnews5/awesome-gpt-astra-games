import json,subprocess,time
PH=["Claude Opus 5.5","Opus 5.5","Claude Sonnet 5.5","Sonnet 5.5","GPT-6.1 Sol","GPT-6.1","GPT-6 Astra","Claude Fable","Gemini 4 Argon","Gemini 4","Fable 5","Opus-5.5","made with Claude"]
PARTS=["2026-10-24T01:00:00Z..2026-10-24T12:59:59Z","2026-10-24T13:00:00Z..2026-10-25T01:00:00Z"]
out=open('repo-searches.jsonl','w');log=[]
for ph in PH:
  for p in PARTS:
    q=f'"{ph}" created:{p}'
    items=[];total=0
    for page in (1,2):
      r=subprocess.run(['gh','api','-X','GET','search/repositories','-f',f'q={q}','-f','per_page=100','-f',f'page={page}'],capture_output=True,text=True)
      if r.returncode: print('ERR',q,r.stderr[:200]); time.sleep(20); continue
      d=json.loads(r.stdout); total=d['total_count']; items+=d['items']
      if len(items)>=total: break
      time.sleep(2.5)
    log.append(dict(query=q,hits=total,fetched=len(items),capped=total>len(items)))
    for it in items: out.write(json.dumps(dict(q=q,full_name=it['full_name'],desc=it['description'],created=it['created_at'],fork=it['fork'],topics=it.get('topics'),homepage=it['homepage'],lang=it['language'],id=it['id'],stars=it['stargazers_count']))+'\n')
    print(q,total,flush=True); time.sleep(2.5)
json.dump(log,open('repo-query-log.json','w'),indent=1)
