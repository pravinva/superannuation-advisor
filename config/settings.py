from dataclasses import dataclass

@dataclass
class AppConfig:
    catalog_name: str = "multi_country_pension"
    enable_judge: bool = True
    llm_temperature: float = 0.3

@dataclass  
class CountryConfig:
    name: str
    flag: str
    colors: dict
