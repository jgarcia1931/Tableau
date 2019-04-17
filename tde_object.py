from tableausdk import *
from tableausdk.Extract import *
from tableausdk.Exceptions import *
import pandas as pd

class tde_object():


    def __init__(self, data, tde_name):
        self.data = data
        self.tde_name = tde_name

    def new_tde(self):
        dataExtract = Extract(self.tde_name)
        if dataExtract.hasTable('Extract'):
            return print("tde already exist use another name")
        return dataExtract

    def convert_to_strings(self, data):
        for col in data.columns.tolist():
            data[col] = data[col].astype('str')

    def set_table_def(self, data):
        cols = data.columns.tolist()
        dataSchema = TableDefinition()
        for col in cols:
            dataSchema.addColumn(col, Type.UNICODE_STRING)
        return dataSchema

    def create_rows(self, data, dataSchema, dataExtract):
        table = dataExtract.addTable('Extract', dataSchema)
        newRow = Row(dataSchema)
        cols = data.columns.tolist()
        for i in range(0, len(data)):
            for col in cols:
                col_index = cols.index(col)
                newRow.setString(col_index, data[col][i])
                table.insert(newRow)
        dataExtract.close()

    def new_tde(self, data):
        # Step 1: Create the Extract File
        dataExtract = Extract(self.tde_name)
        if dataExtract.hasTable('Extract'):
            return print("tde already exist use another name")

        # Step 2: Create the table definition
        cols = data.columns.tolist()
        dataSchema = TableDefinition()
        for col in cols:
            dataSchema.addColumn(col, Type.UNICODE_STRING)

        # Step 3: Create a table in the image of the table definition
        table = dataExtract.addTable('Extract', dataSchema)

        # Step 4: Create rows and insert them one by one
        newRow = Row(dataSchema)
        cols = data.columns.tolist()
        for i in range(0, len(data)):
            for col in cols:
                col_index = cols.index(col)
                newRow.setString(col_index, data[col][i])
                table.insert(newRow)
        dataExtract.close()

        # Step 5: Close the tde
        dataExtract.close()
