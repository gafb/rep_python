import time

######## Modo comum
tempo_inicial = time.clock()
sqr_list = [ x * x for x in range(1,10000)]
tempo_final = time.clock()
#print(sqr_list)

for i in sqr_list:
    if (i ==10000):
        print ("Tempo comum: ")
        print (tempo_final - tempo_inicial)


'''
Pela abordagem normal percorre os elementos existentes
'''
def square(list_num):
    results = []
    for i in list_num:
        results.append(i*i)

    return results


tempo_inicial = time.clock()
sqr_lista = square(range(1,10000))
tempo_final = time.clock()

for i in sqr_lista:
    if (i ==10000):
        print ("Tempo comum sqr: ")
        print (tempo_final - tempo_inicial)


########Modo generator

tempo_inicial_generator = time.clock()
sqr_list_generator = ( x * x for x in range(1,10000)) #trocado o colchetes por parenteses
tempo_final_generator = time.clock()

#print(sqr_list_generator)
for i in sqr_list_generator:
    if (i ==10000):
        print ("Tempo generator: ")
        print (tempo_final_generator -tempo_inicial_generator)


'''
Pela abordagem do generator percorre os elementos existentes
'''
def square_generator(list_num):

    for i in list_num:
        yield i*i

tempo_inicial = time.clock()
sqr_lista = square_generator(range(1,10000))
tempo_final = time.clock()

for i in sqr_lista:
    if (i ==10000):
        print ("Tempo generator sqr: ")
        print (tempo_final - tempo_inicial)