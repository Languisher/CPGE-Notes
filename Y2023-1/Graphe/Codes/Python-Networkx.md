# Python Networkx

Last update : **22 Septembre, 2023**, *Shanghai*

**Brandon Lin**

------



## 简介

### 什么是NetworkX？

NetworkX是用于研究图论和网络的Python库，内置了常用的图与复杂网络分析算法，可以方便的进行复杂网络数据分析、仿真建模等工作。

### 导入

```python
import network as nx
```

## 基本语法

### 添加和删除

#### 创建和清除图

下列语句用来创建一个没有节点和边的空图

```python
G = nx.Graph()# 无多重边无向图
G = nx.DiGraph()# 无多重边有向图
G = nx.MultiGraph()# 有多重边无向图
G = nx.MultiDiGraph()# 有多重边有向图
```

下列语句用来清除图

```python
G.clear()
```

#### 添加和删除节点

下列语句均可以添加节点

```python
# 添加一个节点a
G.add_node('a')
# 添加节点列表
G.add_nodes_from([2, 3])
# 添加node的Iterable对象
N = nx.path_graph(10)
G.add_nodes_from(N)
# 添加其他的图表、图形作为节点
H = nx.path_graph(10)  # 返回由10个节点的无向图
G.add_nodes_from(H)
```

※：注意下列两种语句的区别

```python
G.add_node("spam")        # 添加节点"spam"
G.add_nodes_from("spam")  # 添加4个节点: 's', 'p', 'a', 'm'
```

下列语句用来删除节点

```python
G.remove_node(1)    # 删除指定节点
G.remove_nodes_from(['b','c','d','e'])    # 删除集合中的节点
```

#### 添加和删除边

下列语句均可以添加边

```python
# 添加一条从节点11到节点12的边
F.add_edge(11,12) 
# 添加边列表
G.add_edges_from([(1, 2), (1, 3)])
# 利用包裹传参添加边
e=(13,14)        # e是一个元组
F.add_edge(*e) # 这是python中解包裹的过程
# 利用ebunch (container of edges) 添加边
H = nx.path_graph(10)       # 返回由10个节点的无向图
F.add_edges_from(H.edges()) # 不能写作F.add_edges_from(H) ※:注意和节点区分
```

下列语句用来删除边

```python
G.remove_edge() # 删除单个边
G.remove_edges_from(ebunch) # 删除ebunch中指定的所有边
```

#### 添加一个闭环

```python
# 添加一个节点为f,g,h,j的闭环
G.add_cycle(['f', 'g', 'h', 'j']) 
```

### 访问

#### 对节点相关的访问

```python
nodes(G)  # 在图节点上返回一个迭代器
number_of_nodes(G)  # 返回图中节点的数量
all_neighbors(graph, node)  # 返回图中节点的所有邻居
non_neighbors(graph, node)  # 返回图中没有邻居的节点
common_neighbors(G, u, v)  # 返回图中两个节点的公共邻居

```

#### 对边相关的访问

```python
edges(G[, nbunch]) # 返回与nbunch中的节点相关的边的视图
number_of_edges(G) # 返回图中边的数目
non_edges(graph) # 返回图中不存在的边
G[1][2] # 用下标访问边
G.edges[1,2] # 用下标访问边
```

#### 对邻近的访问

※：对于无向图，邻接迭代可以看到每个边两次。

```python
G.adjacency() # 返回所有节点的迭代器
```

eg：

```python
G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
[(n, nbrdict) for n, nbrdict in G.adjacency()]
# [(0, {1: {}}), (1, {0: {}, 2: {}}), (2, {1: {}, 3: {}}), (3, {2: {}})]
```

### 属性

#### 图的属性

```python
# 图的属性
G = nx.Graph(day='Monday')    #可以在创建图时分配图的属性
print(G.graph)

G.graph['day'] = 'Friday'     #也可以修改已有的属性
print(G.graph)

G.graph['name'] = 'time'      #可以随时添加新的属性到图中
print(G.graph)

#输出：
#{'day': 'Monday'}
#{'day': 'Friday'}
#{'day': 'Friday', 'name': 'time'}
```

