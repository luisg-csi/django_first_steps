from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import JsonResponse
import calendar
import locale
from .models import Proyect, Task
from .forms import CreateNewTask, CreateNewProyect

# Create your views here.


def index(request):
    title = "Django Course!!!"
    return render(request, 'index.html',
                  {'title': title})


def hello(request, username):
    print(f"variable recibida: username-->{username} de tipo {type(username)}")
    # username= username.upper()
    # return HttpResponse("<h1>hello mister %s</h1>" %username.upper())
    return HttpResponse("<h1>hello mister %s</h1>" % username.capitalize())


def about(request):
    username = "Sublian"
    return render(request, 'about.html',
                  {'username': username})


def other(request):
    """
    url_completa = request.build_absolute_uri()
    print("url  desde other-->", url_completa)
    print(obtener_nombre_mes_y_anio(int(url_completa.split("D")[1][:2])))
    """
    return HttpResponse("<h1>Just other page</h1>")


"""def proyects(request):
    proyectos = list(Proyect.objects.values())
    return JsonResponse(proyectos, safe=False)"""


def proyects(request):
    proyects = list(Proyect.objects.values())
    return render(request, "proyects/proyects.html",
                  {"proyects": proyects})


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html",
                  {"tasks": tasks})


"""def tasks(request,id):
    task= get_object_or_404(Task, id=id)
    return HttpResponse("task: %s"% task.title)"""


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], proyect_id=2)
        return redirect('tasks')


def create_proyect(request):
    if request.method == 'GET':
        return render(request, 'proyects/create_proyect.html', {'form': CreateNewProyect()})
    else:

        Proyect.objects.create(
            name=request.POST['name'])
        return redirect('proyects')


def proyect_detail(request, id):

    proyect = get_object_or_404(Proyect, id=id)
    tasks = Task.objects.filter(proyect_id=id)
    print(tasks)
    return render(request, 'proyects/detail.html', {
        'proyect': proyect,
        'tasks': tasks
    })
