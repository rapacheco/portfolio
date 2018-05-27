from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import MessageForm
from .models import Message

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            m = form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # msg = form.cleaned_data['msg']
            # m = Message(name=name, email=email, msg=msg)
            # m.save()

            return HttpResponseRedirect("/")
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})
