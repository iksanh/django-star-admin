from django.urls import reverse_lazy
from django.shortcuts import render, redirect    
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import BerkasItem, Layanan
from .forms import BerkasItemForm
from .mixins import SidebarContextMixin
from django.contrib import messages


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

def pengaturan_urutan_berkas(request):
    jenis_hak = request.GET.get("jenis_hak")  # HM / HGB / HGU
    berkas_list = []

    if jenis_hak:
        berkas_list = BerkasItem.objects.filter(
            layanan__kode=jenis_hak
        ).distinct()

    if request.method == "POST":
        jenis_hak = request.POST.get("jenis_hak")

        for key, value in request.POST.items():
            if key.startswith("berkas_") and value:
                berkas_id = key.replace("berkas_", "")
                berkas = BerkasItem.objects.get(id=berkas_id)

                data = berkas.urutan or {}
                data[jenis_hak] = int(value)
                berkas.urutan = data
                berkas.save()

        messages.success(
            request,
            f"Urutan berkas untuk {jenis_hak} berhasil disimpan"
        )

        return redirect(
            f"{request.path}?jenis_hak={jenis_hak}"
        )

    context = {
        "layanan_list": Layanan.objects.all(),
        "jenis_hak": jenis_hak,
        "berkas_list": berkas_list,
    }
    return render(request, "pages/berkasitem/pengaturan_urutan.html", context)