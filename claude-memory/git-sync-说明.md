# Obsidian 笔记库 —— 自动化 Git 同步说明(Claude 版)

> 用途:让 Claude 定期(或手动)安全地把 Obsidian 笔记库同步到 GitHub。
> 远端:https://github.com/danieldongzy-boop/Notes.git ,主分支 main。
> 这份说明供 Claude 执行;也可配成 Cowork 定时任务(Scheduled),每天自动跑。

## 执行目标

安全地暂存、提交、并推送正常的笔记与附件变更到 `origin/main`,
严格保护敏感信息与 EDA 仿真数据,遇到异常宁可跳过并报告,绝不破坏用户文件。

## 严格红线(任何情况下都不违反)

1. **绝不提交敏感文件**:`.git-credentials`、`.env`、`*.key`、`*.pem`、任何令牌/密码/认证文件。若在改动中发现,跳过并在报告中明确警告。(这些已在 .gitignore,但仍要主动核查。)
2. **绝不 force push**,绝不改写远端历史,绝不擅自删除分支或标签。
3. **绝不丢弃/覆盖/重置用户修改**。出现冲突立即中止 rebase/merge,保留用户文件,转为报告。
4. **不动 EDA 仿真数据**:`IC/Linux/**` 下的 `.state` / `ADE_state.info` / `.oalib` 等是真实 Cadence 工程文件,不做任何清理。
5. 默认不提交易变的 `.obsidian/workspace.json`(已在 .gitignore)。

## 执行步骤

### 1. 体检
- `git status`、`git branch -a`、`git remote -v`,确认在 vault 根、分支为 main、远端正确。
- 检查 `.git/index.lock`:若存在且确认无其它 git 进程在跑,说明后清理(`rm -f .git/index.lock`)。
- **完整性自检**:若 `git status` 显示几乎所有文件为 deleted(D),几乎可以肯定是 index 损坏,**不要提交**。用 `git reset HEAD`(不加 --hard)从 HEAD 重建 index,复查后再继续。

### 2. 安全暂存
- 逐一核查改动,排除红线清单里的敏感文件。
- 暂存正常的笔记/附件变更:`git add -A`(.gitignore 已挡掉敏感/易变/仿真文件;仍需人工扫一眼 `git status` 确认没有漏网的秘密)。
- 没有可提交内容则不创建空提交,直接进入拉取步骤。

### 3. 提交
- 提交信息:`chore(notes): nightly sync YYYY-MM-DD`(用当天日期)。

### 4. 与远端同步
- `git fetch --prune`。若出现瞬时网络错误 / Permission denied / 锁文件占用 / FETCH_HEAD/index.lock 相关错误:等待 5 秒后重试一次;重试成功则继续,不把首次瞬时失败当最终失败。
- 同步 main 与 origin/main。优先不改写历史的安全操作:
  - 本地 main 有新提交且远端也领先时,用 `git rebase origin/main`。
  - 冲突立即 `git rebase --abort`(或 merge --abort),保留用户文件,转报告。

### 5. 其它分支(保守)
- 只在分支用途清晰、内容确属本笔记库、且能无冲突整合时,才考虑合并到 main。
- 不确定 / 分支异常分叉 / 有冲突 → 跳过并报告,不擅自处理。

### 6. 推送
- 成功同步后 `git push origin main`(以及明确需要更新的正常分支)。
- 仅普通 push,绝不 `--force`。

## 报告(简洁中文)

结束时给出:提交了什么、拉取/rebase/合并情况、推送结果、重试情况、跳过项、
敏感