
## shell 脚本文件

### 使用多个命令
- 分号分开 `;`
```bash
data ; who
```
### 创建文件

- 文件第一行指定需要使用的 shell，格式：
	```bash
	#!/bin/bash
	```

- 使 shell 能找到你的文件：
	- 将 shell 脚本文件所处的目录添加到 PATH 环境变量中
	- 在提示符中使用绝对或相对文件路径来引用 shell 脚本文件

- 若无运行权限：`chmod u+x filename`

### 显示消息

- 默认情况，不需要用引号将要现实的文本字符串划定出来，若用到了单引号或双引号，用另外一种来将其华顶起来
- 文本字符串与命令输出在同一行：`echo -n "..."`

### 变量

- **环境变量**
	- 查看当前环境变量列表：`set`
	- 在环境变量前加 `$` 使用，例如：`$PID`
	- `$` 前加 `\` 解读为真正的美元符

- **用户变量**
	- 不能出现空格！`var3=testing`
	- 仍然需要用美元符号引用

- **命令替换**：获取命令输出的信息，并赋给变量
	- 反引号或用 `$()` 格式
		```
		today=$(date +%y%m%d)
		```

### 输入输出重定向
- **输出重定向**：将命令的输出发送到一个文件中：`>`
- 将输出追加到文件：`>>`
- **输入重定向**：`<`

> 重定向符号指向数据流动的方向

```
command > outputfile
command < inputfile
```

- **内联输入重定向**：将数据作为输入导入命令中

### 管道
- **管道**：将命令输出直接重定向到另一个命令（同时运行，不是依次运行：一有前面命令的输出，立即执行后面命令的操作）
	- 最常见的用法发送至 `more` 命令显示内容

### 数学运算
- `expr` 命令：略
- 整数运算：用 `$[expression]` 格式，例如：`var1=$[2/10]`
- 浮点运算：bc 计算器，格式 `varialbe=$(echo "options; expression" | bc)`
	- `options` 中可以指定：
		- 小数位值，默认：`scale=0` 
  
	```bash
	var1=$(echo "scale=4; 3.44 / 5" | bc)
	echo The answer is: $var1
	```

- 内联输入重定向，`EOF` 标记重定向数据的起止：
	```bash
	variable=$(bc << EOF
	options
	statements
	expressions
	EOF)
	#------例子------
	vara=10
	varb=0.1
	var1=$(bc << EOF
	scale = 4
	a1 = $vara * $varb
	a2 = $vara / $varb
	a1 + a2
	EOF
	)
	```

### 退出脚本
- `$?` 查看上一个命令的退出码，缺省值是 0
- 可以通过设置 `exit NUM` 来返回自己的退出码

## 结构化命令

### if 语句

#### if-then
```bash
if command
then 
	commands
fi
```

#### if-then-else

```bash
if command
then
	commands
else
	commands
fi
```

#### 嵌套 if

```bash
if command1
then commands
elif command2
then
	commands
fi
```

### 条件

在`if` 判别的 `command` 处，我们可以做一些修改。

#### test 命令
```bash
test condition
```
- `if` 语句中除了普通 shell 命令，还可以用 `test` 命令，如果条件成立则正常退出、返回状态码 0；反之退出且返回非零状态码

也可以写成：（注意第一个方括号后、第二个方括号前的空格！）
```bash
if [ condition ]
then 
	commands
fi
```

#### 数值比较

- 注意：bash shell 只能处理整数运算
```bash
n1 -eq n2
n1 -ge n2 >=
n1 -gt n2 >
n1 -le n2 <=
n1 -lt n2 <
n1 -ne n2
```

- 如果要任意表达式，请使用：
	```bash
	if (( expression ))
	```
 
#### 字符串比较

- 字符串比较的时候，大写字母 < 小写字母，这与 `sort` 命令相反。
```bash
str1 = str2
str1 != str2
str1 < str2 请注意转义
str1 > str2
-n str1 长度是否为非0
-z str1 长度是否为0
```

- 使用**模式匹配**（正则表达式等），请使用：
	```bash
		if [[ expression ]]
	```
#### 文件比较
```bash
-d file #is exist && directory?
-e file #is exist?
-f file #is exist && file?
-r file #is exist && readable?
-s file #is exist && not empty?
-w file #is exist && writable?
-x file #is exist && executable?
-O file #is owner?
-G file #is group?
file1 -nt file2 #newer than
file1 -ot file2 #older then
```

#### 复合条件
```bash
[ condition1 ] && [ condition2 ]
[ condition1 ] || [ condition2 ]
```

### case 语句
- 多个 `elif` 语句情况
```bash
case variable in
pattern1 | pattern2)
	commands;; # 2个;;
pattern3) commands3;;
*) default commands;;
esac
```

### for 语句
- **列表**
	- 可以直接是一系列值（variable），例如 `Alabama Alaska Arizona`
	- 若有引号，转义或用另一种引号环绕
	- 变量定义 `list="Alab Alas Ariz"`
```bash
for var in list
do 
	commands
done
```

- 修改变量：
	- 增加值：`list=$list" variable"`