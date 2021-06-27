## 凸优化问题

#### 问题描述

考虑一个一般优化问题（primal problem）：
$$
\begin{align}
&\min_{x} &f(x) &\\
&\mathrm{subject\ to} & h_{i}(x)\leq 0 & \quad i=1,\cdots,m \\
&&l_{j}(x)=0& \quad j=1,\cdots,r
\end{align}
\tag{primal}
$$
该优化问题对应的 *feasible set* $C$ 定义为：
$$
C:=\{x:h_{i}(x)\leq 0,\forall i=1,\cdots,m\ \&\& \ l_{j}(x)=0,\forall j=1,\cdots,r\}
$$
*最优点（optimal point）* $x^{*}$ 定义为满足下式的点：
$$
f(x^{*})=\inf\{x\in C:f(x)\},x^{*}\in C
$$
*最优集（optimal set）* 定义为最优点的集合。优化问题 $\text{(primal)}$ 对应的 Lagrangian 为：
$$
L(x,u,v)=f(x)+\sum_{i=1}^{m}u_{i}h_{i}(x)+\sum_{j=1}^{r}v_{j}l_{j}(x)
$$
Lagrangian Dual 为：
$$
g(u,v)=\min_{x}L(x,u,v)
$$
Lagrangian Dual Problem 可以表述为：
$$
\begin{align}
&\max_{u,v}&g(u,v) &\\
&\textrm{subject to}&u_{i}\geq0 & \quad i=1,\cdots,m
\end{align}
\tag{dual}
$$
**凸优化问题**

对于一般优化问题 $\text{(primal)}$，如果 $f,h_{i}$ 为凸函数，$l_{j}$ 关于 $x$ 为仿射函数，那么我们称这个优化问题为凸优化问题。



#### 相关性质

- 对偶问题总是凸的，i.e. $g$ 总是一个凸函数
- 设原问题的最优值为 $f^{*}$，对偶问题的最优值为 $g^{*}$，那么总是满足*弱对偶性*，i.e. $f^{*}\geq g^{*}$。

- 凸优化问题有如下性质：
  - 每个局部最优点也是全局最优点
  - 最优集是一个凸集
  - 如果目标函数是严格凸函数，最优点至多只有一个

#### 相关判别条件

**slater's condition**

如果一般优化问题 $\text{(primal)}$ 是凸优化问题，且存在一个 $x^{*}$ 满足严格 feasible 条件，i.e. 
$$
x^{*}\in C\ \&\ h_{i}(x^{*})<0,\forall i=1,\cdots,m
$$
那么*强对偶性*成立，i.e. $f^{*}=g^{*}$。

**Karush–Kuhn–Tucker conditions**

一般优化问题 $\text{(primal)}$ 对应的KKT 条件为：

- stationarity
  $$
  \nabla_{x}f(x)+\sum_{i=1}^{m}u_{i}\nabla_{x}h_{i}(x)+\sum_{j=1}^{r}v_{j}\nabla_{x}l_{j}(x)=0
  $$
  i.e.
  $$
  \nabla_{x}L(x,u,v)=0
  $$

- complementary slackness
  $$
  u_{i}\cdot h_{i}(x)=0,i=1,\cdots,m
  $$

- primal feasibility
  $$
  \begin{align}
  h_{i}(x)\leq 0 \quad &i=1,\cdots,m \\
  l_{j}(x)=0 \quad &j=1,\cdots,r
  \end{align}
  $$

- dual feasibility
  $$
  u_{i}\geq 0 \quad i=1,\cdots,m
  $$

**KKT 条件的一些性质**

*zero duality gap*: 如果 $x^{*}$ 为原优化问题的一个解（满足约束条件），$u^{*},v^{*}$ 为对偶问题的一个解，且我们有 $f(x^{*})=g(u^{*},v^{*})$，那么我们称三元组 $x^{*},u^{*},v^{*}$ 拥有 zero duality gap。（此时该三元组也达到问题最优）。

**Property** 如果三元组 $x^{*},u^{*},v^{*}$ 拥有 zero duality gap，那么这个三元组同时满足 KKT 条件。

**proof** 根据定义，我们有
$$
\begin{align}
f(x^{*})&=g(u^{*},v^{*}) \\
				&=\min_{x}L(x,u^{*},v^{*})\\
				&\leq L(x^{*},u^{*},v^{*})\tag{1.1}\\
				&\leq f(x^{*})\tag{1.2}
