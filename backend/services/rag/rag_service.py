from services.rag.prompt_builder import (
    PromptBuilder
)

from services.llm.factory import (
    LLMFactory
)


class RAGService:

    @staticmethod
    def ask_question(
        retriever,
        question: str,
        history: str = "",
        language: str = "English"
    ):

        docs = retriever.invoke(question)

        context = "\n\n".join(
            [
                doc.page_content
                for doc in docs
            ]
        )

        prompt = (
            PromptBuilder
            .get_prompt()
            .format(
                context=context,
                history=history,
                question=question,
                language=language
            )
        )

        llm = LLMFactory.create()

        response = llm.invoke(prompt)

        return response.content