from models.profile import Profile

from .utils import plot_multi_bars
import matplotlib.pyplot as plt
import numpy as np

class UnitMetric:
    """
    Generic class for unit metrics.
    This class should be inherited to create specific metrics.
    """

    def __init__(self, samples: int = 1000):
        self.samples = samples
        self.metric_name = "metric name"

    def get_sample(self, unit: Profile):
        pass

    def get_samples(self, unit: Profile, samples: int = None):
        """
        Get multiple samples of the metric for a unit.
        """
        samples = samples if samples is not None else self.samples
        return [self.get_sample(unit) for _ in range(samples)]


def average_metric(unit: Profile, metric: UnitMetric, n_samples: int = 1000):
    """
    Compute the average value of a metric for a unit over a number of samples.
    """
    unit.reset()
    metric_value = 0
    samples = metric.get_samples(unit, n_samples)
    values = []
    for s in samples:
        values.append(s)
        metric_value += s
    return metric_value / n_samples

def median_metric(unit: Profile, metric: UnitMetric, n_samples: int = 1000):
    """
    Compute the median value of a metric for a unit over a number of samples.
    """
    unit.reset()
    samples = metric.get_samples(unit, n_samples)
    return np.median(np.array(samples))


def plot_cdf(unit: Profile, metric: UnitMetric, n_samples: int = 1000):
    """
    Plot the cumulative distribution function (CDF) of a metric for a unit.
    This function samples the metric for a unit multiple times and plots the CDF.
    """

    metric_dict = compute_metric_for_cdf(unit, metric, n_samples)
    mean_val = metric_dict["avg"]
    metric_values_sorted = metric_dict["metric_values"]
    yvals = metric_dict["yvals"]

    plt.axvline(mean_val, linestyle=":")
    plt.plot(metric_values_sorted, yvals, label=unit.name)
    plt.fill_between(metric_values_sorted, yvals, alpha=0.3)
    plt.xlabel(metric.metric_name)
    plt.ylabel("Cumulative Probability")
    plt.legend()
    plt.grid()
    plt.show()


def multi_unit_plot_cdf(units: list[Profile], metric: UnitMetric, n_samples: int = 1000):
    plt.figure(figsize=(10, 6))
    list_outputs = []
    for unit in units:
        list_outputs.append(compute_metric_for_cdf(unit, metric, n_samples))

    list_outputs.sort(key=lambda x: x["avg"], reverse=True)
    for dic in list_outputs:
        metric_values = dic["metric_values"]
        yvals = dic["yvals"]
        unit = dic["unit"]
        mean_val = np.mean(metric_values)
        color = plt.gca()._get_lines.get_next_color()
        plt.axvline(mean_val, linestyle=":", color=color)
        plt.plot(metric_values, yvals, label=unit, color=color)
        plt.fill_between(metric_values, yvals, alpha=0.3, color=color)

    plt.xlabel(metric.metric_name)
    plt.ylabel("Cumulative Probability")
    plt.legend()
    plt.grid()
    plt.show()


def compute_metric_for_cdf(unit: Profile, metric: UnitMetric, n_samples: int = 1000):
    """
    Compute the metric values for a unit to be used in CDF plotting.
    First resets the unit, then samples the metric multiple times before sorting the values.
    The average value is also computed.
    Returns a dictionary with the unit name, average value, metric values, and y-values for the CDF.
    """
    unit.reset()
    metric_values = metric.get_samples(unit, n_samples)
    metric_values = np.array(metric_values)
    metric_values = np.sort(metric_values)[::-1]
    yvals = np.arange(len(metric_values)) / float(len(metric_values))
    avg = np.mean(metric_values)

    return {"unit": unit.name, "avg": avg, "metric_values": metric_values, "yvals": yvals}


def ranking(units: list[Profile], metric: list[UnitMetric], n_samples: int = 1000):
    units_metrics = []
    units_names = []
    for unit in units:
        units_metrics.append(average_metric(unit, metric, n_samples))
        units_names.append(unit.name)

    _, sorted_unit_list = zip(*sorted(zip(units_metrics, units_names), reverse=True))

    return sorted_unit_list


def multimetric_plot(units: list[Profile], metrics: list[UnitMetric], n_samples: int = 1000):
    metric_to_unit_name_to_value = {}  # dic[metric_name][unit_name] = metric_value
    for metric in metrics:
        metric_to_unit_name_to_value[metric.metric_name] = {}
        for unit in units:
            metric_to_unit_name_to_value[metric.metric_name][unit.name] = average_metric(
                unit, metric, n_samples
            )
    plot_multi_bars(metric_to_unit_name_to_value)

