# 会话 1 教案：Git 三件事 + 跑通一个脚本

> 状态：**教案已备，尚未执行**。执行后在本文件末尾补"实际记录"（时间、截图/录屏、对方卡点）。
> 教学方：十三　｜　学习方：搭档L　｜　时长：45 分钟

## 一、目标（学完能做什么）

1. 能独立把一个文件提交到本地 git 仓库，并解释 `git status` 的三行输出。
2. 能跑通 `solve_linalg.py`，看懂 `results_linalg.json` 的一个字段。

## 二、课前准备

- 安装 Git（Windows：git-scm.com；macOS：`xcode-select --install`）
- 准备一个空文件夹 `c3c-practice/`
- 把 `solve_linalg.py` 拷进去

## 三、教学步骤（45 分钟）

| 时间 | 内容 | 演示/练习 |
|---|---|---|
| 0–5 | 为什么需要版本控制：改坏了能回去 | 口头 + 一个"覆盖保存"的反例 |
| 5–15 | `git init` / `git status` / `git add` / `git commit` | 我演示一遍，对方跟着做 |
| 15–25 | 改一个文件，看 `git diff`，再提交 | 对方独立操作，我在旁边只回答"为什么" |
| 25–35 | 跑 `python3 solve_linalg.py`，打开 `results_linalg.json` | 对方改一道题的数字，观察结果变化 |
| 35–45 | 复盘：哪一步最容易忘？ | 对方用自己的话复述三件事 |

## 四、验收（对方独立完成）

- [ ] 在 `c3c-practice/` 里 `git init`，提交至少 2 次
- [ ] 能说出 `git status` 里 "untracked / modified / staged" 的区别
- [ ] 改一个矩阵数字，重新运行脚本，能指出 JSON 里哪一行变了

## 五、常见卡点（预判）

| 卡点 | 提示方式 |
|---|---|
| 忘记 `git add` 就 commit | 让他看 `git status` 的提示，不直接给命令 |
| Python 命令是 `python` 还是 `python3` | 先跑 `python --version` / `python3 --version` |
| 路径里有空格 | 用引号包住路径 |

## 六、实际记录（执行后填写）

- 实际时间：＜待填＞
- 录屏/截图：＜待填＞
- 对方卡住的地方：＜待填＞
- 我讲错/漏讲的地方：＜待填＞
- 下次要改的：＜待填＞
