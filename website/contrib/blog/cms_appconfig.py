from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm


class BlogAppConfig(AppHookConfig):
    pass


class BlogAppConfigForm(AppDataForm):
    pass


setup_config(BlogAppConfigForm, BlogAppConfig)
