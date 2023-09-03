import pytest
from dotenv import load_dotenv
import os

from py_dimensional.hdr import HDR

load_dotenv()
HDR_API_KEY = os.environ.get("HDR_API_KEY")
hdr = HDR(HDR_API_KEY)


class TestPage:
    url = "https://www.sec.gov/Archives/edgar/data/796343/000114036122033413/ny20005310x2_ex99-1.htm"

    def test_sec_page(self):
        page = hdr.page(self.url)
        assert page.url == self.url
        assert page.page_content[0:20] == "Exhibit 99.1\n\n![](ht"


class TestPageSearch:
    query = "How large is the figma aqusistion?"
    url = "https://www.sec.gov/Archives/edgar/data/796343/000114036122033413/ny20005310x2_ex99-1.htm"

    def test_page_search(self):
        results = hdr.page_search(self.url, self.query)
        assert results[0].content[:29] == "Investors and security holder"
        assert results[0].similarity > 0.8


class TestVectorSearch:
    query = "How large is the figma aqusistion?"

    def test_vector_search_engine(self):
        results = hdr.vector_search_engine(self.query)
        assert results[0].similarity > 0.8
