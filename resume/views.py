from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
import tempfile
import os
from resume.managers.authmanager import UserAuthManager
from django.contrib.auth import login



# ============================== Web pages =============================
def index(request):
	return render(request, 'home.html', {})

def signin_page(request):
	user_auth = UserAuthManager(request.user)
	if user_auth.is_authenticated():
		return redirect('view_pdf_resume')
	else:
		return render(request, 'signin.html', {})

def signup_page(request):
	user_auth = UserAuthManager(request.user)
	if user_auth.is_authenticated():
		return redirect('view_pdf_resume')
	else:
		return render(request, 'signup.html', {})

def error_page(request):
	return render(request, 'error_page.html', {})


# ============================ API's ====================================
def login_user(request):
	email = request.POST.get('email')
	password = request.POST.get('password')

	user_auth_manager = UserAuthManager()
	user_logged_in = user_auth_manager.login_user(email, password)

	if user_logged_in:
		login(request, user_logged_in)
		return redirect('view_pdf_resume')
	else:
		return redirect('error_page')

def register_user(request):    
	first_name = request.POST.get('firstName')
	last_name = request.POST.get('lastName')
	email = request.POST.get('email')
	password = request.POST.get('password')

	user_auth_manager = UserAuthManager()
	user_created = user_auth_manager.register_user(first_name, last_name, email, password)

	if user_created:
		return redirect('view_pdf_resume')
	else:
		return redirect('error_page')


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

