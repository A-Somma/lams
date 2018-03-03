from scipy.optimize import minimize 

def optimize_using_cobyla(model, *data):
	res = minimize(model.objective, model.get_variables(), args = data,
			       method='COBYLA', constraints = model.constraints, options = {'maxiter': 10000})
	return res

def optimize_using_nelder_mead(model, *data):
	res = minimize(model.objective, model.get_variables(), args = data,
			       method='Nelder-Mead')
	return res