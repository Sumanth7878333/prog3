from django.shortcuts import render

# Create your views here.
def home(request):
    names ='rohit','kohli','dhoni'  
    return render(request,'template_app/index.html',{'names':names})