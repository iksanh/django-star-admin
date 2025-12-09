from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BerkasItem
from .forms import BerkasItemForm
from .mixins import SidebarContextMixin


class BerkasItemListView(SidebarContextMixin, ListView):
    model = BerkasItem
    template_name = "pages/berkasitem/berkasitem_list.html"
    context_object_name = "berkasitems"
    paginate_by = 10

    parent = 'data_master'
    segment = 'berkas'


class BerkasItemDetailView(SidebarContextMixin, DetailView):
    model = BerkasItem
    template_name = "pages/berkasitem/berkasitem_detail.html"
    context_object_name = "berkasitem"

    parent = 'data_master'
    segment = 'berkas'

class BerkasItemCreateView(SidebarContextMixin, CreateView):
    model = BerkasItem
    form_class = BerkasItemForm
    template_name = "pages/berkasitem/berkasitem_form.html"
    success_url = reverse_lazy("berkasitem_list")

    parent = 'data_master'
    segment = 'berkas'

class BerkasItemUpdateView(SidebarContextMixin, UpdateView):
    model = BerkasItem
    form_class = BerkasItemForm
    template_name = "pages/berkasitem/berkasitem_form.html"
    success_url = reverse_lazy("berkasitem_list")

    parent = 'data_master'
    segment = 'berkas'

class BerkasItemDeleteView(SidebarContextMixin, DeleteView):
    model = BerkasItem
    template_name = "pages/berkasitem/berkasitem_confirm_delete.html"
    success_url = reverse_lazy("berkasitem_list")

    parent = 'data_master'
    segment = 'berkas'