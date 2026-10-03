# Governança Inteligente de Dados

**Detecção de Anomalias e Análise Comparativa de Maturidade com Redes Neurais**

Projeto de Trabalho de Conclusão de Curso do MBA em Data Science & Analytics
da USP/ESALQ (2026).

## Sobre o trabalho

O estudo investiga como técnicas de inteligência artificial e processamento de
linguagem natural podem apoiar a avaliação da governança de dados em
instituições financeiras brasileiras. O objetivo é combinar a análise
semântica de relatórios anuais com indicadores públicos do Banco Central do
Brasil (BACEN) para comparar a maturidade declarada pelas instituições e
investigar sua relação com reclamações e desempenho financeiro.

Para isso, o trabalho:

- analisa relatórios anuais integrados de 35 instituições financeiras,
  referentes a 2024 ou ao ano mais recente disponível;
- utiliza dados públicos do BACEN sobre reclamações e irregularidades,
  incluindo 172 tipologias para caracterizar perfis de governança;
- propõe um Índice de Maturidade Sintético (ISM), fundamentado nos frameworks
  DAMA-DMBOK e BCBS 239, com dimensões de processos e estrutura (40%) e de
  conformidade e risco (60%);
- representa o conteúdo dos relatórios com embeddings do modelo
  `paraphrase-multilingual-MiniLM-L12-v2` e explora comparação semântica por
  meio de uma rede neural siamesa;
- utiliza análise de componentes principais (PCA), agrupamentos e análises de
  correlação para comparar perfis entre instituições.

## Principais resultados reportados

O trabalho descreve três perfis de instituições: bancos com comunicação mais
burocrática, instituições que combinam maturidade técnica e comunicação
moderna, e fintechs em transição. A análise também reporta associação positiva
entre o ISM e indicadores de desempenho financeiro.

**Ressalva sobre os resultados de reclamações:** o texto relata frequência
maior de reclamações para instituições com ISM inferior a 0,15, mas também
descreve como fraca e não estatisticamente significante a correlação entre o
ISM e o índice de reclamações do BACEN. Essa divergência interna deve ser
considerada ao interpretar ou citar esse resultado. Os achados são associações
observadas na amostra e não demonstram, por si só, causalidade.

## Visualizações

### Mapa de maturidade e perfis das instituições

A projeção resume as instituições segundo o ISM e as dimensões semânticas
extraídas dos relatórios. Ela ajuda a comparar perfis e visualizar possíveis
agrupamentos; as cores representam o perfil de negócio (PC2), não rótulos de
clusters.

![Mapa de maturidade de governança de dados](00.g%20Mapa%20de%20Maturidade%20de%20Governan%C3%A7a%20de%20Dados.png)

### Maturidade de governança e desempenho financeiro

O gráfico compara o ISM com o lucro anual; a cor representa o ROE e a linha
vermelha mostra a tendência reportada no estudo.

![Maturidade de governança versus desempenho financeiro](00.g%20Mapa%20de%20Maturidade%20de%20Governan%C3%A7a%20vs.%20Performance%20Financeira.png)

## Estrutura dos arquivos

Os prefixos organizam os materiais por etapa:

- `00.a` — notebook principal de desenvolvimento;
- `00.b` — indicadores e rankings de reclamações;
- `00.c` — bases de reclamações, clientes e irregularidades;
- `00.d` — tabela de irregularidades;
- `00.e` — referências sobre governança de dados e regulação, mantidas fora
  deste repositório enquanto as permissões de redistribuição não forem
  confirmadas;
- `00.f` — relatórios anuais integrados usados na análise, também mantidos fora
  deste repositório até a confirmação das permissões;
- `00.g` — diagramas e visualizações;
- `00.h` — base consolidada gerada pela análise.

## Trabalho completo

Para leitura, consulte o [PDF do trabalho final — versão com dados de contato
pessoais removidos](docs/tcc-final-redigido.pdf). O documento mantém o conteúdo
do trabalho, mas suprime os endereços e e-mails da capa e remove os metadados
pessoais do PDF. Os arquivos originais permanecem fora desta pasta.

Antes de publicar este repositório como público, confirme as regras de
publicação da USP/ESALQ e as permissões aplicáveis a imagens, trechos e demais
materiais de terceiros incluídos no trabalho.

## Como executar

O notebook principal é
[`00.a Código para desenvolvimento do trabalho de conclusão.ipynb`](00.a%20C%C3%B3digo%20para%20desenvolvimento%20do%20trabalho%20de%20conclus%C3%A3o.ipynb).
Ele foi desenvolvido em Python no Google Colab e deve ser executado célula a
célula, em ordem.

1. Abra o notebook no Google Colab ou em um ambiente Jupyter.
2. Disponibilize no ambiente os CSVs e PDFs referenciados pelo notebook.
3. Execute as células na ordem apresentada, incluindo a célula inicial de
   instalação das dependências.

O notebook usa caminhos absolutos como `/content/...`, próprios do Google
Colab; para executá-lo localmente, será necessário adaptar os caminhos dos
arquivos. As dependências utilizadas incluem `pandas`, `numpy`, `pdfplumber`,
`nltk`, `rapidfuzz`, `sentence-transformers`, `scikit-learn`, `scipy`,
`matplotlib`, `seaborn`, `plotly` e `tensorflow`. As versões ainda não estão
fixadas em um arquivo de dependências, portanto a reprodução exata dos
resultados requer validar e registrar o ambiente utilizado.

A execução gera `00.h Relatório Anual Integrado TCC.csv` no diretório de
trabalho.

## Fontes e distribuição

Os dados de reclamações e irregularidades são atribuídos no estudo a fontes
públicas do BACEN; os relatórios anuais são publicados pelas próprias
instituições. Antes de redistribuir esses arquivos, confirme as condições de
uso e as licenças aplicáveis, registre as URLs e datas de acesso e verifique
se há conteúdo pessoal, confidencial ou restrito. Quando a redistribuição não
for permitida, prefira documentar a fonte e como obter os arquivos.

Os PDFs de referência e relatórios anuais existentes na pasta de trabalho não
são versionados neste repositório enquanto suas permissões de redistribuição
não forem verificadas. Para reproduzir a análise, obtenha esses documentos nas
fontes originais e disponibilize-os no diretório esperado pelo notebook.

## Estado e limitações

Este repositório reúne os materiais de análise, mas ainda requer validação da
reprodutibilidade integral do notebook e das versões das dependências. O ISM é
um índice sintético proposto pelo estudo, construído a partir de informações
públicas e declarações institucionais; não deve ser interpretado isoladamente
como certificação independente da maturidade real de uma instituição.

## Licença

Licença do código ainda não definida. A ausência de uma licença não concede
automaticamente permissão para reutilizar ou redistribuir o conteúdo. Dados e
documentos de terceiros podem estar sujeitos a condições próprias,
independentemente da licença que venha a ser escolhida para o código.
