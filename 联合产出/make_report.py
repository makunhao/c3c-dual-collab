#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 results_linalg.json 生成 Markdown 报告（数字不手抄）。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "results_linalg.json").read_text(encoding="utf-8"))

lines = ["# 线代题求解报告（我方半边）", "",
         f"- 题目数：{len(data)}",
         f"- 自校验通过：{sum(1 for d in data if d['self_check']=='ok')}/{len(data)}",
         "- 数据源：`results_linalg.json`（由 `solve_linalg.py` 生成）", "",
         "| 题号 | 题型 | 矩阵 | 答案 | 自校验 | 校验依据 |", "|---|---|---|---|---|---|"]
for d in data:
    m = "<br>".join("[" + ", ".join(str(x) for x in row) + "]" for row in d["matrix"])
    ans = d["answer"] if isinstance(d["answer"], str) else "<br>".join(
        "[" + ", ".join(map(str, row)) + "]" for row in d["answer"]) if isinstance(d["answer"][0], list) else ", ".join(d["answer"])
    lines.append(f"| {d['id']} | {d['type']} | {m} | {ans} | {d['self_check']} | {d['check_detail']} |")

lines += ["", "## 求解与校验是两条路径", "",
          "- det：按第一行展开 vs 按排列定义。",
          "- rref：高斯消元后检查主元列是否为单位列。",
          "- eigen：有理根定理求根后，用 Σλ=tr(A) 与代回特征多项式两条不变量校验。", "",
          "## 校验抓不到什么", "",
          "渲染/排版类错误（例如特征多项式丢负号）不在校验范围内，必须人工看输出。",
          "这条来自 C4C 的真实教训：校验器抓到了符号反转，但没抓到 PDF 里的 `λ²7λ10`。", ""]

(ROOT / "解题报告.md").write_text("\n".join(lines), encoding="utf-8")
print("report → 解题报告.md")
