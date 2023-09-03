import os
from dotenv import load_dotenv
from py_dimensional.hdr import HDR
import openai

load_dotenv()

HDR_API_KEY = os.environ.get("HDR_API_KEY")
GPT_MODEL = "gpt-3.5-turbo"

hdr = HDR(HDR_API_KEY)


def qa_over_webpage(url: str, query: str, limit: int = 3):
    results = hdr.page_search(url, query)

    context_str = ""
    for result in results[:limit]:
        context_str += result.content + "\n"

    completion = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Use the following context to answer the question: "
                + context_str,
            },
            {"role": "user", "content": query},
        ],
        temperature=0.0,
    )
    text = completion.choices[0].message.content
    return text


query = "How large is the figma aqusistion?"
url = "https://www.sec.gov/Archives/edgar/data/796343/000114036122033413/ny20005310x2_ex99-1.htm"


print(f"Source webpage: {url}")
print(
    f"""
    Question: {query}
    Answer: {qa_over_webpage(url, query)}
      """
)
query = "When is the conference call?"
print(
    f"""
    Question: {query}
    Answer: {qa_over_webpage(url, query)}
      """
)

query = "Who is buying figma?"
print(
    f"""
    Question: {query}
    Answer: {qa_over_webpage(url, query)}
    """
)


def rag_over_the_entire_internet(query: str, limit: int = 10):
    results = hdr.vector_search_engine(query)
    context_str = ""
    for result in results[:limit]:
        context_str += result.content + "\n"

    completion = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Use the following context to answer the question: "
                + context_str,
            },
            {"role": "user", "content": query},
        ],
        temperature=0.0,
    )
    text = completion.choices[0].message.content
    return text


query = "Who is buying figma?"
print(
    f"""
    Question: {query}
    Answer: {rag_over_the_entire_internet(query)}
"""
)
