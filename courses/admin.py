from django.contrib import admin
from .models import CodingQuestion, UserCodingQuestion

admin.site.register(CodingQuestion)
admin.site.register(UserCodingQuestion)
