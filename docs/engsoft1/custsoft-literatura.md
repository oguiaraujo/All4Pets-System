<h2>Análise de Trabalhos Acadêmicos</h2>

# Fatores que Impactam o Custo de um Projeto de Software

O custo de um projeto de software é influenciado por uma rede complexa de fatores.  
As estimativas devem considerar diversas variáveis, agrupadas em quatro categorias principais:

## Atributos do Produto
- Complexidade do software  
- Tamanho do banco de dados da aplicação  
- Nível de confiabilidade e segurança exigidos  

## Atributos de Hardware
- Restrições de desempenho  
- Restrições de memória  
- Volatilidade do ambiente de máquina virtual  

## Atributos de Pessoal
- Experiência de analistas e engenheiros  
- Familiaridade com a linguagem de programação  
- Conhecimento do ambiente de aplicação  
- Dados históricos de projetos anteriores  
- Julgamento experiente  

A ausência de dados históricos ou de julgamento qualificado pode resultar em estimativas imprecisas.  

## Atributos do Projeto
- Uso de ferramentas de software  
- Métodos de engenharia de software aplicados  
- Cronograma de desenvolvimento exigido  

---

## Deseconomias de Escala
Em projetos maiores, o esforço de desenvolvimento tende a aumentar mais que o dobro quando o tamanho do projeto dobra.  
Causas principais:  
- Sobrecarga de comunicação entre membros da equipe  
- Complexidade da integração de sistemas maiores  

---

# Modelos de Estimativa de Custo

Existem diversas abordagens, mas duas das mais proeminentes na engenharia de software são:  
1. **COCOMO (Constructive Cost Model)**  
2. **Análise por Pontos de Função (APF)**  

---

## 1. COCOMO (Constructive Cost Model)

O **COCOMO** é um modelo **empírico** de estimativa de custo de software, desenvolvido por **Barry W. Boehm**.  

- Baseado em **equações de regressão** calibradas a partir de dados históricos.  
- **Versões:**  
  - **COCOMO 81:** baseado em 63 projetos.  
  - **COCOMO II:** baseado em 163 projetos, adaptado para:  
    - Ambientes de desenvolvimento modernos  
    - Reuso de código  

### Níveis do COCOMO
- **COCOMO Básico**  
  - Nível mais simples  
  - Usado para estimativas rápidas e preliminares  
  - Baseado apenas no tamanho do programa (KLOC)  
  - Precisão limitada (não considera outros atributos)  

- **COCOMO Intermediário**  
  - Extensão do básico  
  - Inclui drivers de custo (produto, hardware, pessoal e projeto)  
  - Gera um fator de ajuste de esforço 

- **COCOMO Detalhado**  
  - Mais preciso  
  - Decompõe o projeto em módulos  
  - Calcula esforço e tempo para cada parte individualmente  
  - Soma os resultados para obter o total  

---

## 2. Análise por Pontos de Função (APF)

A **APF** é uma metodologia que mede o **tamanho funcional do software** (a funcionalidade entregue ao usuário final).  

- Gerenciada pelo **International Function Point Users Group (IFPUG)**  
- **Padronizada** e **independente da tecnologia** de implementação  

### Componentes Funcionais da APF
1. **Entradas Externas (EE):** Recebem dados ou informações de controle de fontes externas  
2. **Saídas Externas (SE):** Produzem informações para usuários ou sistemas externos, geralmente com lógica de processamento  
3. **Consultas Externas (CE):** Entrada que gera uma saída informativa, sem alterar arquivos lógicos  
4. **Arquivos Lógicos Internos (ALI):** Grupos de dados mantidos dentro da aplicação  
5. **Arquivos de Interface Externa (AIE):** Grupos de dados usados pela aplicação, mas mantidos por outro sistema  

### Usos da APF
- Estimativa de custo e esforço  
- Gerenciamento de projetos  
- Avaliação de produtividade  

**No Brasil, a APF é obrigatória em contratações públicas de desenvolvimento de software.**  
