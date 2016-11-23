from django.views.generic import TemplateView


class MediaServerMap(TemplateView):
    template_name = "map.html"
