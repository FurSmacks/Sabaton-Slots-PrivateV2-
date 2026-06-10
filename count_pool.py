import re
from collections import Counter
text = open('sabaton-slots.html', encoding='utf-8').read()
start = text.index('const POOL = [')
end = text.index('];\n\n// ═══════════════════════════════════════════════════════════════════════════\n// ③ AUSZAHLUNGSTABELLE', start)
items = re.findall(r"'([^']+)'", text[start:end])
c = Counter(items)
print('TOTAL', len(items))
for k, v in c.items():
    print(f'{k}: {v}')
