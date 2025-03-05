from django.contrib import admin
from .models import Users
from .models import Categories
from .models import Skills
from .models import Review

# Register your models here.
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Skills)
admin.site.register(Review)