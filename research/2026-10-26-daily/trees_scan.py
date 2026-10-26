import json,subprocess,re,sys
from concurrent.futures import ThreadPoolExecutor
d=json.load(open('inspect.json'))
repos=list(dict.fromkeys(l.strip() for l in open(sys.argv[1]) if l.strip()))
outp=sys.argv[2]
try: out=json.load(open(outp))
except Exception: out={}
def one(r):
  br=(d.get(r) or {}).get('branch') or 'HEAD'
  p=subprocess.run(['gh','api',f'repos/{r}/git/trees/{br}?recursive=1'],capture_output=True,text=True)
  try: t=json.loads(p.stdout)
  except: t={}
  files=[(e['path'],e.get('size',0)) for e in t.get('tree',[]) if e['type']=='blob']
  code=[(f,s) for f,s in files if re.search(r'\.(html?|js|mjs|ts|tsx|jsx|gd|cs|java|rs|py|swift|lua|luau|kt|cpp|c|h|qml|php|svelte|vue|dart|go|bas|asm|s|sh)$',f,re.I) and not re.search(r'node_modules|vendor/|\.min\.|dist/|build/|test',f)]
  code.sort(key=lambda x:-x[1])
  imgs=[f for f,s in files if re.search(r'(?i)\.(png|jpe?g|webp|gif)$',f) and re.search(r'(?i)screen|shot|preview|gameplay|capture|demo|docs?/|media/|img/|images/',f) and not re.search(r'(?i)icon|logo|favicon|sprite|tile|font|texture|node_modules',f)]
  return r,dict(branch=br,nfiles=len(files),code_bytes=sum(s for _,s in code),top=code[:6],shots=imgs[:12],truncated=t.get('truncated',False))
todo=[r for r in repos if r not in out]
with ThreadPoolExecutor(8) as ex:
  for i,(r,v) in enumerate(ex.map(one,todo)):
    out[r]=v
    if i%40==0: json.dump(out,open(outp,'w'),indent=1); print(i,flush=True)
json.dump(out,open(outp,'w'),indent=1); print('done',len(out))
