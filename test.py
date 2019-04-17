import pandas as pd
import tde_object


data = pd.read_csv('Book1.csv')

x = tde_object.tde_object(data, "testing.tde")
x.convert_to_strings(data=data)
x.new_tde(data=data)

