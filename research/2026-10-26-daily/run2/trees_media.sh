# usage: trees_media.sh BATCH  -> trees for accepted (via gh-read), media-live, contact sheets
set -e; B=$1
python3 - $B <<'P'
import json,sys,re,os
from concurrent.futures import ThreadPoolExecutor
from ghr import get
B=sys.argv[1]; ins=json.load(open('inspect.json')); trees=json.load(open('trees-acc.json')) if os.path.exists('trees-acc.json') else {}
acc=[l.strip() for l in open(f'accept-{B}.txt') if l.strip()]
def one(r):
  br=ins[r]['branch']; t=get(f"/repos/{r}/git/trees/{br}?recursive=1") or {}
  ents=t.get('tree',[]); files=[(e['path'],e.get('size',0)) for e in ents if e['type']=='blob']
  code=[(f,s) for f,s in files if re.search(r'\.(html?|js|mjs|ts|tsx|jsx|gd|cs|java|rs|py|swift|lua|luau|kt|cpp|c|h|qml|php|svelte|vue|dart|go|bas|asm|s|sh)$',f,re.I) and not re.search(r'node_modules|vendor/|\.min\.|dist/|build/|test',f)]
  code.sort(key=lambda x:-x[1])
  imgs=[f for f,s in files if re.search(r'(?i)\.(png|jpe?g|webp|gif)$',f) and re.search(r'(?i)screen|shot|preview|gameplay|capture|demo|docs?/|media/|img/|images/',f) and not re.search(r'(?i)icon|logo|favicon|sprite|tile|font|texture|node_modules',f)]
  ins[r]['tree']=[e['path']+('/' if e['type']=='tree' else '') for e in ents if '/' not in e['path']]
  return r,dict(root=ins[r]['tree'],branch=br,nfiles=len(files),code_bytes=sum(s for _,s in code),top=code[:6],shots=imgs[:12],truncated=t.get('truncated',False))
with ThreadPoolExecutor(12) as ex:
  for r,v in ex.map(one,[r for r in acc if r not in trees]): trees[r]=v
json.dump(trees,open('trees-acc.json','w')); print('trees',len(acc))
P
python3 media_live.py accept-$B.txt media-live.json
python3 mk2.py $B
