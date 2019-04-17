# Tableau
Tableau and python

This script allows you to create a .tde programatically using python and the Tableau SDK library

The tde_object.py file is on improvement on the to_tde.py method.
This updated class allows you to convert a pandas DataFrame directly to a .tde file automatically.

#### Steps:
* import pandas DataFrame
* create tde_object
* convert DataFrame data types to strings
* create new tde
* the tde file will be exported to the current directory.

Example code:
data = pd.read_csv('Book1.csv')
x = tde_object.tde_object(data, "testing.tde")
x.convert_to_strings(data=data)
x.new_tde(data=data)



I provide more details in the following article:
https://medium.com/@jose.m.garcia1931/integrating-python-pandas-with-tableau-data-extracts-63e23f7c5a99
