# 把脚本里的所有关联的程序包、类、函数都 load 一下
from funs.main_test import *
# from main import *
from funs.utils import *

# 初始化数据生成 class
nsample_perepoch = 100  # 每个epoch的样本数
dataset_train = DatasetGenerator(snr=20, nsample_perepoch=nsample_perepoch)  # 训练数据集
dataset_test = DatasetGenerator(snr=20, nsample_perepoch=nsample_perepoch)  # 测试数据集

# 创建一个DataLoader
data_loader = DataLoader(dataset_train, batch_size=32, shuffle=True,)  # 训练数据加载器
test_iter = DataLoader(dataset_test, batch_size=32, shuffle=True,)  # 测试数据加载器

device_ids = [6,7]
device = torch.device(f'cuda:{device_ids[0]}')  # 使用第一个CUDA设备

# 模型和损失历史的输出路径
checkpoint_dir = './checkpoints_cnn/'

# 创建模型    
net, epoch, train_loss_history = load_model(checkpoint_dir)  # 加载模型

if len(device_ids) > 1: # 如果有多个GPU，则使用DataParallel
    print(f"Let's use {len(device_ids)} GPUs!")
    net = nn.DataParallel(net, device_ids=device_ids)
    
net.to(device);  # 将模型转移到设备上

# 优化器参数
lr = 0.001  # 学习率
total_epochs = 100  # 总的训练轮数
total_epochs += epoch  # 加上已经训练过的轮数
output_freq = 1  # 输出频率

# 训练模型
train(net, lr, nsample_perepoch, epoch, total_epochs,
      dataset_train, data_loader, test_iter,
      train_loss_history, checkpoint_dir, device, notebook=False)