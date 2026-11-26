# Git 基本教程与团队协作方法

> 适用对象：MUFFIN Lab 新手成员。目标是用最短路径跑通 clone、提交、分支、push、PR、同步和冲突处理。
>
> 团队规则：`playground/<个人>/` 可直推 `main`，但提交前必须执行 `git pull --rebase origin main`；`docs/`、`projects/`、根目录配置必须走“分支 → PR → 合并”。

---

## 0. 先记住三条底线

1. 不要 `force push main`。
2. 不要提交 `.exe`、`build/`、个人 `.vscode/` 配置、代理端口、PAT、密钥、大文件。
3. 文档一律 Markdown，不交 Word；`docs/notes/` 按技术主题命名，不按人名建目录。

---

## 1. 安装与身份配置

安装 Git 后，在终端检查：

```bash
git --version
```

首次配置身份。邮箱建议用 GitHub 账号邮箱：

```bash
git config user.name "你的名字"
git config user.email "你的GitHub邮箱"
```

查看配置：

```bash
git config --list
```

---

## 2. 克隆团队仓库

```bash
git clone https://github.com/MuffinLab-Org/dev-lab.git
cd dev-lab
git status
git branch
```

正常应看到当前分支为 `main`，工作区干净。

---

## 3. 日常最小闭环

每次开始写代码前先同步：

```bash
git switch main
git pull --rebase origin main
```

然后新建自己的分支。即使是个人练习，也建议用分支跑通流程：

```bash
git switch -c <类型>/<简短说明>

# 例如：
git switch -c onboarding/<github-id>
git switch -c docs/git-tutorial
```

修改文件后查看状态和差异：

```bash
git status
git diff
```

只添加自己改的文件，不要 `git add .` 盲加：

```bash
git add <文件路径>
git commit -m "type(scope): summary"
```

示例：

```bash
git add docs/notes/git-tutorial.md
git commit -m "docs(notes): add git tutorial"
```

首次推送分支：

```bash
git push -u origin <分支名>
```

之后同一分支再推送：

```bash
git push
```

---

## 4. 提交信息格式

统一使用：

```text
type(scope): summary
```

常用 `type`：

- `feat`：新功能
- `fix`：修复
- `docs`：文档
- `chore`：配置、杂项
- `refactor`：重构

示例：

```text
docs(notes): add git tutorial
feat(playground): add hello world in C
fix(playground): correct sensor output format
```

---

## 5. 分支与 PR 流程

团队仓库中 `docs/`、`projects/`、根目录配置走 PR：

```bash
git switch main
git pull --rebase origin main
git switch -c docs/git-tutorial

# 修改文件
git status
git diff
git add docs/notes/git-tutorial.md docs/notes/README.md
git commit -m "docs(notes): add git tutorial and navigation entry"
git push -u origin docs/git-tutorial
```

然后在 GitHub 上开 PR 到 `main`。PR 标题建议：

```text
[Docs] 添加 Git 基本教程与团队协作方法
```

PR 描述写清楚：

- 目的
- 改了哪些文件
- 如何验收
- 是否只改自己负责范围

合并后同步本地：

```bash
git switch main
git pull --rebase origin main
git branch -d docs/git-tutorial
```

---

## 6. 同步与 rebase

推荐始终使用：

```bash
git pull --rebase origin main
```

如果本地有未提交修改，先提交或暂存：

```bash
git stash
git pull --rebase origin main
git stash pop
```

查看历史：

```bash
git log --oneline --graph --decorate -10
```

---

## 7. 冲突处理

`git pull --rebase` 或 PR 出现冲突时：

```bash
git status
```

找到 `both modified` 的文件，手动编辑保留正确内容，删除冲突标记：

```text
<<<<<<< HEAD
=======
>>>>>>>
```

解决后：

```bash
git add <冲突文件>
git rebase --continue
```

如果搞乱了，可以中止：

```bash
git rebase --abort
```

不要在不理解的情况下 `force push`。个人分支确需更新远端时，才可谨慎使用：

```bash
git push --force-with-lease
```

`main` 分支禁止强推。

---

## 8. 443 / HTTPS 连接失败排错

先确认远程地址：

```bash
git remote -v
```

如果本机代理可用，只给当前仓库配置，不要随便全局配置：

```bash
git config http.proxy http://127.0.0.1:<端口>
git ls-remote origin
```

成功后可取消：

```bash
git config --unset http.proxy
```

检查是否残留全局代理：

```bash
git config --global --get http.proxy
```

注意：不要把代理端口、PAT、密码写进 remote URL，也不要提交到仓库。

---

## 9. 常见错误速查

| 现象 | 处理方式 |
| --- | --- |
| `fatal: not a git repository` | 当前目录不是仓库，`cd` 到 `dev-lab`。 |
| `rejected non-fast-forward` | 远端有新提交，先执行 `git pull --rebase origin main`，再 `push`。 |
| `CONFLICT` | 按第 7 节解决，不要直接删文件。 |
| `Authentication failed` | 检查 GitHub 凭据，使用 Git Credential Manager 或 PAT，不要把 PAT 写入 URL。 |
| `nothing to commit` | 没有暂存改动，先 `git status` 看是否已提交或没保存。 |
| 空文件夹不会被 Git 跟踪 | 需要放一个 `.gitkeep` 或真实文件。 |

---

## 10. 速查表

```bash
git status
git diff
git add <文件>
git commit -m "type(scope): summary"
git push -u origin <分支>
git switch main
git pull --rebase origin main
git switch -c <分支>
git log --oneline --graph --decorate -10
git stash
git stash pop
git rebase --continue
git rebase --abort
```

---

## 11. 团队协作边界

- `playground/<个人>/`：个人练习区，可直推 `main`，但推送前必须 rebase 同步。
- `docs/`：公共文档区，必须走分支 + PR。
- `projects/`：联合项目区，必须走 Issue + 分支 + PR。
- 不修改别人 `playground/` 目录。
- 文档首行写 `作者：@github-id`，方便追溯，但不按作者建目录。
