# Setup
### WEAVE pipeline 的基本原理
- 将数据划分为多个片段, 分别进行全相干匹配滤波;
- 将所有片段的结果组合起来进行半相干搜索.

优势: 将半相干搜索方法与最优模板生成技术相结合, 并实现了高效的缓存管理机制.
### $\mathcal{F}$-statistic
对于连续引力波的搜索, 所有的数据分析技术也都是基于匹配滤波: 首先建立一个信号的模型, 然后将计算的模板应用到实验数据上, 并计算一个统计量, 这个统计量会告诉我们数据符合信号的程度. $\mathcal{F}$-statistic 就是这样的一个统计量, 它可以让我们在没有振幅的先验知识时通过最大似然估计得到最合适的振幅参数.
### 相干参数空间矩阵 $\widetilde{\mathbf{g}}_\ell$
相干参数空间矩阵 $\widetilde{\mathbf{g}}_\ell$ 是用于描述数据片段 $\ell$ 中, 当信号参数发生微小变化时, F-statistic 统计量的变化程度. 矩阵元 $g_{ij}$ 表示当信号的第 i 个参数和第 j 个参数发生微小变化时, F-statistic 统计量的二阶偏导数.

半相干矩阵 $\hat{\mathbf{g}}$ 类似.
# WEAVE pipeline 的步骤
1. 运行前置程序 lalapps_WeaveSetup, 将待分析的连续数据划分为N个时间片段, 并提供起止时间.
2. 计算N个相干参数空间矩阵 $\widetilde{\mathbf{g}}_\ell$ 和半相干矩阵 $\hat{\mathbf{g}}$. 将矩阵存储在 setup 文件中, 并结束 lalapps_weavessetup.
3. 运行搜索程序 lalapps_Weave, 参数包括: setup 文件、待搜索的数据、天空参数空间、频率参数空间、最大相干和半相干失配度 (mismatch).
4. 将待搜索的数据载入内存, 准备半相干模板库 {$\lambda$} 和 N 个相干模板库 {$\lambda_l$}. 在半相干模板库 {$\lambda$} 上开始循环.
5. 对于每一个半相干模板 $\lambda$, 计算它的相关度, 在 N 个片段上进行循环.
6. 对于每一个片段, 计算在相干模板库 {$\lambda_l$} 中找到最接近半相干模板 $\lambda$ 的相干模板 $\lambda_l$.
7. 计算每个相干模板对应的 F-statistic 值.
8. 使用“相关性”机制管理缓存，仅保留必要的 F-statistic 值, 也就是说只保留相关性高的模板, 以减少内存使用量. 
9. 将每个片段的 F-statistic 值累加，得到该半相干模板 $\lambda$ 的最终结果.
10. 对所有候选信号进行排序, 并最后以 FITS 格式输出.
# WEAVE 的使用
Ref. [1] 原文说:
 > The implementation is freely available as part of the LALSUITE [60] gravitational-wave data-analysis library.

其中的 [60] 对应的网址为: https://wiki.ligo.org/DASWG/LALSuite. 在不登陆的情况下, 从该网站上没有找到 WEAVE 的相关说明.

利用搜索引擎, 似乎找到了实现 WEAVE 所涉及的两个程序: 
- LALAPPS_WEAVESETUP: lalapps_WeaveSetup has been renamed to lalpulsar_WeaveSetup. 源代码可能是 https://lscsoft.docs.ligo.org/lalsuite/lalpulsar/_weave_setup_8c_source.html
- LALAPPS_WEAVE: lalapps_Weave has been renamed to lalpulsar_Weave. 源代码可能是 https://lscsoft.docs.ligo.org/lalsuite/lalpulsar/_weave_8c_source.html

这些代码是用 C 写的, 于是又在 Jupyter 上利用 dir() 函数在 lalapps 和 lalpulsar 两个包里面搜索这两个函数, 但没有找到.
# 搜索所需要耗费的时间
据 Ref. [2] 所述, 使用完全相干匹配滤波(也就是N=1), 处理 $10^5$ s 和 $10^6$ s的数据, 在单个CPU核心上的搜索时间分别为 ~78天和 ~45000天!
# 参考文献
[1] K. Wette, S. Walsh, R. Prix, and M. A. Papa, Implementing a Semicoherent Search for Continuous Gravitational Waves Using Optimally Constructed Template Banks, Phys. Rev. D 97, 123016 (2018).

[2] C. Dreissigacker, R. Sharma, C. Messenger, R. Zhao, and R. Prix, Deep-Learning Continuous Gravitational Waves, Phys. Rev. D 100, 044009 (2019).
