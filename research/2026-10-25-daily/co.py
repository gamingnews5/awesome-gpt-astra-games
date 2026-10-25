import json,re
fresh=json.load(open('commit-pool-fresh.json'))
PAT=re.compile(r'(?i)claude[ -]opus[ -]5\.5|opus[ -]5\.5|sonnet[ -]5\.5|fable[ -]5|claude[ -]fable|gpt-?6\.1[ -]?sol|gpt-?6[ -]astra|gemini[ -]4[ -]argon')
out=[]
for r,v in fresh.items():
  ok=False
  for c in v['commits']:
    if c['sha'] is None: ok=True; break
    for line in c['msg'].splitlines():
      if line.strip().lower().startswith('co-authored-by') and PAT.search(line): ok=True
  if ok: out.append(r)
open('pool-co.txt','w').write('\n'.join(out)+'\n'); print(len(fresh),len(out))
