from django.shortcuts import render, redirect
from .models import Todo

# Todoリストを表示する
def index(request):
    todos = Todo.objects.all()
    return render(request, "myapp/index.html", {"todos": todos})

# 新しいToDoを追加する
def add_todo(request):
    if request.method == "POST":
        title = request.POST['title']
        Todo.objects.create(title=title)
    return redirect('index')

# ToDoを完了済みにする
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

# ToDoを削除する
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')