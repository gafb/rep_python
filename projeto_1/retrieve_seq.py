import sys
import time
import argparse
from util import db_index, search_fasta


def pair(arg):

    return [int(x) for x in arg.split('-')]



def main():

    # Option Parse
    parser = argparse.ArgumentParser(description="A Tool to index and search large multifasta files")


    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands',
                                       help='Use retrieve_seq.py {subcommand} -h for help with each subcommand'
                                       )


    parser_index = subparsers.add_parser('index', help='Index all sequences in the database')

    parser_index.add_argument("--db", dest='db', default=None, action="store", help="A multifasta DB to be indexed",
                        required=False)


    parser_extract = subparsers.add_parser('extract', help='Extract sequence in a multifasta')

    parser_extract.add_argument('-f', '--file', dest='file', action="store", help="A multifasta file",
                        required=False)

    parser_extract.add_argument('-e','--end', type=int,
                          help="end position on the fasta sequence",
                          required=False)

    parser_extract.add_argument('-s','--start', type=int,
                          help="start position on the fasta sequence",
                          required=False)

    parser_extract.add_argument('-g','--gene', type=str,
                          help="A gene (or chromossome) name",
                          required=False)

    parser_extract.add_argument('-l','--len', action='store_true',
                          help="Get the length of all genes. "
                               "If --gene get the length of the provided gene",
                          required=False)

    #________________________________SPLICE________________________________________#

    parser_splice = subparsers.add_parser('splice', help='Extract multiple sequences in a multifasta')

    parser_splice.add_argument('-f', '--file', dest='file', action="store", help="A multifasta file",
                        required=False)

    parser_splice.add_argument('-r','--range', type=pair, nargs='+',
                          help="A values in the form start-end space separated",
                          required=False)

    parser_splice.add_argument('-g','--gene', type=str,
                          help="A gene (or chromossome) name",
                          required=False)
    
    #______________________________________________________________________________#


    args = parser.parse_args()


    # function hasattr must be used because args may or may not have arg.db, and test it with just an
    # if args.db does not work

    if hasattr(args, 'db'):
        db_index.create_index(args.db)
        print("DB {db} has been indexed".format(db=args.db))


    if hasattr(args, 'start') and args.start is not None:   # args.start exists and has a value
        fasta = args.file
        start = args.start
        end = args.end
        gene_name = args.gene

        ##############Tempo inicial
        tempo_inicial = time.clock()
        
        seq = search_fasta.search(fasta, start, end, gene_name)


        tempo_final = time.clock()
        print ('Tempo: ')
        print (tempo_final - tempo_inicial)

        print('>{gene}:{start}-{end}'.format(gene=gene_name,start=start,end=end))
        for i in seq:
            print (i, end='')
        print()
        #print(list(seq))
        #print(seq)
        

    if hasattr(args, 'len') and args.len:   # arg.len is True
        fasta = args.file
        gene_name = args.gene if args.gene else None
        search_fasta.len(fasta, gene_name)

    if hasattr(args, 'range') and args.range :
        result = ''
        fasta = args.file
        gene_name = args.gene
        
        #print (fasta)
        print ('>'+gene_name+ ':', end='')
        
        for i in args.range:
            #print (i[0])
            fasta = args.file
            start = int(i[0])
            end = int(i[1])
            print("['"+str(i[0])+'-'+str(i[1])+"']", end='')
            #print (i[0]+','+i[1])
            seq = search_fasta.search(fasta, start, end, gene_name)

                    
            for i in seq:
                #print (i)
                result += i
            #result += "\n"
    #print (args.range)
    
        print()
        print (result)
        print (len(result))
        #print (len('CCTTTCTTAGTATCTAACTGATAGATGAGTCTCTACAGGTTTGATTTTTCTGAAAAGAACAAAAACGAAGCAACCAAGGAAGAAGAAGAGAAAAGAAGAGCTCAAGTATGT'))
        #print (len('TTTTTTGTTAACACTGGTGGCAGCTTTTTGACATTTATTCCTTTCTTAGTATCTAACTGATAGATGAGTCTCTACAGGTTTGATTTTTCTGAAAAGAACAAAAACGAAGCAACCAAGGAAGAAGAAGAGAAAAGAAGAGCTCAAGTATGTACAATTATATCAATTTTCCTTTATTTCTTTGATTGTATTTATGTCTTATGCTAAGGGTACATCTTGTCTAGGTTGTTTCCAAACTTCATGGTATACTACGACCATTCATCCTTCGAAGAATGAAATGTGATGTTGAGCTCTCACTTCCACGGAAAAAGGAGATTATAATGTATGCTACAATGACTGATCATCAGAAAAAGTTCCAGGAACATCTGGTGAATAACACGTTGGAAGCACATCTTGGAGAGAATGCCATCCGAGGTACATGATCTATTTTTTTTTTTTAATACTTTGTTTAATTATGTCATTTTCTGCATTGATTTGTTCATCCCCTATACTTCAGGTCAAGGCTGGAAGGGAAAGCTTAACAACCTGGTCATTCAACTTCGAAAGAACTGCAACCATCCTGACCTTCTCCAGGGGCAAATAGATGGTTCATGTATGTCAGTTTCTTTTAAGAAACGTAAGAAAAACTTCTGTCATACTGTTCTGTCTAATTGTTTCATTTCGTGACAGATCTCTACCCTCCTGTTGAAGAGATTGTTGGACAGTGTGGTAAATTCCGCTTATTGGAGAGATTACTTGTTCGGTTATTTGCCAATAATCACAAAGTATGTTTCACAAACCCATGGCTCGTAGCTCATTTCCCTTTGAGAACTTCTCTGATCCATTTGCTGATGACCAGGTCCTTATCTTCTCCCAATGGACGAAACTTTTGGACATTATGGATTACTACTTCAGTGAGAAGGGGTTTGAGGTTTGCAGAATCGATGGCAGTGTGAAGCTGGATGAAAGGAGAAGACAGGTTTCACCTGTGCTTATGCTGCTTTTGCGTTGCTTTTAAGCAATATTCTGACCAAATATTATAACCATAAGGTCTCTCTCTCTCTCTCTTTGCCTTGAAACAGATTAAAGATTTCAGTGATGAGAAGAGCAGCTGTAGTATATTTCTCCTGAGTACCAGAGCTGGAGGACTCGGAATCAATCTTACTGCTGCTGATACATGCATCCTCTATGACAGCGACTGGGTAATCAAATCAATTAATTTATTTTCTTTGAAGGAAAATCTTTCTCTTTCGTGTTGTCTCCAACTGTGTTTTGTCTGATCTCCAGAACCCTCAAATGGACTTGCAAGCCATGGACAGATGCCACAGAATCGGGCAGACGAAACCTGTTCATGTTTATAGGCTTTCCACGGCTCAGTCGATAGAGGTAAAACTCTTTGTTGTTCATATCAATCAATCTTAACTTCAAACCATTGAGATTGTTGCCTCATGAGATTGGTTTATGACATTTGCTCAGACCCGGGTTCTGAAACGAGCGTACAGTAAGCTCAAGCTGGAACATGTGGTTATTGGCCAAGGGCAGTTTCATCAAGAACGTGCCAAGTCTTCAACACCTTTAGAGGTTTTAACTTCTCTTAAAGCTCAATCCTTTTTAGATACACTTATTATCAACAAAATCTCCTATTGACAGCTTGAACCAAACTAACACACAGGAAGAGGACATACTGGCGTTGCTTAAGGAAGATGAAACTGCTGAAGATAAGTTGATACAAACCGATATAAGCGATGCGGATCTTGACAGGTTACTTGACCGGAGTGACCTGACAATTACTGCACCGGGAGAGACACAAGCTGCTGAAGCTTTTCCAGTGAAGGGTCCAGGTTGGGAAGTGGTCCTGCCTAGTTCGGGAGGAATGCTGTCTTCCCTGAACAGTTAGGACACATTAATAAGCCAGGCCTTGAAACCACTTCTGTGTTTTTTTTTTTTTTTTCCGGAACATGATCGGTTACTTTTGGCTGGGAGGATTTAATTATTAGAGGGCTCGGAAGTTTTTGTAAGTTAAAGAACTCACTTAAAACCCTGAAAACATGACAGTTAATGGTGATTAGCTCTCAATGTGATGAAAACAATTGGCCCTCTGATTTTGCTGTTGCGGTAATATTATGACTTGTGTACGTTTATAGTCTTTGTAGTCTGCAATTTTGGCATTGAGCTATTTCTCACGAACTTATGGGATCTTATGTTTTGGATTTGGGATT'))
if __name__ == '__main__':
    main()
