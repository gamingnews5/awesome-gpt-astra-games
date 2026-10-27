# Read-only GitHub GET via the shared helper /workspace/composio/gh-read.sh; stderr lines appended to gh-read.log.
import subprocess,json,tempfile,os,time
LOG=os.path.join(os.path.dirname(os.path.abspath(__file__)),'gh-read.log')
def get(path,retries=2):
  for a in range(retries+1):
    with tempfile.TemporaryFile() as out, open(LOG,'a') as err:
      p=subprocess.run(['/workspace/composio/gh-read.sh',path],stdout=out,stderr=err)
      out.seek(0); body=out.read().decode('utf8','replace')
    try: d=json.loads(body)
    except Exception: d=None
    if p.returncode==0: return d
    msg=json.dumps(d)[:300] if d else body[:300]
    if d and isinstance(d,dict) and d.get('status') in ('404','409','451') or 'Not Found' in msg or 'Git Repository is empty' in msg or 'blocked' in msg: return None
    time.sleep(3)
  return None
