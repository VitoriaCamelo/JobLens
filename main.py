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
      <div class="div-buscar" style="width: 100%; height: 80%; padding:5%; background-img: 'image 1.png'; border-radius: 50%">
        <h1>Buscar vagas</h1>
        <p>A plataforma auxilia estagiários e profissionais em transição de carreira a conseguir vagas.</p>
      </div>
      <div class="div-tecnologia" style="width: 100%; height: 80%; padding:5%; border-radius: 50%">
        <h1>Para tecnologia</h1>
        <p>O setor está em constante expansão e a procura por vagas está cada vez maior.</p>
      </div>
      <div class="div-mecanismos" style="width: 100%; height: 80%; padding:5%; border-radius: 50%">
        <h1>Mecanismos inteligentes</h1>
        <p>Usamos tecnologias de IA para traçar o perfil dos usuários e encontrar as melhores vagas</p>
      </div>
      """,
      unsafe_allow_html=True
  )

cargos = st.container()
# Clear all those elements:
st.button("Voltar para página inicial", type="primary")
if st.button('Pesquisar requisitos'):
  principal.empty()
  cargos.subheader(f"Cargos registrados:")
  for cargo in requisitos_vagas:
      # caixas expansíveis
      with cargos.expander(cargo.upper()):
        for requisito in requisitos_vagas[cargo]:
          st.write(f"- {requisito}")
          st.write(f"- {detalhes}")



search_query = st.text_input("Digite tipo de vaga (ex.: backend)", "")
if search_query.lower() in requisitos_vagas:
  st.subheader(f"Principais Requisitos para a posição de {search_query.capitalize()}:")
  for vaga, requisito in requisitos_vagas[search_query.lower()].items():
      # Use st.expander para criar caixas expansíveis
      with st.expander(vaga):
          st.write(f"- {requisito}")

elif search_query:
  st.warning(f"Nenhuma vaga correspondente encontrada para a pesquisa '{search_query}'.")

# Variável para controlar a visibilidade dos elementos
mostrar_cargos = False

# Adicione uma barra lateral para o filtro de área
with st.sidebar:
    st.header("Filtrar por Área:")
    selected_area = st.selectbox("Escolha uma área:", list(cargos_por_area.keys()))

# Mostrar os cargos na área selecionada quando o usuário selecionar uma área
if selected_area:
    mostrar_cargos = True

# Verifica se a variável mostrar_cargos é verdadeira antes de mostrar os cargos
if mostrar_cargos:
    st.header(f"Cargos na área de {selected_area.capitalize()}:")
    if selected_area in cargos_por_area:
        for vaga in cargos_por_area[selected_area]:
            if st.button(vaga):
                st.write(f"Requisitos para {vaga}:")
                requisito = requisitos_vagas.get(vaga, "Requisitos não encontrados.")
                st.write(requisito)

