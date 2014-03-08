from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from white.models import *
import re


def index(request):
    return render_to_response('2014' + '/index.html')


def year(requrest, year):
    return render_to_response(year + '/index.html')


def info(request, year):
    return render_to_response(year + '/info.html')


def signup(request, year):
    return render_to_response(
        year + '/signup.html',
        context_instance=RequestContext(request)
    )


def result(request, year):
    return render_to_response(year + '/result.html')


def custom_404(request):
    route = request.path_info
    pattern = r'^/(\d{4})/.*$'
    try:
        year = re.match(pattern, route).group(1)
        return render_to_response(year + '/404.html')
    except:
        return HttpResponse('404')


def custom_500(request):
    route = request.path_info
    pattern = r'^/(\d{4})/.*$'
    try:
        year = re.match(pattern, route).group(1)
        return render_to_response(year + '/500.html')
    except:
        return HttpResponse('500')


def participants(request, year):
    members_per_year = Signup2014.objects.filter(year=year)
    teams = members_per_year.exclude(team_num=-1).order_by('team_num').all()
    pairs = members_per_year.exclude(pair_num_fixed=-1).order_by('pair_num_fixed').all()
    team_group = [teams[i:i+2] for i in range(0, len(teams), 2)]
    pair_group = [pairs[i:i+2] for i in range(0, len(pairs), 2)]

    ctx = {
        'team_group': team_group,
        'pair_group': pair_group
    }
    return render_to_response(year + '/participants.html', ctx)


def schedule(request, year):
    schedule = []
    days = Schedule.objects.filter(is_display=True, year=year).order_by('day_id')
    mads = Mad.objects.filter(year=year)
    for day in days:
        obj = {}
        competitors = []
        team1 = mads.filter(team_num=day.team1)
        team2 = mads.filter(team_num=day.team2)

        competitors.append(team1)

        if team2:
            competitors.append(team2)

        obj['day'] = day
        obj['competitors'] = competitors
        schedule.insert(0, obj)

    ctx = {
        'schedule': schedule
    }
    return render_to_response(year + '/schedule.html', ctx)


def display(requiest, year, day):
    schedule = Schedule.objects.filter(year=year)
    day_info = schedule.get(day=day, year=year)
    team1 = day_info.team1
    team2 = day_info.team2

    mads = Mad.objects.filter(year=year).filter(Q(team_num=team1) | Q(team_num=team2)).order_by('team_num')

    ctx = {
        'mads': mads,
        'schedule': schedule
    }
    return render_to_response(year + '/display.html', ctx)


@csrf_exempt
def vote_ajax(request):
    ip_addr = get_ip_addr(request)
    team_num = request.POST.get('team_num')

    if check_vote(ip_addr, team_num):
        return HttpResponse(1)
    else:
        new_vote = VoteDetail(ip_addr=ip_addr, team_num=team_num)
        new_vote.save()
        add_team_vote(team_num)

    return HttpResponse(0)


def get_ip_addr(request):
    try:
        x_ip = request.META['HTTP_X_FORWARDED_FOR']
    except KeyError:
        ip = request.META['REMOTE_ADDR']
    else:
        ip = x_ip.split(",")[0]
    return ip


def check_vote(ip_addr, team_num):
    obj = VoteDetail.objects.filter(ip_addr=ip_addr, team_num=team_num)
    is_voted = True if obj else False

    return is_voted


def add_team_vote(team_num):
    try:
        team = Team.objects.filter(team_num=team_num)[0]
        team.votes += 1
        team.save()
    except:
        team = Team(team_num=team_num, votes='1')
        team.save()

    print 'finish'


@csrf_exempt
def check_author(request):
    if request.is_ajax():
        typeMap = request.POST.get('type')
        if typeMap == 'single':
            obj = Signup2014.objects.filter(author=request.POST.get('author1'))

            isSigned = True if obj else False
            return HttpResponse(isSigned)

        elif typeMap == 'team':
            obj1 = Signup2014.objects.filter(
                author=request.POST.get('author1')
            )
            obj2 = Signup2014.objects.filter(
                author=request.POST.get('author2')
            )

            isSigned = True if obj1 or obj2 else False
            return HttpResponse(isSigned)
        else:
            print 'Unexpect typeMap!'
    else:
        print 'Not Ajax request!'


@csrf_exempt
def signup_ajax(request):
    if request.is_ajax():
        is_team = int(request.POST.get('is_team'))
        if is_team == 0:
            res = check_author(request)

            if res.content == 'True':
                return HttpResponse(-1)
            else:
                author1 = request.POST.get('author1')
                contact1 = request.POST.get('contact1')
                remark1 = request.POST.get('remark1')
                pairNum = request.POST.get('pair-num')

                try:
                    member1 = Signup2014(
                        author=author1,
                        contact=contact1,
                        remark=remark1,
                        pair_num=pairNum,
                        is_team=is_team
                    )
                    member1.save()
                    print member1
                    return HttpResponse(1)
                except Exception, e:
                    print e
                    return HttpResponse(0)
        elif is_team == 1:
            res = check_author(request)

            if res.content == 'True':
                return HttpResponse(-1)
            else:
                author1 = request.POST.get('author1')
                contact1 = request.POST.get('contact1')
                remark1 = request.POST.get('remark1')

                author2 = request.POST.get('author2')
                contact2 = request.POST.get('contact2')
                remark2 = request.POST.get('remark2')

                # Don't use this!
                # if you delete one team,
                # team_num will not be correct.
                # team_num = (len(
                #     Signup2014.objects.filter(is_team=1)) / 2) + 1

                # Use this instead!

                # Because the team_num field is CharField,
                # So it can not use order_by('-team_num')
                # Just use pub_time instead.....
                team_list = Signup2014.objects.filter(is_team=1).order_by('-pub_time')
                team_num = (int(team_list[0].team_num) + 1) if len(team_list) != 0 else 1

                try:
                    member1 = Signup2014(
                        author=author1,
                        contact=contact1,
                        remark=remark1,
                        is_team=is_team,
                        team_num=team_num
                    )
                    member2 = Signup2014(
                        author=author2,
                        contact=contact2,
                        remark=remark2,
                        is_team=is_team,
                        team_num=team_num
                    )
                    member1.save()
                    member2.save()
                    return HttpResponse(1)
                except Exception, e:
                    print e
                    return HttpResponse(0)
        else:
            print 'Unexpect Error!'
            return HttpResponse(0)

    else:
        return HttpResponse(0)
