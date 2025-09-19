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

<h2>Principais Pontos dos Trabalhos Acadêmicos</h2>

# Teses e Dissertações  

## Melhoria Na Consistência da Contagem de Pontos de Função  
- **Autor:** (Informação não disponível na fonte)  
- **Fonte:** Dissertação de Mestrado, Universidade de São Paulo (USP)  
- **Link:** [Acessar PDF](https://teses.usp.br/teses/disponiveis/100/100131/tde-02022016-012253/publico/MelhoriaNaConsistenciaContagemAPF.pdf)  
- **Pontos Principais:**  
  - Aborda a Análise por Pontos de Função (APF) e a crítica sobre a falta de confiabilidade entre diferentes contadores.  
  - Propõe uma ferramenta para melhorar a consistência da medição.  
  - Destaca que a APF é obrigatória em contratações públicas de software no Brasil.  

## Aplicando Aprendizado de Máquina para Estimativa de Esforço no Desenvolvimento de Software  
- **Autor:** Weldson Amaral Corrêa  
- **Fonte:** Dissertação de Mestrado, Universidade Federal do Maranhão (UFMA)  
- **Link:** [Acessar PDF](https://tedebc.ufma.br/jspui/handle/tede/3289)  
- **Pontos Principais:**  
  - Investiga como algoritmos de Aprendizado de Máquina (AM) podem auxiliar na estimativa de esforço de software.  
  - Utiliza bases de dados de projetos concluídos para gerar estimativas mais precisas.  
  - Demonstra que a metodologia proposta é consistente em diferentes conjuntos de dados.  

---

# Artigos Científicos e Manuais  

## Manual do Modelo COCOMO II  
- **Fonte:** Manual técnico da Rose-Hulman Institute of Technology  
- **Link:** [Acessar PDF](https://www.rose-hulman.edu/class/cs/csse372/201310/Homework/CII_modelman2000.pdf)  
- **Pontos Principais:**  
  - Detalha o modelo COCOMO II, que utiliza equações para estimar esforço e tempo de desenvolvimento.  
  - Explica os "fatores de escala", que representam economias e deseconomias de escala.  
  - Descreve o cálculo do tamanho do software a partir de código novo e reutilizado.  

## Methods for Estimating Agile Software Projects: A Systematic Review  
- **Autor:** (Informação não disponível na fonte)  
- **Fonte:** Artigo científico  
- **Link:** [Acessar PDF](https://www.researchgate.net/profile/Ed-Canedo/publication/328688948_Methods-for-Estimating-Agile-Software-Projects_A_Systematic_Review/links/5bf13fa0a6fdcc3a8ddf2a96/Methods-for-Estimating-Agile-Software-Projects-A-Systematic-Review.pdf)  
- **Pontos Principais:**  
  - Revisão sistemática sobre estimativas em projetos ágeis.  
  - Identifica o *Planning Poker* como técnica mais popular.  
  - Story Points e Pontos de Função são as métricas mais usadas.  
  - Ressalta que métricas tradicionais ainda são usadas em gestão de portfólio e benchmarking.  

## Evaluation of the Cost Estimation Models: Case Study of Task Manager Application  
- **Autor:** (Informação não disponível na fonte)  
- **Fonte:** Artigo científico  
- **Link:** [Acessar PDF](https://www.researchgate.net/publication/276232068_Evaluation_of_the_Cost_Estimation_Models_Case_Study_of_Task_Manager_Application)  
- **Pontos Principais:**  
  - Estudo de caso que avalia a precisão dos modelos COCOMO I e II.  
  - O modelo *Application Composition* do COCOMO II foi o mais preciso.  
  - Mostrou melhor desempenho para estimar tempo e custo em projeto de gerenciamento de tarefas.  

## The IFPUG Function Point Counting Method  
- **Autor:** (Informação não disponível na fonte)  
- **Fonte:** Artigo científico  
- **Link:** [Acessar PDF](https://www.researchgate.net/publication/314391334_The_IFPUG_Function_Point_Counting_Method)  
- **Pontos Principais:**  
  - Detalha os objetivos e áreas de aplicação da Análise por Pontos de Função (APF).  
  - Descreve a APF como medida de tamanho funcional sob a perspectiva do usuário.  
  - Método independente da tecnologia.  
  - Pode ser usado em estimativas de custo, gestão de projetos e análise de produtividade.  

<h2> Referências</h2>

# Referências

- **UNIVERSIDADE DE SÃO PAULO (USP).** Melhoria Na Consistência da Contagem de Pontos de Função. 2015. Dissertação (Mestrado em Ciências) – Escola de Artes, Ciências e Humanidades, Universidade de São Paulo, São Paulo, 2015. Disponível em: [https://teses.usp.br/teses/disponiveis/100/100131/tde-02022016-012253/publico/MelhoriaNaConsistenciaContagemAPF.pdf](https://teses.usp.br/teses/disponiveis/100/100131/tde-02022016-012253/publico/MelhoriaNaConsistenciaContagemAPF.pdf). Acesso em: [data de acesso].

- **CORRÊA, Weldson Amaral.** Aplicando Aprendizado de Máquina para Estimativa de Esforço no Desenvolvimento de Software. 2018. Dissertação (Mestrado em Ciência da Computação) – Universidade Federal do Maranhão, São Luís, 2018. Disponível em: [https://tedebc.ufma.br/jspui/handle/tede/3289](https://tedebc.ufma.br/jspui/handle/tede/3289). Acesso em: [data de acesso].

- **CANEDO, E. et al.** Methods for Estimating Agile Software Projects: A Systematic Review. 2018. Artigo científico. Disponível em: [https://www.researchgate.net/profile/Ed-Canedo/publication/328688948_Methods-for-Estimating-Agile-Software-Projects_A_Systematic_Review/links/5bf13fa0a6fdcc3a8ddf2a96/Methods-for-Estimating-Agile-Software-Projects-A-Systematic-Review.pdf](https://www.researchgate.net/profile/Ed-Canedo/publication/328688948_Methods-for-Estimating-Agile-Software-Projects_A_Systematic_Review/links/5bf13fa0a6fdcc3a8ddf2a96/Methods-for-Estimating-Agile-Software-Projects-A-Systematic-Review.pdf). Acesso em: [data de acesso].

- **EVALUATION of the Cost Estimation Models: Case Study of Task Manager Application.** 2015. Artigo científico. Disponível em: [https://www.researchgate.net/publication/276232068_Evaluation_of_the_Cost_Estimation_Models_Case_Study_of_Task_Manager_Application](https://www.researchgate.net/publication/276232068_Evaluation_of_the_Cost_Estimation_Models_Case_Study_of_Task_Manager_Application). Acesso em: [data de acesso].

- **THE IFPUG Function Point Counting Method.** 2017. Artigo científico. Disponível em: [https://www.researchgate.net/publication/314391334_The_IFPUG_Function_Point_Counting_Method](https://www.researchgate.net/publication/314391334_The_IFPUG_Function_Point_Counting_Method). Acesso em: [data de acesso].
