

# from src.langgrapgagents.state.state import State


# class BasicChatBotNode:
#     """
#     Docstring for BasicChatBotNode
#     Basic Chatbot login implementation
#     """
#     def __init__(self,model):
#         self.llm=model 
    
#     def process(self,state:State) -> dict :
#         """
#         Process the input state and generates a chatbot response
#         """
#         return {"messages":self.llm.invoke(state["message"])}
from src.langgrapgagents.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}

