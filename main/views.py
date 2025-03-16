from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib import messages
from .models import Todo

# Create your views here.
def todo_list(request):
    
    
    
    context={
        'todo':Todo.objects.all()
    }
    return render(request,'pages/todo_list.html',context)

def add_task(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        
        if title:
            Todo.objects.create(title=title)
    return redirect('todo_list')


def delete_task(request , id):
    del_task=Todo.objects.get(id=id)
    if request.method == 'GET':
        del_task.delete()
        
    return redirect('todo_list')


def edit_task(request, id):
    try:
        task = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        messages.error(request,'Data does not exist!')
        return redirect('todo_list')
    
    if request.method == 'POST':
            new_title = request.POST.get('title')
            if new_title:
                task.title = new_title
                task.save()
                messages.success(request, " data updates succefully!")  # رسالة النجاح
                return redirect('todo_list')
    return render(request, 'pages/edit_task.html', {'task': task})

   
   
