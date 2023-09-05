from django.contrib import admin
from projectlist_app.models import Project,Category,Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)