import json

def getColumnsByPiece(name, columns): #Return columns that have the string name #Can changeForFiles
        columnlist =[]
        for column in columns:
            if (name in column):
                columnlist.append(column)
        return columnlist

def getActualColumns(table_name):
    with open("./input/tables.json") as json_data:
            tables = json.load(json_data)
            col_value = 0
            for i in tables["tables_files"]:
                col_value += 1
                if (table_name == i):
                    actual_table = "columns_names"+str(col_value)
                    break
                     
    return (tables[actual_table], actual_table)

def getTablesFiles():
    with open("./input/tables.json") as json_data:
            tables = json.load(json_data)
    return (tables["tables_files"])

def getIndexColumn(name_columns, column):
    with open("./input/tables.json") as json_data:
         tables = json.load(json_data)
    count =0
    ans = None   
    for actual_column in tables[name_columns]:
        
        count += 1
        
        if (actual_column == column):
        
          ans = count
          break
        
        
    return ans                

