import json,re,subprocess,sys,base64
from urllib.parse import urljoin
BAD=re.compile(r'(?i)shields\.io|badge|codecov|travis|coveralls|actions/workflows|npmjs|buymeacoffee|logo|icon|favicon|banner-?ad|sponsor|contrib\.rocks|star-history|skillicons|readme-typing|vercel\.app/api|github-readme-stats|komarev|visitor')
def images(md,base):
  out=[]
  for m in re.finditer(r'!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)',md): out.append((m.group(2),m.group(1)))
  for m in re.finditer(r'<img\b[^>]*?src=["\']([^"\']+)["\'][^>]*>',md,re.I): out.append((m.group(1),m.group(0)))
  res=[]
  for u,alt in out:
    u=u.strip('<>')
    if u.startswith('data:'): continue
    u=urljoin(base,u)
    if BAD.search(u+' '+alt): continue
    if not (re.search(r'\.(avif|gif|jpe?g|png|webp)([?#].*)?$',u,re.I) or re.search(r'user-attachments|/assets/',u)): continue
    if u not in res: res.append(u)
  return res
if __name__=="__main__":
  repos=[l.strip() for l in open(sys.argv[1]) if l.strip()]
  out={}
  for r in repos:
    p=subprocess.run(['gh','api',f'repos/{r}/readme'],capture_output=True,text=True)
    if p.returncode: out[r]=[]; continue
    d=json.loads(p.stdout); md=base64.b64decode(d.get('content','')).decode('utf8','replace')
    out[r]=images(md,d['html_url'])
    print(r,out[r][:3],flush=True)
  json.dump(out,open(sys.argv[2],'w'),indent=1)
