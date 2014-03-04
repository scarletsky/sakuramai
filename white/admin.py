from django.contrib import admin
from white.models import *


class Signup2014Admin(admin.ModelAdmin):
    list_filter = ('year',)
    list_display = (
        'author',
        'contact',
        'remark',
        'pair_num',
        'pair_num_fixed',
        'team_num',
        'is_team',
        'year')
    search_fields = (
        'author',
        'contact',
        'remark',
        'pair_num',
        'pair_num_fixed',
        'team_num',
        'is_team',
        'year')


class MadAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    list_display = (
        'title',
        'author',
        'source',
        'music',
        'team_num',
        'is_ntr',
        'year')
    search_fields = (
        'title',
        'author',
        'source',
        'music',
        'team_num',
        'music',
        'is_ntr',
        'year')


class ScheduleAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    list_display = (
        'day',
        'day_id',
        'description',
        'team1',
        'team2',
        'vote_limit_day',
        'is_display',
        'year')
    search_fields = (
        'day',
        'description',
        'team1',
        'team2',
        'vote_limit_day',
        'is_display',
        'year')

admin.site.register(Signup2014, Signup2014Admin)
admin.site.register(Mad, MadAdmin)
admin.site.register(Schedule, ScheduleAdmin)
