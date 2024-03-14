from django.shortcuts import redirect, render

# Create your views here.

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

people = []  

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        people.append(Person(username, password))
        return redirect('show') 
    return render(request, 'add.html') 

def show(request):
    context = {'people': people}
    return render(request, 'show.html', context)