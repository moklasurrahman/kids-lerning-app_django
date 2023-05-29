from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(BanglaLesson)
admin.site.register(Requested_course)
admin.site.register(Contact)