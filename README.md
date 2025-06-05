# 📦 Mapeamento de Exportações no Brasil (2022 - 2025)

📄 [English version](README_English.md)

# Descrição
Este projeto tem como foco a análise das exportações brasileiras no período de 2022 a 2025, com base em dados públicos fornecidos pelo governo federal. Utilizando uma combinação de ferramentas como MySQL, Python e Power BI, foram desenvolvidas soluções para importação, modelagem e visualização interativa dos dados, com foco em insights logísticos e comerciais.

# Objetivo
Analisar o comportamento das exportações brasileiras, buscando responder às seguintes questões:
- Quais URFs (Unidades da Receita Federal) processam as exportações?
- Quais são as principais cargas movimentadas por estado?
- Quais os principais países de destino das exportações?
- Existe sazonalidade no fluxo mensal das cargas exportadas?

# Ferramentas Utilizadas
- **MySQL**: Armazenamento, estruturação e criação de views SQL otimizadas.
- **Python**: Automação da importação de arquivos CSV massivos para o MySQL.
- **Power BI**: Conexão ao banco de dados, modelagem no Power Query, criação de métricas em DAX e desenvolvimento do dashboard.

# Acesse o Dashboard
[Clique aqui para acessar o dashboard no Power BI](https://app.powerbi.com/view?r=eyJrIjoiYTVmZWQ0NWQtOGFjYy00MzhkLWE5MjAtNWZkNzc1ODc4MTllIiwidCI6ImNmNzJlMmJkLTdhMmItNDc4My1iZGViLTM5ZDU3YjA3Zjc2ZiIsImMiOjR9&embedImagePlaceholder=true)

# Visual do Dashboard
![Mapeamento de Exportações do Brasil (2022 - 2025) - Dashboard - Imagem](https://github.com/user-attachments/assets/e4e757a4-f0d4-4d2a-b40b-dd710d200d8a)

# Etapas do Processo (ELT)
**1. Extract (Extração):**
Os dados brutos de exportações foram obtidos a partir da base pública oficial do governo federal, disponível no portal do Ministério do Desenvolvimento, Indústria, Comércio e Serviços, em formato `.csv`.  

**2. Load (Carregamento):**
Os arquivos CSV brutos foram primeiramente carregados para o MySQL com o auxílio de um script em Python, que detecta automaticamente arquivos novos e realiza a importação em tabelas organizadas por ano.  

**3. Transform (Transformação):**
A transformação dos dados (joins, agrupamentos, cálculos e filtros) foi feita diretamente no Power Query do Power BI, garantindo flexibilidade e velocidade de ajustes sem a necessidade de alterar a base original.  

**4. Visualization (Visualização):**
Com os dados tratados, foram criados KPIs, medidas DAX e visuais interativos no Power BI para responder às perguntas-chave propostas no projeto.

# Automação com Python
Um script em Python foi desenvolvido com as seguintes funcionalidades:
- Detecta arquivos `.csv` iniciados por `EXP_` na pasta Downloads.
- Cria uma tabela vazia no MySQL (caso ainda não exista).
- Importa os dados com `LOAD DATA LOCAL INFILE`, otimizando a performance.
- Executa a função `UNION`, fazendo a junção com a tabela consolidada (tb_exportacoes_unificada).
- Renomeia o arquivo original, adicionando o prefixo `Importado_`.
- Move o arquivo processado para uma subpasta chamada `Arquivos processados`.  
📁 [Veja o script Python aqui](importador_exportacoes.py)

# Fonte dos Dados
Os dados utilizados são públicos e foram obtidos no site `GOV.BR`, na página:  
🔗 [Estatísticas de Comércio Exterior em Dados Abertos - Ministério do Desenvolvimento, Indústria, Comércio e Serviços](https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta)

# Arquivo de Teste
Para fins de demonstração e validação do script Python, este repositório inclui um arquivo `.csv` simplificado contendo 500 linhas simuladas, localizado [aqui](EXP_2021_test.csv).
Esse arquivo permite que qualquer usuário teste o fluxo completo do projeto — desde a criação da tabela no MySQL, passando pela importação automatizada via Python, até a atualização da tabela consolidada.
**Pré-requisitos para o teste:**
- Ter o MySQL instalado e em execução;
- Ter o Python instalado e o script de automação configurado corretamente.

# Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina Tecnologia da Informação Aplicada à Gestão de Operações e Processos, no 6º semestre do curso superior de Tecnologia em Gestão da Produção Industrial, da Faculdade de Tecnologia de São José dos Campos - Prof. Jessen Vidal (FATEC SJC).

# Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

# Tags
`#Python` `#MySQL` `#PowerBI` `#Exportações` `#AnáliseDeDados` `#Dashboard` `#EngenhariaDeDados` `#ETL` `#ComércioExterior` `#Python` `#MySQL` `#PowerBI` `#DataAnalysis` `#DataEngineering` `#ETL` `#ELT` `#BusinessIntelligence` `#BI` `#DataVisualization` `#PublicData` `#BrazilExports` `#SQL` `#CSV` `#Automation` `#OpenData`
