from cms.plugin_base import CMSPluginBase
from django.contrib import admin
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from references.models import ReferencePluginModel


class ReferencePlugin(CMSPluginBase):
    model = ReferencePluginModel
    name = _("Reference Plugin")
    render_template = "references/references_plugin_carousel.html"


    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['brands'] = instance.references.all()
        return context

plugin_pool.register_plugin(ReferencePlugin)