from pathlib import Path

import streamlit as st


PROJECT_DIR = Path(__file__).resolve().parent.parent

st.set_page_config(
    page_title="TCC | Governança Inteligente de Dados",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* O header do Streamlit (stHeader) mede 3.75rem (60px), é absolute e
       tem fundo opaco, cobrindo o topo do conteúdo. O padding-top abaixo
       deixa o título abaixo do header sem cortá-lo, mantendo o layout
       compacto (o padrão do Streamlit é 6rem). */
    [data-testid="stMainBlockContainer"] {
        padding-top: 1.5rem;
        padding-bottom: 0.5rem;
    }

    div[data-testid="stImage"] img {
        width: auto !important;
        max-width: 100%;
        max-height: calc(100vh - 390px);
        object-fit: contain;
        margin-left: auto;
        margin-right: auto;
    }

    @media (max-height: 700px) {
        div[data-testid="stImage"] img {
            max-height: calc(100vh - 380px);
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Governança Inteligente de Dados")
st.caption(
    "Detecção de anomalias e análise comparativa de maturidade com redes "
    "neurais · TCC do MBA USP/ESALQ, 2026"
)

def mostrar_grafico(nome_arquivo: str, descricao: str) -> None:
    caminho = PROJECT_DIR / nome_arquivo
    if not caminho.is_file():
        st.error(f"Não foi possível encontrar o gráfico: {nome_arquivo}")
        st.caption(f"Local esperado: {caminho}")
        return

    st.caption(descricao)
    st.image(str(caminho), use_container_width=True)


aba_sobre, aba_maturidade, aba_desempenho, aba_reclamacoes = st.tabs(
    [
        "Sobre o estudo",
        "Maturidade em governança de dados",
        "Vs. Desempenho financeiro",
        "Vs. Reclamações",
    ]
)

with aba_sobre:
    st.subheader("Objetivo, escopo e método")
    st.markdown(
        """
        O TCC investiga como inteligência artificial e processamento de
        linguagem natural podem apoiar a avaliação da governança de dados em
        instituições financeiras brasileiras.

        **Objetivo**  
        Comparar a maturidade declarada em relatórios anuais integrados e
        investigar sua relação com reclamações e desempenho financeiro.

        **Escopo**  
        35 instituições financeiras; relatórios de 2024 ou do ano mais
        recente disponível; dados do Banco Central com 172 tipologias de
        irregularidade.

        **Método**  
        O Índice de Maturidade Sintético (ISM) proposto fundamenta-se em
        DAMA-DMBOK e BCBS 239, ponderando processos e estrutura (40%) e
        conformidade e risco (60%). O texto dos relatórios é representado
        por embeddings `paraphrase-multilingual-MiniLM-L12-v2` e explorado
        com uma rede neural siamesa. PCA, agrupamentos e análises de
        correlação apoiam a comparação entre instituições.

        **Limites da interpretação**  
        O ISM é uma proposta do estudo, não uma certificação independente da
        maturidade real. As associações observadas não demonstram
        causalidade. A correlação entre ISM e reclamações foi descrita como
        fraca e não estatisticamente significante, apesar da maior frequência
        de reclamações reportada para instituições com ISM inferior a 0,15.
        """
    )

with aba_maturidade:
    mostrar_grafico(
        "00.g Mapa de Maturidade de Governança de Dados clean.png",
        "A projeção compara as instituições segundo o ISM e dimensões "
        "semânticas extraídas dos relatórios. As cores representam o perfil "
        "de negócio (PC2), não rótulos de clusters.",
    )

with aba_desempenho:
    mostrar_grafico(
        "00.g Mapa de Maturidade de Governança vs. Performance Financeira.png",
        "O gráfico compara o ISM com o lucro anual. As cores representam "
        "o ROE e a linha vermelha mostra a tendência reportada no estudo. "
        "A associação não demonstra causalidade.",
    )

with aba_reclamacoes:
    mostrar_grafico(
        "00.g Mapa de Maturidade de Governança vs. Índice de Reclamações.png",
        "A correlação foi descrita como fraca e não significante, apesar da "
        "maior frequência reportada para instituições com ISM abaixo de 0,15.",
    )
