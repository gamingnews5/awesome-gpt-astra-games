# REST inspection via gh-read: meta, last 100 commits, README, recursive tree. Writes inspect.json + trees.json (same shape as earlier passes).
import json,sys,re,base64,os
from concurrent.futures import ThreadPoolExecutor
from ghr import get
repos=[l.strip() for l in open(sys.argv[1]) if l.strip() and '/' in l and not l.startswith('#')]
INS='inspect.json'; TR='trees.json'
ins=json.load(open(INS)) if os.path.exists(INS) else {}; trees=json.load(open(TR)) if os.path.exists(TR) else {}
miss=set(json.load(open('miss.json'))) if os.path.exists('miss.json') else set()
PAT=re.compile(r'(?i)claude[ -]opus[ -]5\.5|opus[ -]5\.5|sonnet[ -]5\.5|fable[ -]5|claude[ -]fable|gpt-?6\.1[ -]?sol|gpt-?6[ -]astra|gemini[ -]4[ -]argon')
def one(r):
  m=get(f'/repos/{r}')
  if not m or 'full_name' not in m: return r,None,None
  v=dict(id=m['id'],created=m['created_at'],desc=m['description'],home=m['homepage'],stars=m['stargazers_count'],fork=m['fork'],lang=m['language'],branch=m['default_branch'],readme='',tree=[],commits=[],full=m['full_name'])
  if m['fork']: return r,v,None
  if os.environ.get('CUTOFF') and m['created_at']<os.environ['CUTOFF']: v['old']=True; return r,v,None
  cs=get(f'/repos/{r}/commits?per_page=100') or []
  v['commits']=[dict(sha=c['sha'],msg=c['commit']['message'][:2500],date=c['commit']['committer']['date']) for c in cs if isinstance(c,dict) and 'sha' in c]
  if not any(PAT.search(l) for c in v['commits'] for l in c['msg'].splitlines() if l.strip().lower().startswith('co-authored-by')): return r,v,None
  rd=get(f'/repos/{r}/readme')
  if rd and rd.get('content'): v['readme']=base64.b64decode(rd['content']).decode('utf8','replace')[:6000]; v['readme_url']=rd.get('html_url')
  if os.environ.get('NOTREE'): return r,v,None
  t=get(f"/repos/{r}/git/trees/{m['default_branch']}?recursive=1") or {}
  ents=t.get('tree',[])
  v['tree']=[e['path']+('/' if e['type']=='tree' else '') for e in ents if '/' not in e['path']]
  files=[(e['path'],e.get('size',0)) for e in ents if e['type']=='blob']
  code=[(f,s) for f,s in files if re.search(r'\.(html?|js|mjs|ts|tsx|jsx|gd|cs|java|rs|py|swift|lua|luau|kt|cpp|c|h|qml|php|svelte|vue|dart|go|bas|asm|s|sh)$',f,re.I) and not re.search(r'node_modules|vendor/|\.min\.|dist/|build/|test',f)]
  code.sort(key=lambda x:-x[1])
  imgs=[f for f,s in files if re.search(r'(?i)\.(png|jpe?g|webp|gif)$',f) and re.search(r'(?i)screen|shot|preview|gameplay|capture|demo|docs?/|media/|img/|images/',f) and not re.search(r'(?i)icon|logo|favicon|sprite|tile|font|texture|node_modules',f)]
  tv=dict(branch=m['default_branch'],nfiles=len(files),code_bytes=sum(s for _,s in code),top=code[:6],shots=imgs[:12],truncated=t.get('truncated',False))
  return r,v,tv
todo=[r for r in repos if (r not in ins or (os.environ.get('TREEONLY') and r not in trees)) and r not in miss]
print('todo',len(todo),flush=True)
with ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv)>2 else 16) as ex:
  for i,(r,v,tv) in enumerate(ex.map(one,todo)):
    if v is None: miss.add(r)
    else: ins[r]=v
    if tv: trees[r]=tv
    if i%50==0:
      json.dump(ins,open(INS,'w')); json.dump(trees,open(TR,'w')); json.dump(sorted(miss),open('miss.json','w')); print(i,len(ins),len(miss),flush=True)
json.dump(ins,open(INS,'w')); json.dump(trees,open(TR,'w')); json.dump(sorted(miss),open('miss.json','w')); print('done',len(ins),len(miss))
