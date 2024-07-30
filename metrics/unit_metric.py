from .utils import plot_multi_bars

class unit_metric():
    
    def __init__(self, samples = 1000):
        
        self.samples = samples
        self.metric_name = 'metric name'
    
    def get_metric(self, unit):

        return 0
        
def ranking(units, metric):
    units_metrics = []
    units_names = []
    for unit in units:
        units_metrics.append(metric.get_metric(unit))
        units_names.append(unit.name)

    sorted_metric_list, sorted_unit_list = zip(*sorted(zip(units_metrics, units_names), reverse=True))

    return sorted_unit_list

def multimetric_plot(units, metrics):
    
    dic_of_dic = {}  # dic[metric_name][unit_name] = metric_value
    
    for metric in metrics:
        dic_of_dic[metric.metric_name] = {}
        for unit in units:
            dic_of_dic[metric.metric_name][unit.name] = metric.get_metric(unit)
            
    plot_multi_bars(dic_of_dic)


class DPS(unit_metric):
    
    def __init__(self, save, scale_by_cost = False, samples = 1000):
        
        self.save = save
        self.samples = samples
        self.scale_by_cost = scale_by_cost
        self.metric_name = 'DPS vs ' + str(save) + '+'
        
    def get_metric(self, unit):
        
        return unit.attack(self.save, self.samples).mean()/unit.cost if self.scale_by_cost else unit.attack(self.save, self.samples).mean()
    
    