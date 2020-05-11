from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItems
# Create your views here.
def todoView(request):
    all_todo_items = TodoItems.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def addTodo(request):
    #create a new todo items from form
    new_todo_items = TodoItems(content= request.POST['content'])
    
    #save the item added from input at the database
    new_todo_items.save()

    #redirect the browser
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, to_id):
    items_to_delete = TodoItems.objects.get(id = to_id)
    items_to_delete.delete()
    return HttpResponseRedirect('/todo/')