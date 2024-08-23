import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from rules.fight import fight
from multiprocessing import Pool

class pairwise_metric():
    
    def __init__(self, samples = 1000):
        
        self.samples = samples
        self.metric_name = 'metric name'
    
    def get_metric(self, unit1, unit2):

        return 0
    
def matrix(units, metric):
    
    unit1_list = []
    unit2_list = []
    winrate_list = []
    
    for unit1 in units:
        for unit2 in units:
            unit1_list.append(unit1.name)
            unit2_list.append(unit2.name)
    
    with Pool() as p:
        winrate_list = p.starmap(metric.get_metric, [(u1, u2) for u1 in units for u2 in units])

    dataframe = pd.DataFrame({'unit1': unit1_list, 'unit2': unit2_list, metric.metric_name: winrate_list})
    dataframe = pd.pivot_table(dataframe, values = metric.metric_name, index = 'unit1', columns = 'unit2')
    
    print(dataframe)    
    fig,ax = plt.subplots()
    sns.heatmap(dataframe, ax = ax, vmin = 0, vmax = 1)
    plt.show()
    
    
class winrate(pairwise_metric):
    
    def __init__(self, samples=100, initiative = 'random'):
        
        self.samples = samples
        self.initiative = initiative
        self.metric_name = 'Winrate'
        
    def get_metric(self, unit1, unit2):
        
        win1 = 0
        win2 = 0
        
        for _ in range(self.samples):
            log_dic = fight(unit1, unit2, initiative = self.initiative)
            winner = log_dic['winner']
            if winner == 1:
                win1 += 1
            else:
                win2 += 1

        return win1/self.samples
        
        
    