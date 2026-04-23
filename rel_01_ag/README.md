# 🧬 Implementação do Algoritmo Genético

Projeto desenvolvido para a disciplina de **Computação Evolucionária**, no **Programa de Pós-Graduação em Engenharia de Sistemas e Automação** da Universidade Federal de Lavras (UFLA).

Este trabalho consiste na implementação de um **Algoritmo Genético (AG)** para resolução de problemas de otimização com duas variáveis, utilizando representação binária e diferentes operadores genéticos clássicos, além da execução automatizada de experimentos e análise estatística dos resultados.

---

## 📚 Informações Acadêmicas

**Disciplina:** Computação Evolucionária
**Professor:** Bruno Henrique Groenner Barbosa

**Discentes:**

* Matheus Higino
* Marcos Vinicius Cardoso Reis

**Programa:** Programa de Pós-Graduação em Engenharia de Sistemas e Automação
**Instituição:** Universidade Federal de Lavras (UFLA)

---

## 🎯 Objetivo da Atividade

Implementar um Algoritmo Genético simples para solução de **dois problemas de otimização com duas variáveis**, contemplando:

* Representação cromossomial binária
* Seleção por roleta viciada e torneio
* Cruzamento com um ponto de corte por variável
* Mutação bit a bit
* Com e sem elitismo
* Execução de 30 rodadas por configuração
* Estatísticas: média, mediana, máximo e mínimo
* Boxplots comparativos
* Gráfico de convergência
* Relatório final em LaTeX/PDF

---

## ⚙️ Características Implementadas

### ✔ Representação cromossomial

Cada indivíduo possui:

* 16 bits para variável `x`
* 16 bits para variável `y`

Totalizando:

```text
32 bits por indivíduo
```

Os valores são convertidos para o intervalo:

```text
[-10, 10]
```

---

## 🔬 Funções de Otimização

Foram utilizadas duas funções clássicas da literatura:

---

### 🔹 Cross-in-Tray

* Alta multimodalidade
* Muitos ótimos locais profundos
* Problema mais desafiador

Essa função exige maior capacidade de exploração do algoritmo.

---

### 🔹 Drop-Wave

* Multimodal suave
* Convergência mais estável
* Menor dificuldade relativa

Permite observar diferenças claras entre configurações.

---

## 🧠 Operadores Genéticos

### Seleção

* Roleta viciada
* Torneio

### Cruzamento

* Um ponto de corte por variável

### Mutação

* Bit a bit

### Elitismo

* Ativado ou desativado por configuração

O elitismo preserva o melhor indivíduo da geração.

---

## 🧪 Configurações Testadas

Foram avaliadas combinações com:

### Probabilidade de cruzamento (`pc`)

```text
0.6, 0.8, 1.0
```

### Probabilidade de mutação (`pm`)

```text
0.01, 0.05, 0.1
```

### Método de seleção

```text
roleta, torneio
```

### Tamanho da população

```text
20, 50, 100
```

### Número de gerações

```text
50, 100
```

### Elitismo

```text
True, False
```

### Função objetivo

```text
Cross-in-Tray, Drop-Wave
```

Cada configuração foi executada:

```text
30 vezes
```

---

## 📁 Estrutura do Projeto

```bash
rel_01_ag/
│
├── src/
│   ├── algoritmo_genetico.py
│   ├── crossover.py
│   ├── fitness.py
│   ├── mutacao.py
│   ├── populacao.py
│   ├── representacao.py
│   └── selecao.py
│
├── experiments/
│   ├── run_experiments.py
│   ├── analise_final.py
│   ├── boxplots_parametros.py
│   └── configs/
│
├── results/
│   ├── dados_brutos/
│   ├── estatisticas/
│   ├── boxplots/
│   └── graficos/
│
├── report/
│   ├── relatorio_final.tex
│   ├── relatorio_final.pdf
│   ├── referencias.bib
│   └── imagens/
│
├── utils/
│   ├── estatisticas.py
│   ├── graficos.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

## ▶️ Como Executar

---

### 1. Criar ambiente virtual

```bash
python -m venv env
```

### Ativar ambiente virtual

### Windows (Git Bash)

```bash
source env/Scripts/activate
```

### Linux / Mac

```bash
source env/bin/activate
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

ou manualmente:

```bash
pip install numpy matplotlib pandas
```

---

### 3. Executar os experimentos

```bash
python main.py
```

ou

```bash
python -m experiments.run_experiments
```

---

### 4. Gerar análise final automática

```bash
python -m experiments.analise_final
```

Isso gera:

* top 10 configurações
* melhor configuração encontrada
* gráfico de convergência
* análise textual automática

---

### 5. Gerar boxplots por parâmetro

```bash
python -m experiments.boxplots_parametros
```

São gerados:

* boxplot de crossover
* boxplot de mutação
* boxplot de seleção
* boxplot de população
* boxplot de gerações
* boxplot de elitismo

---

## 📊 Resultados Obtidos

A melhor configuração encontrada foi:

```text
pc = 1.0
pm = 0.1
seleção = roleta
população = 100
gerações = 100
elitismo = True
função = Cross-in-Tray
fitness médio ≈ 2.0626
```

---

## 📈 Principais Conclusões

Os experimentos mostraram que:

* populações maiores apresentaram melhor desempenho
* 100 gerações produziram melhores resultados
* elitismo aumentou estabilidade e convergência
* `pm = 0.1` foi superior às demais taxas testadas
* `pc = 1.0` apareceu na melhor configuração global
* Cross-in-Tray foi mais difícil que Drop-Wave
* a seleção por roleta foi altamente competitiva quando combinada com elitismo

Também foi necessário corrigir a seleção por roleta devido ao uso de fitness negativos, aplicando normalização para garantir o funcionamento correto.

---

## 📄 Relatório Final

O relatório foi desenvolvido em LaTeX e compilado em PDF, contendo:

* introdução
* metodologia
* resultados
* análise dos resultados
* conclusão
* repositório do código
* referências bibliográficas

Arquivos:

```bash
report/relatorio_final.tex
report/relatorio_final.pdf
```

---

