import streamlit as st
if "visibility" not in st.session_state:
  st.session_state.visibility = "visible"
  st.session_state.disabled = False
# Dados do perfil do usuário (exemplo)
perfil_usuario = {
    "Nome": "João Silva",
    "E-mail": "joao.silva@example.com",
    "Cargo": "Desenvolvedor Full Stack",
    "Experiência": "5 anos",
    "Habilidades": "Python, JavaScript, React, Node.js",
    "Descrição": "Desenvolvedor apaixonado por tecnologia e inovação."
}

st.set_page_config(
    page_title="JobLens",
    page_icon="👋",
)

st.title("Perfil do Usuário")
principal = st.empty()
with principal.container():
  st.subheader("Informações Pessoais")
  for campo, valor in perfil_usuario.items():
      st.write(f"{campo}: {valor}")
  editar = st.button("Editar perfil")

if editar:
  principal.empty()
  st.subheader("Edite as informações de conta desejadas")
  i = 0
  for campo in perfil_usuario.keys():
    text_input = st.text_input(
    f"{campo}",
    f"{perfil_usuario[campo]}",
    key="placeholder"+str(i),
    )
    st.write(f"Você digitou: {text_input}")
    if text_input:
      perfil_usuario[campo] = text_input
    i += 1
  if st.button("Salvar alterações"):
    st.subheader("Informações Pessoais")
    for campo, valor in perfil_usuario.items():
        st.write(f"{campo}: {valor}")
    editar = st.button("Editar perfil")
      

# Botão para assinar a assinatura premium
if st.button("Assinar Premium"):
  st.text("Implemente aqui a lógica para edição do perfil.")
