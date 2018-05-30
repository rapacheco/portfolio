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
            return HttpResponseRedirect("/")
    else:
        form = MessageForm()
    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    with open(os.path.join(MEDIA_DIR, 'rafaelRibeiroResumePortfolio.docx', 'rb')) as doc:
        response = HttpResponse(doc.read())
        response['content_type'] = 'application/docx'
        response['Content-Disposition'] = 'attachment;rafaelRibeiroResumePortfolio.docx'
        return response
