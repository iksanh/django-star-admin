class SidebarContextMixin:
    parent = None
    segment = None
    page_title = None        # contoh: "Layanan"
    page_mode = None         # list | form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["parent"] = self.parent
        context["segment"] = self.segment

        obj = getattr(self, "object", None)
        is_edit = bool(obj and obj.pk)
        context["is_edit"] = is_edit

        # === TITLE HANDLING ===
        if self.page_title:
            if self.page_mode == "list":
                context["page_title"] = f"Daftar {self.page_title}"

            elif self.page_mode == "form":
                context["page_title"] = (
                    f"Edit {self.page_title}"
                    if is_edit
                    else f"Tambah {self.page_title}"
                )

        return context
