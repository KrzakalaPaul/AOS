from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from numpy.random import randint
import numpy as np


def plot_multi_bars(dic_of_dic, alpha = 0.5):
    # dic_of_dic[metric_name][unit_name]
    
    fig,ax = plt.subplots()

    legend_boxes = []
    
    for i,metric in enumerate(dic_of_dic):
        
        dic = dic_of_dic[metric]
        n_units = len(dic)
        
        for j,unit in enumerate(dic):
        
            position = i + 0.8*j/n_units + 0.2
            print(position)
            width = 0.8/n_units - 0.4
            value = dic[unit]
            color = 'C'+str(j)
            
            ax.add_patch(Rectangle((position - width/2, 0), width, value, color=color, alpha=alpha))

            if i == 0:
                color_box = mpatches.Patch(color=color, label=unit, alpha=alpha)
                legend_boxes.append(color_box)
        
    ax.set_xticks(ticks = [i + 0.5 for i in range(len(dic_of_dic))], labels = [metric for metric in dic_of_dic])
            
    plt.legend(handles=legend_boxes, loc='upper center', frameon=True)
    plt.xlim(0, len(dic_of_dic))
    plt.ylim(0, 1.2*max([max(dic_of_dic[metric].values()) for metric in dic_of_dic]))
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