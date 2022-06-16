from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Lost)
admin.site.register(Found)
admin.site.register(Post)
admin.site.register(Comment)