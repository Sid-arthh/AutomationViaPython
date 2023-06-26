# AutomationViaPython
## 1. How to Use Jinja Template
### Introduction
The Jinja2 template allows you to create resources by providing a parameter YAML file.

### Prerequisites
    Python 3.x installed on your system.
    Required dependencies: jinja2, yaml, and awscli.
    AWS CLI configured with the necessary credentials and access rights to perform CloudFormation deployment.

### Usage Instructions
### Download the Pthon script for jinja template File

Download the JinjaTemplate.py file, which contains the python Code to handle Jinja template and deployment logic.
    
### Prepare the Resource Template File

Create or obtain a Resource YAML file (ResourceName.yml) that contains the necessary data for resource creation.
The resource file should follow the required structure specified in the jinja file format.
    
### Prepare the Parameter File

Create or obtain a parameter YAML file (parameter.yml) that contains the necessary data for resource creation.
The parameter file should follow the required structure specified in the template.

### Run the Template

Open a terminal or command prompt and navigate to the directory where the template.py file is saved.
Execute the following command, providing the path to the parameter YAML file as a command-line argument:

    python3 template.py parameter.yml

## Python Code Overview
### CODE 
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
    
    output = template.render(s3Bucket=template_data.get('s3Bucket', {}))
    
    with open('output.yml', 'w') as f:
        f.write(output)
    
      # deploy command
    bash_command = f"aws cloudformation deploy --template-file output.yml --stack-name {template_value} --capabilities CAPABILITY_NAMED_IAM --region us-east-1"
    subprocess.run(bash_command, shell=True)
    print("The output is saved in 'output.yml'.")