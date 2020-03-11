import os

# Evaluate attacks (fgs vs rand_fgs)
attacks = ['fgs', 'rand_fgs']
command = 'python -m'
test_type = 'simple_eval'
models_directory = 'models/'
models = ['modelA', 'modelB', 'modelC', 'modelD', 'modelA_adv', 'modelB_adv', 'modelC_adv', 'modelD_adv']


print('Evaluating attacks...')

for attack in attacks:
	for model in models:
		print('Launching attack ({}) against model ({})'.format(attack, model))
		full_command = "{} {} {} {}{}".format(command, test_type, attack, models_directory, model)
		print('Executing command: {}'.format(full_command))
		os.system(full_command)


source = 'modelB'
targets = ['modelA', 'modelA_adv', 'modelA_ens']

print('Evaluating defense...')

for attack in attacks:
	for target in targets:
		print('Launching attack ({}) against model ({})'.format(attack, target))
		full_command = "{} {} {} {}{} {}{}".format(command, test_type, attack, models_directory, source, models_directory, target)
		print('Executing command: {}'.format(full_command))
		os.system(full_command)