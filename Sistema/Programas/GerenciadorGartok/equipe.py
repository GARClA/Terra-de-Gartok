from datetime import datetime
from personagem import Personagem
import pandas as pd

class Equipe:
    def __init__(self, tamanho):
        self.cria_personagens(tamanho)
        self.cria_planilha()
        self.exporta_planilha()

    def cria_personagens(self,tamanho):
        self.personagens = []
        for i in range(tamanho):
            x = Personagem()
            self.personagens.append(x)
            print(len(self.personagens))

    def cria_planilha(self):
        self.planilha_equipe = pd.DataFrame(columns=['Nome','CA','HP','Arma','Mod_Força','Mod_Destreza','Mod_Constituição',
        'Mod_Inteligência','Mod_Sabedoria','Mod_Carisma',
        'Carga Atual','Carga Normal','Carga Alta'])

        for personagem in self.personagens:
            data_char = {'Nome':f'{personagem.raça}_{personagem.ocupacao}','CA':personagem.ca,'HP':personagem.hp,
            'Arma':personagem.arma,'Mod_Força':personagem.mod_força,
            'Mod_Destreza':personagem.mod_destreza,
            'Mod_Constituição':personagem.mod_constituiçao,'Mod_Inteligência':personagem.mod_inteligencia,
            'Mod_Sabedoria':personagem.mod_sabedoria,'Mod_Carisma':personagem.mod_carisma,
            'Carga Atual':'-','Carga Normal':personagem.capacidade_carga_normal,'Carga Alta':personagem.capacidade_carga_alta}

            self.planilha_equipe = self.planilha_equipe.append(data_char , ignore_index=True)

    def exporta_planilha(self):
        self.planilha_equipe.to_excel(f'Equipe.xlsx',encoding='utf-8')

    def exporta_equipe(self):
        for personagem in self.personagens:
            personagem.exportar()