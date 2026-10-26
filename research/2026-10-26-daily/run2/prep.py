# Evidence + triage for the Oct 25 daily pass (args: listfile batchprefix); writes auto decisions and batched review lines.
import json,re,collections
d=json.load(open('inspect.json')); import sys,os
order=[l.strip() for l in open(sys.argv[1]) if l.strip()]; PFX=sys.argv[2]
PAT=[('Claude Opus 5.5',r'claude[ -]opus[ -]5\.5|opus[ -]5\.5'),('Claude Sonnet 5.5',r'sonnet[ -]5\.5'),('Claude Fable 5.1',r'fable[ -]5(\.1)?|claude[ -]fable'),
('GPT-6.1 Sol',r'gpt-?6\.1[ -]?sol'),('GPT-6 Astra',r'gpt-?6[ -]astra'),('Gemini 4 Argon',r'gemini[ -]4[ -]argon')]
POS=re.compile(r'(?i)\b(game|games|gameplay|playable|arcade|platformer|shooter|roguelike|roguelite|rpg|puzzle|tower defen[cs]e|dungeon|survival|endless runner|idle|clicker|high ?score|boss|enemies|enemy|power-?ups?|levels?|lives|game over|controls|wasd|arrow keys|spacebar|joystick|mini-?games?|player|score|multiplayer|chess|sudoku|tetris|snake|card|board|quiz|trivia)\b')
ev=json.load(open('evidence.json')) if os.path.exists('evidence.json') else {}
auto=json.load(open('auto-rejects.json')) if os.path.exists('auto-rejects.json') else {}
review=[]
for r in order:
  v=d.get(r)
  if not v: auto[r]='repository not reachable at inspection (deleted, renamed or private)'; continue
  co={};anyc={}
  for c in reversed(v['commits']):
    for line in c['msg'].splitlines():
      L=line.lower()
      for name,p in PAT:
        if re.search(p,L):
          anyc.setdefault(name,c['sha'])
          if L.strip().startswith('co-authored-by:'): co.setdefault(name,c['sha'])
  ev[r]=dict(co=co,any=anyc)
  if v.get('fork'): auto[r]='fork'; continue
  if v.get('old'): auto[r]='repository created before 2026-10-24T01:00Z (older repo with new commits)'; continue
  if not co: auto[r]='no tracked-model co-author trailer in the last 100 commits'; continue
  text=r.split('/')[1]+' '+(v['desc'] or '')+' '+v['readme'][:3000]
  G=re.compile(r'(?i)game|play|quest|runner|shoot|jump|dungeon|tetris|snake|pong|chess|racer|craft|arena|tower|rogue|puzzle|blast|invader|zombie|maze|battle|war|hero|kart|golf|pinball|breakout|asteroid|clicker|idle')
  if len(set(m.lower() for m in POS.findall(text)))<2 and not (G.search(r.split('/')[1]) or G.search(v['desc'] or '')): auto[r]='weak game signal in name, description and README (fewer than two distinct game terms)'; continue
  review.append(r)
json.dump(ev,open('evidence.json','w'),indent=1)
json.dump(auto,open('auto-rejects.json','w'),indent=1)
def line(r):
  v=d[r]; tag=','.join(k.split()[-2][:3]+k.split()[-1] for k in ev[r]['co'])
  rd=re.sub(r'<[^>]+>|!\[[^\]]*\]\([^)]*\)|\[!\[.*?\]\(.*?\)\]\(.*?\)|[#*`|>\-]+|\s+',' ',v['readme']).strip()[:140]
  return f"{r} [{tag}] {v['lang']} c{len(v['commits'])} | {(v['desc'] or '')[:90]} | {rd} | {' '.join(v['tree'][:8])}"
B=150
for i in range(0,len(review),B):
  open(f'review-{PFX}{i//B+1:02d}.txt','w').write('\n'.join(f'{k} '+line(r) for k,r in enumerate(review[i:i+B]))+'\n')
print(len(order),'auto',collections.Counter(auto.values()).most_common(),'review',len(review),'batches',-(-len(review)//B))
