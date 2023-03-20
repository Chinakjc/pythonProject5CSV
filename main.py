import re
import matplotlib.pyplot as plt
import imageio
import numpy as np

# 读取数据文件
with open('5.dat', 'r') as f:
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
fig, ax = plt.subplots(figsize=(6, 6), dpi=100, facecolor='black')
ax.set_facecolor('black')
for coords in coords_list:
    ax.scatter([coord[0] for coord in coords], [coord[1] for coord in coords], color='white')
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 30)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Orbits')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid()
    fig.canvas.draw()
    img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    images.append(img)
    ax.clear()
plt.close(fig)

imageio.mimsave('animation.gif', images, fps=20)

imageio.mimsave('animation.gif', images, duration=0.05)

