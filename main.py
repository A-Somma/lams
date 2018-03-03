from src.sampler import Bootstrap
from src.models import LavalModel
import src.repository as repo

print('Starting...')

repo.GROUP = 'randoA_g1'

data = repo.get_source_data()

model = LavalModel()
bootstrap = Bootstrap(data)

repo.add_header_to_results('{},{}'.format('file_name', model.header))
bootsrapped_data = bootstrap.resample(50)
for dataset in bootsrapped_data:
	file_name = repo.save_bootstrap_data(dataset)
	print ('Fitting model to bootstrapped data {}'.format(file_name))
	res = model.fit(dataset)
	repo.append_result('{},{}'.format(file_name, res))
