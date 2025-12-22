import streamlit as st 
from src.langgrapgagents.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Docstring for load_langgraph_agenticai_app
    """ 
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Erorr: Falied to load user input from the ui ")

    user_message=st.chat_input("Entrr Your Message")
