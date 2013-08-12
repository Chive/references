from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar

@toolbar_pool.register
class MoopModifier(CMSToolbar):

    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('references-app', _('References'))
            menu.add_sideframe_item(_('References Overview'), url=reverse('admin:references_reference_changelist'))
            menu.add_sideframe_item(_('Add new Reference'), url=reverse('admin:references_reference_add'))
