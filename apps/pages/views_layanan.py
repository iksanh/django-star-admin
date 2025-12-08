from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Layanan
from .forms import LayananForm
from .mixins import SidebarContextMixin


class LayananListView(SidebarContextMixin, ListView):
    model = Layanan
    template_name = "pages/layanan/layanan_list.html"
    context_object_name = "layanans"
    parent = "data_master"
    segment = 'layanan'


class LayananDetailView(SidebarContextMixin, DetailView):
    model = Layanan
    template_name = "pages/layanan/layanan_detail.html"
    context_object_name = "layanan"

    parent = "data_master"
    segment = 'layanan'


class LayananCreateView(SidebarContextMixin, CreateView):
    model = Layanan
    form_class = LayananForm
    template_name = "pages/layanan/layanan_form.html"
    success_url = reverse_lazy("layanan_list")

    parent = "data_master"
    segment = 'layanan'

class LayananUpdateView(SidebarContextMixin, UpdateView):
    model = Layanan
    form_class = LayananForm
    template_name = "pages/layanan/layanan_form.html"
    success_url = reverse_lazy("layanan_list")

    parent = "data_master"
    segment = 'layanan'

class LayananDeleteView(SidebarContextMixin, DeleteView):
    model = Layanan
    template_name = "pages/layanan/layanan_confirm_delete.html"
    success_url = reverse_lazy("layanan_list")

    parent = "data_master"
    segment = 'layanan'