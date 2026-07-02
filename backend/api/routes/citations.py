from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def find_citations(
    text: str
):

    import re

    citations = re.findall(
        r'\(\d{4}\)\s*\d+\s*SCC\s*\d+',
        text
    )

    return {
        "citations": citations
    }