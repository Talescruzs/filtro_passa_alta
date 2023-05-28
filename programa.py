#bibliotecas utilizadas:
import math
import plotly.express as px
import pandas as pd
#criação das listas onde serão inseridos os resultados:
listGanhog = list()
listGanhodb = list()
listFrequencias = [[],[]]
#definição de dados estáticos:
c = 0.000001
r = 150
pi = math.pi
#definição de frequência de corte: 
corte = 1/(2*pi*r*c)
#criação de arquivo onde ficarão salvos os resultados:
text = open("log.txt", "w")
#escreve no arquivo dos resultados, a frequência de corte:
text.write("frequancia de corte e: {0} hertz \n\n".format(corte))
#passa por todas as frequências solicitadas(de 0 até 10000):
for f in range(0, 10001, 10):
    #insere frequência atual na lista das frequências utilizadas no gráfico de ganho:
    listFrequencias[0].append(f)
    #faz a conta do ganho na frequência atual
    ganhog = (2*pi*f*r*c)/math.sqrt(1+(2*pi*f*r*c)**2)
    #adiciona o ganho na lista dos ganhos para futura criação do gráfico:
    listGanhog.append(ganhog)
    #escreve no arquivo dos resultados a frequência atual e seu ganho:
    text.write("frequencia =  {0} \n".format(f))
    text.write("ganho G = {0} \n".format(ganhog))
    #abre bloco de código que pode haver problema:
    try:
        #tenta fazer o cálculo do ganho em decibéis, caso não exista(na frequência 0), vai para a linha 40(except):
        ganhodb = 20*math.log(ganhog, 10)
        #adiciona o resultado na lista dos resultados dos ganhos em db para futura criação do gráfico:
        listGanhodb.append(ganhodb)
        #insere frequência atual na lista das frequências utilizadas no gráfico de ganho em db:
        listFrequencias[1].append(f)
        #escreve no arquivo dos resultados o ganho em db:
        text.write("Ganho em decibeis = {0}\n\n".format(ganhodb))
    except:
        #escreve no arquivo dos resultados que não foi possível aferir o ganho em decibéis:
        text.write("nao e possivel tirar os decibeis deste ganho\n\n")
#cria tipo de dado necessário para criação do primeiro gráfico:
df1 = pd.DataFrame(dict(
    Freq = listFrequencias[0],
    GanhoG = listGanhog
))
#cria tipo de dado necessário para criação do segundo gráfico:
df2 = pd.DataFrame(dict(
    Freq = listFrequencias[1],
    Ganhodb = listGanhodb
))
#cria os gráficos:
fig = px.line(df1 , x="Freq", y="GanhoG", title="Unsorted Input") 
fig.show()
fig = px.line(df2 , x="Freq", y="Ganhodb", title="Unsorted Input") 
fig.show()

text.close()