O objetivo desse projeto é ajudar engenheiros e jardineiros amadores a planificar seus campos de hortaliça, a realizar o plantio de cada espécie de hortaliça em seu devido espaçamento, evitar o desperdício de plantas e aumentar a produtividade de maneira geral.
Os passos utilizados para escrever o programa foram:

1. Definição do problema:
O programa deve calcular a área de um campo de hortaliças, que pode ser um círculo ou um retângulo.
Deve ler um arquivo de texto (`espaçamentos.txt`) que contém o espaçamento entre plantas e fileiras para diferentes tipos de hortaliças.
Com base na área calculada e nos espaçamentos, o programa deve determinar quantas plantas são necessárias.

2. Estrutura do Programa:
O programa é dividido em funções para modularizar e organizar o código:
- `ler_espacamentos`: Lê o arquivo de espaçamentos e armazena os dados em um dicionário.
- `calcular_plantas`: Calcula o número de plantas necessárias com base na área e nos espaçamentos.
- `calcular_area_circulo`: Calcula a área de um círculo.
- calcular_area_retangulo: Calcula a área de um retângulo.
- main: Função principal que coordena a execução do programa.

  
3. Implementação das Funções:
-ler_espacamentos:
Abre o arquivo espaçamentos.txt e lê cada linha.
Divide cada linha em partes (hortaliça, espaçamento entre plantas, espaçamento entre fileiras).
Armazena os dados em um dicionário com a hortaliça como chave e os espaçamentos como valores.
-calcular_plantas:
Recebe a área do campo e os espaçamentos.
Calcula o número de plantas usando a fórmula: area / (espaco_plantas * espaco_fileiras).
calcular_area_circulo:
Recebe o raio do círculo e calcula a área usando a fórmula: π * raio².
calcular_area_retangulo:
Recebe o comprimento e a largura do retângulo e calcula a área usando a fórmula: comprimento * largura.

4. Interação com o Usuário:
O programa solicita ao usuário que insira o tipo de hortaliça e o formato do campo.
Dependendo do formato, solicita as dimensões necessárias (raio para círculo, comprimento e largura para retângulo).

5. Cálculo e Saída:
Com a área calculada e os espaçamentos lidos, o programa calcula o número de plantas necessárias.
Exibe o resultado ao usuário, informando quantas plantas são necessárias para a área especificada.

7. Tratamento de Erros:
O programa inclui tratamento de exceções para lidar com erros comuns, como arquivo não encontrado ou valores inválidos.

**Código completo**
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
    espacamentos = ler_espacamentos("espaçamentos.txt")
    
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
        print(f"Para uma área de {area:.2f} m², você precisa de aproximadamente {num_plantas} plantas de {hortaliça}.")
    else:
        print("Hortaliça não encontrada.")

if __name__ == "__main__":
    main()












