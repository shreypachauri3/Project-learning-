from django.http import HttpResponse
from django.shortcuts import render

from home.models import fileupload

# Create your views here.
def home(request):
    if request.method =='POST':
        file=request.FILES["img"]
        data=fileupload.objects.create(img=file)
        data.save()
        return HttpResponse('File has been uploaded successfully!!')
    else:
        print(render)
        return render(request,'index.html')
        