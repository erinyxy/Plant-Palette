# Plant Palette · 植栽パレット

593 株植物筛选浏览工具，单页应用，纯 HTML + CSS + JS。

## 运行

由于浏览器对 `file://` 协议下 fetch 有限制，需要起个本地服务器：

```bash
cd /Users/errena/Claude/project/配植工具/ui
python3 -m http.server 8000
```

然后浏览器打开 http://localhost:8000

按 Ctrl+C 停止服务器。

## 数据更新

如果 `植栽_Layer2.csv` 变了（重跑了 `layer2_transform.py`），重新生成 JSON：

```bash
python3 generate_json.py
```

刷新浏览器即可。

## 文件说明

- `index.html` — 单页应用（HTML + 内嵌 CSS + 内嵌 JS）
- `plants.json` — 593 株数据，从 `植栽_Layer2.csv` 生成
- `generate_json.py` — CSV → JSON 转换器

## UI 使用

- **顶栏搜索框**：日文 / 英文 / 别名都能搜
- **左侧筛选面板**（手机版点 ≡ Filters 展开）
  - **Basic Attributes**（7 类基本属性）：樹高 / 必要日照 / 常緑性 / 花色 / 耐寒 / 気候帯 / 地域限定
  - **Themes**（16 组主题 tag）：风格庭 / 招鸟 / 形态 / 葉色 / 花期 / 香り / 果实 / 樹皮 / 耐性 / 結構機能 / 場所 / 特殊用途 / 剪定 / ツル / 非木本
- 同一组内 tag 之间是 **OR**（任一即可）
- 不同组之间是 **AND**（全部满足）
- 点击植物卡片看完整属性

## 部署到 GitHub Pages

把 `ui/` 子目录推到 GitHub 仓库，仓库设置启用 Pages → 选 `ui` 分支根目录 → 几分钟后获得公网 URL。

## 下次迭代清单（已知可优化项）

- [ ] 按 theme tag 数量排序的选项
- [ ] 收藏 / 标星功能（localStorage）
- [ ] 选项组之间的 AND/OR 切换
- [ ] URL 状态持久化（?filter=xxx 分享链接）
- [ ] 植物图片（需要图源）
