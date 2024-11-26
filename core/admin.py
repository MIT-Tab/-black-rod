from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from import_export.admin import ImportExportModelAdmin

from core.models import *
from core.resources import *

# Register your models here.


class SchoolAdmin(ImportExportModelAdmin):
    resource_class = SchoolResource


class DebaterAdmin(ImportExportModelAdmin):
    resource_class = DebaterResource


class TournamentAdmin(ImportExportModelAdmin):
    resource_class = TournamentResource


class TeamAdmin(ImportExportModelAdmin):
    resource_class = TeamResource


class TeamResultAdmin(ImportExportModelAdmin):
    resource_class = TeamResultResource


class SpeakerResultAdmin(ImportExportModelAdmin):
    resource_class = SpeakerResultResource


class NOTYAdmin(ImportExportModelAdmin):
    resource_class = NOTYResource


class SOTYAdmin(ImportExportModelAdmin):
    resource_class = SpeakerResultResource

    # Display debater's name and other fields in the admin
    list_display = ('debater_name', 'season', 'place', 'marker_one', 'marker_two')
    list_filter = ('debater__first_name', 'debater__last_name', 'season')
    search_fields = ('debater__first_name', 'debater__last_name')
    ordering = ('debater__first_name', 'debater__last_name') 

    def debater_name(self, obj):
        return f"{obj.debater.first_name} {obj.debater.last_name}"
    
    debater_name.admin_order_field = 'debater__first_name'
    debater_name.short_description = 'Debater Name' 


class TOTYAdmin(ImportExportModelAdmin):
    resource_class = TOTYResource


class COTYAdmin(ImportExportModelAdmin):
    resource_class = COTYResource

    
class QualPointsAdmin(ImportExportModelAdmin):
    resource_class = QualPointsResource


class QUALAdmin(ImportExportModelAdmin):
    resource_class = QUALResource


admin.site.register(User, UserAdmin)

admin.site.register(Round)
admin.site.register(RoundStats)

admin.site.register(SchoolLookup)

admin.site.register(School, SchoolAdmin)
admin.site.register(Debater, DebaterAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamResult, TeamResultAdmin)
admin.site.register(SpeakerResult, SpeakerResultAdmin)

admin.site.register(SOTY, SOTYAdmin)
admin.site.register(NOTY, NOTYAdmin)
admin.site.register(TOTY, TOTYAdmin)
admin.site.register(COTY, COTYAdmin)
admin.site.register(QualPoints, QualPointsAdmin)
admin.site.register(QUAL, QUALAdmin)
