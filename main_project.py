import os
from typing import TypedDict


# lets create the state first

class pipelinestate(TypedDict):
    raw_input:str
    edited_text:str
    script_text:str
    final_output:str


from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatMistralAI(model="mistral-small-2603",temperature=0.7)

def editior_node(state:pipelinestate)->dict:
    """stage 1. cleans up grammer, remove typos, and refines the tone."""

    prompt=(
        "you are an expert copyeditor. clean up the following raw text."
        "fix any grammatical errors, spelling mistakes, and smooth out the the transition flow."
        "while keeping the core message intact. return onlythe edited text.\n\n"
        f"Text:\n{state['raw_input']}"
    )

    response=llm.invoke(prompt)

    return {"edited_text": response.content.strip()}


def scriptwriter_node(state: pipelinestate)->dict:
    """stage 2 : formats the clean text into an engaging video script style."""
    print("\n----stage 2 Executing scriptwriter Node ---")

    prompt=(
        "you are a charismatic youtube content creator. Take this edited text and transform"
        "it into a highly engaging, punching and conversational video script hook. Make it sound"
        "like a real person is speaking passionately. Return the script content.\n\n"
        f"Edited text : \n{state['edited_text']}"

    )

    response=llm.invoke(prompt)

    return {"script_text": response.content.strip()}


def translator_node(state:pipelinestate)->dict:
    """it translate the output of scriptwriter node in hinglish"""
    print("\n\nstage 3 scriptwriter node is executing....")


    prompt=(
        "you are a excellent translator who translate the script into hinglish"
        "translate the script provided by the scriptwriter node."
        "and also remove the ai generated symbols like *** when you provide the answer"
        f"script:\n{state["script_text"]}"
    )

    response=llm.invoke(prompt)

    return {"final_output":response.content.strip()}

# now your state and nodes are ready and now it is time to create the graph
# and for creating the graph you have to connect the these nodes and for that you have
# to use the edges 
# edges are very important to create the workflows


from langgraph.graph import StateGraph, START,END

graph=StateGraph(pipelinestate)
graph.add_node("editor",editior_node)
graph.add_node("script_writer",scriptwriter_node)
graph.add_node("translator",translator_node)


# Add edges (sequential)

graph.add_edge(START,"editor")
graph.add_edge("editor","script_writer")
graph.add_edge("script_writer","translator")
graph.add_edge("translator",END)


# compile the graph


app=graph.compile()

result=app.invoke({
    "raw_input": "Ai agents are the future of tech. They can think, plan, and act on there own."
})

# output

print("Your result are : \n\n")
print(result["final_output"])