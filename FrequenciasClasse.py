import math

listaDedados = [30,49,105,115, 118,148,178,185,196,210,236,236,278,287,329,362,366,399,430,434,451,451,477,488,508,531,539]
# listaDedados = [30,35,32,28,25,26,28,30,35,40,26,27,45,36,30,30,26,34,28,29,22,30,28,36,30,28,35,40,39,29,30,28,34,39,26,28,30,34,35,34,28,29,34,35,37,48,30,22,26,30]


def ft(lista):
    at = max(lista) - min(lista)
    k = math.ceil(math.sqrt(len(lista))) 
    c = at / k

    intervalos = range(min(lista), max(lista) + round(c), round(c))
    frequencias = [0] * (len(intervalos) - 1)
    frequenciasAcumuladas = [0] * (len(intervalos) - 1)
    produtos = [0] * (len(intervalos) - 1)
    limiteInferior = intervalos[0]
    tabela = []

    tabela.append(['Intervalo', 'Ponto Médio', 'Frequência', 'Frequência Relativa', 'Frequência Acumulada',
                   'Frequência Rel. Acumulada', 'Produto'])

    for i in range(len(intervalos) - 1):
        limiteSuperior = intervalos[i + 1]
        pontoMedio = (limiteInferior + limiteSuperior) / 2
        for numero in lista:
            if limiteInferior <= numero < limiteSuperior:
                frequencias[i] += 1
                produtos[i] += pontoMedio * 1
        limiteInferior = limiteSuperior
        frequenciasAcumuladas[i] = sum(frequencias[:i + 1])

    for i in range(len(intervalos) - 1):
        frequenciaRelativa = frequencias[i] / len(lista)
        frequenciaRelativaAcumulada = frequenciasAcumuladas[i] / len(lista)
        tabela.append([f'{intervalos[i]} - {intervalos[i + 1]}', f'{(intervalos[i] + intervalos[i+1])/2:.2f}', f'{frequencias[i]}',
                       f'{frequenciaRelativa:.4f}', f'{frequenciasAcumuladas[i]}', f'{frequenciaRelativaAcumulada:.4f}', f'{produtos[i]:.2f}'])

    return tabela

tabela = ft(listaDedados)
for linha in tabela:
    print(f'{linha[0]:<15}{linha[1]:<15}{linha[2]:<15}{linha[3]:<25}{linha[4]:<25}{linha[5]:<30}{linha[6]:<15}')
