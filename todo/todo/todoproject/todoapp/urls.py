from .import views
from django.urls import path,include
app_name= 'todoapp'

urlpatterns = [
    
    path("",views.index,name="index"),
    path("delete/<int:taskid>/",views.delete,name="delete"),
    path("update/<int:taskid>/",views.update,name="update"),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
]

