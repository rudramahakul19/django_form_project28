from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic inserted successfully!!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}

    if request.method == 'POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            nm=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ur,email=em)[0]
            WO.save()
            return HttpResponse('<center>Webpage inserted successfully!!</center>')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EARFO=AccessRecordform()
    d={'EARFO':EARFO}

    if request.method == 'POST':
        ARFDO=AccessRecordform(request.POST)
        if ARFDO.is_valid():
            nm=ARFDO.cleaned_data['name']
            WPO=Webpage.objects.get(pk=nm)
            dt=ARFDO.cleaned_data['date']
            au=ARFDO.cleaned_data['author']
            ARO=AccessRecord.objects.get_or_create(name=WPO,date=dt,author=au)[0]
            ARO.save()
            return HttpResponse('Accessrecord inserted successfully!!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_accessrecord.html',d)
