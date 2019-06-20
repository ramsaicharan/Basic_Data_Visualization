from django.shortcuts import render
from django.http import HttpResponse  
from fileupload.functions import handle_uploaded_file  
from fileupload.forms import Dataform
from fileupload.graph import graph
import time

#

# Create your views here.
def input_file(request):  
    if request.method == 'POST':  
        data = Dataform(request.POST,request.FILES)  
        if data.is_valid():  
            handle_uploaded_file(request.FILES['file'])
            #code to get the plot
            graph(request.FILES['file'].name)
            return render(request,'output.html')
        else:
        	return HttpResponse("File uploaded failed")
    else:  
        data = Dataform()  
        return render(request,"fileupload/upload.html",{'form':data}) 