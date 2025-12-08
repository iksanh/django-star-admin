from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import CatatanTemplate as Catatan
from .forms import CatatanTemplateForm
from .mixins import SidebarContextMixin


class CatatanListView(SidebarContextMixin, ListView):
    model = Catatan
    template_name = "pages/catatan/catatan_list.html"
    context_object_name = "catatans"

    parent = "data_master"
    segment = 'catatan'

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = "Catatan"

        return context


class CatatanDetailView(SidebarContextMixin, DetailView):
    model = Catatan
    template_name = "pages/catatan/catatan_detail.html"
    context_object_name = "catatan"

    parent = "data_master"
    segment = 'catatan'


class CatatanCreateView(SidebarContextMixin, CreateView):
    model = Catatan
    form_class = CatatanTemplateForm
    template_name = "pages/catatan/catatan_form.html"
    success_url = reverse_lazy("catatan_list")

    parent = "data_master"
    segment = 'catatan'


class CatatanUpdateView(SidebarContextMixin, UpdateView):
    model = Catatan
    form_class = CatatanTemplateForm
    template_name = "pages/catatan/catatan_form.html"
    success_url = reverse_lazy("catatan_list")

    parent = "data_master"
    segment = 'catatan'


class CatatanDeleteView(SidebarContextMixin, DeleteView):
    model = Catatan
    template_name = "pages/catatan/catatan_confirm_delete.html"
    success_url = reverse_lazy("catatan_list")

    parent = "data_master"
    segment = 'catatan'