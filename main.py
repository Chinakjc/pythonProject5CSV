import re
import matplotlib.pyplot as plt
import imageio
import numpy as np
import matplotlib as mpl
mpl.style.use('dark_background')

def csv2D(data_name,fps,duration,rayon):
    # lire donnees
    with open(data_name+'.dat', 'r') as f:
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
        ax.set_xlim(-rayon, rayon)
        ax.set_ylim(-rayon, rayon)
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
    imageio.mimsave('animation2D_'+data_name+'.gif', images, fps = fps,duration=duration)


def csv3D(data_name,fps,duration,rayon):
    # lire donnees
    with open(data_name+'.dat', 'r') as f:
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
    fig.patch.set_facecolor('black')  # add this line
    ax = fig.add_subplot(111, projection='3d')
    for coords in coords_list:
        ax.scatter([coord[0] for coord in coords], [coord[1] for coord in coords],
                   [coord[2] for coord in coords], color='white')
        ax.set_xlim3d(-rayon, rayon)
        ax.set_ylim3d(-rayon, rayon)
        ax.set_zlim3d(-rayon, rayon)
        ax.set_title('Orbits')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.grid()
        plt.draw()
        #plt.pause(0.01)

        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        img = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        images.append(img)
        ax.clear()

    plt.close(fig)

    imageio.mimsave('animation3D_'+data_name+'.gif', images, fps=fps, duration=duration)



csv3D(data_name='13',fps=60,duration=0.01,rayon=10)
#csv2D(data_name='11',fps=60,duration=0.01,rayon=10)

