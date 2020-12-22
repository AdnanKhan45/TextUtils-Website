from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def analyze(request):
    
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    uppercase = request.POST.get('capsall', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    if removepunc == "on":
        if djtext == "":
            return render(request, 'req.html')
        else:
            punctuations = '''!-()[]{};:'"\,|?`<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
                    params = {'analyzed_text':analyzed}
                    djtext = analyzed
    
    if uppercase == "on":
        if djtext == "":
            return render(request, 'req.html')
        else:
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
                params = {'analyzed_text':analyzed}
                djtext = analyzed

    if removenewline == "on":
        if djtext == "":
            return render(request, 'req.html')
        else:
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
                    params = {'analyzed_text':analyzed}
                    djtext = analyzed
        
    if extraspaceremover == "on":
        if djtext == "":
            return render(request, 'req.html')
        else:
            analyzed = ""
            for index, char in enumerate(djtext):
                if djtext[index] == " " and djtext[index+1] == " ":
                    pass
                else:
                    analyzed = analyzed + char
                    params = {'analyzed_text':analyzed}
                    
    if removepunc != "on" and uppercase != "on" and removenewline != "on" and extraspaceremover != "on":
        return render(request, 'error.html',{'error':'Please select atleast one opition.'})
   
    return render(request, 'analyze.html',params)
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')




