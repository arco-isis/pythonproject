O objetivo desse projeto é ajudar engenheiros e jardineiros amadores a planificar seus campos de hortaliça, a realizar o plantio de cada espécie de hortaliça em seu devido espaçamento, evitar o desperdício de plantas e aumentar a produtividade de maneira geral.
Os passos utilizados para escrever o programa foram:

Importações
-abstractmethod
import math: Importa o módulo math, que fornece funções matemáticas, como pi, que é usado para calcular a área de um círculo.
-from abc import ABC, abstractmethod: Importa ABC e abstractmethod do módulo abc (Abstract Base Classes), que são usados para criar classes abstratas em Python.

Classe Abstrata Campo
pass
-class Campo(ABC):: Define uma classe abstrata Campo que herda de ABC. Isso significa que Campo não pode ser instanciada diretamente e serve como uma base para outras classes.
-@abstractmethod: Decora o método calcular_area, indicando que qualquer classe derivada de Campo deve implementar este método.

Classe Derivada CampoCirculo

-class CampoCirculo(Campo): Define uma classe CampoCirculo que herda de Campo.
__init__: Método construtor que inicializa a instância com um raio.
-calcular_area: Implementa o método abstrato para calcular a área de um círculo usando a fórmula π * raio².

Classe Derivada CampoRetangulo

-class CampoRetangulo(Campo): Define uma classe CampoRetangulo que herda de Campo.
__init__: Método construtor que inicializa a instância com comprimento e largura.

-calcular_area: Implementa o método abstrato para calcular a área de um retângulo usando a fórmula comprimento * largura.

Função ler_espacamentos

-ler_espacamentos: Lê um arquivo de texto que contém espaçamentos entre plantas e fileiras para diferentes hortaliças.

-try/except: Tenta abrir e ler o arquivo, capturando erros como arquivo não encontrado.

-espacamentos: Dicionário que armazena os espaçamentos, com a hortaliça como chave.

Função calcular_plantas

-calcular_plantas: Calcula o número de plantas que cabem em uma área, dado o espaçamento entre plantas e fileiras.

Função mensagem_boas_vindas 

-mensagem_boas_vindas: Exibe uma mensagem de introdução ao usuário, explicando o propósito do programa.

Função Principal main

-main: Coordena a execução do programa.
Chama mensagem_boas_vindas para exibir a introdução.
Lê os espaçamentos do arquivo.
Solicita ao usuário a hortaliça e o formato do campo.
Cria uma instância de CampoCirculo ou CampoRetangulo com base na entrada do usuário.
Calcula a área do campo e o número de plantas necessárias.
Exibe o resultado ou uma mensagem de erro se a hortaliça não for encontrada.

Execução do Programa

-if __name__ == "__main__":: Garante que main seja executado apenas quando o script é executado diretamente, e não quando importado como um módulo.
Este programa é um exemplo de como usar classes abstratas e derivadas para estruturar um problema de forma modular e extensível. Ele também demonstra o uso de funções para organizar o código e interagir com o usuário.











