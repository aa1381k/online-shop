from django.contrib import admin
from . import models
# Register your models here.

class adminmodel(admin.ModelAdmin):
    list_display = ['title','parrent','is_active']
    list_editable = ['parrent','is_active']

class adminarticlemodel(admin.ModelAdmin):
    list_display = ['title','is_active','author']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(models.articlecategorymodel, adminmodel)
admin.site.register(models.articlemodel, adminarticlemodel)
admin.site.register(models.articlecomments)
