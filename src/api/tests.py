from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from page.models import Page


class PageTests(APITestCase):
    fixtures = ['fixtures.json']

    def test_page_list(self):
        url = reverse('page-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Page.objects.count())

    def test_page_detail(self):
        url = reverse('page-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], Page.objects.get(id=1).title)
