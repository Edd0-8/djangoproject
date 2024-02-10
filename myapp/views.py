from django.shortcuts import render
from django.http import HttpResponse, JsonResponse  
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from .forms import CreateNewTask 

# Create your views here.
def index(request):
    title = 'Django Title!'
    return render(request, 'index.html', {
        'titulo':title
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    username = 'Eddo'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html', {
        'projects': projects
    })

def tasks(request):
    # task = get_object_or_404(Task)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks':tasks
    })

def create_tasks(request):
    return render(request, 'create_tasks.html', {
        'form': CreateNewTask()
    })