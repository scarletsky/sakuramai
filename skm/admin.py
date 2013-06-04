from django.contrib import admin
from skm.models import *

class StaffAdmin(admin.ModelAdmin):
	list_display = ('name', 'join_in', 'remark', 'is_active')

class DayAdmin(admin.ModelAdmin):
	list_display = ('display', 'url_index')
		
class SignupAdmin(admin.ModelAdmin):
	list_display = ('author', 'contact', 'remark', 'pair_num', 'team_num', 'is_team', 'pub_time')
	search_fields = ('author', 'pair_num', 'team_num', 'is_team')

class MadAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'music', 'day', 'team_num', 'votes', 'limit_days', 'is_ntr', 'is_display')
	search_fields = ('title', 'author', 'day', 'music')

class VoteAdmin(admin.ModelAdmin):
	list_display = ('ipaddr', 'day', 'team_num', 'pub_time')


admin.site.register(Staff, StaffAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Mad, MadAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(Vote, VoteAdmin)