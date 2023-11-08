import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader

with open('pages/contas.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Formulário de login principal
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    if username == 'jsmith':
        st.write(f'Welcome {name}')
        st.title('Application 1')
    elif username == 'rbriggs':
        st.write(f'Welcome {name}')
        st.title('Application 2')
elif authentication_status == False:
    st.error('Nome de usuário/senha está incorreto(a)')
elif authentication_status == None:
    st.warning('Por favor digite seu nome de usuário e sua senha')
