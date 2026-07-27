from django.urls import path
from . import views

from django.urls import path


urlpatterns = [
    path("courselist", views.about_view,name = "about_view"),
    path("course/<str:course>", views.course_view,name="courses")   

]


'''
    from django.urls import reverse
    bu fonksiyon ile bir reverse degiskeni tanimlayarak yonlendirmeyi urlspatterns listesinde verilen isimlere gore yonlendirme yapabiliriz

    yonlendirme view fonksiyonlari icinde return HttpResponseRedirect(response) ile istenen baska bir fonksiyona ya da enpoint e redirect edilebilir

    
    !! Eger endpoint argumabn aliyorsa reverse degiskeni asagidaki gibi tnaimlnanir


    page_to_go = reverse("{Yonlendirecek view in name i}",args=[{tum argumanlar sira ile bu liste icinde verilir}])


'''