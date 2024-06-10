# Generated by Django 4.2.13 on 2024-06-10 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("title", models.CharField(max_length=32, verbose_name="部门标题")),
            ],
        ),
        migrations.CreateModel(
            name="PrettyNum",
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
                ("mobile", models.CharField(max_length=11, verbose_name="手机号")),
                ("price", models.IntegerField(default=0, verbose_name="价格")),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "1级"), (2, "2级"), (3, "3级"), (4, "4级")], default=1
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "占用"), (2, "未占用")], default=2, verbose_name="状态"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                ("name", models.CharField(max_length=16)),
                ("password", models.CharField(max_length=64)),
                ("age", models.IntegerField()),
                (
                    "account",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="账户余额"
                    ),
                ),
                ("create_time", models.DateField(verbose_name="入职时间")),
                (
                    "gender",
                    models.SmallIntegerField(choices=[(1, "male"), (2, "female")]),
                ),
                (
                    "depart",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app01.department",
                    ),
                ),
            ],
        ),
    ]
