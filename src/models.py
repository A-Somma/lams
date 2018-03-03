import math
import optimize as solver



class LavalModel():

	def __init__(self):
		self.gamma = 2
		self.time_of_half_2 = 8
		self.time_of_half_3 = 58.
		self.constraints = {'type':'ineq', 'fun':lambda gamma: gamma[0]-1}
		self.header = '{},{},{},{},{},{}\n'.format('gamma', 't_half_2', 't_half_3',
						 						   'converged', 'iterations', 'objective_value')

	def get_variables(self):
		return [self.gamma,  self.time_of_half_2, self.time_of_half_3]

	def set_variables(self, variables):
		self.gamma = variables[0]
		self.time_of_half_2 = variables[1]
		self.time_of_half_3 = variables[2]

	def probability_function(self, time, time_of_half):
		return time**self.gamma/(time**self.gamma+time_of_half**self.gamma)

	def probability_of_score_greater_or_equal_than_1(self):
		return 1

	def probability_of_score_greater_or_equal_than_2(self, time):
		return self.probability_function(time, self.time_of_half_2)

	def probability_of_score_greater_or_equal_than_3(self, time):
		return self.probability_function(time, self.time_of_half_3)

	def probability_score_is_1(self, time):
		return self.probability_of_score_greater_or_equal_than_1() - self.probability_of_score_greater_or_equal_than_2(time)

	def probability_score_is_2(self, time):
		return 1 - self.probability_score_is_1(time) - self.probability_score_is_3(time)
	
	def probability_score_is_3(self, time):
		return self.probability_of_score_greater_or_equal_than_3(time)

	def objective(self, x0, data):
		self.set_variables(x0)
		probability_dictionary={1:self.probability_score_is_1,
								2:self.probability_score_is_2,
								3:self.probability_score_is_3}
		return -sum([math.log10(probability_dictionary[row[1]['score']](row[1]['time'])) for row in data.iterrows()])

	def fit(self, data):
		res = solver.optimize_using_nelder_mead(self, data)
		return '{},{},{},{},{},{}\n'.format(res.x[0], res.x[1], res.x[2],
							  				res.success, res.nit, res.fun)

