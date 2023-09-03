from urllib.parse import urljoin, urlencode
from .hdr_types import PageResponse, PageSearchResult
from typing import List, Dict
import httpx


class HDR:
    api_key: str
    base_url: str = "https://api.hdr.is/"
    api_version: str = "v1"
    api_endpoint: str
    headers: Dict[str, str]

    _client: httpx.Client
    _aclient: httpx.AsyncClient

    def __init__(self, api_key: str, **client_kwargs):
        super().__init__()
        self.api_key = api_key

        self.headers = self._construct_headers(self.api_key, uses_x_key=True)
        self.api_endpoint = urljoin(self.base_url, self.api_version)

        self._client = httpx.Client(**client_kwargs)
        self._aclient = httpx.AsyncClient(**client_kwargs)

    def _construct_headers(self, api_key: str, uses_x_key: bool = False):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        return headers

    def _construct_url(self, path: str, **kwargs):
        return f"{self.api_endpoint}/{path}"

    def page(self, url: str) -> PageResponse:
        response = self._client.get(
            self._construct_url("pageproxy"), params={"url": url}, headers=self.headers
        )
        if response.status_code == 200:
            return PageResponse(**response.json())
        else:
            return f"Request failed with status code {response.status_code}"

    def page_search(
        self,
        url: str,
        query: str,
    ) -> PageSearchResult:
        endpoint = self._construct_url("pagequery")
        response = self._client.get(
            endpoint, params={"url": url, "query": query}, headers=self.headers
        )
        if response.status_code == 200:
            return [PageSearchResult(**obj) for obj in response.json()]
        else:
            raise httpx._exceptions.HTTPError(
                f"Request failed with status code {response.status_code}"
            )

    def vector_search_engine(
        self, query: str, limit: int = 3
    ) -> List[PageSearchResult]:
        endpoint = self._construct_url("vectorsearch")
        response = self._client.get(
            endpoint,
            params={"query": query},
            headers=self.headers,
            timeout=1000,
        )

        if response.status_code == 200:
            return [PageSearchResult(**payload) for payload in response.json()]
        else:
            print(response.text)
            raise httpx._exceptions.HTTPError(
                f"Request failed with status code {response.status_code}"
            )
