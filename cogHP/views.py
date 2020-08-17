from django.shortcuts import render, get_object_or_404

from .models import *

#トップページ
def top(request):
    return render(request, "cogHP/top.html")

# 研究実績
def achivements(request):
    # 年度、査読の有無毎にリストを取得
    reviewed_2020 = Achivement.objects.order_by('-year','review').filter(year=2020, review = True)#この行をコピペして年数を変更
    reviewed_2019 = Achivement.objects.order_by('-year','review').filter(year=2019, review = True)
    reviewed_2018 = Achivement.objects.order_by('-year','review').filter(year=2018, review = True)
    reviewed_2017 = Achivement.objects.order_by('-year','review').filter(year=2017, review = True)
    reviewed_2016 = Achivement.objects.order_by('-year','review').filter(year=2016, review = True)
    reviewed_2015 = Achivement.objects.order_by('-year','review').filter(year=2015, review = True)
    notreviewed_2020 = Achivement.objects.order_by('-year','review').filter(year=2020, review = False)#この行をコピペして年数を変更
    notreviewed_2019 = Achivement.objects.order_by('-year','review').filter(year=2019, review = False)
    notreviewed_2018 = Achivement.objects.order_by('-year','review').filter(year=2018, review = False)
    notreviewed_2017 = Achivement.objects.order_by('-year','review').filter(year=2017, review = False)
    notreviewed_2016 = Achivement.objects.order_by('-year','review').filter(year=2016, review = False)
    notreviewed_2015 = Achivement.objects.order_by('-year','review').filter(year=2015, review = False)
    context = {
        "2020_reviewed": reviewed_2020,#この行をコピペして年数を変更
        "2019_reviewed": reviewed_2019,
        "2018_reviewed": reviewed_2018,
        "2017_reviewed": reviewed_2017,
        "2016_reviewed": reviewed_2016,
        "2015_reviewed": reviewed_2015,
        "2020_notreviewed": notreviewed_2020,#この行をコピペして年数を変更
        "2019_notreviewed": notreviewed_2019,
        "2018_notreviewed": notreviewed_2018,
        "2017_notreviewed": notreviewed_2017,
        "2016_notreviewed": notreviewed_2016,
        "2015_notreviewed": notreviewed_2015,
    }
    return render(request, "cogHP/achivement.html", context)

# 実験参加者募集一覧
def recruiting_index(request):
    recruitiong_list = Recruiting.objects.all()
    context = {
        "recruiting_list": recruitiong_list,
    }
    return render(request, "cogHP/recruiting_index.html", context)

# 実験参加者募集詳細
def recruiting_detail(request, recruiting_id):
    recruiting = get_object_or_404(Recruiting, pk=recruiting_id)
    return render(request, "cogHP/recruiting_detail.html", {"recruiting": recruiting})
