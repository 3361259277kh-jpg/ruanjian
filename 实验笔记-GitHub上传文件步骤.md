# 实验笔记：把文件上传到 GitHub 仓库

## 一、准备工作

1. 注册 GitHub 账号并完成邮箱验证。
2. 新建一个仓库，选择 Public，勾选 `Add a README file`。
3. 本机安装 Git，配置提交身份：

```bash
git config --global user.name  "GitHub 用户名"
git config --global user.email "注册邮箱"
```

## 二、方式一：网页上传（最简单）

1. 打开仓库主页，点击 **Add file → Upload files**。
2. 把文件拖入虚线框，或点击 `choose your files` 选择文件。
3. 想放进子目录，就在路径框中把 `仓库名 /` 改成 `仓库名 / 目录名 /`。
4. 下方 **Commit changes** 填写说明，例如 `add: 第一个实验文件`。
5. 点击绿色按钮 **Commit changes**，回到仓库首页即可看到文件。

单个文件上限 25 MB。适合实验报告、笔记、少量代码。

## 三、方式二：命令行上传（批量、需要本地改代码时）

```bash
git clone https://github.com/<用户名>/<仓库名>.git
cd <仓库名>

# 把文件复制进这个目录，然后：
git add .
git commit -m "add: 第一个实验文件"
git push origin main
```

以后修改文件的标准循环：

```bash
git pull
# 修改文件
git add .
git commit -m "update: 补充实验结论"
git push
```

## 四、上传到别人的仓库（共享仓库 / Fork）

- 已被加为 Collaborators：`git clone` 后建新分支提交，再发起 PR，不要直接推 `main`。
- 没有写权限：先点 **Fork**，克隆自己的副本，修改提交后向原仓库发起 PR。

```bash
git switch -c feat-<姓名>
git add .
git commit -m "add: <姓名>的实验文件"
git push -u origin feat-<姓名>
```

## 五、检查清单

1. 仓库首页能看到文件，点开能预览。
2. `Commits` 记录里作者是自己。
3. 中文文件名显示正常（文件保存为 UTF-8）。
4. 该走 PR 的改动没有直接推进 `main`。

## 六、常见错误

| 报错 | 原因与处理 |
| --- | --- |
| `Permission denied` | 没有写权限；接受 Collaborators 邀请，或改用 Fork 流程 |
| `Authentication failed` | 不能用账号密码，改用 PAT 或 SSH |
| `Updates were rejected` | 远端有新提交，先 `git pull --rebase` 再 `push` |
| `nothing to commit` | 文件没放进仓库目录，或被 `.gitignore` 忽略 |
| 网页上传后看不到文件 | 检查当前所在分支是否为 `main` |

## 七、实验记录

- 仓库地址：https://github.com/1308456432qaz-spec/ruanjian
- 首次上传文件：`README.md`、`实验笔记-GitHub上传文件步骤.md`、`hello.py`
- 上传方式：网页 `Upload files`
- 结论：文件可通过网页或命令行两种方式提交到远程仓库，提交后可在 `Commits` 记录中追溯。