#### 节点属性

```
# 节点的属性
G = nx.Graph(day='Monday')
G._node()

G.add_node(1, index='1th')             #在添加节点时分配节点属性
# print(G.node(data=True))  #TypeError: 'dict' object is not callable
print(G.node) 
#{1: {'index': '1th'}}


G.node[1]['index'] = '0th'             #通过G.node[][]来添加或修改属性
print(G.node)
# {1: {'index': '0th'}}


G.add_nodes_from([2,3], index='2/3th') #从集合中添加节点时分配属性
print(G.node)
# {1: {'index': '0th'}, 2: {'index': '2/3th'}, 3: {'index': '2/3th'}}

PYTHON
```

#### 边的属性

```
#边的属性
import networkx as nx

G = nx.Graph(day='manday')
G.add_edge(1,2,weight=10)                    #在添加边时分配属性
print(G.edges(data=True))
#[(1, 2, {'weight': 10})]

G.add_edges_from([(1,3), (4,5)], len=22)     #从集合中添加边时分配属性
print(G.edges(data='len'))
# [(1, 2, None), (1, 3, 22), (4, 5, 22)]

G.add_edges_from([(3,4,{'hight':10}),(1,4,{'high':'unknow'})])
print(G.edges(data=True))
# [(1, 2, {'weight': 10}), (1, 3, {'len': 22}), (1, 4, {'high': 'unknow'}), (3, 4, {'hight': 10}), (4, 5, {'len': 22})]


G[1][2]['weight'] = 100000                   #通过下标来添加或修改属性
print(G.edges(data=True))
# [(1, 2, {'weight': 100000}), (1, 3, {'len': 22}), (1, 4, {'high': 'unknow'}), (3, 4, {'hight': 10}), (4, 5, {'len': 22})]

PYTHON
```

※：特殊属性 `weight` 应该是数字，因为它被需要加权边缘的算法使用

### 有向图

#### 有向图和无向图互转

有些算法只适用于有向图，而另一些算法不适用于有向图。实际上，将有向图和无向图集中在一起的趋势是危险的。所以有必要进行两者的相互转换。

下列语句和两种图的互转有关

```
#有向图转化成无向图

H=DG.to_undirected()
#或者
H=nx.Graph(DG)

#无向图转化成有向图

F = H.to_directed()
#或者
F = nx.DiGraph(H)

PYTHON
```

#### 有向图添加、删除和访问

有向图的添加、删除和访问和无向图基本上是一样的，在这里不做赘述。

### 图形分析

#### 介数中心性

```
betweenness_centrality(G,k=None,normalized=True,weight=None,endpoints=False, seed=None)
#参数说明
#G--网络图。
#k--如果k不是“无”，则使用k节点样本来估计中间值。k的值<=n，其中n是图中的节点数。值越大，近似值越高。
#归一化--如果为真，则中间值通过 2/((n-1)(n-2)) 对于图，以及 1/((n-1)(n-2)) 对于有向图，其中 n 是g中的节点数。
#权重--如果没有，则认为所有边权重相等。否则将保留用作权重的边缘属性的名称。
#端点--如果为真，则在最短路径计数中包括端点。
#seed--随机数生成状态的指示器。见 Randomness . 请注意，这仅在k不是“无”时使用。

PYTHON
```

更多的算法可见下列站点：

- https://www.osgeo.cn/networkx/reference/algorithms/index.html
- https://networkx.github.io/documentation/stable/reference/algorithms/index.html

### 图片绘制

可以利用matplotlib库进行图形可视化，常见的语句如下：

| draw (g) [, pos, ax] )                           | 用matplotlib绘制图g。   |
| ------------------------------------------------ | ----------------------- |
| draw_networkx (g) [, pos, arrows, with_labels] ) | 使用matplotlib绘制图g。 |
| draw_networkx_nodes (G，POS) [, nodelist, ...] ) | 绘制图G的节点。         |
| draw_networkx_edges (G，POS) [, edgelist, ...] ) | 绘制图G的边。           |
| draw_networkx_labels (G，POS) [, labels, ...] )  | 在图G上绘制节点标签。   |
| draw_networkx_edge_labels (G，POS) [, ...] )     | 绘制边缘标签。          |

