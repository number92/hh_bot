from app.api_hh import entities as hh
from typing import List, Optional, Type, TypeVar

T = TypeVar("T")


class ApiResponseVacancyParser:
    """
    Docs: https://api.hh.ru/openapi/redoc
    """

    def __init__(self, response_data):
        self.data = response_data

    def _parse_optional(self, key, cls: Type[T]) -> Optional[T]:
        if key in self.data and self.data[key] is not None:
            if hasattr(cls, "__dataclass_fields__"):
                return cls(**{k: v for k, v in self.data[key].items() if k in cls.__dataclass_fields__})
        return None

    def _parse_boolean(self, key: str, default: bool = False) -> bool:
        return self.data.get(key, default)

    def _parse_list_of_objects(self, key: str, cls: Type[T]) -> List[T]:
        """Парсит список объектов по ключу."""
        return [cls(**item) for item in self.data.get(key, []) if isinstance(item, dict)]

    def parse_has_test(self):
        return self._parse_boolean("has_test")

    def parse_initial_created_at(self):
        return self.data.get("initial_created_at")

    def parse_premium(self):
        return self.data.get("premium", False)

    def parse_area(self):
        return hh.Area(**self.data["area"])

    def parse_salary(self):
        salary = self.data.get("salary")
        if salary:
            salary_data = {
                "from_amount": salary.get("from"),
                "to_amount": salary.get("to"),
                "currency": salary.get("currency"),
                "gross": salary.get("gross"),
            }
            return hh.Salary(**salary_data)
        return None

    def parse_employer(self):
        return hh.Employer(**self.data["employer"])

    def parse_snippet(self):
        return self._parse_optional("snippet", hh.Snippet)

    def parse_address(self):
        return self._parse_optional("address", hh.Address)

    def parse_contacts(self):
        return self._parse_optional("contacts", hh.Contact)

    def parse_department(self):
        return self._parse_optional("department", hh.Department)

    def parse_employment_form(self):
        return self._parse_optional("employment_form", hh.EmploymentForm)

    def parse_experience(self):
        return self._parse_optional("experience", hh.Experience)

    def parse_professional_roles(self):
        return self._parse_list_of_objects("professional_roles", hh.ProfessionalRoles)

    def parse_work_format(self):
        return self._parse_list_of_objects("work_format", hh.WorkFormat)

    def parse_key_skills(self):
        return self._parse_list_of_objects("key_skills", hh.KeySkill)

    def parse_languages(self):
        return self._parse_list_of_objects("languages", hh.Language)

    def parse_vacancy_type(self):
        return self._parse_optional("type", hh.TypeVacancy)

    def parse_employer_info(self) -> hh.EmployerInfo:
        return hh.EmployerInfo(
            id=self.data["id"],
            name=self.data["name"],
            description=self.data.get("description"),
            area=self.parse_area(),
            open_vacancies=self.data.get("open_vacancies", 0),
            logo_urls=self.data.get("logo_urls"),
            alternate_url=self.data.get("alternate_url"),
            vacancies_url=self.data.get("vacancies_url"),
            trusted=self.data.get("trusted"),
            accredited_it_employer=self.data.get("accredited_it_employer"),
        )

    def parse_vacancy(self) -> hh.Vacancy:
        return hh.Vacancy(
            id=self.data["id"],
            name=self.data["name"],
            area=self.parse_area(),
            salary=self.parse_salary(),
            employer=self.parse_employer(),
            snippet=self.parse_snippet(),
            has_test=self.parse_has_test(),
            initial_created_at=self.parse_initial_created_at(),
            premium=self.parse_premium(),
            professional_roles=self.parse_professional_roles(),
            published_at=self.data["published_at"],
            url=self.data.get("url"),
            alternate_url=self.data["alternate_url"],
            response_url=self.data.get("response_url"),
            description=self.data.get("description"),
            address=self.parse_address(),
            contacts=self.parse_contacts(),
            department=self.parse_department(),
            key_skills=self.parse_key_skills(),
            languages=self.parse_languages(),
            employment_form=self.parse_employment_form(),
            experience=self.parse_experience(),
            work_format=self.parse_work_format(),
            vacancy_type=self.parse_vacancy_type(),
        )
