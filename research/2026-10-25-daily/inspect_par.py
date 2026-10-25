import json,subprocess,sys
repos=[l.strip() for l in open(sys.argv[1]) if l.strip()]
outp=sys.argv[2]
try: res=json.load(open(outp))
except Exception: res={}
repos=[r for r in repos if r not in res]
def run(chunk):
  parts=[]
  for j,r in enumerate(chunk):
    o,n=r.split('/',1)
    parts.append(f'''r{j}: repository(owner:{json.dumps(o)}, name:{json.dumps(n)}){{nameWithOwner createdAt databaseId description homepageUrl stargazerCount isFork owner{{login}} primaryLanguage{{name}} defaultBranchRef{{name target{{... on Commit{{history(first:100){{nodes{{oid message committedDate}}}}}}}}}}
      readme: object(expression:"HEAD:README.md"){{... on Blob{{text}}}}
      tree: object(expression:"HEAD:"){{... on Tree{{entries{{name type}}}}}} }}''')
  q='query{'+' '.join(parts)+'}'
  p=subprocess.run(['gh','api','graphql','-f',f'query={q}'],capture_output=True,text=True)
  d=json.loads(p.stdout or '{}').get('data') or {}
  for j,r in enumerate(chunk):
    v=d.get(f'r{j}')
    if not v: print('miss',r,file=sys.stderr); continue
    br=v['defaultBranchRef'] or {}
    commits=((br.get('target') or {}).get('history') or {}).get('nodes',[])
    res[r]=dict(id=v['databaseId'],created=v['createdAt'],desc=v['description'],home=v['homepageUrl'],stars=v['stargazerCount'],fork=v['isFork'],lang=(v['primaryLanguage'] or {}).get('name'),branch=br.get('name'),
      readme=((v.get('readme') or {}).get('text') or '')[:6000],tree=[e['name']+('/' if e['type']=='tree' else '') for e in ((v.get('tree') or {}).get('entries') or [])],
      commits=[dict(sha=c['oid'],msg=c['message'][:2500],date=c['committedDate']) for c in commits])
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(5) as ex:
  for k,_ in enumerate(ex.map(run,[repos[i:i+8] for i in range(0,len(repos),8)])):
    if k%10==0: json.dump(dict(res),open(outp,"w"),indent=1); print(k,len(res),file=sys.stderr,flush=True)
json.dump(res,open(outp,'w'),indent=1)
print(len(res),file=sys.stderr)
