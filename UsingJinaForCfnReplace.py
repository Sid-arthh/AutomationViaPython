from jinja2 import Template
import yaml
import sys
import subprocess
if len(sys.argv) < 2:
    print("Please provide the data file as a command-line argument.")
    sys.exit(1)

data_file = sys.argv[1]

with open(data_file, 'r') as f:
     data_content = f.read()

template_data = yaml.safe_load(data_content)
template_value = template_data.get('template', '')


template_file = template_value + '.yml'

with open(template_file, 'r') as f:
    template_content = f.read()


template = Template(template_content)
if not template_file:
    template_file = template_value + '.yaml'
    
output = template.render(**template_data)

with open('output.yml', 'w') as f:
    f.write(output)

  # deploy command
bash_command = f"aws cloudformation deploy --template-file output.yml --stack-name {template_value} --capabilities CAPABILITY_NAMED_IAM --region us-east-1"
subprocess.run(bash_command, shell=True)
print("The output is saved in 'output.yml'.")
