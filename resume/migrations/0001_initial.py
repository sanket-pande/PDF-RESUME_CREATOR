# Generated by Django 3.2.7 on 2021-09-26 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('resume_template', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SkillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeobject')),
            ],
        ),
        migrations.CreateModel(
            name='SkillDetailsField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30)),
                ('skill_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.skilldetails')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetailsField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_description', models.CharField(max_length=100)),
                ('project_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.projectdetails')),
            ],
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeobject'),
        ),
        migrations.CreateModel(
            name='PersonalDetailsField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_label', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
                ('personal_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.personaldetails')),
            ],
        ),
        migrations.AddField(
            model_name='personaldetails',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeobject'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('profile_headline', models.CharField(max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeobject')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentDetailsField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
                ('from_date', models.CharField(max_length=30)),
                ('to_date', models.CharField(max_length=30)),
                ('employment_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.employmentdetails')),
            ],
        ),
        migrations.AddField(
            model_name='employmentdetails',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeobject'),
        ),
        migrations.CreateModel(
            name='EducationalDetailsField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('pass_year', models.CharField(max_length=30)),
                ('institute_name', models.CharField(max_length=30)),
                ('marks', models.CharField(max_length=30)),
                ('educational_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.educationaldetails')),
            ],
        ),
        migrations.AddField(
            model_name='educationaldetails',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resumeobject'),
        ),
    ]
