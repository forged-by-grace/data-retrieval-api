import os
from src.constants.constant import CONFIG_FILE_PATH
from src.utils.common import read_yaml
from src.entity.config_entity import AppConfig, DatabaseConfig


class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH):
        self.configs = read_yaml(config_filepath)


    def get_app_config(self) -> AppConfig:
        app_config = AppConfig(
            app_debug=self.configs.APP_DEBUG,
            app_title=self.configs.APP_TITLE,
            app_version=self.configs.APP_VERSION,
            app_host=self.configs.APP_HOST,
            app_port=self.configs.APP_PORT,
            app_reload=self.configs.APP_RELOAD,
            app_description=self.configs.APP_DESCRIPTION,
            app_entry_point=self.configs.APP_ENTRY_POINT,
            app_lifespan=self.configs.APP_LIFESPAN,
            app_developer_name=self.configs.APP_DEVELOPER_NAME,
            app_developer_email=self.configs.APP_DEVELOPER_EMAIL,
            app_developer_repo_url=self.configs.APP_DEVELOPER_REPO_URL
        )

        return app_config
    

    def get_database_config(self) -> DatabaseConfig:
        db_config = DatabaseConfig(
            database_url=self.configs.APP_DATABASE_URL
        )

        return db_config