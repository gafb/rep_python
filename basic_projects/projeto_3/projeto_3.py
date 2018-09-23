import logging
import os
import sys
import util.dbconnect as db
import util.logger as utl 
import util.argparser as arg
import util.readFiles as rfiles

import os.path



# Initialize log object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
utl.initialize_logger(os.getcwd(), logger)

def main():

    tmpColumns = ['cell_type_category','cell_type','cell_type_track_name','cell_type_short','assay_category','assay','assay_track_name','assay_short,donor','time_point','view','track_name','track_type','track_density','provider_institution','source_server','source_path_to_file','server,path_to_file','new_file_name']  
    args = arg.callArgparser()


    conn = db.connect_db(args.db, logger)
    #1
    if args.command == "createdb":

        db.create_tables(conn, logger)

    #2
    elif args.command == "insert":
        list_of_data = []

        jsonFiles = rfiles.getTablesFiles()
        columns = []

        for actual_file in jsonFiles:
            #print (args.file)
            if (actual_file in args.file): # Existem casos que podem dar erro com nomes de caminhos estranhos
               
                columns, name_columns =  rfiles.getActualColumns(actual_file)
                #print (name_columns)
                break

        with open(args.file, 'r') as f:
            next(f) #skip first line because it has columns names
            for line in f:

                # reset dictionary
                line_dict = dict()

                # Skip empty lines
                if not line.strip():
                    continue

                # split line
                values = line.strip().split(",")

                # put each field in a dict
                if (not any (value is ''  for value in values) or any (value is not '' for value in values)): # taking off lines where all elements are null (,,,,,)

                    for column in columns:

                        index = rfiles.getIndexColumn(name_columns ,column)

                        if (index != None):

                               
                                line_dict[column] = values[index-1]
                
                    list_of_data.append(line_dict)

        db.insert_data(conn, list_of_data, logger, actual_file)
                        

    elif args.command == "update":

        db.update_status(conn, args.old_assay,args.new_assay ,args.old_donor,args.new_donor ,logger)


    #3A
    elif args.command == "select" and args.ct is not False:
        all_cells_type = db.select_cell_type(conn, logger)
        for cell_type in all_cells_type:
            print(cell_type[0])

    #3B

    #3C
    elif args.command == "select" and args.at is not None:

        all_tracknames = db.select_searchByCondition(conn, logger,"track_name",args.at, "assay_track_name")
        for trackname in all_tracknames:
            print(trackname[0])

    #3D
    elif args.command == "select" and args.ca is not None:

        all_cellstype = db.select_searchByCondition(conn, logger,"cell_type",args.ca, "assay")
        for celltype in all_cellstype:
            print(celltype[0])

    elif args.command == "select" and args.tracks is not False:
        
        piece_col = rfiles.getColumnsByPiece("track", tmpColumns)
        piece_col = ','.join(piece_col)
        all_tracks = db.select_searchByCondition(conn, logger,piece_col,args.tracks , "assay") #conn, logger, condition,search, allColumns, conditionVar

    #4
    elif args.command == "delete":
        db.delete_byTrackName(conn, args.a, logger)


if __name__ == '__main__':
    main()
