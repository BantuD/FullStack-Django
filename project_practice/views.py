from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    
    return HttpResponse("hello world");

def htmlResponse(request):
    data={'list':[{"name":"Rajul Dubey","age":"27","number":"9981852584"},
                {"name":"Bantu Dubey","age":"27","number":"6232738937"},
                {"name":"ranbir Dubey","age":"27","number":"9993507083"}]}

    return render(request,'index.html',data)

def dynamicRequest(request,courseId):
    return HttpResponse(f'course id is: {courseId}')

def htmlAnimation(request):
    return render(request,"bouncingBall-fullstack.html")

def getGeolocation(request):
    return render(request,"geolocation.html")