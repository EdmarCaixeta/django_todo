from django.shortcuts import render, redirect
import datetime

from .models import *
from .forms import *

# Create your views here.

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)

def update(request, pk):
    item = Task.objects.get(id=pk)
    if item.complete == False:
        item.complete = True
    else:
        item.complete = False
    item.updated = datetime.datetime.now()
    item.save()
    return redirect('/')

def delete(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/')