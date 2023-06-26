# AutomationViaPython
## 1. How to Use Jinja Template
### Introduction
The Jinja2 template allows you to create resources by providing a parameter YAML file.

### Prerequisites
    Python 3.x installed on your system.
    Required dependencies: jinja2, yaml, and awscli.
    AWS CLI configured with the necessary credentials and access rights to perform CloudFormation deployment.

### Usage Instructions
### Download the Python script for jinja template File

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
    
### Review the Output

The template will read the provided parameter YAML file and render the template accordingly.
The rendered output will be saved in an output.yml file.
Check the terminal or command prompt for any error messages or status updates during the execution.

## Python Code Overview
### This section will give a basic understanding of Code used.
#### Imports
    from jinja2 import Template
    import yaml
    import sys
    import subprocess

The first line imports the Template class from the jinja2 module.
The second line imports the yaml module, which allows working with YAML files.
The third line imports the sys module, which provides access to system-specific parameters and functions.
The fourth line imports the subprocess module, which allows running shell commands from within Python.

#### Interacting with Console
a. This block of code checks if the script was executed with at least two command-line arguments. If not, it prints an error message and exits the script with a status code of 1. Then fourth line assigns the value of the second command-line argument to the variable data_file
    if len(sys.argv) < 2:
        print("Please provide the data file as a command-line argument.")
        sys.exit(1)
    data_file = sys.argv[1]

#### File handling 
a. This opens the data_file in read mode and assigns its content to the variable data_content. The with statement ensures that the file is automatically closed after reading.

    with open(data_file, 'r') as f:
    data_content = f.read()

b. This block uses the yaml.safe_load() function from the yaml module to parse the content of data_content as YAML data. The resulting data is stored in the template_data variable.
The next line uses the get() method on template_data to retrieve the value associated with the key 'template'. If the key does not exist, it assigns an empty string to template_value

    template_data = yaml.safe_load(data_content)
    template_value = template_data.get('template', '')
    

c. This line concatenates the value of template_value with the string '.yml' or '.yaml' to form the name of the template file and assigns it to template_file.

    template_file = template_value + '.yml'
    if not template_file:
    template_file = template_value + '.yaml'


d.This opens the template_file in read mode and assigns its content to the variable template_content. Again, the with statement ensures the file is closed after reading.

    with open(template_file, 'r') as f:
    template_content = f.read()

e. This line creates a Jinja2 Template object using the template_content as the template source.

    template = Template(template_content)

f. In this line of code, the double asterisks (**) are used to pass the dictionary template_data as keyword arguments to the render() method. This syntax is known as "unpacking" the dictionary, and it allows each key-value pair in template_data to be passed as a separate keyword argument to the render() method.

    output = template.render(**template_data)

g. This block opens a file named 'output.yml' in write mode and writes the output string to the file. The with statement ensures the file is automatically closed after writing.

    with open('output.yml', 'w') as f:
    f.write(output)

#### CFN deploy

a. This line constructs a shell command as a string, which will be executed using the `subprocess
b. Also If desired, you can deploy the rendered template using AWS CloudFormation.
Ensure that you have the necessary AWS CLI credentials configured on your system.
Execute the following command to initiate the deployment

    bash_command = f"aws cloudformation deploy --template-file output.yml --stack-name {template_value} --capabilities CAPABILITY_NAMED_IAM --region us-east-1"
    subprocess.run(bash_command, shell=True)



## 2. How to Use Python Script.
### Introduction
The Jinja2 template allows you to create resources by providing a parameter YAML file.

### Prerequisites
    Python 3.x installed on your system.
    Required dependencies:yaml, and awscli.
    AWS CLI configured with the necessary credentials and access rights to perform CloudFormation deployment.

### Usage Instructions
### Download the Cfn Python wraper script template File

Download the CfnOptimized.py file, which contains the python Code.

### Prepare the Resource Template File

Create or obtain a Resource YAML file (ResourceName.yml) that contains the necessary data for resource creation.
The resource file should follow the required structure should follow the required file format.
    
### Prepare the Parameter File

Create or obtain a parameter YAML file (parameter.yml) that contains the necessary data for resource creation.
The parameter file should follow the required structure specified in the template.

### Run the Template

Open a terminal or command prompt and navigate to the directory where the template.py file is saved.
Execute the following command, providing the path to the parameter YAML file as a command-line argument:

    python3 template.py parameter.yml
    
### Review the Output

The template will read the provided parameter YAML file and render the template accordingly.
The rendered output will be saved in an out.yml file.
Check the terminal or command prompt for any error messages or status updates during the execution.

## Python Code Overview
### This section will give a basic understanding of Code used.
#### Imports
The first five lines import necessary modules (yaml, re, sys, os, subprocess) used in the script.
    import yaml
    import re
    import sys
    import os
    import subprocess

#### File handling and Functions
a. This is a function named read_file that takes a file_path argument. It opens the file located at file_path, reads its content, and returns it as a string.    
    
    def read_file(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        return content

b. Parameter and Resource template
This is a function named process_template that takes a template_file argument. It processes the template file by performing several operations:
   * It determines the directory of the template_file using os.path.dirname().
   * It assigns template_file to parameter_file.
   * It reads the content of parameter_file using the read_file() function and loads it as YAML data into parameter_template using yaml.safe_load().
   * It retrieves the value associated with the key 'template' from parameter_template and assigns it to template_value.
   * It generates the resource file name by appending .yml to template_value and checks if the file exists in the template directory. If not, it tries with .yaml           extension.
   * It reads the content of the resource file using the read_file() function and loads it as YAML data into resource_template using yaml.safe_load().

