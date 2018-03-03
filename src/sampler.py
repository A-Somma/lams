import pandas
import random

def resample_by_group(data, number_of_samples=1, group_identifier=None):
    print(data)
    groups = data.groupby(data[group_identifier])

    def sample():
        resampled_groups = [groups.get_group(random.choice(groups.keys)) for times in range(len(groups))]
        return pandas.concat(resampled_groups)

    return [sample() for times in range(0, number_of_samples)]
