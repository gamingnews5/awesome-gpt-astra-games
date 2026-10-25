# Receipts for the 2026-10-24 daily pass.
import json,collections,os
by=collections.defaultdict(set)
for f in ('repo-searches.jsonl','commit-searches.jsonl'):
  for l in open(f):
    try: x=json.loads(l)
    except ValueError: continue
    by[x['q']].add((x.get('full_name') or x.get('repo') or '').lower())
man=json.load(open('manual-decisions.json')) if os.path.exists('manual-decisions.json') else {}
auto=json.load(open('auto-rejects.json'))
dup={l.strip() for l in open('id-dup-rejects.txt') if l.strip()} if os.path.exists('id-dup-rejects.txt') else set()
acc=sorted(r for r,v in man.items() if v['decision']=='accept' and r not in dup)
accl={r.lower() for r in acc}
def rows(L): return [{'run_on':'2026-10-24','query':q['query'],'hits':q['hits'],'fetched':q['fetched'],'capped':q['capped'],'verified_yield':len(by[q['query']]&accl)} for q in L]
rq=rows(json.load(open('repo-query-log.json'))); cq=rows(json.load(open('commit-query-log.json')))
co=[l.strip() for l in open('pool-co.txt') if l.strip()]
pend=[l.strip() for l in open('pending-candidates.txt') if l.strip()] if os.path.exists('pending-candidates.txt') else []
out={'timezone':'Asia/Phnom_Penh (UTC+7)',
 'window':'commit and repository search 2026-10-23T01:00Z..2026-10-24T01:00Z (2026-10-23 08:00..2026-10-24 08:00 local); repositories created after 2026-10-22T01:00Z',
 'run_on':'2026-10-24','repository_queries':rq,'commit_queries':cq,
 'commit_pool':{'fresh_non_fork_unknown':len(json.load(open('commit-pool-fresh.json'))),'with_tracked_model_trailer':len(co)},
 'inspected':len(co),'manually_reviewed':len(man),'auto_rejected':len(auto),'accepted':len(acc),'pending_unreviewed':len(pend)}
json.dump(out,open('search-results.json','w'),indent=2,ensure_ascii=False)
rej={}
for r,v in man.items():
  if v['decision']!='accept': rej[r]='manual review ('+v['batch']+'): port, recomp, decomp, remake, mod, tool, launcher, site, portfolio, platform, template, AI bot, non-game, or no README with unclear content'
for r in dup: rej[r]='duplicate repository id of an already-catalogued game (mirror)'
rej.update(auto)
json.dump({'accepted':acc,'rejected':rej,'held':{r:'pending manual review next run' for r in pend}},open('candidate-decisions.json','w'),indent=2,ensure_ascii=False)
print(len(acc),len(rej),len(pend),len(rq),len(cq),sum(q['capped'] for q in cq))
