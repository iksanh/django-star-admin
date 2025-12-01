from django.urls import reverse_lazy    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BerkasItem
from .forms import BerkasItemForm


class BerkasItemListView(ListView):
    model = BerkasItem
    template_name = "pages/berkasitem/berkasitem_list.html"
    context_object_name = "berkasitems"


class BerkasItemDetailView(DetailView):
    model = BerkasItem
    template_name = "pages/berkasitem/berkasitem_detail.html"
    context_object_name = "berkasitem"


class BerkasItemCreateView(CreateView):
    model = BerkasItem
    form_class = BerkasItemForm
    template_name = "pages/berkasitem/berkasitem_form.html"
    success_url = reverse_lazy("berkasitem_list")


class BerkasItemUpdateView(UpdateView):
    model = BerkasItem
    form_class = BerkasItemForm
    template_name = "pages/berkasitem/berkasitem_form.html"
    success_url = reverse_lazy("berkasitem_list")


class BerkasItemDeleteView(DeleteView):
    model = BerkasItem
    template_name = "pages/berkasitem/berkasitem_confirm_delete.html"
    success_url = reverse_lazy("berkasitem_list")