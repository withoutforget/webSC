from dataclasses import dataclass, field
from adaptix import Retort
from dynaconf import Dynaconf


@dataclass(slots=True)
class ApiConfig:
    project_name: str = ''

    allow_origins: list[str] = field(default_factory = lambda: list())
    allow_headers: list[str] = field(default_factory = lambda: list())
    allow_methods: list[str] = field(default_factory = lambda: list())

    allow_credentials: bool = True

@dataclass(slots=True)
class Config:
    api: ApiConfig

def get_config() -> Config:
    dynaconf = Dynaconf(
        settings_files = ['./src/config.toml'],
        load_dotenv = True
    )

    retort = Retort()
    cfg: Config = retort.load(dynaconf, Config)

    return cfg

