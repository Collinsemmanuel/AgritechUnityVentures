# Register your models here.
# core/admin.py

from django.contrib import admin
from .models import User, Project, Loan, BlogPost

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Loan)
admin.site.register(BlogPost)
