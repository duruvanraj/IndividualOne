from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='visitor'),
    path('save',views.save, name='Details Saved'),
    path('co',views.co,name='Check Out'),
    path('check0',views.check0,name='Check out successful'),
    path('check',views.check,name='Check out successful'),
    path('detail',views.detail,name='Check out successful'),
    path('submit',views.submit,name='Check out successful'),
    path('view',views.view,name='Visitor details'),
]
