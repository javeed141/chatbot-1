from langgraph.graph import StateGraph ,START,END 
from src.langgrapgagents.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgrapgagents.nodes.chatbot_with_tool import ChatbotWithToolNode
from src.langgrapgagents.state.state import State
from src.langgrapgagents.tools.search_tool import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition,ToolNode

class GraphBuilder :
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)


    def basic_chatbot_build_graph(self):


        self.basic_chatbot_node=BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools(self):
        """
        Docstring for chatbot_with_tools
        
        :param self: Description
        """
        tools=get_tools()
        tool_node=create_tool_node(tools)
        # Defnining the model

        llm=self.llm 
        #defint chatbot node 
        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)


        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition
        )
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase =="Chatbot With Tool":
            self.chatbot_with_tools()
        return self.graph_builder.compile()