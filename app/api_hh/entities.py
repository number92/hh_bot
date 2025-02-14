from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass
class BaseDataClass:
    id: str
    name: str


@dataclass
class EmploymentForm(BaseDataClass):
    """Название типа занятости"""

    pass


@dataclass
class TypeVacancy(BaseDataClass):
    """Название типа вакансии"""

    pass


@dataclass
class ProfessionalRoles(BaseDataClass):
    """Название профессиональной роли"""

    pass


@dataclass
class Experience(BaseDataClass):
    """Требуемый опыт работы"""

    pass


@dataclass
class WorkFormat(BaseDataClass):
    """Требуемый опыт работы"""

    pass


@dataclass
class Area(BaseDataClass):
    """Класс для представления региона."""

    url: str


@dataclass
class Employer(BaseDataClass):
    """Класс для представления работодателя."""

    url: str | None = ""
    alternate_url: str | None = ""
    logo_urls: Dict[str, str] | None = None
    vacancies_url: str = ""
    accredited_it_employer: Optional[bool] = None
    trusted: Optional[bool] = None


@dataclass
class Salary:
    """Класс для представления информации о зарплате."""

    from_amount: Optional[float]
    to_amount: Optional[float]
    currency: Optional[str] = None
    gross: Optional[bool] = None


@dataclass
class Snippet:
    """Класс для представления требований и обязанностей вакансии."""

    requirement: str | None = None
    responsibility: str | None = None


@dataclass
class Address:
    """Класс для представления адреса вакансии."""

    building: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    metro_stations: Optional[List[Dict[str, str]]] = None
    street: Optional[str] = None


@dataclass
class Contact:
    """Класс для представления контактной информации."""

    email: Optional[str] = None
    name: Optional[str] = None
    phones: Optional[List[Dict[str, str]]] = None

    def get_full_phone_numbers(self) -> List[str]:
        full_numbers = []
        if self.phones:
            for phone in self.phones:
                full_number = f"+{phone.get('country', '')} {phone.get('city', '')} {phone.get('number', '')}"
                comment = phone.get("comment")
                if comment:
                    full_number += f" ({comment})"
                full_numbers.append(full_number)
        return full_numbers


@dataclass
class Department(BaseDataClass):
    """Класс для представления информации о департаменте."""

    pass


@dataclass
class KeySkill:
    """Класс для представления ключевых навыков."""

    name: Optional[str] = None


@dataclass
class Language(BaseDataClass):
    """Класс для представления информации о языке."""

    level: Optional[Dict[str, str]] = None


@dataclass
class Vacancy(BaseDataClass):
    """Класс для представления вакансии."""

    area: Area
    employer: Employer
    snippet: Snippet
    published_at: str
    has_test: bool
    initial_created_at: str
    published_at: str
    premium: bool
    vacancy_type: TypeVacancy
    professional_roles: List[ProfessionalRoles]
    work_format: Optional[List[WorkFormat]] = None
    url: str | None = None
    alternate_url: str | None = None
    response_url: Optional[str] = None
    description: Optional[str] = None
    salary: Optional[Salary] = None
    address: Optional[Address] = None
    contacts: Optional[Contact] = None
    department: Optional[Department] = None
    key_skills: Optional[List[KeySkill]] = None
    languages: Optional[List[Language]] = None
    employment_form: EmploymentForm | None = None
    experience: Experience | None = None


@dataclass
class ShortVacancy(BaseDataClass):
    """Класс для представления вакансии."""

    area: Area
    vacancy_type: TypeVacancy
    salary: Optional[Salary]
    employer: Employer
    snippet: Snippet
    published_at: str
    created_at: str
    premium: bool
    url: str = None
    alternate_url: str = None
    response_url: Optional[str] = None


@dataclass
class EmployerInfo(BaseDataClass):
    """Класс для представления информации о работодателе."""

    open_vacancies: int
    logo_urls: Dict[str, str] | None = None
    description: str = None
    area: Area | None = None
    alternate_url: str = None
    vacancies_url: str = None
    trusted: Optional[bool] = None
    accredited_it_employer: Optional[bool] = None


@dataclass
class EmployerVacanciesResponse:
    """Класс для представления ответа с вакансиями работодателя."""

    items: List[Vacancy]
