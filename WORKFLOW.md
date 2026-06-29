# 团队 Git / GitHub 工作流 SOP

适用人数：3 人小团队。每个功能/修复走独立分支，经 PR + 1 人 review 后合并进 main。

---

## 核心原则

- **main 永远是可以运行的稳定版本**，任何人不直接往 main 上提交
- **一个分支只做一件事**，做完就合并，不攒着
- **所有改动都经过 PR**，至少 1 个非本人 approve 才能合并

---

## 分支命名规范

```
feat/功能描述        # 新功能，例如 feat/用户登录
fix/问题描述         # 修 bug，例如 fix/结算金额错误
chore/任务描述       # 升级依赖、调整配置等，例如 chore/升级eslint
docs/文档描述        # 只改文档，例如 docs/补充readme
```

---

## 完整流程

### 第一步：开始一个新任务前，先同步最新的 main

```bash
git checkout main
git pull
```

> 养成习惯：每次开始新任务前先拉一下，避免后面出现不必要的冲突。

### 第二步：建一个新分支并切过去

```bash
git checkout -b feat/你的功能名
```

> `-b` 是"新建并切换"的意思。建完之后你就在这个分支上工作了，不会影响 main。

### 第三步：写代码（或让 Claude Code 写）

在这里开发功能、修 bug，随时可以查看状态：

```bash
git status        # 看哪些文件被改了
git diff          # 看具体改了什么（按 q 退出）
```

### 第四步：提交改动（三条命令，顺序不能乱）

```bash
git add .                          # 把所有改动放进暂存区
git commit -m "feat: 描述做了什么"  # 在本地存一个快照
git push -u origin feat/你的功能名  # 推到 GitHub（第一次加 -u，之后只需 git push）
```

**提交信息格式：**`类型: 简短描述`，例如：
```
feat: 添加邮箱注册流程
fix: 修复结算页面金额计算错误
chore: 升级 eslint 至 v9
docs: 更新部署说明
```

### 第五步：在 GitHub 上开 PR

push 完之后去 GitHub 仓库页面，会看到黄色提示条，点 **"Compare & pull request"**。

PR 描述里填清楚（模板会自动出现）：
- 改了什么
- 为什么改
- 怎么测的

然后指定一个同事来 review，等他 approve 后点 **"Merge pull request"**，再点 **"Delete branch"** 删掉已合并的分支。

### 第六步：本地清理

```bash
git checkout main
git pull                        # 把刚合并的内容同步到本地
git branch -d feat/你的功能名   # 删掉本地分支
```

---

## 让 Claude Code 做这些事

### 前提：装好 GitHub CLI 并登录

**Windows**（在普通终端里跑，不是在 Claude Code 里）：
```bash
winget install --id GitHub.cli
```
安装完关掉终端重开，再运行：
```bash
gh auth login
```

**Mac**：
```bash
# 先装 Homebrew（如果还没装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 再装 GitHub CLI
brew install gh

# 登录
gh auth login
```

按提示选择浏览器授权，登录你的 GitHub 账号即可。Claude Code 之后就能直接操作 GitHub。

### 怎么给 Claude Code 指令

直接用自然语言说，例如：

> 帮我建一个 fix/结算bug 的分支，修复 `checkout.py` 里的金额计算问题，提交信息用 "fix: 修复结算金额计算错误"，然后 push 到 GitHub。

Claude Code 会自动执行：建分支 → 改代码 → git add → git commit → git push。

PR 也可以让它开：

> 帮我基于刚才的改动在 GitHub 上开一个 PR，标题是"修复结算金额错误"，描述里写清楚改了什么。

---

## ⚠️ 重要提醒：同一个 repo 开多个 session，先让 AI 建 worktree

**什么情况会遇到：** 你在同一个 repo 目录下同时开了**两个 Claude Code session**，想各自处理不同的任务。

**坑在哪：** 一个 git 目录同一时间只能停在一个分支上。两个 session 在同一个目录里，一个切分支、另一个的未提交改动就会被踩乱甚至丢失。

**你要做的只有一件事：** 开第二个 session 时，第一句话就让它给自己建一个独立的 worktree，例如：

> 我们在同一个 repo 里并行工作，你先用 git worktree 给自己新建一个独立的工作目录再开始，不要直接在当前目录切分支。

AI 会自己跑 `git worktree add` 建好独立目录、切过去工作，干完再清理。你不用记任何命令——**只要记得提醒它先开 worktree**。

> 一句话：**同一个 repo 想并行多开 session，第一句话就让 AI 自己开 worktree。**

---

## 常见问题

### push 失败：`Connection was reset`
网络问题，需要走代理。打开 Clash Verge 查看混合端口号（一般是 7890），然后：
```bash
git config --global http.proxy http://127.0.0.1:7890
git push
```

### push 失败：`rejected - non-fast-forward`
远端 main 有你没有的新 commit，先拉下来再推：
```bash
git pull
git push
```

### PR 合并时有冲突
说明你和同事改了同一个文件的同一行。解决方法：
```bash
git checkout main
git pull
git checkout feat/你的分支
git merge main        # 这一步会提示冲突
```
打开冲突文件，找到 `<<<<<<<` / `=======` / `>>>>>>>` 三行标记，手动或让 Claude Code 决定保留哪个版本，然后：
```bash
git add .
git commit
git push
```

### 提交信息写错了（还没 push）
```bash
git commit --amend -m "新的正确信息"
```

### 想撤销已经合并进 main 的改动
即使 PR 已经 close 了也能撤，`git revert` 会新建一个抵消 commit，原历史不会丢：
```bash
git revert <commit的hash>    # hash 在 GitHub 的 commit 列表里能找到
git push
```

---

## 快速检查清单

开始前：
- [ ] `git checkout main && git pull`（先同步）
- [ ] `git checkout -b 类型/描述`（建新分支）

提交前：
- [ ] `git status` 确认改动范围
- [ ] 提交信息符合格式 `类型: 描述`

PR 前：
- [ ] 描述里写了"改了什么 / 为什么 / 怎么测"
- [ ] 指定了 reviewer

合并后：
- [ ] GitHub 上删掉远端分支
- [ ] 本地 `git pull` + `git branch -d 分支名`
