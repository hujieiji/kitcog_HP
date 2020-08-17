from django.db import models

class Recruiting(models.Model):
    title = models.CharField("募集タイトル",max_length=200)
    apply_link = models.URLField("募集URL", blank=True)
    period_start = models.DateField("実験開始日時")
    period_end = models.DateField("実験終了日時")
    duration_hour = models.DurationField("実験時間")
    place = models.CharField("実験場所",max_length=200)
    experimenter = models.CharField("実験者",max_length=200, blank=True)
    exp_grade = models.CharField("実験者の学年", max_length=50, blank=True)
    reward = models.CharField("報酬",max_length=200, blank=True)
    conditions = models.CharField("条件",default = "特になし",max_length=200)
    precautions = models.TextField("注意事項",default = "※事前アンケートあり（アンケートの結果，実験参加者として採用されない場合がございます．ご了承ください．）")
    def __str__(self):
        return self.title

class Achivement(models.Model):
    author = models.CharField("著者",max_length=500)
    year = models.CharField("発表年度",max_length=50)
    title = models.CharField("タイトル",max_length=1000)
    journal = models.CharField("ジャーナル名",max_length=200)
    issue = models.CharField("ジャーナル掲載号",max_length=200,blank=True)
    pages = models.CharField("ジャーナル掲載ページ",max_length=50, default="pp.", blank=True)
    review = models.BooleanField("査読の有無")
    def __str__(self):
        return self.title