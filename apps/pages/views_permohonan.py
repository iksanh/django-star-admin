from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Permohonan
from .forms import PermohonanForm


class PermohonanListView(ListView):
    model = Permohonan
    template_name = "pages/permohonan/permohonan_list.html"
    context_object_name = "permohonan_list"
    ordering = ['-tanggal_permohonan']


    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(object_list=object_list, **kwargs)
        context['segment'] = 'permohonan'

        return context


class PermohonanDetailView(DetailView):
    model = Permohonan
    template_name = "pages/permohonan/permohonan_detail.html"
    context_object_name = "permohonan"


class PermohonanCreateView(CreateView):
    model = Permohonan
    form_class = PermohonanForm
    template_name = "pages/permohonan/permohonan_form.html"
    success_url = reverse_lazy("permohonan")


class PermohonanUpdateView(UpdateView):
    model = Permohonan
    form_class = PermohonanForm
    template_name = "pages/permohonan/permohonan_form.html"
    success_url = reverse_lazy("permohonan")


class PermohonanDeleteView(DeleteView):
    model = Permohonan
    template_name = "pages/permohonan/permohonan_confirm_delete.html"
    success_url = reverse_lazy("permohonan")