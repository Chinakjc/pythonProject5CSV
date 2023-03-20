import matplotlib.pyplot as plt
import imageio
import os

import re
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import imageio
import re

import numpy as np

# 读取数据文件
with open('5.dat') as f:
    lines = f.readlines()

# 解析坐标数据
coords_list = []
for line in lines[1:]:
    coords_str = re.findall(r'\((.*?)\)', line)
    coords = [tuple(map(float, coord.split())) for coord in coords_str]
    coords_list.append(coords)

plt.switch_backend('agg')
# 生成gif图像
images = []
for coords in coords_list:
    fig = plt.figure(figsize=(6, 6), dpi=100)
    plt.scatter([coord[0] for coord in coords], [coord[1] for coord in coords])
    plt.xlim(0, 30)
    plt.ylim(0, 30)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Orbits')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.draw()
    plt.pause(0.01)
    img = np.array(fig.canvas.renderer.buffer_rgba())
    images.append(img)
    plt.clf()

imageio.mimsave('animation.gif', images, duration=0.1)




 # 删除临时文件
for file in os.listdir('.'):
    if file.startswith('frame_') and file.endswith('.png'):
        os.remove(file)
