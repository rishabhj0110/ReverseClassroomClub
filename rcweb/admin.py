from django.contrib import admin
from .models import SignUp,UserProfile,Newsletter,Contact,Instructor,Workshop,Courses,Ngo,Emailsystem
# Register your models here.
admin.site.register(SignUp)
admin.site.register(UserProfile)
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Instructor)
admin.site.register(Workshop)
admin.site.register(Courses)
admin.site.register(Ngo)
admin.site.register(Emailsystem)