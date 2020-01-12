from django.shortcuts import render
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items=ToDo.objects.all().order_by("-added_date")
    return render(request,'todoapp/index.html',{"todo_items":todo_items})

def add_todo(request):
    date=timezone.now()
    content=request.POST['content']
    ToDo.objects.create(added_date=date,text=content)
    return HttpResponseRedirect('/')

def delete_todo(request,item_id):
    ToDo.objects.get(id=item_id).delete()
    return HttpResponseRedirect('/')
