from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Layanan
from .forms import LayananForm


class LayananListView(ListView):
    model = Layanan
    template_name = "pages/layanan/layanan_list.html"
    context_object_name = "layanans"


class LayananDetailView(DetailView):
    model = Layanan
    template_name = "pages/layanan/layanan_detail.html"
    context_object_name = "layanan"


class LayananCreateView(CreateView):
    model = Layanan
    form_class = LayananForm
    template_name = "pages/layanan/layanan_form.html"
    success_url = reverse_lazy("layanan_list")


class LayananUpdateView(UpdateView):
    model = Layanan
    form_class = LayananForm
    template_name = "pages/layanan/layanan_form.html"
    success_url = reverse_lazy("layanan_list")


class LayananDeleteView(DeleteView):
    model = Layanan
    template_name = "pages/layanan/layanan_confirm_delete.html"
    success_url = reverse_lazy("layanan_list")