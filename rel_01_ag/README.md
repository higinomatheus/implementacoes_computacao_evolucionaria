# Algoritmo Genético para Otimização de Funções de Duas Variáveis

Este projeto implementa um **Algoritmo Genético (AG)** para resolução de problemas de otimização contínua com duas variáveis, como parte da disciplina de **Computação Evolucionária**.

O trabalho inclui desde a implementação do algoritmo até a execução automatizada de experimentos, análise dos resultados e geração de relatório científico.

---

## Sobre o Projeto

O Algoritmo Genético foi desenvolvido utilizando:

* Representação cromossomial binária
* Seleção por **roleta viciada** e **torneio**
* Cruzamento com um ponto de corte por variável
* Mutação bit a bit
* Suporte a **elitismo (opcional)**
* Execução de múltiplos experimentos automatizados

---

## Funções de Otimização

Foram utilizadas duas funções clássicas da literatura:

### 🔹 Cross-in-Tray

* Função altamente multimodal
* Possui múltiplos mínimos locais profundos
* Maior dificuldade de convergência

### 🔹 Drop-Wave

* Função multimodal suave
* Convergência mais estável

---

## Estrutura do Projeto

```bash
rel_01_ag/
├── src/
│   ├── algoritmo_genetico.py
│   ├── selecao.py
│   ├── crossover.py
│   ├── mutacao.py
│   ├── populacao.py
│   ├── representacao.py
│   └── fitness.py
│
├── experiments/
│   ├── configs/
│   │   ├── config_01.json
│   │   ├── config_02.json
│   │   └── config_03.json
│   ├── run_experiments.py
│   └── analise_final.py
│
├── results/
│   ├── dados_brutos/
│   │   ├── execucao_01.csv
│   │   └── execucao_02.csv
│   ├── estatisticas/
│   │   ├── resumo.csv
│   │   ├── resumo_geral.csv
│   │   ├── top10.csv
│   │   └── analise.txt
│   ├── graficos/
│   │   └── convergencia_melhor.png
│   └── boxplots/
│       ├── config_01.json.png
│       ├── config_02.json.png
│       ├── config_03.json.png
│       └── comparativo_top5.png
│
├── report/
│   ├── relatorio_final.tex
│   ├── relatorio_final.pdf
│   ├── comparativo_top5.png
│   ├── convergencia_melhor.png
│   ├── referencias.bib
│   └── ufla-logo.png
│
├── utils/
│   ├── estatisticas.py
│   └── graficos.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv env
source env/Scripts/activate   # Windows (Git Bash)
# ou
source env/bin/activate       # Linux/Mac
```

---

### 2. Instalar dependências

```bash
pip install numpy matplotlib pandas
```

---

### 3. Executar experimentos

```bash
python main.py
```

---

### 4. Gerar análise final

```bash
python -m experiments.analise_final
```

---

## Resultados

O projeto executa automaticamente:

* 30 execuções por configuração
* Cálculo de:

  * média
  * mediana
  * máximo
  * mínimo
* Geração de:

  * Boxplots
  * Gráficos de convergência
  * CSV com resultados completos

---

## Principais Conclusões

* O **elitismo** melhora a estabilidade do algoritmo
* Populações maiores aumentam a qualidade das soluções
* Taxas de mutação moderadas proporcionam melhor equilíbrio
* A função **Cross-in-Tray** é mais difícil de otimizar que a Drop-Wave

---

## Relatório

O relatório completo pode ser encontrado em:

```bash
report/relatorio_final.pdf
```


---

## Autores

* Matheus Higino
* Marcos Vinicius Cardoso Reis

---

## Disciplina

* Computação Evolucionária
* Professor: Bruno Henrique Groenner Barbosa


---
