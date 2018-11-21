from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

# Create your views here.
def index(request):
    candidate = Candidate.objects.all()
    context = {'candidate':candidate}
    return render(request, 'elections/index.html',context)

def areas(request, area):
    return HttpResponse(area)
    str = ''
    for candidate in candidate:
        str += "<p>{} 기호{}번({})<br>".format(candidate.name,
            candidate.party_number,
            candidate.area)
        str += candidate.introduction+"</p>"

    return HttpResponse(str)
