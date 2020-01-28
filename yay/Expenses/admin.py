from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

@admin.register(Farhan, Nadia, FarhanFamilySuperFund, Ongie, OrangeTrust)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
