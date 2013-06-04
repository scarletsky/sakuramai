#-*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from skm.models import *

def Index(request):
	return render_to_response('skm/index.html')

def Introduce(request):
	return render_to_response('skm/introduce.html')

@csrf_exempt
def WhiteDaySignup(request):
	if request.is_ajax():
		is_team = int(request.POST.get('is_team'))
		if is_team == 0:
			author0 = request.POST.get('author0').strip()
			contact0 = request.POST.get('contact0').strip()
			remark0 = request.POST.get('remark0').strip()
			pair_num = request.POST.get('pair_num')

			if (author0 and contact0 and remark0):
				test_exist0 = Signup.objects.filter(author=author0)
				if not test_exist0:
					try:
						test_pair_num = int(pair_num)
						if test_pair_num/10 != 0:
							ret = 4
							return HttpResponse(4)
						sign_member0 = Signup(author=author0, contact=contact0, 
							remark=remark0, pair_num=pair_num, is_team=is_team)
						sign_member0.save()
						ret = 1
						return HttpResponse(ret)
					except:
						ret = 4
						return HttpResponse(ret)
				else:
					ret = 2
					return HttpResponse(ret)
			else:
				ret = 3
				return HttpResponse(ret)

		if is_team == 1:
			author1 = request.POST.get('author1').strip()
			contact1 = request.POST.get('contact1').strip()
			remark1 = request.POST.get('remark1').strip()

			author2 = request.POST.get('author2').strip()
			contact2 = request.POST.get('contact2').strip()
			remark2 = request.POST.get('remark2').strip()

			team_list = Signup.objects.filter(is_team=1).order_by('-team_num')
			team_num = team_list[0].team_num + 1

			if (author1 and contact1 and remark1 and author2 and contact2 and remark2):
				test_exist1 = Signup.objects.filter(author=author1)
				test_exist2 = Signup.objects.filter(author=author2)
				if not (test_exist1 or test_exist2):
					try:
						sign_member1 = Signup(author=author1, contact=contact1, 
							remark=remark1, team_num=team_num, is_team=is_team)
						sign_member2 = Signup(author=author2, contact=contact2, 
							remark=remark2, team_num=team_num, is_team=is_team)
						sign_member1.save()
						sign_member2.save()
						ret = 1
						return HttpResponse(ret)
					except:
						ret = 0
						return HttpResponse(ret)
				else:
					ret = 2
					return HttpResponse(ret)
			else:
				ret = 3
				return HttpResponse(ret)

	sign_member_list = Signup.objects.all()
	count = len(sign_member_list)
	ctx = {'count':count}
	return render_to_response('skm/signup.html', ctx, context_instance=RequestContext(request))



def Participants(request):
	final_team_list = []
	final_single_list = []
	all_members = Signup.objects.all()

	""" Team """
	team_list = all_members.filter(is_team=1).order_by('team_num')
	unique_team_num = team_list.values('team_num').distinct()
	for i in unique_team_num:
		each_team = team_list.filter(team_num=i['team_num'])
		final_team_list.append(each_team)

	""" Single """
	single_list = all_members.filter(is_team=0).order_by('pair_num')
	unique_pair_num = single_list.values('pair_num').distinct()
	for j in unique_pair_num:
		each_pair = single_list.filter(pair_num=j['pair_num'])
		if len(each_pair) == 1:
			tmp = []
			tmp.append(each_pair[0])
			tmp.append(each_pair[0])
			each_pair = tmp
		final_single_list.append(each_pair)

	ctx = {'final_team_list':final_team_list, 'final_single_list':final_single_list}
	return render_to_response('skm/participants.html', ctx)


def Mads(request):
	try:
		x_ip = request.META['HTTP_X_FORWARDED_FOR']
	except KeyError:
		ip = request.META['REMOTE_ADDR']
	else:
		ip = x_ip.split(",")[0]
	
	mads = Mad.objects.all()
	ctx = {'mads':mads, 'ip':ip}
	return render_to_response('skm/mads.html', ctx)

def SkmStaff(request):
	staff = Staff.objects.all()
	ctx = {'staff':staff}
	return render_to_response('skm/staff.html', ctx)



