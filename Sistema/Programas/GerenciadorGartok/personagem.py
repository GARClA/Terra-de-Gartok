import random
import string
import pandas as pd
import math

class Personagem:
    def __init__(self):
        self.rola_atributos()
        self.rola_raça()
        self.rola_ocupaçao()
        self.rola_tendencia()
        self.rola_ouro()

    def rola_atributos(self):
        self.força = random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)
        self.destreza  = random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)
        self.constituicao = random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)
        self.inteligencia = random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)
        self.sabedoria = random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)
        self.carisma = random.randrange(1,7) + random.randrange(1,7) + random.randrange(1,7)

    def rola_raça(self):
        raça = random.randrange(1,101)
        tabelaraças = pd.read_excel('tabelaraças.xlsx')

        index = 0
        for i in tabelaraças.Valor:
            if raça <= tabelaraças.Valor[index]:
                self.raça = tabelaraças.Raça[index]

                self.força += tabelaraças.For[index]
                self.destreza += tabelaraças.Des[index]
                self.constituicao += tabelaraças.Con[index]
                self.inteligencia += tabelaraças.Int[index]
                self.sabedoria += tabelaraças.Sab[index]
                self.carisma += tabelaraças.Car[index]

                self.calcula_modificadores()

                self.raciais = tabelaraças.Raciais[index]
                self.tamanho = tabelaraças.Tamanho[index]
                self.idioma = tabelaraças.Idioma[index]

                self.deriva_tamanho()

                self.capacidade_carga_normal = round((self.mod_força + 5)*self.mod_carga,0)
                self.capacidade_carga_alta = round((self.mod_força + 10)*self.mod_carga,0)

                self.ca = 10 + self.mod_destreza
                self.hp = random.randrange(1,tabelaraças['Dado de vida'][index]) + self.mod_constituiçao
                if self.hp < 1: self.hp = 1

                self.idade = int(round(random.randrange(1,101) * tabelaraças.Idade[index],0))

                return 0

            index += 1

    def calcula_modificadores(self):
        self.mod_força = math.floor((self.força - 10)/2)
        self.mod_destreza = math.floor((self.destreza - 10)/2)
        self.mod_constituiçao = math.floor((self.constituicao - 10)/2)
        self.mod_inteligencia = math.floor((self.inteligencia - 10)/2)
        self.mod_sabedoria = math.floor((self.sabedoria - 10)/2)
        self.mod_carisma = math.floor((self.carisma - 10)/2)

    def deriva_tamanho(self):
        tabelatamanhos = pd.read_excel('tabelatamanhos.xlsx')
        self.mod_carga = float(tabelatamanhos.Carga.where(tabelatamanhos.Tamanho == self.tamanho).dropna())
        self.deslocamento = float(tabelatamanhos.Deslocamento.where(tabelatamanhos.Tamanho == self.tamanho).dropna())

    def rola_ocupaçao(self):
        ocupacao = random.randrange(1,101)
        tabelaocupacoes = pd.read_excel('tabelaocupaçoes.xlsx')

        index = 0
        for i in tabelaocupacoes.Valor:
            if ocupacao <= tabelaocupacoes.Valor[index]:
                self.ocupacao = tabelaocupacoes.Ocupação[index]
                self.arma = tabelaocupacoes.Arma[index]
                self.item = tabelaocupacoes.Item[index]

                return 0
            
            index += 1

    def rola_tendencia(self):
        tendencia = random.randrange(1,101)
        tabelatendencia = pd.read_excel('tabelatendencias.xlsx')

        index = 0
        for i in tabelatendencia.Valor:
            if tendencia <= tabelatendencia.Valor[index]:
                self.tendencia = tabelatendencia.Tendência[index]

                return 0
            
            index += 1

    def rola_ouro(self):
        self.moedas = random.randrange(1,11) + random.randrange(1,11) + random.randrange(1,11) + random.randrange(1,11) + random.randrange(1,11)

    def __str__(self):
        string = f'''
Nome: (NOMEAR)
Tendência: {self.tendencia}
Raça: {self.raça}
Ocupação: {self.ocupacao}
IDADE: {self.idade}
Nível/XP: 0/1000

HP: {self.hp}
CA: {self.ca} (Sem armadura)

FORÇA (MOD): {self.força} ({self.mod_força})
DESTREZA (MOD): {self.destreza}({self.mod_destreza})
CONSTITUIÇÃO (MOD): {self.constituicao} ({self.mod_constituiçao})
INTELIGÊNCIA (MOD): {self.inteligencia} ({self.mod_inteligencia})
SABEDORIA (MOD): {self.sabedoria} ({self.mod_sabedoria})
CARISMA (MOD): {self.carisma} ({self.mod_carisma})

CAPACIDADE DE CARGA (NORMAL/ALTA): {self.capacidade_carga_normal}/{self.capacidade_carga_alta}
TAMANHO: {self.tamanho}
DESLOCAMENTO: {self.deslocamento} metros

INVENTÁRIO(Peso): 
    {self.moedas} moedas de cobre (VER PESO)

    {self.item} (VER PESO)
    {self.arma} (VER PESO)

Carga atual: (SOMAR PESO)

HABILIDADES: {self.raciais}
IDIOMAS: {self.idioma}
'''
        return string

    def exportar(self):
        f = open(f'{self.raça}_{self.ocupacao}.txt','w', encoding='utf-8')
        f.write(str(self))
        f.close()