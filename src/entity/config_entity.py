from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    app_title: str
    app_version: str
    app_debug: bool
    app_port: int
    app_host: str
    app_reload: bool
    app_description: str
    app_lifespan: str
    app_entry_point: str
    app_developer_email: str
    app_developer_name: str
    app_developer_repo_url: str


@dataclass(frozen=True)
class DatabaseConfig:
    database_url: Path
    