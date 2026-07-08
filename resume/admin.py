from django.contrib import admin

from .models import (
    ResumeObject,
    Person,
    PersonalDetails,
    PersonalDetailsField,
    EducationalDetails,
    EducationalDetailsField,
    EmploymentDetails,
    EmploymentDetailsField,
    ProjectDetails,
    ProjectDetailsField,
    SkillDetails,
    SkillDetailsField,
)


class PersonalDetailsFieldInline(admin.TabularInline):
    model = PersonalDetailsField
    extra = 1


class EducationalDetailsFieldInline(admin.TabularInline):
    model = EducationalDetailsField
    extra = 1


class EmploymentDetailsFieldInline(admin.TabularInline):
    model = EmploymentDetailsField
    extra = 1


class ProjectDetailsFieldInline(admin.TabularInline):
    model = ProjectDetailsField
    extra = 1


class SkillDetailsFieldInline(admin.TabularInline):
    model = SkillDetailsField
    extra = 1


@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    inlines = [PersonalDetailsFieldInline]


@admin.register(EducationalDetails)
class EducationalDetailsAdmin(admin.ModelAdmin):
    inlines = [EducationalDetailsFieldInline]


@admin.register(EmploymentDetails)
class EmploymentDetailsAdmin(admin.ModelAdmin):
    inlines = [EmploymentDetailsFieldInline]


@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailsFieldInline]


@admin.register(SkillDetails)
class SkillDetailsAdmin(admin.ModelAdmin):
    inlines = [SkillDetailsFieldInline]


@admin.register(ResumeObject)
class ResumeObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'resume_template')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'designation', 'resume')
