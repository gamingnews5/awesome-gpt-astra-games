# Build one review batch of the 2026-10-26 daily pass, attach rated screenshots, and append records to games.json.
import json,math,re,sys
TODAY='2026-10-26'; D='research/2026-10-26-daily/'; B=sys.argv[1]; S=f'/workspace/shots26/{B}/'
games=json.load(open('games.json')); known={g['github_url'].casefold() for g in games}
ins=json.load(open(D+'inspect.json'))
for _r in [l.strip() for l in open(D+f'accept-{B}.txt') if l.strip()]:
  ins[_r]['readme']=ins[_r]['readme']; trees=json.load(open(D+'trees.json')); ev=json.load(open(D+'evidence.json'))
media=json.load(open(D+'media-live.json'))
acc=[l.strip() for l in open(D+f'accept-{B}.txt') if l.strip()]
acc=[r for r in acc if r not in set(open(D+'post-reject.txt').read().split())] if __import__('os').path.exists(D+'post-reject.txt') else acc
CARRY=set()
repo_hits={json.loads(l)['full_name'] for f in (D+'repo-searches.jsonl',) for l in open(f)} if __import__('os').path.exists(D+'repo-searches.jsonl') else set()
RS24='GitHub repository search: exact model phrase, created 2026-10-23T01:00Z..2026-10-24T01:00Z'
CP24='GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list'
RS='GitHub repository search: exact model phrase, created 2026-10-25T01:00Z..2026-10-26T01:00Z'
CP='GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z'
ORDER=['Claude Opus 5.5','Claude Sonnet 5.5','Claude Fable 5.1','GPT-6.1 Sol','GPT-6 Astra','Gemini 4 Argon']
MEV={}
NAME_OVR=json.load(open(D+'name-overrides.json')) if __import__('os').path.exists(D+'name-overrides.json') else {}
def tidy(n):
  n=re.sub(r'[\U0001F000-\U0001FFFF\u2600-\u27BF\uFE0F]+','',n).strip()
  for sep in (' — ',' – ',' - ',': start here'):
    if sep in n and len(n.split(sep)[0].strip())>=3: n=n.split(sep)[0].strip()
  n=re.sub(r'\s*[（(][^)）]*(prototype|demo|v\d|ue \d|版|beta|alpha|wip)[^)）]*[)）]\s*$','',n,flags=re.I).strip()
  n=re.sub(r'\s+v?\d+(\.\d+)+\s*$','',n).strip()
  n=re.sub(r'\s+V\d+(\.\d+)*\s*$','',n).strip()
  return n or n
def clean(s):
  s=re.sub(r'<[^>]+>','',s); s=re.sub(r'!\[[^\]]*\]\([^)]*\)','',s); s=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',s)
  s=re.sub(r'[*_`]+','',s); s=re.sub(r'\s+',' ',s).strip(' #-|:')
  return s
def name_of(r,m):
  if r in NAME_OVR: return NAME_OVR[r]
  for line in m['readme'].splitlines():
    line=line.lstrip('\ufeff ')
    if line.startswith('# ') or line.startswith('#\t'):
      n=clean(line[2:]);
      n=re.sub(r'^[^\w\d]+','',n,flags=re.U).strip()
      n=tidy(n)
      if 2<len(n)<=90 and n.lower() not in ('readme','game','my app','test','index'): return n
  desc=clean(m['desc'] or '')
  base=r.split('/',1)[1]; b=re.sub(r'[-_]+',' ',base).strip()
  return b.title() if b.lower()!='game' or not desc else tidy(desc)[:60]
def note_of(r,m):
  if r in MEV and r.startswith('novaki'):
    pass
  desc=clean(m['desc'] or '')
  body=m['readme']
  lines=[l for l in body.splitlines() if l.strip() and not l.lstrip().startswith(('#','!','<','[!','|','```','>','-','*'))]
  para=clean(lines[0]) if lines else ''
  t=desc if len(desc)>=30 else (para or desc)
  t=t[:260].rsplit(' ',1)[0]+'…' if len(t)>260 else t
  if t and not t.endswith(('.','!','?','…')): t+='.'
  return t or 'Game source inspected in the repository.'
