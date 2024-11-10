from django.shortcuts import render , HttpResponse
def index(request):
    return HttpResponse("This is a homepage")
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is services page")


