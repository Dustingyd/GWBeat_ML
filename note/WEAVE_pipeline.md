# Setup
### $\mathcal{F}$-statistic
连续引力波搜索的基本挑战在于从相对嘈杂的数据中提取非常微弱的信号, 
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
