# Generated by Django 4.1.4 on 2023-02-06 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "org_name",
                    models.CharField(max_length=15, verbose_name="단체 및 시설 이름"),
                ),
                ("addr", models.CharField(max_length=100, verbose_name="주소")),
                ("director", models.CharField(max_length=15, verbose_name="담당자")),
                ("phone_num", models.CharField(max_length=15, verbose_name="담당자 연락처")),
            ],
        ),
        migrations.CreateModel(
            name="Volunteer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=15, verbose_name="제목")),
                ("content", models.TextField(default="", null=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록일"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="이미지"
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("url", models.URLField(blank=True, null=True, verbose_name="홈페이지")),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="volunteer.organization",
                        verbose_name="봉사단체",
                    ),
                ),
                (
                    "sign_vol",
                    models.ManyToManyField(
                        related_name="sign_up",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="신청",
                    ),
                ),
            ],
        ),
    ]