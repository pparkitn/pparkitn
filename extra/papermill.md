# Papermill Example: Running Parameterized Jupyter Notebooks
- This repository provides an example of using Papermill to parameterize and execute Jupyter Notebooks programmatically and from the command line.

## Installation
To install Papermill, use pip:

```
pip install papermill
```

## Example Usage
Imagine you have a notebook called analysis.ipynb that takes in parameters, such as start_date and end_date, to filter data. With Papermill, you can set these parameters at runtime and execute the notebook.

1. Setting Up the Parameterized Notebook
First, set up your notebook to accept parameters. In analysis.ipynb, define parameters using a designated parameters cell.

For example:

python
```
# Parameters
start_date = None  # Placeholder values
end_date = None
```

To add the parameters tag:

Open the notebook in Jupyter,
Select the cell with the parameters,
Go to View > Cell Toolbar > Tags,
Add the parameters tag to the cell.
2. Executing the Notebook with Papermill
You can run the notebook and pass in parameters either from Python code or directly from the command line.

## Running with Python Code
Use Papermill in a Python script to execute analysis.ipynb and pass in parameters:

python
```
import papermill as pm

# Execute notebook with parameters
pm.execute_notebook(
   'analysis.ipynb',           # Input notebook
   'output_analysis.ipynb',    # Output notebook
   parameters={
       'start_date': '2024-01-01',
       'end_date': '2024-01-31'
   }
)
```

## Running from the Command Line
You can also use Papermill directly from the command line to execute the notebook with parameters.

```
papermill analysis.ipynb output_analysis.ipynb -p start_date 2024-01-01 -p end_date 2024-01-31
```
In this example:

analysis.ipynb is the input notebook.
output_analysis.ipynb is the output notebook where results will be saved.
The -p flag is used to pass each parameter (start_date and end_date with their respective values).
3. Viewing the Output
After execution, open output_analysis.ipynb to view the results with the updated parameters.

## Official Site
https://papermill.readthedocs.io/en/latest/