@csrf_exempt
def Schedule(request):
	if request.method == "GET":
		final_index = []
		mads = Mad.objects.all().exclude(day=99).filter(is_display=1)	
		sps = Mad.objects.filter(day=99).filter(is_display=1)
		###########sp day############
		try:
			sps_day = sps.values('team_num').distinct().order_by('team_num')
			sort_sps_day = sorted([t['team_num'] for t in sps_day])
			sp_list = [sps.filter(team_num=i) for i in sort_sps_day]
		except:
			pass
		###########sp day############

		### mads -> filter_day -> filter_team_num -> append in list(array)
		days = mads.values('day').distinct()
		day_list = sorted([d['day'] for d in days])
		for d in day_list:
			per_day_mad = mads.filter(day=d)
			filter_team_num = per_day_mad.values('team_num').distinct()
			team_unique = [t['team_num'] for t in filter_team_num]
			team = [per_day_mad.filter(team_num=i) for i in team_unique]
			final_index.append(team)
			###########################
			#4 mads per day
			#team2 = per_day_mad.filter(team_num=team[1])
			#final_index.append([team1, team2])
		#Dessert
		if sps:
			try:
				final_index.insert(8, [sp_list[0]])
				final_index.insert(15, [sp_list[1]])
			except:
				pass

	if request.method == "POST":
		try:
			x_ip = request.META['HTTP_X_FORWARDED_FOR']
		except KeyError:
			ip = request.META['REMOTE_ADDR']
		else:
			ip = x_ip.split(",")[0]
		team_num = request.POST.get("team_num")
		day = request.POST.get("day")


		#####Votes -> filter unique ip votes -> filter ip day votes -> judge is the same day

		####--------filter unique ip day votes--------####
		all_votes = Vote.objects.all()
		ipvotes = all_votes.filter(ipaddr=ip)
		ipvotes_this_day = ipvotes.filter(day=day)
		####---------------end------------------------####


		#####------------here are new votes-----------####
		mads_this_day = Mad.objects.filter(day=day, team_num=team_num)
		mad_vote1 = mads_this_day[0]
		mad_vote2 = mads_this_day[1]
		####-----------------end----------------------####


		if ipvotes_this_day:
			return HttpResponse(1)
		else:
			new_vote = Vote(ipaddr=ip, day=day, team_num=team_num)
			new_vote.save()
			return HttpResponse(0)
	final_index = final_index[::-1]
	ctx = {'final_index':final_index}
	return render_to_response('skm/schedule.html', ctx)


def Display(request, day):
	if day == "sp1":
		mads = Mad.objects.filter(day=99).order_by('team_num').filter(is_display=1)[0:2]
	elif day == "sp2":
		mads = Mad.objects.filter(day=99).order_by('team_num').filter(is_display=1)[2:4]
	else:
		mads = Mad.objects.filter(day=day).order_by('team_num').filter(is_display=1)
	urls = Day.objects.all().order_by('id')
	ctx = {'mads':mads, 'urls':urls}
	return render_to_response('skm/display.html', ctx)

def Result(request):
	mads = Mad.objects.all().exclude(day=99).order_by('-votes')[:6]
	ctx={ 'mads':mads}
	return render_to_response('skm/result.html', ctx)


def Category(request):
	return render_to_response('skm/onlytest.html')





######################C  r  o  n######################
def CountDay(request):
	mads = Mad.objects.all()
	need_to_cron = mads.filter(is_display=1).filter(limit_days__gt=0)
	for mad in need_to_cron:
		mad.limit_days -= 1
		mad.save()
	return render_to_response('skm/index.html')



def SyncVotes(request):
	mads = Mad.objects.all()
	votes = Vote.objects.all()
	temp = votes.values('team_num').distinct()
	unique_team_num = [num['team_num'] for num in temp]

	if votes:
		for i in unique_team_num:
			team = mads.filter(team_num=i)
			mad1 = team[0]
			mad2 = team[1]
			team_votes = votes.filter(team_num=i).count()
			mad1.votes = team_votes
			mad2.votes = team_votes
			mad1.save()
			mad2.save()
	else:
		for mad in mads:
			mad.votes = 0
			mad.save()
	return render_to_response('skm/index.html')
