from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
class TutorialAdmin(admin.ModelAdmin):
    #fields = ["tutorial_content","tutorial_published","tutorial_title"]

    fieldsets = [
        ("Title/Date",{"fields":["tutorial_published"]}),
        ("Content",{"fields":["tutorial_title","tutorial_content"]})
    ]


    #below is awesome
    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}

    }
admin.site.register(Tutorial, TutorialAdmin)
# Register your models here.
