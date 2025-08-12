# Simulação Epidemiológica com Modelo SEIR

## Descrição

Este projeto implementa um modelo de simulação epidemiológica baseado no modelo SEIR (Suscetíveis, Expostos, Infeciosos, Recuperados) para a COVID-19. O objetivo é capturar a dinâmica temporal da propagação de uma doença infeciosa que possui um período de incubação, permitindo análises visuais e quantitativas do comportamento de uma epidemia através da solução de equações diferenciais.

## Motivação

Modelos epidemiológicos compartimentais são ferramentas poderosas para entender e prever a trajetória de surtos. O modelo SEIR, em particular, é uma evolução do modelo SIR clássico que introduz o compartimento "Exposto". Isso permite uma representação mais realista de doenças como a COVID-19, onde existe um período de latência entre a infeção de um indivíduo e o momento em que ele se torna capaz de transmitir o vírus.

## Funcionalidades

A simulação é configurada com os seguintes parâmetros base:

* **Implementação do modelo SEIR através de um sistema de equações diferenciais ordinárias.
* **Simulação da evolução de uma epidemia ao longo do tempo.
* **Parâmetros configuráveis, como número de reprodução (R0), período de incubação e período infeccioso.
* **Visualização gráfica da evolução dos compartimentos (S, E, I, R) ao longo do tempo.

## Como Executar

Para executar este projeto, necessita de ter o Python 3 e as seguintes bibliotecas instaladas no seu ambiente.

### Pré-requisitos

* Python 3.x
* NumPy
* SciPy
* Matplotlib

### Instalação

Abra o seu terminal ou linha de comandos e instale as dependências necessárias:

`pip install numpy scipy matplotlib`

### Execução

1.  Guarde o código do algoritmo num ficheiro Python (ex: `simulador_covid.py`).
2.  Navegue até ao diretório onde guardou o ficheiro através do terminal.
3.  Execute o script com o seguinte comando:

`python simulador_covid.py`

## Resultado Esperado

Após a execução, serão gerados dois outputs:

1.  **Gráfico Visual:** Uma janela pop-up exibirá um gráfico intitulado "Implementação do Modelo SEIR para Surto de COVID-19", mostrando as curvas de Suscetíveis, Expostos, Infetados e Recuperados ao longo de 150 dias.
2.  **Output na Consola:** O terminal exibirá os parâmetros utilizados na simulação para referência.

    ```
    Parâmetros da Simulação:
    População Total (N): 1000000
    Número Básico de Reprodução (R0): 3.0
    Taxa de Transmissão (beta): 0.4286
    Taxa de Progressão (sigma): 0.2000 (Período de Incubação: 5.0 dias)
    Taxa de Recuperação (gamma): 0.1429 (Período Infeccioso: 7.0 dias)
    ```
