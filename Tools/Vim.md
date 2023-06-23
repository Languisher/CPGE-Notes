
## 为什么使用 Vim
- 让你的整个开发过程手指不需要离开键盘，而且光标的移动不需要方向键使得你的手指一直处在打字的最佳位置。
- 方便的文件切换以及面板控制可以让你同时开发多份文件甚至同一个文件的不同位置。
- Vim 的宏操作可以批量化处理重复操作（例如多行 tab，批量加双引号等等）
- Vim 是很多服务器自带的命令行编辑器，当你通过 `ssh` 连接远程服务器之后，由于没有图形界面，只能在命令行里进行开发（当然现在很多 IDE 如 PyCharm 提供了 `ssh` 插件可以解决这个问题）。
- 异常丰富的插件生态，让你拥有世界上最花里胡哨的命令行编辑器。

## 如何学习 Vim
- 先阅读[这篇 tutorial](https://missing.csail.mit.edu/2020/editors/)，掌握基本的 Vim 概念和使用方式，不想看英文的可以阅读[这篇教程](https://github.com/wsdjeg/vim-galore-zh_cn)。
- 用 Vim 自带的 `vimtutor` 进行练习，安装完 Vim 之后直接在命令行里输入 `vimtutor` 即可进入练习程序。
- 最后就是强迫自己使用 Vim 进行开发，IDE 里可以安装 Vim 插件。
- 等你完全适应 Vim 之后新的世界便向你敞开了大门，你可以按需配置自己的 Vim（修改 `.vimrc` 文件），网上有数不胜数的资源可以借鉴。
- 如果你想对配置 Vim 有更加深入的了解，[_Learn Vim Script the Hard Way_](https://learnvimscriptthehardway.stevelosh.com/) 是一个很好的资源。

## Vim 笔记

### 命令行模式、Ex 命令
> 在命令行模式执行的命令称为 **Ex 命令**。

- Ex 命令据有*能够在多行上同时执行的能力*。
    ```vim
    :[range]operation
    ```

- 重复上一次命令：`@:`
    
#### 定义范围 range
以 `p(print)` 为例，可以替换为 `d(delete)` 等
```
:3p
:2,5p 形式：`:{start},{end}`
------
:.,$p 当前行到文末所有行
:%p 所有行 = :1,$p
------
:'<,'>p 高亮选取范围
------
:/<html>/,/<\/html>/p 用模式指定范围
------
:{address}+n 偏移修正
address 可以是：0, 1, $, ., 'm, '<, '>, %
```
#### 操作 operation

- 复制和移动行：`:[range]t {address}`, `:[range]m {address}`，不覆盖寄存器
    ```
    :t. = yyp
    :t$
    :'<,'>m$
    ```
- 执行普通模式命令 `:[range]normal {command}`
    ```
    :'<,'>normal . = 对高亮选取的每一行，执行普通模式下的 . 命令
    ```
- 把当前单词插入命令行（用于统一替换变量名等）：命令行状态下`<C-r><C-w>`
    ```
    *
    cw{variable name}<Esc>
    :%s//<C-r><C-w>/g
    ```

#### 命令行窗口
- 按 `q:` 调出窗口
- 可以编辑历史命令，然后按 `@:` 重复上一次命令，如 `write| !ruby %`
## 参考资料
1. [CS 自学指南](https://csdiy.wiki/必学工具/Vim/)
2. [Practical Vim, Second Edition Edit Text at the Speed of Thought by Drew Neil](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/)