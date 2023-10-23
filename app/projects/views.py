from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    # tags = projectObject.tags.all()
    # reviews = projectObject.review_set.all()
    context = {
        'project': projectObject,
        # 'tags': tags,
        # 'reviews': reviews
    }
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print('FORM DATA:', request.POST)
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


def updatedProject(request, pk):
    context = {}
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    template = 'projects/project-form.html'

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context['form'] = form
    return render(request, template, context)


def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    template = 'projects/delete.html'

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'object': project
    }
    return render(request,template, context)