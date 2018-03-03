import src.repository as repo
import src.sampler as sampler
import src.models as models

print('Starting...')

model = models.LavalModel()
repo.DATA_FILE = 'randoA_g1'
repo.add_header_to_results('{},{}'.format('file_name', model.header))
data = repo.get_source_data()
bootsrapped_data = sampler.resample_by_group(data, number_of_samples=50, group_identifier='patient')

for dataset in bootsrapped_data:
	file_name = repo.save_bootstrap_data(dataset)
	print ('Fitting model to bootstrapped data {}'.format(file_name))
	res = model.fit(dataset)
	repo.append_result('{},{}'.format(file_name, res))