除此之外，也可以通过下列语句进行指定节点的**布局**

| bipartite_layout (g,node) [, align, scale, ...] ) | 将节点定位在两条直线上。         |
| ------------------------------------------------- | -------------------------------- |
| circular_layout (g) [, scale, center, dim] )      | 节点在一个圆环上均匀分布         |
| planar_layout (g) [, scale, center, dim] )        | 没有边缘交点的节点分布           |
| random_layout (g) [, center, dim, seed] )         | 在单位正方形内均匀随机定位节点。 |
| shell_layout (g) [, nlist, scale, center, dim] )  | 节点在同心圆上分布               |

下列给出了一些图片绘制中可能用到的**参数**

| pos(dictionary, optional) | 图像的布局，可选择参数；如果是字典元素，则节点是关键字，位置是对应的值。如果没有指明，则会是spring的布局； |
| ------------------------- | ------------------------------------------------------------ |
| arrows                    | 布尔值，默认True; 对于有向图，如果是True则会画出箭头         |
| with_labels:              | 节点是否带标签（默认为True）                                 |
| ax：                      | 坐标设置，可选择参数；依照设置好的Matplotlib坐标画图         |
| nodelist                  | 一个列表，默认G.nodes(); 给定节点                            |
| edgelist                  | 一个列表，默认G.edges();给定边                               |
| node_siz                  | 指定节点的尺寸大小(默认是300)                                |
| node_color                | 指定节点的颜色 (默认是红色，可以用字符串简单标识颜色，具体可查看手册) |
| node_shape:               | 节点的形状（默认是圆形，用字符串’o’标识，具体可查看手册）    |
| alpha                     | 透明度 (默认是1.0，不透明，0为完全透明)                      |
| cmap                      | Matplotlib的颜色映射，默认None; 用来表示节点对应的强度       |
| vmin,vmax                 | 浮点数，默认None;节点颜色映射尺度的最大和最小值              |
| linewidths                | [None\|标量\|一列值];图像边界的线宽                          |
| width                     | 边的宽度 (默认为1.0)                                         |
| edge_color                | 边的颜色(默认为黑色)                                         |
| edge_cmap                 | Matplotlib的颜色映射，默认None; 用来表示边对应的强度         |
| edge_vmin,edge_vmax       | 浮点数，默认None;边的颜色映射尺度的最大和最小值              |
| style                     | 边的样式(默认为实现，可选： solid\|dashed\|dotted,dashdot)   |
| labels                    | 字典元素，默认None;文本形式的节点标签                        |
| font_size                 | 节点标签字体大小 (默认为12)                                  |
| font_color                | 节点标签字体颜色（默认为黑色）                               |
| font_weight               | 字符串，默认’normal’                                         |
| font_family               | 字符串，默认’sans-serif’                                     |

### 图表读写

详见下列站点：

- https://www.osgeo.cn/networkx/reference/readwrite/index.html
- https://networkx.github.io/documentation/stable/reference/readwrite/index.html

## 参考资料

- https://www.osgeo.cn/networkx/index.html
- https://networkx.github.io/documentation/stable/
- https://blog.csdn.net/yyl424525/article/details/102539703

------

Networkx 是 Python 的一个包，用于构建和操作复杂的图结构，提供分析图的算法。图是由顶点、边和可选的属性构成的数据结构，顶点表示数据，边是由两个顶点唯一确定的，表示两个顶点之间的关系。顶点和边也可以拥有更多的属性，以存储更多的信息。

对于networkx创建的无向图，允许一条边的两个顶点是相同的，即允许出现自循环，但是不允许两个顶点之间存在多条边，即出现平行边。边和顶点都可以有自定义的属性，属性称作边和顶点的数据，每一个属性都是一个 Key:Value 对。

```python
import network as nx
```

## 基础操作

### 创建图

在创建图时，可以通过 `help(g)` 来获得图的帮助文档。

```python
g = nx.Graph() # 创建空的无向图
g = nx.DiGraph() # 创建空的有向图
```

