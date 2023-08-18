from django.contrib import admin

# Register your models here.
from .models import Story, Comments, Ask, askComments, Job

admin.site.register(Story)
admin.site.register(Comments)
admin.site.register(Ask)
admin.site.register(askComments)
admin.site.register(Job)

