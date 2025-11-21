from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  # kita akan pakai csrf token header dari JS, jadi tidak perlu csrf_exempt


from .models import Pemohon, BerkasItem, Pemeriksaan, CatatanTemplate




# Create your views here.

def index(request):

    # Page from the theme 
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'pages/index.html', context)

def permohonan(request):
    context = {
        'segment': 'permohonan'
    }
    return render(request, 'pages/permohonan.html', context)




@require_POST
def ajax_create_catatan(request):
    """
    Terima AJAX JSON:
    {
      "berkas_id": 12,
      "teks": "Perbaiki batas utara"
    }
    Membuat CatatanTemplate(berkas=..., teks=..., is_global=True)
    Return JSON { "id": 45, "teks": "Perbaiki batas utara" }
    """
    try:
        data = json.loads(request.body.decode('utf-8'))
        berkas_id = int(data.get('berkas_id'))
        teks = data.get('teks', '').strip()
    except Exception:
        return HttpResponseBadRequest("Bad payload")

    if not teks:
        return HttpResponseBadRequest("Teks catatan kosong")

    berkas = get_object_or_404(BerkasItem, id=berkas_id)
    cat = CatatanTemplate.objects.create(berkas=berkas, teks=teks, is_global=True)

    return JsonResponse({"id": cat.id, "teks": cat.teks})


def pemeriksaan_input(request, pemohon_id):
    pemohon = get_object_or_404(Pemohon, id=pemohon_id)
    daftar_berkas = BerkasItem.objects.all()

    # Ambil semua pemeriksaan yang pernah tersimpan untuk pemohon ini
    pemeriksaan_map = {
        p.berkas.id: p
        for p in Pemeriksaan.objects.filter(pemohon=pemohon).prefetch_related("catatan")
    }

    if request.method == "POST":
        # Untuk tiap berkas, buat atau update Pemeriksaan
        for berkas in daftar_berkas:

            selected_raw = request.POST.getlist(f"catatan_{berkas.id}")
            extras = request.POST.getlist(f"catatan_extra_{berkas.id}")
            manual_txt = request.POST.get(f"catatan_baru_{berkas.id}", "").strip()

            pemeriksaan, created = Pemeriksaan.objects.get_or_create(
                pemohon=pemohon,
                berkas=berkas,
                defaults={'catatan_baru': manual_txt or None}
            )

            # update catatan tambahan
            catatan_baru_parts = []
            # if pemeriksaan.catatan_baru:
            #     catatan_baru_parts.append(pemeriksaan.catatan_baru)
            if manual_txt:
                catatan_baru_parts.append(manual_txt)
            for e in extras:
                if e.strip():
                    catatan_baru_parts.append(e.strip())

            pemeriksaan.catatan_baru = "\n".join(catatan_baru_parts) if catatan_baru_parts else None
            pemeriksaan.save()

            # Only integer values for global template ids
            template_ids = []
            for raw in selected_raw:
                try:
                    template_ids.append(int(raw))
                except ValueError:
                    pass

            pemeriksaan.catatan.set(template_ids) if template_ids else pemeriksaan.catatan.clear()

        return redirect("detail_pemohon", pemohon_id=pemohon.id)

    context = {
        "pemohon": pemohon,
        "daftar_berkas": daftar_berkas,
        "pemeriksaan_map": pemeriksaan_map,
    }
    return render(request, "pages/pemeriksaan_input.html", context)


def detail_pemohon(request, pemohon_id):
    pemohon = get_object_or_404(Pemohon, id=pemohon_id)

    # Ambil semua hasil pemeriksaan yang sudah dibuat untuk pemohon ini
    pemeriksaan_list = Pemeriksaan.objects.filter(pemohon=pemohon).select_related("berkas").prefetch_related("catatan")

    context = {
        "pemohon": pemohon,
        "pemeriksaan_list": pemeriksaan_list,
    }
    return render(request, "pages/detail_pemeriksaan.html", context)
