# Step One
import os
from langchain_core.prompts import PromptTemplate # Import PromptTemplate for creating structured prompts
from langchain_openai import ChatOpenAI # Import ChatOpenAI for interacting with OpenAI's chat models

information = "" # Define a variable to hold the input information

if __name__ == "__main__": 
    print("hello lagchain")

    summary_template = ( # Define a string template for the prompt, including placeholders for question and information
        "Based on the following information, give a direct one-line answer to the question:\n"
        "Question: {question}\n"
        "Information: {information}\n"
        "Answer:"
    )

    # Create a PromptTemplate instance, specifying the input variables it expects
    summary_prompt_template = PromptTemplate(input_variables=["question", "information"], template=summary_template)

    # Initialize the ChatOpenAI language model with a temperature of 0 (for deterministic output) and a specific model
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    # Create a chain by piping the prompt template to the language model
    chain = summary_prompt_template | llm

    # Invoke the chain with the input information and a dummy question, then store the result
    # Corrected input_variables to include "question"
    res = chain.invoke(input={"information" : information, "question": "What is the summary?"}) 

    print(res)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Step Two 
import os
from langchain_core.prompts import PromptTemplate # Import PromptTemplate for creating structured prompts
from langchain_openai import ChatOpenAI # Import ChatOpenAI for interacting with OpenAI's chat models

# Ensure OpenAI API key is available
assert os.getenv("OPEN_AI_KEY")

# Initialize the OpenAI chat model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) # Initialize the ChatOpenAI model with specific parameters

# Prompt to ensure one-line factual response
# Create a PromptTemplate instance directly from a template string
prompt_template = PromptTemplate.from_template(
    "Answer the following question in one short, factual line:\n\nQuestion: {question}\nAnswer:"
)

# Create chain by combining prompt and LLM
# Create a chain by piping the prompt template to the language model
chain = prompt_template | llm 

def ask(question: str):
    response = chain.invoke({"question": question}) # Invoke the chain with the given question
    return response.content.strip()

# Example questions
if __name__ == "__main__":
    questions = [
        "Who is the Prime Minister of India?",
        "...."
    ]

    for q in questions: 
        print(f"Q: {q}\nA: {ask(q)}\n")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

