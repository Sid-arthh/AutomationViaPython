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
    from jinja2 import Template
    import yaml
    import sys
    import subprocess

The first line imports the Template class from the jinja2 module.
The second line imports the yaml module, which allows working with YAML files.
The third line imports the sys module, which provides access to system-specific parameters and functions.
The fourth line imports the subprocess module, which allows running shell commands from within Python.