def tech_of(r,m,t):
  rd=(m['readme']+' '+(m['desc'] or '')).lower(); tree=' '.join(m['tree']).lower(); files=' '.join(f for f,_ in t['top']).lower()
  T=[]
  if 'project.godot' in tree or '.gd' in files: T+=['Godot','GDScript']
  elif 'projectsettings/' in tree or 'assets/' in tree and 'unity' in rd: T+=['Unity','C#']
  elif '.uproject' in tree or 'unreal' in rd: T+=['Unreal Engine','C++']
  elif '.luau' in files or 'roblox' in rd: T+=['Roblox','Luau']
  elif 'pubspec.yaml' in tree or 'flutter' in rd: T+=['Flutter','Dart']
  else:
    lang=m['lang'] or ''
    if lang in ('TypeScript','JavaScript','HTML','CSS','Vue','Svelte'): T+=['TypeScript' if lang=='TypeScript' else 'JavaScript']
    elif lang: T+=[lang]
    if 'three.js' in rd or 'threejs' in rd or 'three@' in rd or 'react-three' in rd or 'r3f' in r.lower(): T+=['Three.js']
    if 'babylon' in rd: T+=['Babylon.js']
    if 'phaser' in rd: T+=['Phaser']
    if 'pixijs' in rd or 'pixi.js' in rd: T+=['PixiJS']
    if 'react' in rd and 'React' not in T: T+=['React']
    if re.search(r'\.(html?|js|ts|tsx)\b',files) or 'index.html' in tree: T+=['Browser']
  if 'webxr' in rd or 'meta quest' in rd: T+=['WebXR']
  if not T: T=['Unknown']
  return list(dict.fromkeys(T))
def flops_of(T,rd):
  s=' '.join(T)
  if any(k in s for k in ('Three.js','Babylon','Unity','Unreal','Godot','Roblox','WebXR')) or ' 3d' in rd: return 1e9
  if any(k in s for k in ('Phaser','PixiJS','Flutter')) or 'canvas' in rd: return 1e8
  if 'Browser' in s or 'React' in s: return 1e7
  return 1e6
# screenshots
tiles=json.load(open(S+'tiles.json'))
rated={}
for line in open(S+'ratings.tsv'):
  ti,sc,kind,why=line.rstrip('\n').split('\t'); t=tiles[int(ti)]; kind={'concept_art':'asset','model_render':'asset','title_card':'title_or_menu','ui':'interface','menu':'title_or_menu'}.get(kind,kind); rated[t[0]]=(t[2],float(sc),kind,why)
reviews=json.load(open('research/screenshot-reviews.json'))
def add_review(repo_url,u,game,sc,kind,why):
  reviews['reviews'].append({'repository_url':repo_url,'url':u,'game':game,'score_10':sc,'image_kind':kind,'reason':'Use this frame for the game-level score. '+why,'reviewed_on':TODAY,'rating_method':'manual_visual_review'})
