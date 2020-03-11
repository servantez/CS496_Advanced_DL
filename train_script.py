import os

# Train undefended models
command = 'python -m'
train_type = 'train'
models_directory = 'models/'
models = {'modelA': '0', 'modelB': '1', 'modelC': '2', 'modelD':'3'}

print('Training undefended models...')

for name, type_ in models.items():
	full_command = "{} {} {}{} --type={}".format(command, train_type, models_directory, name, type_)
	print('Executing command: {}'.format(full_command))
	os.system(full_command)


# Train adversarial models
train_type = 'train_adv'
models = {'modelA_adv': '0', 'modelB_adv': '1', 'modelC_adv': '2', 'modelD_adv':'3'}

print('Training adversarial models...')

for name, type_ in models.items():
	full_command = '{} {} {}{} --type={} --epochs=12'.format(command, train_type, models_directory, name, type_)
	print('Executing command: {}'.format(full_command))
	os.system(full_command)