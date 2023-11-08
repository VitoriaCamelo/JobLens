import streamlit as st
from dados import requisitos_vagas, cargos_por_area

st.set_page_config(
    page_title="JobLens",
    page_icon="👋",
)

with st.container():
  image_url = "joblens2.png"
  st.image(image_url, caption="", use_column_width=True, width=50)

# conteudo principal
principal = st.empty()
with principal.container():
  st.markdown(
      """
      <div class="div-buscar" style="width: 100%; height: 80%; padding:5%; background-img: 'image 1.png'; border-radius: 20%">
        <h2>Buscar vagas e requisitos</h1>
        <p>A plataforma auxilia estagiários e profissionais em transição de carreira a conseguir vagas.</p>
      </div>
      <div class="div-tecnologia" style="width: 100%; height: 80%; padding:5%; border-radius: 20%">
        <h2>Para tecnologia</h1>
        <p>O setor está em constante expansão e a procura por vagas está cada vez maior.</p>
      </div>
      <div class="div-mecanismos" style="width: 100%; height: 80%; padding:5%; border-radius: 20%">
        <h2>Mecanismos inteligentes</h1>
        <p>Usamos tecnologias de IA para traçar o perfil dos usuários e encontrar as melhores vagas</p>
      </div>
      """,
      unsafe_allow_html=True
  )
  st.markdown(
    """
    <style>
    [data-testid="baseButton-secondary"]{
    margin-left: 20%
    }
    </style>
    """, unsafe_allow_html=True
  )
  botao_pesquisar = st.button("Clique aqui para pesquisar requisitos")

cargos = st.container()
# transicao de pagina
if botao_pesquisar:
  principal.empty()
  cargos.subheader(f"Cargos registrados:")
  for cargo in requisitos_vagas.keys():
    # caixas expansíveis
    with cargos.expander(cargo.upper()):
      for requisito in requisitos_vagas[cargo]:
        st.write(f"- {requisito}")
        for detalhe in requisitos_vagas[cargo][requisito].split(","):
          st.write(f"-- {detalhe}")
  st.button("Voltar para página inicial", type="primary")

# Variável para controlar a visibilidade dos elementos
mostrar_cargos = False

# Adicione uma barra lateral para o filtro de área
with st.sidebar:
    st.header("Filtrar por Área:")
    selected_area = st.selectbox("Escolha uma área:", list(cargos_por_area.keys()))

