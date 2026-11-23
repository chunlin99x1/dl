import torch
from torch.utils.tensorboard import SummaryWriter
import math

# 1. 初始化 Writer，指定日志保存目录（默认是 'runs' 文件夹）
writer = SummaryWriter(log_dir='runs/experiment_1')

# 2. 模拟训练过程，记录 Loss 和 Learning Rate
for step in range(100):
    # 模拟一个逐渐下降的 Loss
    loss = 1.0 / (step + 1) + 0.1 * math.sin(step)
    lr = 0.01 * (0.95 ** step)

    # 将数据写入 TensorBoard
    writer.add_scalar('Loss/train', loss, step)
    writer.add_scalar('Learning Rate', lr, step)

# 3. (可选) 记录模型结构或图片（以时序波形为例）
# 假设你有一个形状为 [1, 3, 100] 的张量，代表 3 个传感器的 100 个时间步
fake_sensor_data = torch.randn(1, 3, 100)
writer.add_image('Sensor_Data', fake_sensor_data, global_step=0)

# 4. 关闭 Writer
writer.close()
print("数据已写入 runs/ 目录，请启动 TensorBoard 查看！")