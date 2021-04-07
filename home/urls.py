from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'home'

router=routers.DefaultRouter()
router.register("employee",views.EmployeeViewset,basename="employee")


urlpatterns = [
    path('api/',include(router.urls)),
    path('api/archive/<str:pk>', views.archive, name="archive"),

]