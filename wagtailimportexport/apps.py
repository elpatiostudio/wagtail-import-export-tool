from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailImportExportAppConfig(AppConfig):
    name = 'wagtailimportexport'
    label = 'wagtailimportexport'
    verbose_name = _("Import/Export Tool")