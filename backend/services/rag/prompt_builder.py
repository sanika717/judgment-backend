try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    from langchain.prompts import PromptTemplate


class PromptBuilder:

    @staticmethod
    def get_prompt():

        return PromptTemplate(
            input_variables=[
                "context",
                "history",
                "question",
                "language"
            ],
            template="""
You are an AI Legal Judgement Assistant specializing in Indian Law.

Use only the provided context.

Context:
{context}

History:
{history}

Question:
{question}

Answer in {language}.
"""
        )
