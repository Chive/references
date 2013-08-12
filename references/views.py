from django.shortcuts import render, get_object_or_404
from references.models import Reference
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

def index(request):
    reference_list = Reference.objects.all().order_by('-pub_date')
    context = {'reference_list': reference_list}
    return render(request, 'references/index.html', context)

def detail(request, reference_id):
    reference = get_object_or_404(Reference, pk=reference_id)
    request.toolbar.populate()
    menu = request.toolbar.get_or_create_menu('references-app', _('References'))
    menu.add_modal_item(_('Change this Reference'), url=reverse('admin:references_reference_change', args=[reference_id]))
    menu.add_modal_item(_('Show History of this Reference'), url=reverse('admin:references_reference_history', args=[reference_id]))
    menu.add_sideframe_item(_('Delete this Reference'), url=reverse('admin:references_reference_delete', args=[reference_id]))
    return render(request, 'references/detail.html', {'reference': reference})
