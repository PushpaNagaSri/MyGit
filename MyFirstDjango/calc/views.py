from django.shortcuts import render
def home(request):
 return render(request,'home.html',{'name':'Raju'})

# Create your views here.
