class SidebarContextMixin:
    parent = None
    segment = None 


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.parent:
            context['parent'] = self.parent

        if self.segment:
            context['segment'] = self.segment


        return context