import re
import matplotlib.pyplot as plt
import imageio
import numpy as np


def csv2D(data_name,fps,duration):
    # lire donnees
    with open(data_name, 'r') as f:
        lines = f.readlines()

    # coordonnes
    coords_list = []
    for line in lines[1:]:
        coords_str = re.findall(r'\((.*?)\)', line)
        coords = [tuple(map(float, coord.split())) for coord in coords_str]
        coords_list.append(coords)

    plt.switch_backend('agg')
   # generer gif
    images = []
    fig, ax = plt.subplots(figsize=(6, 6), dpi=100, facecolor='black')
    ax.set_facecolor('black')
    for coords in coords_list:
        ax.scatter([coord[0] for coord in coords], [coord[1] for coord in coords], color='white')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
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
    imageio.mimsave('animation2D.gif', images, fps = fps,duration=duration)


def csv3D(data_name,fps,duration):
    # lire donnees
    with open(data_name, 'r') as f:
        lines = f.readlines()

    # coordonnees
    coords_list = []
    for line in lines[1:]:
        coords_str = re.findall(r'\((.*?)\)', line)
        coords = [tuple(map(float, coord.split())) for coord in coords_str]
        coords_list.append(coords)

    # generer 3d gif
    images = []
    plt.switch_backend('agg')
    fig = plt.figure(figsize=(6, 6), dpi=100,facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    for coords in coords_list:
        ax.scatter([coord[0] for coord in coords], [coord[1] for coord in coords],
                   [coord[2] for coord in coords], color='white')
        ax.set_xlim3d(-10, 10)
        ax.set_ylim3d(-10, 10)
        ax.set_zlim3d(-10, 10)
        ax.set_title('Orbits')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.grid()
        plt.draw()
        plt.pause(0.01)

        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        images.append(img)
        ax.clear()

    plt.close(fig)

    imageio.mimsave('animation3D.gif', images, fps=fps, duration=duration)



csv3D(data_name='6.dat',fps=60,duration=0.1)
csv2D(data_name='5.dat',fps=60,duration=0.02)
''''# 读取数据文件
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
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
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


imageio.mimsave('animation.gif', images, fps = 30,duration=0.02)'''

