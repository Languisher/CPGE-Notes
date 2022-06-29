## Nvim 使用手册

[TOC]

### NERDTree - file explorer

输入 `:NERDTree` 或是输入 [F3]（自定义按键）打开

#### Directory operation

1. 打开/关闭所有的文件/文件夹

   | Default Key | Description       |
   | ----------- | ----------------- |
   | o           | 打开文件、目录    |
   | O           | Open recursively  |
   | x           | 关闭目录          |
   | X           | Close recursively |

2. 在目前目录下【创建，移动，删除，复制，重命名】文件/文件夹；复制路径；用 Finder 打开

   输入`m`，然后输入

   | Default Key | Description    |
   | ----------- | -------------- |
   | a           | 创建           |
   | m           | 移动           |
   | d           | 删除           |
   | c           | 复制、重命名   |
   | p           | 复制路径       |
   | f           | 用 Finder 打开 |

3. __打开目前目录的上一级目录__：`u`

4. __将根目录改变为目前目录__ : `C`

#### File node operations

1. __打开文件__

   ```arcade
   i       竖直窗口 一个新窗口打开选中文件，并跳到该窗口
   gi      竖直窗口 一个新窗口打开选中文件，但不跳到该窗口
   s       水平窗口 一个新窗口打开选中文件，并跳到该窗口
   gs      水平窗口 一个新 窗口打开选中文件，但不跳到该窗口
   ```

3. __How to reveal or show current file in nerdtree window?__ [F2]（自定义）

   `:NERDTreeFind` : reveal the position of current file in the file tree.

### Vim-Commentary - make comments

输入 `gcc`，自动将该行转为注释。

### Vim-Fugitive - git in vim

1. `git status`

   The `:Gstatus` command opens a status window. The contents closely resemble the output from running `git status` in the shell, but fugitive makes the window interactive. 

   | command   | affect                                    |
   | --------- | ----------------------------------------- |
   | `-`       | add/reset file (works in visual mode too) |
   | `<Enter>` | open current file in the window below     |
   | `p`       | run `git add –patch` for current file     |
   | `C`       | invoke `:Gcommit`                         |

2. 
