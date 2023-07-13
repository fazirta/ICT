from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . import models

@admin.register(models.PendaftaranValorant)
@admin.register(models.PendaftaranShortMovie)
class PendaftaranAdmin(ImportExportModelAdmin):
    pass
