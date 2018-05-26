from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import MessageForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})
