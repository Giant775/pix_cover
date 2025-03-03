from django.contrib import admin
from .models import Users
from .models import Categories
from .models import Skills


# Register your models here.
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Skills)