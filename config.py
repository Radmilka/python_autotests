from environs import Env

environments = Env()
environments.read_env()


class Config:
    BEST_TRAINER_TOKEN = environments.str('BEST_TRAINER_TOKEN')
    TRAINER_ID = environments.str('TRAINER_ID')
    PROJECT_LOG_LEVEL = environments.str('LOG_LEVEL', 'INFO')  # INFO by default
