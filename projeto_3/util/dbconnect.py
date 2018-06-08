import sqlite3
import util.readFiles as rfiles



def connect_db(db_name, logger):
    try:
        conn = sqlite3.connect(db_name + '.db')
        logger.info(f'Connection stablished with DB: {db_name}.db')

        return conn


    except sqlite3.OperationalError:
        logger.error(f'Could not connect with {db_name}.db. Make sure the DB name is right')


def create_tables(conn, logger):
    c = conn.cursor()
    
    tables_names = rfiles.getTablesFiles()
    
    numTable =0

    for table in tables_names:
        aux = ""
        numTable += 1
        columns_names = rfiles.getActualColumns(table)
        for column in columns_names[0]:
            aux = aux + column + ' TEXT NOT NULL,'
        aux = aux[0: len(aux)-1]

        argtable = '('+ aux +');'
        #sqlite doesn't allow to put var name in var table

        try: #Max of 2 tables
            if numTable==1:
                c.execute('CREATE TABLE IF NOT EXISTS myTable'+ argtable)
            elif numTable==2:
                c.execute('CREATE TABLE IF NOT EXISTS myTable2'+ argtable)

            logger.info('Table myTable'+str(numTable)+' was created')

        except sqlite3.OperationalError:
            logger.error('Table could not be created')


def insert_data(conn, list_of_data, logger, argfile):
    c = conn.cursor()

    


    tables_names = rfiles.getTablesFiles()
    
    numTable =0

    for table in tables_names:
        aux = ""
        numTable += 1
        if (argfile == table):
            columns_names = rfiles.getActualColumns(table) #o retorno da funcao eh uma tupla
         
            #print( type(columns_names) )
            argtable = ", :".join(columns_names[0]) 


            argtable = "(:"+ argtable +")"
           # print (argtable)
            
            try:
                with conn:
                   # print (list_of_data)
                    
                    for data in list_of_data:
                        #print (data)
                        #print (data)
                        if numTable ==1 :
                            query = "INSERT INTO myTable VALUES "+ argtable
                           # print (query)
                            c.execute(query, data)

                        elif numTable==2:
                            query = "INSERT INTO myTable2 VALUES "+ argtable
                            c.execute(query, data)

                    logger.info('Data was inserted on the DB')
            except sqlite3.OperationalError:
                logger.error('Data could not be inserted')
            break

def update_status(conn, old_assay, new_assay, old_donor, new_donor , logger):
     # Por enquanto so para a tabela myTable
    c = conn.cursor()
    #print (old_assay)
    try:
        with conn:
            if (old_assay!=None and new_assay!=None and old_donor!=None and new_donor!=None):
                
                c.execute("UPDATE myTable SET assay = :new_assay, donor = :new_donor WHERE donor = :old_donor OR assay = :old_assay", {'old_assay': old_assay, 'new_assay': new_assay, 'old_donor': old_donor, 'new_donor': new_donor})
            elif (old_assay!='' and new_assay!=''):
                c.execute("UPDATE myTable SET assay = :new_assay WHERE assay = :old_assay", {'old_assay': old_assay, 'new_assay': new_assay})                
            elif (old_donor!='' and new_donor!=''):
                c.execute("UPDATE myTable SET donor = :new_donor WHERE donor = :old_donor", {'old_donor': old_donor, 'new_donor': new_donor})                
            
            logger.info(f'Assay: {old_assay} for {new_assay} was updated and donor : {old_donor} for {new_donor}')
    
    except sqlite3.OperationalError:
            logger.error(f'COULD NOT UPDATE assay:{new_assay} and donor: {new_donor}')
    


def select_cell_type(conn, logger):

    c = conn.cursor()

    try:
        with conn:
            c.execute("SELECT cell_type FROM myTable")
            all_cells_type = c.fetchall()

            logger.info(f'Selected cell_type elements')
            return all_cells_type

    except sqlite3.OperationalError:
        logger.error(f'Could not Select cell_type elements. Check if the table exists.')



def select_searchByCondition(conn,logger, search ,condition, condition_name): # conn, logger, what we want, condition, condition_name
    c = conn.cursor()
    #print (assay)
    try:
        with conn:
            c.execute("SELECT "+search+ " FROM myTable WHERE "+ condition_name+" = :condition",{"condition": condition})
            all_tracknames = c.fetchall()
            print (all_tracknames)
            logger.info(f'Selected {search}')

            return all_tracknames

    except sqlite3.OperationalError:
        logger.error(f'Could not Select {search}. Check if the table exists.')

def select_cellByAssay(conn,logger, assay):
    c = conn.cursor()
    #print (assay)
    try:
        with conn:
            c.execute("SELECT cell_type FROM myTable WHERE assay = :assay",{"assay": assay})
            all_tracknames = c.fetchall()
            print (all_tracknames)
            logger.info(f'Selected tracknames')

            return all_tracknames

    except sqlite3.OperationalError:
        logger.error(f'Could not Select tracknames. Check if the table exists.')





def delete_byTrackName(conn, trackname, logger):
    c = conn.cursor()
    
    try:
        with conn:
            c.execute("DELETE FROM myTable WHERE track_name = :trackname", {"trackname": trackname})

            logger.info(f'Rows where trackname is: "{trackname}",  were deleted')

    except sqlite3.OperationalError:
        logger.error(f'Could not delete row of trackname {trackname}')