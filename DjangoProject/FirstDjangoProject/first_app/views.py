from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

courses_dict = {"java" : "Welcome to Java Course Page",
                "python" : "Welcome to Python Course Page"
                 ,"swift" : "Welcome to Swift Course Page"
                  ,"ruby" : "Welcome to Ruby Course Page"
                   ,"go" : "Welcome to Go Course Page"
                    ,"csharp" : "Welcome to C# Course Page" }



def about_view(request):
    return HttpResponse("Gidilebilir kurslar: </br> 1.Java </br> 2.Python </br> 3.Swift </br> 4.Ruby </br> 5.Go </br> 6."  )

def course_view(request,course):

    current_course= courses_dict.get(course)

    if(current_course == None):
        return HttpResponse("undenified course entered")
    return HttpResponse(current_course)
    

    