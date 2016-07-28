from pyrouge import Rouge155

r = Rouge155()
r.system_dir = 'system'
r.model_dir = 'model'
r.system_filename_pattern = 'summ.(\d+).txt'
r.model_filename_pattern = 'summ.[A-Z].#ID#.txt'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)