batch=[]
KIDS={x.get('repository_id') for x in json.load(open('games.json'))}
IDDUP=[]
for r in acc:
  url=f'https://github.com/{r}'; assert url.casefold() not in known, r
  m=ins[r]
  if m['id'] in KIDS: IDDUP.append(r); continue
  KIDS.add(m['id'])
  t=trees[r]; br=m['branch'] or t['branch']
  co=ev[r]['co']
  name=name_of(r,m)
  extra=''
  if r in MEV: mev,models,extra=MEV[r]; evidence=f'{url}/blob/{br}/README.md' if m['readme'] else url
  else:
    mev='confirmed'; models=[x for x in ORDER if x in co]; evidence=f"{url}/commit/{co[models[0]]}"
  from urllib.parse import urlsplit
  def canon(v):
    x=urlsplit(v); return f"{x.scheme}://{x.netloc.lower()}{x.path.rstrip('/') or '/'}"+(('?'+x.query) if x.query else '')
  seen=set(); lives=[]
  for v in media[r]['live']:
    if canon(v) not in seen: seen.add(canon(v)); lives.append(v)
  kb=t['code_bytes']/1000
  q=round(min(8.6,5.8+0.6*math.log10(kb+1)+(0.3 if lives else 0)),1)
  T=tech_of(r,m,t); rd=(m['readme']+' '+(m['desc'] or '')).lower()
  note=note_of(r,m)
  rec={'name':name,'github_url':url,'repository_id':m['id'],'repository_created_at':m['created'],'added_to_repo_on':TODAY,'evidence_url':evidence,
    'game_links':[f'{url}/blob/{br}/{p}' for p,_ in t['top'][:3]] or [url],'live_demo_url':lives[0] if lives else None,'live_demo_urls':lives,
    'technology':T,'model_family':models,'method_evidence':mev,'model_evidence':mev,
    'game_count':1,'contained_games':[name],'counted_game_units':1,'is_independent_game':True,
    'verification_status':'verified_source','verified_on':TODAY,
    'discovery_sources':[(CP24 if r in CARRY else (RS if r in repo_hits else CP)),url],
    'verification_notes':(note+' '+extra).strip()+(' Commit carries an exact '+' / '.join(models)+' co-author trailer.' if mev=='confirmed' else '')+(' Live demo returned HTTP 200 (availability only, not a playtest).' if lives else '')+' Source inspected from README, file tree and commit history only; no playtest.',
    'gauntlet_loop':False,'flops_estimate_raw':int(flops_of(T,rd)),'flops_estimate_unit':'estimated FP32 operations per second at 60 FPS','flops_estimate_confidence':'low',
    'flops_estimate_basis':'Static order-of-magnitude estimate from the renderer and simulation type; not measured.',
    'quality_estimate_10':q,'quality_estimate_basis':'Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.',
    'screenshot_urls':[],'youtube_urls':[],'publication_date_status':'repository_created_only',
    'prompt':'The complete prompt was not published in the verified source.','prompt_origin':'unknown','prompt_evidence_url':None,
    'quality_category':'curated_games' if q>=7 else 'bad_games','runtime_test_status':'Source inspected; live demo HTTP 200 only.' if lives else 'Source inspected; no live demo checked or runtime playtest.'}
  if r.startswith('novaki-ai/'):
    rec['prompt']='Identical single-message brief for all Novaki test 06 agents, published as PROMPT.md in the repository.'; rec['prompt_origin']='creator_published'; rec['prompt_evidence_url']=f'{url}/blob/{br}/PROMPT.md'
  if r in rated:
    u,sc,kind,why=rated[r]
    rec['screenshot_urls']=[u]; rec['screenshot_rating_10']=sc; rec['screenshot_rating_evidence_url']=u; rec['screenshot_rating_on']=TODAY
    add_review(url,u,name,sc,kind,why)
  batch.append(rec)
nb=0
names=[b['name'] for b in batch]+[g['name'] for g in games]
dups={n for n in names if names.count(n)>1}
for b in batch:
  if b['name'] in dups:
    b['name']=f"{b['name']} ({b['github_url'].split('/')[3]})"; b['contained_games']=[b['name']]
import os
gb=json.load(open(D+'game-batch.json')) if os.path.exists(D+'game-batch.json') else {'verified_on':TODAY,'timezone':'Asia/Phnom_Penh','window_start':'2026-10-23','window_end':'2026-10-26','date_basis':'repository creation proxy only','records':[]}
gb['records']+=[{k:b[k] for k in ('name','github_url','repository_id','repository_created_at','counted_game_units','evidence_url','publication_date_status','game_links','model_family','method_evidence','added_to_repo_on','verified_on','verification_status','live_demo_url')} for b in batch]
gb['expected_repositories']=len(gb['records']); gb['expected_game_units']=sum(x['counted_game_units'] for x in gb['records'])
out=gb
json.dump(out,open(D+'game-batch.json','w'),indent=2,ensure_ascii=False)
games.extend(batch); json.dump(games,open('games.json','w'),indent=2,ensure_ascii=False); open('games.json','a').write('\n')
open('research/screenshot-reviews.json','w').write(json.dumps(reviews,indent=2,ensure_ascii=False)+'\n')
from collections import Counter
print(len(batch),'records',sum(1 for b in batch if b['live_demo_urls']),'live',sum(1 for b in batch if b['screenshot_urls']),'rated new',nb,'rated backlog')
print(Counter(m for b in batch for m in b['model_family']))
print('dups',dups)
if IDDUP:
  print('id-dup skipped',IDDUP); open(D+'id-dup-rejects.txt','a').write(''.join(x+'\n' for x in IDDUP))
