from django.contrib import admin

# Register your models here.
from .models import User,Cart
admin.site.register(User)
admin.site.register(Cart)