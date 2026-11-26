# MuffinLab - Dev-Lab

> **MUFFIN**：**M**ulti-disciplinary **U**nified **F**ramework **F**or **I**nterdisciplinary **N**etworking（多学科交叉与互联统一框架）。
> 
> 这里是 MuffinLab 的开发实验室与协作沙盒区域。
## 目录结构

- `docs/`：团队文档、接口规范与 MUFFIN 架构探讨（公共区域，必须走 PR 合并）
- `playground/`：成员个人练习沙盒（允许随意折腾、试错）
- `projects/`：团队联合开发的实战项目（公共区域，必须走 PR 合并）

## 快速开始

刚加入团队？请先阅读以下资料：

1. 查阅 [Git 基本教程与团队协作方法](docs/notes/git-tutorial.md) 熟悉协作流程。
2. 浏览 [笔记导航目录](docs/notes/README.md) 了解当前知识库进度。
3. 前往 Issue 列表，寻找并认领你的首次 Onboarding 任务。

## 协作规范

1. **个人沙盒 (`playground/`)**：现阶段允许直接在主分支上修改和提交代码，但在推送前请务必执行 `git pull --rebase origin main` 同步最新代码。
2. **公共区域 (`docs/`, `projects/`)**：为保证代码与文档质量，请勿直接修改 `main` 分支。请新建分支（如 `docs/your-feature`），完成后发起 PR 由队长审查合并。
3. **个人目录命名**：请先在 `playground/` 目录下建一个**以你 GitHub ID 命名**的文件夹（全小写，避免空格），用于存放你的代码草稿或笔记。
4. **Commit 信息**：提交时，尽量用一句话说清楚你干了啥。推荐使用约定式提交格式，例如：`feat: add intro file for [name]`。
5. **修改注意事项**：请勿随意破坏他人代码或成果，在进行本地 `git` 操作时，留意不要误删别人的文件。

---

*Maintained by the MuffinLab Team.*
