from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Permohonan
from .forms import PermohonanForm
from .mixins import SidebarContextMixin


class PermohonanListView(SidebarContextMixin, ListView):
    model = Permohonan
    template_name = "pages/permohonan/permohonan_list.html"
    context_object_name = "permohonan_list"
    ordering = ['-tanggal_permohonan']
    parent = "permohonan"
    segment = 'permohonan'





class PermohonanDetailView(DetailView):
    model = Permohonan
    template_name = "pages/permohonan/permohonan_detail.html"
    context_object_name = "permohonan"

    


class PermohonanCreateView(SidebarContextMixin, CreateView):
    model = Permohonan
    form_class = PermohonanForm
    template_name = "pages/permohonan/permohonan_form.html"
    success_url = reverse_lazy("permohonan")
    parent = "permohonan"
    segment = 'permohonan'

class PermohonanUpdateView(SidebarContextMixin, UpdateView):
    model = Permohonan
    form_class = PermohonanForm
    template_name = "pages/permohonan/permohonan_form.html"
    success_url = reverse_lazy("permohonan")

    parent = "permohonan"
    segment = 'permohonan'



class PermohonanDeleteView(DeleteView):
    model = Permohonan
    template_name = "pages/permohonan/permohonan_confirm_delete.html"
    success_url = reverse_lazy("permohonan")

    parent = "permohonan"
    segment = 'permohonan'

class PermohonanHistoryView(DetailView):
    model = Permohonan
    template_name = "pages/permohonan/history.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['history'] = self.object.history.all()
        return ctx
