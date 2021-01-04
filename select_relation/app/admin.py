from django.contrib import admin
from .models import Student,Department,House,Contest,HeadOfDept
# Register your models here.

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(House)
admin.site.register(Contest)
admin.site.register(HeadOfDept)