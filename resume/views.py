from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
import tempfile
import os

from .models import (
    ResumeObject,
    Person,
    PersonalDetailsField,
    EducationalDetailsField,
    EmploymentDetailsField,
    ProjectDetailsField,
    SkillDetailsField,
)

# Create your views here.

def index(request):
    return render(request, 'home.html', {})

def signin_page(request):
    return render(request, 'signin.html', {})

def signup_page(request):
    return render(request, 'signup.html', {})


def login(request):
    return HttpResponse('Hello')

def register(request):
    return HttpResponse('Hello')


def get_resume_context(username=None):
    if username:
        resume = get_object_or_404(ResumeObject, username=username)
    else:
        resume = ResumeObject.objects.first()
        if resume is None:
            return None
    person = get_object_or_404(Person, resume=resume)
    return {
        'person': person,
        'personal_fields': PersonalDetailsField.objects.filter(personal_details__resume=resume),
        'educational_fields': EducationalDetailsField.objects.filter(educational_details__resume=resume),
        'employment_fields': EmploymentDetailsField.objects.filter(employment_details__resume=resume).order_by('id'),
        'skill_fields': SkillDetailsField.objects.filter(skill_details__resume=resume),
        'project_fields': ProjectDetailsField.objects.filter(project_details__resume=resume),
    }


def view_pdf_resume(request, username=None):
    context = get_resume_context(username)
    if context is None:
        return HttpResponseNotFound('No resume found')
    return render(request, 'simple_resume.html', context)

def print_pdf_resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'resumePage.html')
    if os.path.exists(file_path):
        html_string = render_to_string(file_path)
        # html = HTML(string=html_string)
        # result = html.write_pdf()

        # Creating http response
        # response = HttpResponse(content_type='application/pdf;')
        # response['Content-Disposition'] = 'inline; filename=list_people.pdf'
        # response['Content-Transfer-Encoding'] = 'binary'
        # with tempfile.NamedTemporaryFile(delete=True) as output:
        #     output.write(result)
        #     output.flush()
        #     output = open(output.name, 'r')
        #     response.write(output.read())

        response = HttpResponse('Hello, File Found')
    else:
        response = HttpResponseNotFound('File Not Found')

    return response

