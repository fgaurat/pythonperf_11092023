import streamlit as st

from TodoDAO import TodoDAO 

def main():
    dao = TodoDAO('todos_db.db')
    st.title('Todos App !')
    todos = dao.findAll()
    st.table(data=todos)



if __name__=='__main__':
    main()
