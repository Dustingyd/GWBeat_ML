# 目标
本项目旨在利用机器学习来搜索引力波拍(GW Beats), 这种引力波拍来源于超轻玻色子在旋转黑洞周围形成的凝聚体. 如果得到的是零结果, 则相应地给出不利的参数空间.
# 波形
see waveform.ipynb(筹)
# 进度
- [x] 波形生成
- [x] 深度学习测试(1s的数据)
   - [ ] 扩展到更长时间 ~$10^6$ s
   - [ ] 调研前人的方法 see [Introduction](note/Introduction.md)
- [ ] 使用匹配滤波法与机器学习的结果对比
- [ ] 利用LIGO数据进行搜索
# 代码来源
本项目波形生成的框架和机器学习的模型来自于王赫老师 (https://github.com/iphysresearch) 所主讲的“引力波数据探索：编程与分析实战训练营” (https://github.com/iphysresearch/GWData-Bootcamp).
