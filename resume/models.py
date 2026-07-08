from django.db import models
from django.contrib.auth.models import User

# Unique Resume For every user
class ResumeObject(models.Model):
    username = models.CharField(max_length=30)
    resume_template = models.CharField(max_length=30)

# Person
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation  = models.CharField(max_length=100)
    profile_headline = models.TextField()
    resume = models.ForeignKey(ResumeObject, on_delete=models.CASCADE)

# Main Sections
class PersonalDetails(models.Model):
    resume = models.ForeignKey(ResumeObject, on_delete=models.CASCADE)

class EducationalDetails(models.Model):
    resume = models.ForeignKey(ResumeObject, on_delete=models.CASCADE)

class EmploymentDetails(models.Model):
    resume = models.ForeignKey(ResumeObject, on_delete=models.CASCADE)

class ProjectDetails(models.Model):
    resume = models.ForeignKey(ResumeObject, on_delete=models.CASCADE)

class SkillDetails(models.Model):
    resume = models.ForeignKey(ResumeObject, on_delete=models.CASCADE)


# Repeating Fields 
class PersonalDetailsField(models.Model):
    info_label = models.CharField(max_length=30)
    value = models.CharField(max_length=255)
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)

class EducationalDetailsField(models.Model):
    course_name = models.CharField(max_length=100)
    pass_year = models.CharField(max_length=30)
    institute_name = models.CharField(max_length=150)
    marks = models.CharField(max_length=30)
    educational_details = models.ForeignKey(EducationalDetails, on_delete=models.CASCADE)

class EmploymentDetailsField(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    from_date = models.CharField(max_length=30)
    to_date = models.CharField(max_length=30)
    employment_details = models.ForeignKey(EmploymentDetails, on_delete=models.CASCADE)

class ProjectDetailsField(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_details = models.ForeignKey(ProjectDetails, on_delete=models.CASCADE)

class SkillDetailsField(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_details = models.ForeignKey(SkillDetails, on_delete=models.CASCADE)
