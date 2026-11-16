# C3C 交付包 · 双人协作与技能迁移（shisan-l）

## 文件

```
C3C交付包/
├── README.md
├── shisan-l_C3C_协作方案.md
├── shisan-l_C3C_技能画像_十三.md
├── shisan-l_C3C_技能画像_搭档L.md        ← 模板，待本人填写
├── shisan-l_C3C_学习笔记_十三.md
├── shisan-l_C3C_学习笔记_搭档L.md        ← 模板
├── shisan-l_C3C_教学记录/
│   ├── 会话1_异步_GitHub与API配置_记录.md ← 已发生（2026-09-25，31 条私聊）
│   ├── 会话1_Git与Python入门_教案.md     ← 教案（未执行的正式会话）
│   └── 会话2_数学规范_提纲.md            ← 提纲，待执行
├── 联合产出/
│   ├── solve_linalg.py                  ← 6 题求解，6/6 自校验
│   ├── results_linalg.json
│   ├── make_report.py
│   ├── 解题报告.md
│   └── README.md
├── shisan-l_C3C_前后对比.md
├── shisan-l_C3C_AAR.md
└── shisan-l_C3C_AI日志.md
```

## 当前状态

| 项 | 状态 |
|---|---|
| 我方联合产出 | ✅ 6/6 求解与自校验通过 |
| 协作方案 / 教案 / 提纲 | ✅ |
| 搭档画像与学习笔记 | ⏳ 待本人填写 |
| 教学会话 1 | ⚠️ 已发生（异步 31 条），缺对方独立产物 |
| 教学会话 2 | ⏳ 待执行 |
| 双人 AAR | ⏳ 待共同完成 |

## 验证

```bash
cd 联合产出
python3 solve_linalg.py     # 6/6 自校验通过
python3 make_report.py      # 生成报告
```

## 诚实边界

- 搭档半边未执行；不代写画像、不伪造教学记录。
- 6 道题是示例题，不是搭档提供的真实课程题。
- 没有 PDF 排版；报告是 Markdown。
- 已知限制：eigen 只支持有理根；自校验不覆盖排版错误。
