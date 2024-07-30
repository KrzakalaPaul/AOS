import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from rules.fight import fight

class pairwise_metric():
    
    def __init__(self, samples = 1000):
        
        self.samples = samples
        self.metric_name = 'metric name'
    
    def get_metric(self, unit1, unit2):

        return 0
    
def matrix(units, metric):
    
    dataframe = pd.DataFrame(index = [unit.name for unit in units], columns = [unit.name for unit in units])
    
    for unit1 in units:
        for unit2 in units:
            dataframe.loc[unit1.name, unit2.name] = metric.get_metric(unit1, unit2)
            
    fig,ax = plt.subplots()
    sns.heatmap(dataframe, ax = ax)
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
            winner = fight(unit1, unit2, initiative = self.initiative)
            if winner == unit1:
                win1 += 1
            else:
                win2 += 1
                
        return win1/self.samples
        
        
    