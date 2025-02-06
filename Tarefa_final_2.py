import math

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

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

def main():
    espacamentos = ler_espacamentos("espacamentos.txt")
    
    hortaliça = input("Digite a espécie de hortaliça: ").strip().lower()
    
    formato = input("Digite o formato do campo (c para círculo ou r para retângulo): ").strip().lower()
    if formato == "c":
        raio = float(input("Digite o raio da circunferência do campo em metros: "))
        area = calcular_area_circulo(raio)
    elif formato == "r":
        comprimento = float(input("Digite o comprimento do campo em metros: "))
        largura = float(input("Digite a largura do campo em metros: "))
        area = calcular_area_retangulo(comprimento, largura)
    else:
        print("Formato inválido.")
        return
    
    if hortaliça in espacamentos:
            espaco_plantas, espaco_fileiras = espacamentos[hortaliça]
            num_plantas = calcular_plantas(area, espaco_plantas, espaco_fileiras)
            print(f"Para uma área de {area:.2f} m2, você precisa de aproximadamente {num_plantas} plantas de {hortaliça}.")
    else:
        print("Hortaliça não encontrada.")
    
if __name__ == "__main__":
    main()