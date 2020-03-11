import os

# Evaluate attacks (fgs vs rand_fgs)
attack = 'rand_fgs'
command = 'python -m'
test_type = 'simple_eval'
models_directory = 'models/'
models = ['modelA_adv', 'modelB_adv', 'modelC_adv', 'modelD_adv']

alphas = []
current_alpha = 0.00
increment_alpha = 0.01
epsilon = 0.3

while current_alpha <= epsilon:
	alphas.append(current_alpha)
	current_alpha += increment_alpha

print('Evaluating optimal alpha...')


for model in models:
	for alpha in alphas:
		print('Launching random fgsm with alpha ({}) against model ({})'.format(alpha, model))
		full_command = "{} {} {} {}{} --eps={} --alpha={}".format(command, test_type, attack, models_directory, model, epsilon, alpha)
		print('Executing command: {}'.format(full_command))
		os.system(full_command)

