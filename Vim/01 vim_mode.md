# Vim 模式 


## 普通模式

- 大小写：
    - 反转大小写：`g~`
    - 转换为大小写：`gu`, `gU`，作用于行：`gugu`, `gUgU`
- 注释：
    - `gc{motion}`，例如 `gcc` 当前行，`gcap` 当前段落的注释状态，`gcG` 当前行到文章所有范围

### 文档中移动
#### 常见查找

- 光标位置与当前行行尾之间，查找指定的字符：`f{char}`, `;`, `,`
- 正向移动到下一个 `{char}` 所在之处的前一个字符：`t{char}`
- 反向移动到下一个 `{char}` 所在之处的后一个字符：`T{char}`
- 查找：`/{word}`（开动作，找到的字符在操作之外）
    - 配合命令：`d/ge<CR>`, `v/ge<CR>hd`

#### 文本对象

**文本对象**：两个字符组成，第一个是 `i` (inside) 或 `a` (around, all)，例如：
```
a), a}, a], a>, a', a", a`, at
i), i}, i], i>, i', i", i`, it
一对圆括号，一对花括号等
t:  XML 标签
```
应用：`citclick here<Esc>` 

#### 文本块
**文本块**：单词、句子和段落

**字串**

``` 
iw, iW, is, ip, aw, aW, as, ap
单词，字串，句子，段落
```

#### 位置标记
```
`m{a-zA-Z}` 设定当前光标的位置。
mm + `m 常用
```
- 命令：
```
`{a-zA-Z} 跳转回设定位置
`` 上次跳转前的位置（`m + `` = 原地）
`^ 上次插入的位置
`[, `] 上次修改或复制的起始或结束位置
`<, `> 上次高亮选区的起始或结束位置
```

## 插入模式

- 不离开插入模式退格键（通用）
    - `<C-h>` 前一个字符 = Backspace
    - `<C-w>` 前一个单词
    - `<C-u>` 删至行首

- 不离开插入模式粘贴寄存器中的文本
    - `<C-r>0`
        
### 插入-普通模式

在插入模式中执行一次普通模式指令：`<C-o>`，例如：
```
<C-o>zz：重绘屏幕，使当前行居于正中
```

## 可视模式

- 重新选择上一次的高亮选区：`gv`
### 列可视模式

使用 `<C-v>` 进入列块可视模式
- 同时往若干行插入文本
- 不局限于操作方形文本区域
    ```
    {start}
    <C-v>jj$
    A;
    <Esc>
    ```
## 命令行模式、Ex 命令
> 在命令行模式执行的命令称为 **Ex 命令**。

- Ex 命令据有*能够在多行上同时执行的能力*。
    ```vim
    :[range]operation
    ```

- 重复上一次命令：`@:`
    
### 定义范围 range
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
### 操作 operation

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

### 命令行窗口
- 按 `q:` 调出窗口
- 可以编辑历史命令，然后按 `@:` 重复上一次命令，如 `write| !ruby %`

### 运行 shell 程序
- 给命令加 `!` 前缀，如：`:!ls`
- 在 `shell` 中运行 `{cmd}`，读入命令的输出：`:read !{cmd}`
- 在 `shell` 中运行 `{cmd}`，以 `[range]` 作为标准输入：`:[range]write !{cmd}`
- 使用外部程序 `{filter}` 过滤指定的 `[range]`：`:[range]!{filter}`

### 批处理运行 Ex 命令
```
----------
batch.vim
%normal A: http://vimcasts.org
%normal yi"$p
%substitute/\v^[^\>]+\>\s//g
```
并运行：`:source batch.vim`


## 参考资料

1. [Practical Vim, Second Edition Edit Text at the Speed of Thought by Drew Neil](https://pragprog.com/titles/dnvim2/practical-vim-second-edition/)
