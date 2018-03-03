import pandas

class Bootstrap():

    def __init__(self, data):
        self.data = data
        self.groups = data.groupby(data.columns[1])

    def resample(self, number_of_samples):
        return [self._sample() for times in range(0, number_of_samples)]

    def _sample(self):
        return pandas.concat([self.groups.get_group(group) for group in self.data[self.data.columns[1]].sample(n = len(self.groups), replace = True)])