\end{align}
$$
可知上式中的不等号均为等号。将 $(1.1)$ 的不等号换为等号我们可以得知 KKT 条件中的 stationarity 成立。将 $(1.2)$ 中的不等号换为等号后可得：
$$
\sum_{i=1}^{m}u_{i}h_{i}(x^{*})+\sum_{j=1}^{r}v_{j}l_{j}(x^{*})=0
$$
结合上 $x^{*}$ 的约束条件，我们可以得知 KKT 条件中的 complementary slackness 成立。由于三元组分别为原问题和对偶问题的解，我们可知 feasibility 条件成立

**endproof**

**Property** 如果原优化问题中的 $f,h_{i}$ 为凸函数，$l_{j}$ 为仿射函数，且三元组 $x^{*},u^{*},v^{*}$ 满足 KKT 条件，那么 $x^{*},u^{*},v^{*}$ 分别为原问题与对偶问题的最优点。

**proof** 由于原问题是凸优化问题，$L(x,u^{*},v^{*})$ 为关于 $x$ 的凸函数。由 KKT 条件中的 stationarity，我们可知
$$
L(x^{*},u^{*},v^{*})=\min_{x}L(x,u^{*},v^{*})
$$
由上式，我们可得
$$
\begin{align}
g(u^{*},v^{*}) &=\min_{x}L(x,u^{*},v^{*})\\
							 &= L(x^{*},u^{*},v^{*})\\
							 &= f(x^{*})+\sum_{i=1}^{m}u_{i}h_{i}(x^{*})+\sum_{j=1}^{r}v_{j}l_{j}(x^{*})\\
							 &=f(x^{*})
\end{align}
$$
如果 $\exist x'\in C,f(x')<f(x^{*})$，我们有
$$
\begin{align}
f(x')&<g(u^{*},v^{*}) \\
				&=\min_{x}L(x,u^{*},v^{*})\\
				&\leq L(x',u^{*},v^{*})\\
				&\leq f(x')
\end{align}
$$
矛盾。所以 $x^{*}$ 为原问题的最优点。如果 $\exist u'\geq0,v'$ 满足 $g(u',v')>g(u^{*},v^{*})$，那么违反弱对偶性，矛盾。所以 $u^{*},v^{*}$ 为对偶问题的最优点。

**endproof**

## SVM 算法

## SMO 算法

序列最小优化算法 (Sequential Minimal Optimization, SMO) 是为了解决 SVM 对偶优化问题而提出的，它使用了*坐标上升算法*的思想，比一般的二次规划解法有更高的收敛速度。

#### 坐标上升算法 (Coordinate Ascent)

在SMO算法之前，还是需要总结下坐标上升算法，因为SMO算法的思想与坐标上升算法的思想类似。

坐标上升算法每次通过更新多元函数中的一维，经过多次迭代直到收敛来达到优化函数的目的。简单的讲就是不断地选中一个变量做一维最优化直到函数达到局部最优点。

假设我们需要求解的问题形式为(类似我们SVM的对偶形式):
$$
\max_{\alpha}W(\alpha_{1},\alpha_{2},\cdots,\alpha_{N})
$$
算法过程可以描述为

```python
# 返回使得f取到最大值的x
def argmax(f):
    ...
    return x

while abs(alpha_n - alpha_o) > epsilon
    alpha_o = alpha_n
    for i in range(len(alpha_o)):
    		def f(x):
            temp = alpha_o
          	temp[i] = x
            return w(temp)
        alpha_n[i] = argmax(f)
```

#### SVM 的对偶形式

考虑 SVM 的 Lagrangian Dual Problem：
$$
\begin{align}
&\arg\max_{\alpha}\sum_{i=1}^{N}\alpha_{i}-\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}y_{i}y_{j}\alpha_{i}\alpha_{j}K(x_{i},x_{j}) \\
&\text{subject to}\ 0\leq\alpha_{i}\leq C,\ \sum_{i=1}^{N}\alpha_{i}y_{i}=0
\end{align}
$$
其中 $C$ 为惩罚参数。同时我们

#### 优化变量的选择

**第一个变量 $\alpha_{1}$**

**第二个变量 $\alpha_{2}$** 

#### SMO中的缓存 trick

