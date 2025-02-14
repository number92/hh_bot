from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass
class Area:
    """Класс для представления региона."""

    id: str
    name: str
    url: str


@dataclass
class Employer:
    """Класс для представления работодателя."""

    id: str
    name: str
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
    currency: str | None = None
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


@dataclass
class Contact:
    """Класс для представления контактной информации."""

    email: Optional[str] = None
    name: Optional[str] = None
    phones: Optional[List[Dict[str, str]]] = None


@dataclass
class Department:
    """Класс для представления информации о департаменте."""

    id: Optional[str] = None
    name: Optional[str] = None


@dataclass
class KeySkill:
    """Класс для представления ключевых навыков."""

    name: Optional[str] = None


@dataclass
class Language:
    """Класс для представления информации о языке."""

    id: Optional[str] = None
    name: Optional[str] = None
    level: Optional[Dict[str, str]] = None


@dataclass
class Vacancy:
    """Класс для представления вакансии."""

    id: str
    name: str
    area: Area
    employer: Employer
    snippet: Snippet
    published_at: str
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


@dataclass
class ShortVacancy:
    """Класс для представления вакансии."""

    id: str
    name: str
    area: Area
    salary: Optional[Salary]
    employer: Employer
    snippet: Snippet
    published_at: str
    url: str = None
    alternate_url: str = None
    response_url: Optional[str] = None


@dataclass
class EmployerInfo:
    """Класс для представления информации о работодателе."""

    id: str
    name: str
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
