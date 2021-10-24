from django.apps import apps
from django.contrib import admin

models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

for model_name, model in apps.get_app_config('api').models.items():
    admin.site.register(model)
