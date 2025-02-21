from django.shortcuts import render
from .models import Todo

# Todoリストを表示する
def index(request):
    todos = Todo.objects.all()
    return render(request, "myapp/index.html", {"todos": todos})

# 新しいTodoを追加する
def add_todo(request):
    pass
    
# Todoを完了済みにする



# Todoを削除する