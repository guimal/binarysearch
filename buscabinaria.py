#feito no python 3.6.2

import struct
import sys
if len(sys.argv) != 2:
	print ('USO %s [CEP]' % sys.argv[0])
	quit()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print ("Tamanho da Estrutura: %d" % registroCEP.size)
f = open("cep_ordenado.dat","r")
line = f.read(registroCEP.size)
while line != "":
	record = registroCEP.unpack(line)
	if record[cepColumn] == sys.argv[1]:
		for i in range(0,len(record)-1):
			print (record[i]) # .decode('latin1') 
    		break
line = f.read(registroCEP.size)
counter += 1
print ("Total de Registros Lidos: %d" % counter)
f.close()

def buscabinaria(vet, cep):
	esquerda, direita, tentativa = 0, len(vet), 1
	while 1:
		meio = (esquerda + direita) // 2
		aux_cep = vet[meio]
		if cep == aux_cep:
			return tentativa
		elif cep > aux_cep:
			esquerda = meio
		else:
			direita = meio
tentativa += 1
