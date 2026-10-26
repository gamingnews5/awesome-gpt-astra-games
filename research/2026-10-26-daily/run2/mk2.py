# Download up to 2 README (or tree screenshot) images per accepted repo and tile them into contact sheets.
import json,subprocess,sys,re,os
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw
D='/workspace/find-games-last-week-made-with/research/2026-10-26-daily/run2/'
b=sys.argv[1]; O=f'/workspace/shots26r2/{b}/'; os.makedirs(O,exist_ok=True)
media=json.load(open(D+'media-live.json')); trees=json.load(open(D+'trees-acc.json'))
acc=[l.strip() for l in open(D+f'accept-{b}.txt') if l.strip()]
jobs=[]
for r in acc:
  imgs=list(media[r]['images'][:2]); src='readme'
  if not imgs:
    t=trees[r]; imgs=[f"https://github.com/{r}/blob/{t['branch']}/{quote(p)}" for p in t['shots'][:2]]
  for i,u in enumerate(imgs): jobs.append((r,i,u))
def raw(u):
  m=re.match(r'https://github\.com/([^/]+/[^/]+)/(?:blob|raw)/(.+)$',u)
  return f'https://raw.githubusercontent.com/{m.group(1)}/{m.group(2)}' if m else u
def dl(j):
  r,i,u=j; fn=f"{r.replace('/','__')}__{i}.raw"
  subprocess.run(['curl','-sL','--max-time','20','-o',O+fn,raw(u)])
  try:
    im=Image.open(O+fn); im.seek(0); w,h=im.size
    if w<200 or h<120: return None
    return [r,i,u,fn,w,h]
  except Exception: return None
with ThreadPoolExecutor(12) as ex: tiles=[t for t in ex.map(dl,jobs) if t]
json.dump(tiles,open(O+'tiles.json','w'),indent=0)
TW,TH,C=400,225,4
for s in range(0,len(tiles),16):
  sheet=Image.new('RGB',(TW*C,(TH+20)*4),'white'); d=ImageDraw.Draw(sheet)
  for k,t in enumerate(tiles[s:s+16]):
    try:
      im=Image.open(O+t[3]); im.seek(0); im=im.convert('RGB'); im.thumbnail((TW,TH))
    except Exception: continue
    x=(k%C)*TW; y=(k//C)*(TH+20); sheet.paste(im,(x,y+20)); d.text((x+4,y+4),f"{s+k} {t[0]}"[:58],fill='black')
  sheet.save(O+f'sheet{s//16:02d}.jpg',quality=82)
print(len(jobs),len(tiles),len(set(t[0] for t in tiles)),'repos', -(-len(tiles)//16),'sheets')
