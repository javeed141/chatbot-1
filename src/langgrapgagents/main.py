import streamlit as st 
from src.langgrapgagents.LLMS.llm_grok import GrowLLM
from src.langgrapgagents.graph.graph_builder import GraphBuilder
from src.langgrapgagents.ui.streamlitui.display_result import DisplayResultStreamlit
from src.langgrapgagents.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    Docstring for load_langgraph_agenticai_app
    """ 
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Erorr: Falied to load user input from the ui ")

    user_message=st.chat_input("Enter Your Message")
    if user_message :
        try :
            obj_llm_config=GrowLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error :LLm model cound not be initilalised")
        
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Error : No use case selected")
                 
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set  up failed - {e}")
                return 
         
        except Exception as e:
                st.error(f"Error: Graph set  up failed - {e}")
                return 
