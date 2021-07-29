from django.db import transaction
from rest_framework import generics
from api.serializers import PageListSerializer, PageDetailSerializer
from page.models import Page
from page.tasks import increment_content


class PageListView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer


class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super(PageDetailView, self).retrieve(request, *args, **kwargs)
        transaction.on_commit(lambda: increment_content.delay(kwargs.get(self.lookup_field)))
        return response
