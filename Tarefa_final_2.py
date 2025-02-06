import math
from abc import ABC, abstractmethod

class Campo(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class CampoCirculo(Campo):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

class CampoRetangulo(Campo):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

def ler_espacamentos(nome_arquivo):
    espacamentos = {}
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split(',')
                if len(partes) == 3:
                    hortaliça, espaco_plantas, espaco_fileiras = partes
                    espacamentos[hortaliça.lower()] = (float(espaco_plantas), float(espaco_fileiras))
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    return espacamentos

def calcular_plantas(area, espaco_plantas, espaco_fileiras):
    return int(area / (espaco_plantas * espaco_fileiras))

def mensagem_boas_vindas():
    print("Bem-vindo ao Programa de Planejamento de Hortaliças!")
    print("Este programa ajuda você a calcular a área do seu campo de hortaliças")
    print("e determina quantas plantas você pode cultivar com base nos espaçamentos.")
    print("Você poderá escolher entre um campo em formato de círculo ou retângulo.")
    print("Vamos começar!\n")

def main():
    mensagem_boas_vindas()
    espacamentos = ler_espacamentos("espacamentos.txt")
    
    hortaliça = input("Digite a espécie de hortaliça: ").strip().lower()
    
    formato = input("Digite o formato do campo (c para círculo ou r para retângulo): ").strip().lower()
    if formato == "c":
        raio = float(input("Digite o raio da circunferência do campo em metros: "))
        campo = CampoCirculo(raio)
    elif formato == "r":
        comprimento = float(input("Digite o comprimento do campo em metros: "))
        largura = float(input("Digite a largura do campo em metros: "))
        campo = CampoRetangulo(comprimento, largura)
    else:
        print("Formato inválido.")
        return
    
    area = campo.calcular_area()
    
    if hortaliça in espacamentos:
        espaco_plantas, espaco_fileiras = espacamentos[hortaliça]
        num_plantas = calcular_plantas(area, espaco_plantas, espaco_fileiras)
        print(f"Para uma área de {area:.2f} m², você precisa de aproximadamente {num_plantas} plantas de {hortaliça}.")
    else:
        print("Hortaliça não encontrada.")

if __name__ == "__main__":
    main()
