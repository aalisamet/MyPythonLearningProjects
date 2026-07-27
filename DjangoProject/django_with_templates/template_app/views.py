from django.shortcuts import render

# Create your views here.
def first_temp(request):
    return render(request,"template_app/index.html")