### 绘制图

使用 `nx.draw(graph)` 函数

```python
import matplotlib.pyplot as plt
nx.draw(G, with_labels="True")
plt.show()
```

#### 指定绘制图形形状

```python
nx.draw_circular(G)
```

### 图的顶点

图中的每一个顶点Node都有一个关键的ID属性，用于唯一标识一个节点，ID属性可以整数或字符类型；顶点除了ID属性之外，还可以自定义其他的属性。

#### 向图中增加顶点

在向图中增加顶点时，可以一次增加一个顶点 `add_node()`，也可以一次性增加多个顶点 `add_nodes_from(list)`，顶点的 ID 属性是必需的。

在添加顶点之后，可以通过 `g.nodes()` 函数获得图的所有顶点的视图，返回 NodeView对象；如果为`g.nodes(data=True)`，那么返回的是 NodeDataView 对象，该对象不仅包含每个顶点的ID属性，还包括顶点的其他属性。

```python
g.add_node(1)
g.add_node("coin")
g.add_nodes_from([2,3,4])
g.nodes() # NodeView((1,2,3,4))
```

- 在向图中添加顶点时，除ID属性之外，也可以向顶点中增加自定义的属性，例如，名称属性，权重属性

    ```python
    g.add_node(1, name='n1', weight=1)
    g.add_node(2, name='n2', weight=1.2)
    ```

    

#### 查看顶点的属性

通过属性 `_node` 获得图的所有顶点和属性的信息，`_node` 属性返回的是一个字典结构，字典的Key属性是顶点的ID属性，Value属性是顶点的其他属性构成的一个字典。

```python
g._node
# {1: {'name': 'n1', 'weight': 1}, 2: {'name': 'n2', 'weight': 1.2}, 3: {}, 4: {}}
g.nodes(data=True)
```

可以通过顶点的ID属性来查看顶点的其他属性：

```python
g.node[1]
# {'name': 'n1', 'weight': 1}
g.node[1]['name']
# 'n1 new'
```

通过 `g.nodes(condition)`，按照特定的条件来查看顶点：

```python
list(g.nodes(data=True))
# [(1, {'time': '5pm'}), (3, {'time': '2pm'})]
```

#### 删除顶点

通过 `remove_node(node_ID)` 函数删除图的顶点，由于顶点的ID属性能够唯一标识一个顶点，通常删除顶点都需要通过传递ID属性作为参数。同理，使用 `remove_nodes_from(node_list)` 删除一个列表的参数。

```
g.remove_node(node_ID)
g.remove_nodes_from(nodes_list)
```

#### 更新顶点

更新图的顶点，有两种方式，第一种方式使用字典结构的`update` 函数，第二种方式是通过索引来设置新值：

```
>>> g._node[1].update({'name':'n1 new'})
>>> g.node[1]['name']='n1 new'
{1: {'name': 'n1 new', 'weight': 1}, 2: {'name': 'n2', 'weight': 1.2}, 3: {}, 4: {}}
```

#### 删除顶点的属性

使用 `del` 命令删除顶点的属性

```
del g.nodes[1]['room'] 
```

#### 检查是否存在顶点

检查一个顶点是否存在于图中，可以使用 `n in g` 方式来判断，也可以使用函数：

```
g.has_node(n)
```

### 图的边

图的边用于表示两个顶点之间的关系，因此，边是由两个顶点唯一确定的。为了表示复杂的关系，通常会为边增加一个权重weight属性；为了表示关系的类型，也会设置为边设置一个关系属性。

#### 向图中增加边

通过 `add_edge(*(node1,node2))` 向图中添加一条边，也可以通过 `add_edges_from(list)` 向图中添加多条边；在增加边时，也可以为不同的边设置不同的属性：

```python
g.add_edge(*(2,3)) # 请注意 * 解包
g.add_edges_from([(1,2),(1,3)])
g.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
g.edges() # EdgeView([(1, 2), (1, 3), (2, 3)])
```

- 在添加边时，如果顶点不存在，那么 `networkx` 会自动把相应的顶点加入到图中。

