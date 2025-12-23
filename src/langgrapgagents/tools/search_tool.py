from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode 


def get_tools():
    """
    Docstring for get_tools
    Retruns the list of tools to be used in the chatbot
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Docstring for create_tool_node
    creates and returns a tool node for the graph
    :param tools: Description
    """
    return ToolNode(tools)