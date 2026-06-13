#!/usr/bin/env python3
"""配植案例（pattern）源 案例.json → ui/patterns.json。
- 校验每个案例 layers 里的植物名是否存在于 plants.json（保证 UI 交叉链接打得通）
- 未匹配的植物名会打印警告，方便录入时发现拼写/归一化问题
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '案例.json')
PLANTS = os.path.join(ROOT, 'ui', 'plants.json')
OUT = os.path.join(ROOT, 'ui', 'patterns.json')

cases = json.load(open(SRC, encoding='utf-8'))
plant_names = {p['plant_name'] for p in json.load(open(PLANTS, encoding='utf-8'))}

missing = []
for c in cases:
    for layer, names in c.get('layers', {}).items():
        for n in names:
            if n not in plant_names:
                missing.append((c['id'], layer, n))

if missing:
    print('⚠️ 以下案例植物名在 plants.json 中找不到（请检查归一化/拼写）：')
    for cid, layer, n in missing:
        print(f'   案例{cid} {layer}: {n}')
else:
    print('✅ 所有案例植物名均能链到植物库')

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(cases, f, ensure_ascii=False, indent=0)
print(f'{len(cases)} 案例 → {OUT}')