- 可以向边中增加属性，例如，权重，关系等：

    ```python
    g.add_edge(1, 2, weight=4.7, relationship='renew')
    ```

- 由于在图中，边的权重weight是非常有用和常用的属性，因此，networkx模块内置以一个函数 `add_weighted_edges_from(list)`，专门用于在添加边时设置边的权重，该函数的参数是三元组，前两个字段是顶点的ID属性，用于标识一个边，第三个字段是边的权重：

    ```python
    g.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
    ```

#### 查看边的属性

查看边的属性，就是查看边的数据 (data)，查看所有边及其属性：

```python
g.edges(data=True) # EdgeDataView([(1, 2, {}), (1, 3, {}), (2, 3, {})])
```

查看特定的边的信息有两种方式：

```python
g[1][2]
g.get_edge_data(1,2)
# {'weight': 0.125, 'relationship': 'renew', 'color': 'blue'}
```

#### 删除边

边是两个顶点的ID属性构成的元组，通过 `remove_edge(edge)` 且 `edge=(node1,node2)` 来标识边，进而从图中找到边：

```python
g.remove_edge(edge)
g.remove_edges_from(edges_list)
```

#### 更新边的属性

通过边来更新边的属性，由两种方式，一种是使用 `update` 函数，一种是通过属性赋值来实现：

```
g[1][2]['weight'] = 4.7
g.edge[1][2]['weight'] = 4
g[1][2].update({"weight": 4.7})
g.edges[1, 2].update({"weight": 4.7})   
```

#### 删除边的属性

通过 del命令来删除边的属性

```
del g[1][2]['name']
```

#### 检查边是否存在

检查一条边是否存在于图中

```
g.has_edge(1,2)
```

## 图的属性

图的属性主要是指相邻数据，节点和边。

**1，adj**

ajd返回的是一个AdjacencyView视图，该视图是顶点的相邻的顶点和顶点的属性，用于显示用于存储与顶点相邻的顶点的数据，这是一个只读的字典结构，Key是顶点，Value是顶点的属性数据。

```
>>> g.adj[1][2]
{'weight': 0.125, 'relationship': 'renew', 'color': 'blue'}
>>> g.adj[1]
AtlasView({2: {'weight': 0.125, 'relationship': 'renew', 'color': 'blue'}, 3: {'weight': 0.75}})
```

**2，edges**

