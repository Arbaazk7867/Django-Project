from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    jtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./@?#$%^&*_~'''
        analyzed=""
        for char in jtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        jtext=analyzed
        #return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        analyzed=""
        for char in jtext:
            analyzed=analyzed + char.upper()
        params={'purpose' : 'Changed to Uppercase', 'analyzed_text':analyzed }
        jtext=analyzed
        #return render(request,'analyze.html',params)
    if(newlineremover=='on'):
        analyzed=""
        for char in jtext:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char
        params={'purpose':'Removed New Lines','analyzed_text':analyzed}
        jtext=analyzed
        #return render (request,'analyze.html',params)

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index,char in enumerate(jtext):
            if  not(jtext[index]==" " and jtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

    if(removepunc!='on' and newlineremover!='on' and extraspaceremover!='on' and fullcaps!='on'):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)