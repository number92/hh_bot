import asyncio
import aiohttp
from contextlib import asynccontextmanager
from typing import List, Optional
from app.api_hh.response import ApiResponseVacancyParser
from app.api_hh import entities as type_hh


class HHApi:
    BASE_URL = "https://api.hh.ru"
    HH__USER_AGENT = "HHbot(rav.92@list.ru)"

    def __init__(self, user_agent: Optional[str] = None, hh_user_agent: Optional[str] = None):
        self.session = aiohttp.ClientSession()
        self.user_agent = user_agent or self.HH__USER_AGENT
        self.hh_user_agent = hh_user_agent

    async def close(self):
        await self.session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    def _get_headers(self) -> dict:
        headers = {}
        if self.hh_user_agent:
            headers["HH-User-Agent"] = self.hh_user_agent
        else:
            headers["User-Agent"] = self.user_agent

        if not headers:
            raise aiohttp.ClientError("400 Bad Request: Neither User-Agent nor HH-User-Agent was provided.")

        return headers

    async def _make_request(self, url: str, params: Optional[dict] = None) -> dict:
        async with self.session.get(url, params=params, headers=self._get_headers()) as response:
            response.raise_for_status()
            return await response.json()

    def _vacancy_is_open(self, vacancy: type_hh.Vacancy) -> bool:
        return vacancy.vacancy_type.id == "open"

    async def get_vacancy(self, vacancy_id) -> type_hh.Vacancy:
        """Получить информацию о конкретной вакансии по ID."""
        data = await self._make_request(f"{self.BASE_URL}/vacancies/{vacancy_id}")
        parser = ApiResponseVacancyParser(data)
        return parser.parse_vacancy()

    async def get_area_by_id(self, area_id) -> type_hh.Area:
        """Получить информацию о регионе по ID."""
        data = await self._make_request(f"{self.BASE_URL}/areas/{area_id}")
        parser = ApiResponseVacancyParser(data)
        return parser.parse_area()

    async def get_employer(self, employer_id: str) -> type_hh.EmployerInfo:
        """Получить информацию о работодателе по ID."""
        data = await self._make_request(f"{self.BASE_URL}/employers/{employer_id}")
        parser = ApiResponseVacancyParser(data)
        return parser.parse_employer_info()

    async def get_vacancies_by_employer_id(
        self, employer_id: str, page=0, per_page=20
    ) -> type_hh.EmployerVacanciesResponse:
        """Получить список вакансий конкретного работодателя по его ID."""
        params = {"employer_id": employer_id, "page": page, "per_page": per_page}
        data = await self._make_request(f"{self.BASE_URL}/vacancies", params=params)

        vacancies = []
        for item in data["items"]:
            vacancy = ApiResponseVacancyParser(item).parse_vacancy()
            vacancies.append(vacancy)

        return type_hh.EmployerVacanciesResponse(items=vacancies)

    async def get_full_vacancies_info_by_employer_id(
        self, employer_id: str, page=0, per_page=20
    ) -> List[type_hh.Vacancy]:
        """Получить полную информацию о всех вакансиях конкретного работодателя по его ID."""
        employer_vacancies_response = await self.get_vacancies_by_employer_id(employer_id, page, per_page)
        full_vacancies_info = await asyncio.gather(
            *(
                self.get_vacancy(vacancy.id)
                for vacancy in employer_vacancies_response.items
                if self._vacancy_is_open(vacancy)
            )
        )
        return full_vacancies_info


@asynccontextmanager
async def get_hh_client():
    hh_api = HHApi()
    try:
        yield hh_api
    finally:
        await hh_api.close()


async def test():
    async with get_hh_client() as hh_api:
        vacans = await hh_api.get_vacancy(116726962)
        print(vacans)


if "__main__" == __name__:
    asyncio.run(test())
