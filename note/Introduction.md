# 黑洞超辐射与引力波拍
超轻标量场可以通过超辐射机制从 Kerr 黑洞中提取能量和角动量, 并呈指数增长. 类似于氢原子, 标量场的不同模式用 $\{n, l, m\}$ 标记, 它与黑洞形成黑洞–标量凝聚体系统, 并可以辐射连续的引力波.

在以往的研究中, 通常只考虑一种模式, 这样辐射的引力波是单色连续的, 与旋转中子星辐射的引力波存在简并性. 而当多种模式并存时, 由于能级的微小差别, 引力波拍出现并打破这种简并性.

# 传统的连续引力波搜索方法
如果有一个连续引力波信号波形模型, 最佳的算法是根据模型在相关参数空间内对整个数据集进行简单的匹配过滤 [1]. 但是，如果在全天空范围对1年的数据进行搜索, Ref. [1] 估计可以用 50 亿台计算机运行 50 亿年来完成搜索--正好赶在太阳变成红巨星并吞噬地球之前. 显然这种方法是不可行的.

Ref. [1] 总结了80篇已发表文章中所述的297次连续引力波搜寻, 这些搜索的方法都具有分层的(hierarchical)结构:
1. Coherent stage: 首先, 将将整个数据集(时间跨度为 T)按时间划分为 N 个片段, 每个片段的相干时间满足 $T_{coh} \ll T$. 对于每个片段单独进行匹配滤波, 所需匹配滤波器的数量 $\propto (T_{coh})^\delta$ ($\delta\gtrsim 6$). 因此尽可能地减小相干时间即可减小计算成本.
2. Semi-coherent stage: 其次, 选择一种算法处理来自N段的匹配滤波结果, 以寻找在整个观测时间内都存在的信号. 需要注意的是, 当双星绕行轨道下降或中子星自旋下降时, 连续引力波的频率会降低, 因此不同片段中相位会发生变化.

这两个阶段都有很丰富的算法. 其中 Ref. [2]的算法, [WEAVE pipeline](note/WEAVE_pipeline.md), Ref. [3]称其为“state-of-the-art”.

# Deep neural networks
半相干方法虽然提高了计算效率但牺牲了灵敏度, 那有没有其它方法在不牺牲灵敏度但也能提高计算效率? Ref. [3] 提出使用 deep neural networks (DNN) 来搜索. 一旦训练完成, DNN 进行预测的速度非常快, 通常只需要几毫秒就可以处理一个数据样本. 这对于需要快速分析大量数据的连续引力波搜索非常有利. 

鉴于连续引力波信号持续时间长且频率窄, **Ref. [3]使用频域数据而不是时域数据作为输入.**

但灵敏度仍然被牺牲了, 即便使用多个探测器, 灵敏度相对于全相干匹配滤波(使用Ref. [2]的算法)降低了 ~7%(低频) 到 ~51%(高频) [4].

# 目前的想法
1. 继续研究 Ref. [2]的算法, 使其适用于引力波拍, 最后和 DNN 比较;
2. 修改深度学习模型并使用频域数据作为输入. 在时域上, 我本来想的是“拍”可以作为一个额外的特征, 从而提高对连续引力波的灵敏度. 但改到频域上, 好像这种额外的特征就不存在了, 因为中子星辐射的引力波频率也不是单值.

# 参考文献
1. Wette, Karl. “Searches for Continuous Gravitational Waves from Neutron Stars: A Twenty-Year Retrospective.” Astroparticle Physics 153 (November 2023): 102880. https://doi.org/10.1016/j.astropartphys.2023.102880.
2. Wette, K., S. Walsh, R. Prix, and M. A. Papa. “Implementing a Semicoherent Search for Continuous Gravitational Waves Using Optimally Constructed Template Banks.” Physical Review D 97, no. 12 (June 28, 2018): 123016. https://doi.org/10.1103/PhysRevD.97.123016.
3. Dreissigacker, Christoph, Rahul Sharma, Chris Messenger, Ruining Zhao, and Reinhard Prix. “Deep-Learning Continuous Gravitational Waves.” Physical Review D 100, no. 4 (August 7, 2019): 044009. https://doi.org/10.1103/PhysRevD.100.044009.
4. Dreissigacker, Christoph, and Reinhard Prix. “Deep-Learning Continuous Gravitational Waves: Multiple Detectors and Realistic Noise.” Physical Review D 102, no. 2 (July 6, 2020): 022005. https://doi.org/10.1103/PhysRevD.102.022005.