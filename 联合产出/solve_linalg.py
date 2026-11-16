#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""C3C 联合产出的我方半边：线代题确定性求解 + 自校验。

设计原则（来自 C4C 踩坑）：
  1. 求解与校验走两条不同路径；
  2. 校验抓不到的渲染错误，靠人工看输出；
  3. 结果写 JSON，报告由 JSON 生成，不手抄数字。

题型：det / rref / eigen（3×3 以内，Fraction 精确运算）。
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def mat(rows):
    return [[Fraction(x) for x in r] for r in rows]


def det3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def rref(m):
    a = [row[:] for row in m]
    rows, cols = len(a), len(a[0])
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if a[i][c] != 0), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return a, piv


def charpoly3(m):
    """返回 λ^3 + c2 λ^2 + c1 λ + c0 的系数 [1,c2,c1,c0]（精确）。"""
    tr = m[0][0] + m[1][1] + m[2][2]
    # 二阶主子式之和
    s2 = 0
    for i in range(3):
        for j in range(i + 1, 3):
            s2 += m[i][i] * m[j][j] - m[i][j] * m[j][i]
    # 行列式
    d = det3(m)
    return [Fraction(1), -tr, s2, -d]


def roots_rational(coeffs):
    """有理根定理找整数根，再做降次；返回实根（可能是重根）。"""
    c = [Fraction(x) for x in coeffs]
    roots = []
    for cand in range(-20, 21):
        x = Fraction(cand)
        val = sum(coef * x ** (len(c) - 1 - i) for i, coef in enumerate(c))
        if val == 0:
            roots.append(x)
            # 合成除法
            out = [c[0]]
            for coef in c[1:]:
                out.append(coef + out[-1] * x)
            c = out[:-1]
            if len(c) == 1:
                break
    return roots, c


def fmt(x):
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def det_perm(m):
    """按排列定义计算 3×3 行列式（与按行展开是两条路径）。"""
    from itertools import permutations
    total = Fraction(0)
    for perm in permutations(range(3)):
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
        prod = m[0][perm[0]] * m[1][perm[1]] * m[2][perm[2]]
        total += (-1 if inv % 2 else 1) * prod
    return total


def solve(problem):
    A = mat(problem["matrix"])
    kind = problem["type"]
    if kind == "det":
        value = det3(A)
        check = det_perm(A)
        return {"answer": fmt(value), "self_check": "ok" if check == value else "fail",
                "check_detail": f"按行展开={fmt(value)}，按排列定义={fmt(check)}"}
    if kind == "rref":
        R, piv = rref(A)
        # 自校验：R 的每个主元列必须是单位列
        ok = True
        for idx, c in enumerate(piv):
            col = [R[i][c] for i in range(len(R))]
            if col[idx] != 1 or any(col[i] != 0 for i in range(len(R)) if i != idx):
                ok = False
        return {"answer": [[fmt(x) for x in row] for row in R], "pivots": piv,
                "self_check": "ok" if ok else "fail", "check_detail": "主元列为单位列"}
    if kind == "eigen":
        coeffs = charpoly3(A)
        roots, rest = roots_rational(coeffs)
        # 自校验 1：Σλ = tr(A)
        tr = A[0][0] + A[1][1] + A[2][2]
        sum_ok = sum(roots) == tr
        # 自校验 2：每个根代回特征多项式为 0
        eval_ok = all(sum(cf * r ** (3 - i) for i, cf in enumerate(coeffs)) == 0 for r in roots)
        return {"answer": [fmt(r) for r in roots],
                "charpoly": " + ".join(f"{fmt(cf)}λ^{3-i}" for i, cf in enumerate(coeffs)),
                "self_check": "ok" if (sum_ok and eval_ok) else "fail",
                "check_detail": f"Σλ=tr(A): {sum_ok}; 代回为 0: {eval_ok}"}
    raise ValueError(kind)


PROBLEMS = [
    {"id": "L1", "type": "det", "matrix": [[1, 2, 3], [0, 1, 4], [5, 6, 0]]},
    {"id": "L2", "type": "det", "matrix": [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]},
    {"id": "L3", "type": "rref", "matrix": [[1, 2, 1, 4], [2, 5, 3, 9], [1, 3, 2, 5]]},
    {"id": "L4", "type": "rref", "matrix": [[0, 2, 1], [1, -1, 3], [2, 1, 1]]},
    {"id": "L5", "type": "eigen", "matrix": [[2, 0, 0], [0, 3, 4], [0, 4, 9]]},
    {"id": "L6", "type": "eigen", "matrix": [[4, 1, 0], [1, 4, 0], [0, 0, 6]]},
]


def main():
    results = []
    for p in PROBLEMS:
        r = solve(p)
        results.append({**p, **r})
        print(f"{p['id']} {p['type']:5s} → {r['answer']}  [{r['self_check']}] {r['check_detail']}")
    out = ROOT / "results_linalg.json"
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    ok = sum(1 for r in results if r["self_check"] == "ok")
    print(f"\n{ok}/{len(results)} 自校验通过 → {out}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