def scatter_plot_two_metrics(units: list[Profile], metric_A: UnitMetric, metric_B: UnitMetric, n_samples: int = 1000):

    fig, ax = plt.subplots()
    max_A = 0
    max_B = 0
    for unit in units:
        value_A = average_metric(unit, metric_A, n_samples)
        value_B = average_metric(unit, metric_B, n_samples)
        max_A = max(max_A, value_A)
        max_B = max(max_B, value_B)
        ax.scatter(value_A, value_B, label=unit.name, alpha=0.5, color=plt.gca()._get_lines.get_next_color(), marker='o', s=100)
    ax.set_xlabel(metric_A.metric_name)
    ax.set_ylabel(metric_B.metric_name)
    plt.ylim(0, 1.2 * max_B)
    plt.xlim(0, 1.2 * max_A)
    ax.legend()
    plt.show()



class DamageOneActivation(UnitMetric):
    """
    Compute the damage of a unit for one activation against a given save.
    If scale_by_cost is True, the damage is divided by the unit's cost to give damage per point.
    """

    def __init__(self, save: int, scale_by_cost: bool = False):
        self.save = save
        self.scale_by_cost = scale_by_cost
        self.metric_name = "Damage on one activation vs " + str(save) + "+"

    def get_sample(self, unit: Profile, combat_context: dict = None):
        if combat_context is None:
            combat_context = {}
        # Default mutable argument, see https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
        dmg = unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=self.save)
        return dmg / unit.cost if self.scale_by_cost else dmg

class AlphaStrike(UnitMetric):
    """
    Computes either the damage dealt or the number of slain models by a unit
    in an alpha strike against an enemy unit, which is defined as the first
    activation of the unit against the enemy before the enemy had struck.
    """

    def __init__(self, ennemy_unit: Profile, return_n_slain_models: bool = True, scale_by_cost: bool = False):
        self.ennemy_unit = ennemy_unit
        self.scale_by_cost = scale_by_cost
        self.return_n_slain_models = return_n_slain_models
        self.metric_name = (
            f"Alpha strike vs {ennemy_unit.name} (number of slain models)"
            if return_n_slain_models
            else f"Alpha strike vs {ennemy_unit.name} (damage)"
        )

    def get_sample(self, unit: Profile, combat_context: dict = None) -> int:
        if combat_context is None:
            combat_context = {}
        ennemy_unit = self.ennemy_unit
        ennemy_unit.reset()
        dmg = unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=ennemy_unit.save)
        damage, killed_models = ennemy_unit.receive_damage(dmg)
        if self.return_n_slain_models:
            metric = killed_models
        else:
            metric = damage / unit.cost if self.scale_by_cost else damage
        return metric


class BetaStrike(UnitMetric):
    def __init__(self, ennemy_unit, return_n_slain_models=True, scale_by_cost=False):
        self.ennemy_unit = ennemy_unit
        self.scale_by_cost = scale_by_cost
        self.return_n_slain_models = return_n_slain_models
        self.metric_name = (
            f"Beta strike vs {ennemy_unit.name} (number of slain models)"
            if return_n_slain_models
            else f"Beta strike vs {ennemy_unit.name} (damage)"
        )

    def get_sample(self, unit, combat_context={}):
        ennemy_unit = self.ennemy_unit
        self.ennemy_unit.reset()
        unit.reset()
        dmg_taken = ennemy_unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=unit.save)
        unit.receive_damage(dmg_taken)
        dmg = unit.attack_with_all_weapons(combat_context=combat_context, enemy_save=ennemy_unit.save)
        damage, killed_models = ennemy_unit.receive_damage(dmg)
        if self.return_n_slain_models:
            metric = killed_models
        else:
            metric = damage / unit.cost if self.scale_by_cost else damage
        return metric

class EffectiveHP(UnitMetric):
    def __init__(self, ennemy_rend: int, scale_by_cost: bool = False):
        self.ennemy_rend = ennemy_rend
        self.scale_by_cost = scale_by_cost
        if scale_by_cost:
            self.metric_name = (
                f"Effective HP vs rend {ennemy_rend} (scaled by cost)"
            )
        else:
            self.metric_name = (
                f"Effective HP vs rend {ennemy_rend}"
            )

    def get_sample(self, unit, combat_context={}):
        
        ward = unit.ward if unit.ward else 7
        ward_proba = (7 - ward)/6
        #print(f"Unit {unit.name} ward: {ward}, ward_proba: {ward_proba}")
        save = unit.save + self.ennemy_rend
        if save < 1:
            save = 2
        if save > 6:
            save = 7
        save_proba = (7 - save)/6
        #print(f"Unit {unit.name} save: {unit.save}, ennemy_rend: {self.ennemy_rend}, save_proba: {save_proba}")
        hp = unit.health * unit.total_models
        effective_hp = hp / ( (1-ward_proba) *(1-save_proba) )
        if self.scale_by_cost:
            effective_hp /= unit.cost
        return effective_hp
    
    def get_samples(self, unit: Profile, samples: int = None):
        """
        Overrides the get_samples method because the EffectiveHP metric is deterministic and does not require sampling.
        """
        value = self.get_sample(unit)
        return [value]*samples