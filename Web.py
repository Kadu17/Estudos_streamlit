import streamlit as st

st.sidebar.title('Menu')
pagina = st.sidebar.selectbox('select the page',['options', 'files','date'])

if pagina == 'options':
    st.title('options')
    st.selectbox('Pick an option', ['Opção 1', 'Opção 2','Opção3'])
elif pagina == 'files':
    st.title('files')
    file = st.file_uploader("Pick a file")
elif pagina == 'date':
    st.title('Calendar')
    data = st.date_input("Pick a date")
