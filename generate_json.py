#!/usr/bin/env python3
"""CSV → JSON 转换，给前端使用。每行 plant 转成 JS-friendly 对象。"""
import csv
import json
import os

CSV = '/Users/errena/Claude/project/配植工具/植栽_Layer2.csv'
OUT = '/Users/errena/Claude/project/配植工具/ui/plants.json'

# 多值字段（用 ; 分隔）
MULTI_FIELDS = {
    'aliases','cultivars_listed','花色','theme_tags',
    'hedge_purpose','shitate_type','conifer_shape_type','bark_stripe_pattern',
    'lawn_grass_type','pergola_category','autumn_color_type','leaf_color_system',
    'symbol_tree_category','bloom_period','understory_light','garden_orientation',
    'fruit_color','leaf_persistence_subcat','source_pages',
}

# 字段顺序：UI 上展示从重要到次要
plants = []
with open(CSV, encoding='utf-8') as f:
    for row in csv.DictReader(f):
        p = {}
        for k, v in row.items():
            v = v.strip() if v else ''
            if k in MULTI_FIELDS:
                # 花色用全角 ；，其他用 ;
                sep = '；' if k == '花色' else ';'
                p[k] = [x.strip() for x in v.split(sep) if x.strip()] if v else []
            elif k == 'source_section_count':
                p[k] = int(v) if v else 0
            else:
                # 把 unknown 也保留为字符串，UI 决定是否显示
                p[k] = v
        plants.append(p)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(plants, f, ensure_ascii=False, indent=0)

size_kb = os.path.getsize(OUT) / 1024
print(f'{len(plants)} 株 → {OUT}（{size_kb:.1f} KB）')
