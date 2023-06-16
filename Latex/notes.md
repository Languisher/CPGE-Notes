# Notes on Latex

## 文字排版

1. 更改*无序列表*符号和*有序列表*的标号方式，见章节 3.5 
    ```latex 
    % 方法 1
    \begin{itemize}
        \item[+] Non-numbered list. 
        \item[Itemize] Non-numbered list. 
    \end{itemize}

    % 方法 2
    \renewcommand{\labelitemi}{\textbullet}
    \renewcommand{\labelitemii}{\textendash} % itemize 中 itemize
    \renewcommand{\labelenumi}%
        {\Alph{enumi}>}
    ```

2. 排版表格：[点击这个链接](https://www.tablesgenerator.com)
3. 插入单张图片：使用模版，需要提前申明 `\usepackage{float}` 浮动体包
    ```latex
    \begin{figure}[H] % h:当前位置, t:顶部, b:底部, p:浮动页
	\centering
	\includegraphics[width=0.8\textwidth]{file directory}
	\caption{caption}
	\label{fig:caption}
    \end{figure}
    ```
4. 插入更多图片和浮动题：见章节 3.9

## 数学公式

1. 可伸展的箭头 `\xleftarrow` 和 `\xrightarrow`
    $$
    a\xleftarrow{x+y+z} b
    $$

2. 多行公式
    - 长公式 `multline` 环境，它允许用 \\ 折行，将 公式编号放在最后一行。多行公式的首行左对齐，末行右对齐，其余行居中。
    - 多行公式 `align` 环境，按等号对齐，用 `&` 分隔，用 `\\` 换行
    - 多行公式 `gather` 环境，只罗列等式不按等号对齐

3. 矩阵排版分式使用 `\dfrac` 命令，行紧贴着时使用 `\\[8pt]` 调节间距
4. 调节被积函数和微元之间关系使用 `\,` 
    $$
    \int_a^b f(x) \, dx
    $$

5. 调节符号尺寸：`\displaystyle` 行间公式尺寸, `textstyle` 行内公式尺寸

## Tikz 绘图

详情请见 7.2 节
1. 点
    - 直角坐标系 `(x,y)`，极坐标 `(angle:radius)`
    - 命名点：`\coordinate (name) at (coordinate);`
2. 直线
    - 直线：`\draw (coordinate) -- (coordinate);`
    - 箭头：`\draw[->, thick, color] (coordinate) -- (coordinate);`
3. 矩形、圆、椭圆、正弦曲线
    - 矩形：`\draw (coordinate) rectangle (coordinate);`
    - 圆：`\draw (coordinate) circle (radius);`
    - 椭圆：`\draw (coordinate) ellipse (x radius and y radius);`
    - 正弦曲线：`\draw (coordinate) sin (coordinate);`
4. 网格、函数图像
    - 网格：`\draw[step=1cm, gray, very thin] (coordinate) grid (coordinate);`
    - 函数图像：`\draw[domain=0:2*pi] plot (\x, {sin(\x r)});`
5. 填充
    - 填充：`\fill[color] (coordinate) -- (coordinate) -- (coordinate) -- cycle;`
    - 填充：`\filldraw[fill=yellow,draw=red] (coordinate) -- (coordinate) -- (coordinate) -- cycle;`
6. 节点
    ```latex
        \node[options] (name) at (coordinate) {text};
        \draw (name) -- (name);
    ```
7. 线条类型 `solid/dashed/dotted/dash dot/dash dot dot`
  
## 排版模版

[template-of-latex](template.tex)

## Reference 

[一份(不太)简短的 LATEX2ε 介绍](assets/lshort-zh-cn.pdf)