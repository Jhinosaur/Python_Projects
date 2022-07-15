from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import Http404
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        if not link:
            return HttpResponseBadRequest('Link is not provided')
        uid = str(uuid.uuid4())[:5]
        new_url = Url.objects.create(link=link,uuid=uid)
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.filter(uuid=pk).first()
    if url_details:
        return redirect('https://'+url_details.link)

    raise Http404

def delete(self):
    current_date = timezone.now()
    date_to_filter = current_date - timezone.timedelta(days=30)
    Url.objects.filter(created_at__gt=date_to_filter).delete()


