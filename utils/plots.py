import os
import numpy as np
import matplotlib.pyplot as plt

def plot_embedding_groups(dict_embed,
                          title = 'Embeddings',
                          legend_title = 'Groups',
                          fig_size = (12,12),
                          colors = None,
                          lgdn_loc = 'upper right',
                          save_image = None):
    _, ax = plt.subplots(figsize=fig_size)

    for idxc, key in enumerate(dict_embed.keys()):
        xy = np.array(dict_embed[key]['xy'])
        if colors:
            ax.scatter(xy[:,0], xy[:,1], label=key, color=colors[idxc], s=60)
        else:
            ax.scatter(xy[:,0], xy[:,1], label=key, s=60)
        for idx, text in enumerate(dict_embed[key].get('sentences', [])):
            ax.annotate(text, (xy[idx,0],xy[idx,1]), (xy[idx,0],xy[idx,1]), fontsize=15)

    lgnd = ax.legend(loc=lgdn_loc, title=legend_title, scatterpoints=1, fontsize=12, title_fontsize=12)
    for hdl in lgnd.legendHandles:
        hdl._sizes = [100]
    ax.set_facecolor('whitesmoke')
    plt.grid(color='lightgray', alpha=0.5)
    plt.title(title, size=20)
    if save_image:
        plt.savefig(save_image)
    plt.show()

def plot_embedding_groups_3d(dict_embed,
                             title = 'Embeddings',
                             legend_title = 'Groups',
                             angles = None,
                             fig_size = (12,12),
                             colors = None,
                             lgdn_loc = 'upper right',
                             save_image = None,
                             save_gif_dir = None):
    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111, projection='3d')
    # colors = ['blueviolet', 'orange', 'turquoise']

    for idxx, key in enumerate(dict_embed.keys()):
        xyz = np.array(dict_embed[key]['xyz'])
        if colors:
            ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], label=key, color=colors[idxx], s=60)
        else:
            ax.scatter(xyz[:,0], xyz[:,1], xyz[:,2], label=key, s=60)
        for idx, text in enumerate(dict_embed[key]['sentences']):
            ax.text(xyz[idx,0], xyz[idx,1], xyz[idx,2], text, zdir=None)

    lgnd = ax.legend(loc=lgdn_loc, title=legend_title, scatterpoints=1, fontsize=12, title_fontsize=12)
    for hdl in lgnd.legendHandles:
        hdl._sizes = [100]
    ax.set_facecolor('whitesmoke')
    if angles:
        ax.view_init(angles[0], angles[1])
    plt.grid(color='lightgray', alpha=0.5)
    plt.title(title, size=20)
    if save_image:
        plt.savefig(save_image)
    if save_gif_dir:
        for angle in range(0,360,2):
            if angles:
                ax.view_init(angles[0],angle)
            else:
                ax.view_init(30,angle)
            filename = os.path.join(f'{save_gif_dir}/', f'step_{angle:03d}.png')
            plt.savefig(filename)
        os.system(f'zip -mj {save_gif_dir}/figures.zip {save_gif_dir}/step_*.png')
    plt.show()
