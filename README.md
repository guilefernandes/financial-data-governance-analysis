# Governança Inteligente de Dados

**Detecção de Anomalias e Análise Comparativa de Maturidade com Redes Neurais**

Projeto de Trabalho de Conclusão de Curso do MBA em Data Science & Analytics
da USP/ESALQ (2026).

## Sobre o trabalho

O estudo investiga como técnicas de inteligência artificial e processamento de
linguagem natural podem apoiar a avaliação da governança de dados em
instituições financeiras brasileiras. O objetivo é combinar a análise
semântica de relatórios anuais e dados de reclamações do Banco Central do
Brasil (BCB) com indicadores financeiros coletados nas próprias instituições,
para comparar a maturidade declarada e investigar sua relação com reclamações
e desempenho financeiro.

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
- `00.b` — PDFs do ranking de reclamações do BCB e CSV de indicadores
  financeiros e institucionais compilados;
- `00.c` — bases do ranking de reclamações do Banco Central;
- `00.d` — tabela de irregularidades regulatórias do Banco Central;
- `00.e` — referências sobre governança de dados e regulação; inclui uma
  apresentação do BCB sobre autorregulação bancária e a publicação BCBS 239;
  a obra DAMA-DMBOK não está incluída;
- `00.f` — relatórios anuais integrados usados na análise; os PDFs são fontes
  de terceiros e não são versionados. O inventário em `docs/` mantém os links
  oficiais para consulta e obtenção local;
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
2. Disponibilize no ambiente os arquivos `00.b`–`00.d` e os PDFs das
   instituições referenciados pelo notebook. As bases e os PDFs de `00.b`–`00.d`
   e os relatórios institucionais não são distribuídos neste repositório.
   Consulte as fontes oficiais na seção abaixo, baixe ou prepare os arquivos
   localmente na pasta raiz, usando os nomes esperados pelo notebook. Para os
   relatórios, use também os links de `docs/fontes-relatorios-anuais.csv`.
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

As fontes devem ser citadas junto com o período e a data de consulta quando
esses dados estiverem disponíveis:

| Material | Fonte | Referência |
| --- | --- | --- |
| CSVs de reclamações e clientes (`00.c`) | Banco Central do Brasil (BCB) | Os três arquivos CSV foram obtidos do conjunto [Ranking de Instituições por Índice de Reclamações](https://dadosabertos.bcb.gov.br/dataset/ranking-de-instituicoes-por-indice-de-reclamacoes). Confira o período ao obter uma versão atualizada. |
| PDFs do ranking de reclamações (`00.b`) e tabela de irregularidades (`00.d`) | Banco Central do Brasil (BCB) | Consulte a [página oficial dos rankings do Banco Central](https://www.bcb.gov.br/estabilidadefinanceira/rankingsbc) e selecione o período correspondente. |
| Indicadores financeiros e institucionais (`00.b`) | Instituições financeiras individualmente | Os indicadores foram coletados nas fontes oficiais de cada banco, como demonstrações financeiras e páginas de relações com investidores. |
| Material de referência sobre autorregulação bancária | Banco Central do Brasil (BCB), sobre a autorregulação da Febraban | [Apresentação “Autorregulação Bancária Febraban”, do diretor Isaac Sidney](https://www.bcb.gov.br/conteudo/home-ptbr/TextosApresentacoes/Autorregula%C3%A7%C3%A3o%20Banc%C3%A1ria%20Febraban%20-%20Diretor%20Isaac%20Sidney.pdf), hospedada no site do BCB. |
| Principles for Effective Risk Data Aggregation and Risk Reporting (BCBS 239) | Basel Committee on Banking Supervision / Bank for International Settlements | [Publicação oficial do BIS](https://www.bis.org/publ/bcbs239.htm); a cópia PDF local não é distribuída, mas no link está disponível para download da versão. |
| Relatórios anuais integrados (`00.f`) | Instituições financeiras identificadas no inventário | Os PDFs não são distribuídos neste repositório. O [inventário por arquivo](docs/fontes-relatorios-anuais.csv) registra o portal oficial, a data de verificação e os links. As observações identificam referências complementares que não correspondem ao relatório integrado do ano listado. |
| Gráficos e base consolidada (`00.g`–`00.h`) | Resultados deste projeto | Produzidos pelo notebook deste projeto a partir dos dados e documentos identificados acima. |

As bases do BCB são públicas, mas os arquivos locais `00.b`–`00.d` (CSVs e
PDFs) ficam fora do Git; consulte os portais oficiais para obter os dados e
confira o período antes de reutilizá-los. Os relatórios anuais estão
disponíveis nas instituições emissoras, mas isso não torna automaticamente
irrestrita a redistribuição de cada documento. Por isso, os PDFs dos
relatórios institucionais também ficam fora do Git; consulte os links do
inventário e as condições de uso de cada fonte. O inventário reúne as
referências diretas e complementares e registra as ressalvas sobre o tipo e o
ano do documento. A data registrada é a verificação do portal oficial.

O PDF do DAMA-DMBOK e a cópia local da publicação BCBS 239 não são
versionados. Para consultar a apresentação do BCB sobre autorregulação e a
publicação BCBS 239, use os links indicados acima; para o DAMA-DMBOK, consulte
a fonte e as condições de acesso do editor.

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
