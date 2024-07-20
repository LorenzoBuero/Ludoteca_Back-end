from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado', 'id')
    
    


admin.site.register(Project)

