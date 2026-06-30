import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama   # ✅ replaced Gemini
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Default local model (can change in .env: OLLAMA_MODEL=llama3)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

def build_rag_chain(retriever, history=None, language=None):
    prompt = PromptTemplate(
        input_variables=["context", "history", "question", "language"],
        template="""
You are a helpful assistant specialized in Indian law.
Use the provided context and chat history to answer the question.

Rules:
- Answer only if the question is about Indian law or the context.
- If unrelated → reply: "I don't know."
- If no relevant history → say: "No relevant chat history."
- Always include source/page when possible.
- PDFs may be in any language → detect automatically.
- If user specifies a preferred language, reply strictly in {language}.

Context:
{context}

Chat History:
{history}

Question: {question}

Answer:
"""
    )

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        temperature=0,
    )

    def format_history(messages):
        return "\n".join([f"{m['role'].capitalize()}: {m['message']}" for m in messages]) if messages else ""

    history_str = format_history(history)

    chain = (
        {
            "context": lambda x: retriever.invoke(x["question"]),
            "history": lambda x: history_str,
            "question": RunnablePassthrough(),
            "language": lambda x: language or "the PDF's language",
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain
