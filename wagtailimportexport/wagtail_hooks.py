from django.urls import include, re_path, reverse
from django.utils.translation import gettext_lazy as _

from wagtail import hooks
from wagtail.admin.menu import MenuItem

from wagtailimportexport import admin_urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    """
    Register 'import-export/' url path to admin urls.
    """
    return [
        re_path(r'^import-export/', include(admin_urls, namespace='wagtailimportexport')),
    ]


class ImportExportMenuItem(MenuItem):
    """
    Add the menu item to admin side menu. This will be only shown if the user is
    superuser. This will be only shown if the user is
    superuser.
    """
    def is_shown(self, request):
        return request.user.is_superuser


@hooks.register('register_admin_menu_item')
def register_import_export_menu_item():
    """
    Add the menu item to admin side menu.
    """
    return ImportExportMenuItem(
        _('Import / Export'), reverse('wagtailimportexport:index'), classnames='icon icon-download', order=800
    )