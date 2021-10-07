from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
import tempfile
import os

# Create your views here.

def index(request):
    return render(request, 'home.html', {})

def view_pdf_resume(request):
    return render(request, 'simple_resume.html', {})

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