from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage

from weasyprint import HTML, CSS
from datetime import datetime

from .models import Question
from .forms import QuestionForm, SearchForm


def index(request):
    return render(request, 'index.html', {'user': request.user})


@login_required
def profile(request):
    user = request.user
    questions_list = Question.objects.filter(target=user).order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(questions_list, 10)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'profile.html', {'questions': questions})


def user_profile(request, pk):
    user = User.objects.filter(username=pk)
    form, target = None, None

    if user:
        target = user[0]

        if request.user and target.username == request.user.username:
            return redirect('profile')

        # Creating a question
        if request.method == 'POST':
            form = QuestionForm(request.POST)

            if form.is_valid():
                question = form.save(commit=False)

                if not question.is_anonymous and request.user.is_authenticated:
                    question.author = request.user
                    question.target = target
                    form.save()
                elif not question.is_anonymous and not request.user.is_authenticated:
                    form.add_error('is_anonymous', 'You are not logged in')
                else:
                    question.target = target
                    form.save()
        else:
            form = QuestionForm()

    return render(request, 'user_profile.html', {'target': target, 'form': form})


def find_user(request):
    data = {}

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            users = User.objects.filter(username__contains=username)

            data['html'] = render_to_string('includes/users.html', {'users': users}, request=request)
            return JsonResponse(data)
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


@login_required
def delete_question(request, pk=None):
    data = {}

    if request.method == 'POST':
        question = Question.objects.get(pk=pk)
        question.delete()
        questions = Question.objects.filter(target=request.user)
        data['html'] = render_to_string('includes/questions.html', {'questions': questions}, request=request)

    return JsonResponse(data)


# TODO: Pagination
@login_required
def download_pdf(request):
    user = request.user
    questions = Question.objects.filter(target=user).order_by('-created_at')

    html_string = render_to_string('pdf/pdf_template.html', {'questions': questions}, request=request)

    html = HTML(string=html_string)
    bootstrap_css = CSS(filename='static/css/libs/bootstrap.min.css')
    fonts_css = CSS(filename='static/css/pdf.css')

    file_name = f'{user.username}-{datetime.now().strftime("%m-%d-%Y-%H-%M-%S")}'
    html.write_pdf(target=f'/tmp/{file_name}', stylesheets=[bootstrap_css, fonts_css])

    fs = FileSystemStorage('/tmp')
    with fs.open(file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response

    return redirect('profile')
