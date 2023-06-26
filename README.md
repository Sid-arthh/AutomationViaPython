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
    if len(sys.argv) < 2:
        print("Please provide the data file as a command-line argument.")
        sys.exit(1)
    data_file = sys.argv[1]
This block of code checks if the script was executed with at least two command-line arguments. If not, it prints an error message and exits the script with a status code of 1. Then fourth line assigns the value of the second command-line argument to the variable data_file

#### File handling 
    with open(data_file, 'r') as f:
    data_content = f.read()
This opens the data_file in read mode and assigns its content to the variable data_content. The with statement ensures that the file is automatically closed after reading.
------------------->
    template_data = yaml.safe_load(data_content)
    template_value = template_data.get('template', '')
    
This block uses the yaml.safe_load() function from the yaml module to parse the content of data_content as YAML data. The resulting data is stored in the template_data variable.
The next line uses the get() method on template_data to retrieve the value associated with the key 'template'. If the key does not exist, it assigns an empty string to template_value
-------------------

