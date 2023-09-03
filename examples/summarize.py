import os
from dotenv import load_dotenv
from py_dimensional.hdr import HDR
import openai

load_dotenv()

HDR_API_KEY = os.environ.get("HDR_API_KEY")
hdr = HDR(HDR_API_KEY)
GPT_MODEL = "gpt-3.5-turbo-16k"


def page_summary(url: str):
    page_content = hdr.page(url).page_content
    completion = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[
            {
                "role": "user",
                "content": "Please summarize the following web page: " + page_content,
            },
        ],
        temperature=0.0,
    )
    text = completion.choices[0].message.content
    return text


url = "https://www.sec.gov/Archives/edgar/data/796343/000114036122033413/ny20005310x2_ex99-1.htm"
print(f"Source webpage: {url}")
print(f"Page summary: {page_summary(url)}")
