from django.shortcuts import render, HttpResponse

def ind(request):
    return render(request,'Original2.html')


def m(request):
    return render(request,'menu2.html')