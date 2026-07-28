from pathlib import Path
html = Path('mg-bucket-bag.html').read_text()
assert 'img_marigold' not in html, 'FAIL: topiary/marigold still referenced'
assert 'gap: 2px' in html, 'FAIL: emotional grid hairline gap missing'
assert 'max-width: 1040px' in html, 'FAIL: coffee portrait sizing missing'
import re
refs = sorted(set(re.findall(r'src="images/([^"]+)"', html)))
problems = [n for n in refs if not (Path('images')/n).exists() or (Path('images')/n).stat().st_size < 1000]
print('referenced:', len(refs), '| problems:', len(problems))
for x in problems: print('  MISSING/SMALL:', x)
assert not problems, 'FAIL: missing images'
print('ALL CHECKS PASSED')
