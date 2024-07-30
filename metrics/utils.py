from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from numpy.random import randint
import numpy as np


def plot_multi_bars(dic, alpha = 0.5):
    
    fig,ax = plt.subplots()

    keys = dic.keys()

    legend_boxes = []
    
    for i,key in enumerate(keys):
    
        values = dic[key]
        
        for j,value in enumerate(values):
        
            position = i + 0.8*j/len(values) - 0.4
            width = 0.8/len(values) - 0.4
            color = 'C'+str(i)
            
            ax.add_patch(Rectangle((position - width/2, 0), width, value, color=color, alpha=alpha))

        color_box = mpatches.Patch(color=color, label='Example Legend', alpha=alpha)
        legend_boxes.append(color_box)
            
    plt.legend(handles=legend_boxes, loc='upper right', frameon=True)

    plt.show()
    



'''
for s in save:
    dmg_sample = randint(1, 7, 1000)
    
    avg_dmg = np.mean(dmg_sample)
    sorted = np.sort(dmg_sample)
    good_dmg = np.mean(sorted[-int(len(dmg_sample)*0.25):])
    bad_dmg = np.mean(sorted[:int(len(dmg_sample)*0.25)])
    
    position = s + 0.8*i/n_options - 0.4
    width = 0.8/n_options - 0.4
    color = 'C'+str(i)
    
    ax.add_patch(Rectangle((position - width/2, bad_dmg), width, good_dmg-bad_dmg, color=color, alpha=alpha))
    x = [position - width/2, position + width/2]
    y = [avg_dmg, avg_dmg]
    plt.plot(x, y, color=color)

color_box = mpatches.Patch(color=color, label='Example Legend', alpha=alpha)
legend_boxes.append(color_box)
        
plt.legend(handles=legend_boxes, loc='upper right', frameon=True)

'''