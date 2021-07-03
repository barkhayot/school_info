from django.shortcuts import render, redirect, get_object_or_404
from .models import University
from .forms import UniversityAddForm



def home(request):
    univers = University.objects.all()

    context = {
        'univers':univers,
    }
    return render(request, 'home.html', context)

def detail(request, pk):
    univer = get_object_or_404(University, pk=pk)

    context = {
        'univer':univer
    }

    return render(request, 'detail.html', context)


def add_school(request):
    form = UniversityAddForm()
    if request.method == 'POST':
        form = UniversityAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = UniversityAddForm()

    context = {
        'form':form
    }
    return render(request, 'add_school.html', context)
