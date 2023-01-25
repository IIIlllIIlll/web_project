from django.db import models
from django.contrib.auth.models import User
# from imagekit.models import ImageSpecField
# from imagekit.processors import Thumbnail
# from imagekit.processors import ResizeToFill
# Create your models here.


class Care(models.Model):
    title = models.CharField(max_length=15)
    place = models.CharField(max_length=15)
    content = models.TextField(null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, verbose_name="이미지")
    updated_at = models.DateTimeField(auto_now=True)
    best = models.ManyToManyField(
        User, related_name="best", verbose_name="추천수")
    view_cnt = models.BigIntegerField(default=0)  # 조회수

    # image_thumbnail = ImageSpecField(source='image',
    #                                  processors=[ResizeToFill(100, 50)],
    #                                  format='JPEG', options={'quality': 60})

    # image_thumbnail = ImageSpecField(
    #     source='image',
    #     processors=[Thumbnail(120, 60)],
    #     format='JPEG',
    #     options={'quality': 100}
    # )

    def __str__(self):
        return self.title


class CareCount(models.Model):
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Care, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.ip


class Answer(models.Model):
    question = models.ForeignKey(Care, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자", related_name="author_answer")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")
    voter = models.ManyToManyField(
        User, related_name="voter_answer", verbose_name="추천수")


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")
    question = models.ForeignKey(
        Care, on_delete=models.CASCADE, null=True, blank=True)  # 답변에 대한 댓글일 경우 이부분은 입력 안됨
    # 질문에 대한 댓글일 경우 이부분은 입력 안됨
    answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, null=True, blank=True)

# "board/files/covers"
