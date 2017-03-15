from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm


def index(request):
    return HttpResponse("hey guys")


def register(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = NameForm()

    return render(request, 'templates/register.html', {'form' : form})