图的边是由边的两个顶点唯一确定的，边还有一定的属性，因此，边是由两个顶点和边的属性构成的：

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
>>> g.edges
EdgeView([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
>>> g.edges.data()
EdgeDataView([(1, 2, {'weight': 0.125, 'relationship': 'renew', 'color': 'blue'}), 
(1, 3, {'weight': 0.75}), 
(2, 3, {'weight': 8}), 
(2, 4, {'weight': 1.2}), 
(3, 4, {'weight': 0.375})])
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

EdgeView仅仅提供边的信息，可以通过属性g.edges或函数g.edges()来获得图的边视图。

EdgeDataView提供图的边和边的属性，可以通过EdgeView对象来调用data()函数获得。

**3，nodes**

图的顶点是顶点和顶点的属性构成的

```
>>> g.nodes
NodeView((1, 2, 3, 4))
>>> g.nodes.data()
NodeDataView({1: {'name': 'n1 new', 'weight': 1}, 2: {'name': 'n2', 'weight': 1.2}, 3: {}, 4: {}})
```

NodeView 通过属性g.nodes或函数g.nodes()来获得。

NodeDataView提供图的边和边的属性，可以通过NodeView对象来调用data()函数获得。

**4，degree**

对于无向图，顶点的度是指跟顶点相连的边的数量；对于有向图，顶点的图分为入度和出度，朝向顶点的边称作入度；背向顶点的边称作出度。

通过g.degree 或g.degree()能够获得DegreeView对象，

## 五，图的遍历

 图的遍历是指按照图中各顶点之间的边，从图中的任一顶点出发，对图中的所有顶点访问一次且只访问一次。图的遍历按照优先顺序的不同，通常分为深度优先搜索（DFS）和广度优先搜索（BFS）两种方式。

**1，查看顶点的相邻顶点**

查看顶点的相邻顶点，有多种方式，例如，以下代码都用于返回顶点1的相邻顶点，g[n]表示图g中，与顶点n相邻的所有顶点：

```
g[n]
g.adj[n]
g.neighbors(n)
```

其中，g.neighbors(n)是g.adj[n]的迭代器版本。

**2，查看图的相邻**

该函数返回顶点n和相邻的节点信息：

```
>>> for n, nbrs in g.adjacency():
...     print(n)
...     print(nbrs)
```

**3，图的遍历**

深度优先遍历的算法：

- 首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的相邻顶点；
- 当当前顶点没有未访问过的相邻顶点时，则回到上一个顶点，继续试探别的相邻顶点，直到所有的顶点都被访问过。

深度优先遍历算法的思想是：从一个顶点出发，一条路走到底；如果此路走不通，就返回上一个顶点，继续走其他路。

广度优先遍历的算法：

- 从顶点v出发，依次访问v的各个未访问过的相邻顶点；
- 分别从这些相邻顶点出发依次访问它们的相邻顶点；

广度优先遍历算法的思想是：以v为起点，按照路径的长度，由近至远，依次访问和v有路径相通且路径长度为1,2...，n的顶点。

在进行图遍历时，需要访问顶点的相邻顶点，这需要用到adjacency()函数，例如，g是一个无向图，n是顶点，nbrs是顶点n的相邻顶点，是一个字典结构

```
for n,nbrs in g.adjacency(): 
    print (n, nbrs)
    for nbr,attr in nbrs.items():
        # nbr表示跟n连接的顶点，attr表示这两个点连边的属性集合
        print(nbr,attr）
```

## 六，绘制Graph

使用networkx模块draw()函数构造graph，使用matplotlib把图显示出来：

```
nx.draw(g)

import matplotlib.pyplot as plt
plt.show()
```

修改顶点和边的颜色：

```
g = nx.cubical_graph()
nx.draw(g, pos=nx.spectral_layout(g), nodecolor='r', edge_color='b')
plt.show()
```

完整的示例如下面的代码所示：

![复制代码](https://common.cnblogs.com/images/copycode.gif)

```
from matplotlib import pyplot as plt
import networkx as nx
g=nx.Graph()
g.add_nodes_from([1,2,3])
g.add_edges_from([(1,2),(1,3)])
nx.draw_networkx(g)
plt.show()
```

![复制代码](https://common.cnblogs.com/images/copycode.gif)

## 七，计算每个顶点的PageRank值

每个顶点的PageRank（简称PR）值，是访问顶点的概率，可以通过networkx.pagerank()函数来计算，该函数根据顶点的入边和边的权重来计算顶点的PR值，也就是说，PR值跟顶点的入边有关，跟入边的weight（权重）属性有关：

```
pagerank(g, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)
```

常用参数注释：

- g：无向图会被转换为有向图，一条无向边转换为两条有向边；
- alpha：阻尼参数，默认值是0.85，取值范围为 0 到 1, 代表从图中某一特定点指向其他任意点的概率；
- weight：默认值是weight，表示使用edge的weight属性作为权重，如果没有指定，那么把edge的权重设置为1；

**1，举个例子**

例如，创建一个有向图，由三个顶点（A、B和C），两条边（A指向B，A指向C），边的权重都是0.5

```
g=nx.DiGraph()
g.add_weighted_edges_from([('A','B',0.5),('A','C',0.5)])
print( nx.pagerank(g))
#{'A': 0.259740259292235, 'C': 0.3701298703538825, 'B': 0.3701298703538825}
```

修改边的权重，并查看顶点的PR值：

```
g['A']['C']['weight']=1
print( nx.pagerank(g))    
# {'A': 0.259740259292235, 'C': 0.40692640737443164, 'B': 0.3333333333333333}
```

**2，查看各个顶点的PR值**

根据图来创建PageRank，并查看各个顶点的PageRank值

```
pr=nx.pagerank(g)
#page_rank_value=pr[node]
for node, pageRankValue in pr.items():
    print("%s,%.4f" %(node,pageRankValue))
```

 

 