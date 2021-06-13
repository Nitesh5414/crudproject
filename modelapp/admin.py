from django.contrib import admin

from modelapp.models import Student

# Register your models here.


########### class for representation data in table form         #################
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'marks', 'roll_num']

################### end class ##############################


admin.site.register(Student, StudentAdmin)                   # class register here
