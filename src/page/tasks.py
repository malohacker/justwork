from django.db.models import F

from core.celery import app
from page.models import Page


@app.task
def increment_content(page_id):
    Page.objects.get(id=page_id).contents.all().update(counter=F('counter') + 1)
