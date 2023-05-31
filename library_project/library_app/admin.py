from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(book)
admin.site.register(issue_book)
admin.site.register(i_b_data)