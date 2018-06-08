import argparse

def callArgparser():

    parser = argparse.ArgumentParser(description="A Tool manipulate a sqlite DB")

    subparsers = parser.add_subparsers(title='actions',
                                       description='valid actions',
                                       help='Use sqlite-python.py {action} -h for help with each action',
                                       dest='command'
                                       )

    parser_index = subparsers.add_parser('createdb', help='Create database and tables')

    parser_index.add_argument("--db", dest='db', default=None, action="store", help="The DB name",
                        required=True)

    parser_insert = subparsers.add_parser('insert', help='Insert data on tables')

    parser_insert.add_argument("--file",  default=None, action="store", help="TSV file with the data to be inserted",
                        required=True)

    parser_insert.add_argument("--db", default=None, action="store", help="The DB name",
                        required=True)

    parser_update = subparsers.add_parser('update', help='Update a field in a db')

    parser_update.add_argument("--db", default=None, action="store", help="The DB name",
                        required=True)

    parser_update.add_argument("--old_assay", default=None, action="store", help="assay ",
                        required=False)

    parser_update.add_argument("--old_donor", default=None, action="store", help="donor ",
                        required=False)

    parser_update.add_argument("--new_assay", default=None, action="store", help="assay ",
                        required=False)

    parser_update.add_argument("--new_donor", default=None, action="store", help="donor ",
                        required=False)


    parser_select = subparsers.add_parser('select', help='Select  fields from the db')

    parser_select.add_argument("--db", default=None, action="store", help="The DB name",
                        required=True)

    parser_select.add_argument("--ct", action="store_true", help="Select all Cell types",
                        required=False)
    parser_select.add_argument("--tracks", action="store", help="Select all information about tracks belonging to an specific assay",
                        required=False)
    parser_select.add_argument("--at", action="store", help="Select all track name associated with a specific assay_track_name",
                        required=False)
    parser_select.add_argument("--ca", action="store", help="Select all cell_types associated with a assay",
                        required=False)
  
    parser_delete = subparsers.add_parser('delete', help='delete rows from the db')

    parser_delete.add_argument("-a", default=None, action="store", help="Delete rows where this track_names appears",
                        required=False)

    parser_delete.add_argument("--db", default=None, action="store", help="The DB name",
                        required=True)

    args = parser.parse_args()

    return args