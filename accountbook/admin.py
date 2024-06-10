from django.contrib import admin

from accountbook.models import AccountBook, Category

admin.site.register(Category)
admin.site.register(AccountBook)