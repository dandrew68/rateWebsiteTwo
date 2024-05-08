from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import nbconvert
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from nbformat import read, v4

load_dotenv()

def runNotebook(theNotebookFile):

    # Load the notebook
    #with open('CreditAggregatesExample.ipynb', 'r') as f:
    #    notebook = read(f, as_version=4)
    with open(theNotebookFile, 'r') as f:
        notebook = read(f, as_version=4)

    # Execute the notebook
    exec_proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
    exec_proc.preprocess(notebook, {'metadata': {'path': '.'}})

    # Execute the notebook again - DR edit
    #exec_proc = ExecutePreprocessor(timeout=600, kernel_name='python3')
    #exec_proc.preprocess(notebook, {'metadata': {'path': '.'}})

    # Exporter to exclude input cells
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = True

    # Convert notebook to HTML
    html_body, _ = html_exporter.from_notebook_node(notebook)

    # Save the HTML
    #with open('labourForce.html', 'w') as f:
    #    f.write(html_body)

    return html_body