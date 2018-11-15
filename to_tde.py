from tableausdk import *
from tableausdk.Extract import *
from tableausdk.Exceptions import *

# You cannot delete or append to a .tde file if it is opened in Tableau
def to_tde(dataset, tde_mode, tde_name):

    if tde_mode == 'new':

        # Step 1: Create the Extract File
        dataExtract = Extract(tde_name)

        if dataExtract.hasTable('Extract'):
            return print("tde already exist use another name")

        # Step 2: Create the table definition
        dataSchema = TableDefinition()
        dataSchema.addColumn('Station', Type.UNICODE_STRING)
        dataSchema.addColumn('Time', Type.UNICODE_STRING)
        dataSchema.addColumn('Date', Type.DATE)
        dataSchema.addColumn('all', Type.DOUBLE)
        dataSchema.addColumn('n7', Type.DOUBLE)
        dataSchema.addColumn('n8', Type.DOUBLE)
        dataSchema.addColumn('y_serries', Type.DOUBLE)

        # Step 3: Create a table in the image of the table definition
        table = dataExtract.addTable('Extract', dataSchema)

        # Step 4: Create rows and insert them one by one
        newRow = Row(dataSchema)
        for i in range(0, len(dataset)):
            print(i)
            newRow.setString        (0, dataset['Station'][i])
            newRow.setString        (1, dataset['Time'][i])
            newRow.setDate          (2, dataset['Date'][i].year, dataset['Date'][i].month, dataset['Date'][i].day)
            newRow.setDouble        (3, dataset['all'][i])
            newRow.setDouble        (4, dataset['n7'][i])
            newRow.setDouble        (5, dataset['n8'][i])
            newRow.setDouble        (6, dataset['y_serries'][i])
            table.insert(newRow)

        # Step 5: Close the tde
        dataExtract.close()

    elif tde_mode == 'append':

        # Step 1: Import the Extract File
        preExtract = Extract(tde_name)

        # Step 2: Open existing table
        table = preExtract.openTable('Extract')

        # Step 3: Import the table definition
        tableDef = table.getTableDefinition()

        # Step 4: Create rows and insert them one by one
        newRow = Row(tableDef)
        for i in range(0, len(dataset)):
            print(i)
            newRow.setString	    (0, dataset['Station'][i])
            newRow.setString		(1, dataset['Time'][i])
            newRow.setDate          (2, dataset['Date'][i].year, dataset['Date'][i].month, dataset['Date'][i].day)
            newRow.setDouble	    (3, dataset['all'][i])
            newRow.setDouble		(4, dataset['n7'][i])
            newRow.setDouble	    (5, dataset['n8'][i])
            newRow.setDouble        (6, dataset['y_serries'][i])
            table.insert(newRow)

        # Step 5: Close the extract
        preExtract.close()
