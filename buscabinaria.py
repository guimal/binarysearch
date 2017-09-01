def buscabinaria(vet, num):
	esquerda, direita, tentativa = 0, len(vet), 1
	while 1:
		meio = (esquerda + direita) // 2
		aux_num = vet[meio]
		if num == aux_num:
			return tentativa
		elif num > aux_num:
			esquerda = meio
		else:
			direita = meio
tentativa += 1
