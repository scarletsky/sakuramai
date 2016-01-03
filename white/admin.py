from django.contrib import admin
from white.models import *


class SignupAdmin(admin.ModelAdmin):
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


class VoteDetailAdmin(admin.ModelAdmin):
    list_display = (
        'ip_addr',
        'team_num',
        'year',
        'vote_time')


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'team_num',
        'votes',
        'year')

admin.site.register(Signup, SignupAdmin)
admin.site.register(Mad, MadAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(VoteDetail, VoteDetailAdmin)
admin.site.register(Team, TeamAdmin)
