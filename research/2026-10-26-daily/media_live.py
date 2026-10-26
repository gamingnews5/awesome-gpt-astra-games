import json,re,subprocess,base64,sys
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'.')
from readme_images import images
d=json.load(open('inspect.json'))
acc=[l.strip() for l in open(sys.argv[1]) if l.strip()]
OUT=sys.argv[2]
HOST=re.compile(r'https?://[^\s)\]"\'<>]+?(github\.io|vercel\.app|netlify\.app|pages\.dev|workers\.dev|itch\.io|surge\.sh|web\.app|firebaseapp\.com|run\.app|onrender\.com|fly\.dev|glitch\.me|replit\.app)[^\s)\]"\'<>]*',re.I)
def one(r):
  p=subprocess.run(['gh','api',f'repos/{r}/readme'],capture_output=True,text=True)
  md='';base=f'https://github.com/{r}/blob/HEAD/README.md'
  if p.returncode==0:
    j=json.loads(p.stdout); md=base64.b64decode(j.get('content','')).decode('utf8','replace'); base=j['html_url']
  imgs=images(md,base)
  urls=[]
  h=(d[r].get('home') or '').strip()
  if h.startswith('http'): urls.append(h)
  for m in HOST.finditer(md):
    u=m.group(0).rstrip('.,;:*_`')
    if re.search(r'(?i)\.(png|jpe?g|gif|webp|svg|mp4)$',u) or 'shields.io' in u: continue
    if u not in urls: urls.append(u)
  live=[]
  for u in urls[:4]:
    q=subprocess.run(['curl','-sL','-o','/dev/null','-w','%{http_code} %{size_download}','--max-time','15',u],capture_output=True,text=True)
    try: code,size=q.stdout.split(); 
    except: continue
    if code=='200' and int(size)>=500: live.append(u)
  return r,dict(images=imgs,live=live,checked=urls[:4])
out={}
with ThreadPoolExecutor(10) as ex:
  for i,(r,v) in enumerate(ex.map(one,acc)):
    out[r]=v
    if i%50==0: print(i,flush=True)
prev=json.load(open(OUT)) if __import__('os').path.exists(OUT) else {}
prev.update(out); json.dump(prev,open(OUT,'w'),indent=1)
print('done',sum(1 for v in out.values() if v['images']),'with images',sum(1 for v in out.values() if v['live']),'live')
