from django.contrib import admin

from .models import Questions
from .models import Choice

admin.site.register(Questions)
admin.site.register(Choice)
