# Record manual review decisions for one batch: python3 decide.py BATCH "accept indices"
import json,sys,os
b=sys.argv[1]; acc={int(x) for x in sys.argv[2].split()}
lines=[l.split(' ',2) for l in open(f'review-{b}.txt') if l.strip()]
f='manual-decisions.json'
d=json.load(open(f)) if os.path.exists(f) else {}
for k,r,_ in lines: d[r]=dict(batch=b,decision='accept' if int(k) in acc else 'reject')
json.dump(d,open(f,'w'),indent=1)
a=[r for k,r,_ in lines if int(k) in acc]
open(f'accept-{b}.txt','w').write('\n'.join(a)+'\n'); print(len(lines),'accepted',len(a))
