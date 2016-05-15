# Base setting file, content will be imported in DjangoAutoConf
# Default database name, can be override in extra_settings.settings
from django_dev_server_auto_conf import DjangoDevServerAutoConf

MYSQL_DATABASE_NAME = "test"

AUTHENTICATION_BACKENDS = []

TEMPLATE_CONTEXT_PROCESSORS = []

f = DjangoDevServerAutoConf()
f.configure()

final_settings = f.django_auto_conf.setting_storage.get_settings()

for attr in dir(final_settings):
    vars()[attr] = getattr(final_settings, attr)
