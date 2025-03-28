# Generated by Django 4.2.18 on 2025-02-01 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0001_initial"),
        ("student_panel", "0003_studentanswer_score"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="studentanswer",
            unique_together={("student", "question")},
        ),
        migrations.CreateModel(
            name="StudentExam",
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
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("is_completed", models.BooleanField(default=False)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin_panel.exam",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student_panel.student",
                    ),
                ),
            ],
        ),
    ]
