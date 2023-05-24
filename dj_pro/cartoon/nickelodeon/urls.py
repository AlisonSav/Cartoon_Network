from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexList.as_view(), name='index'),
    path('<int:sign_path>/', views.get_info_numb, name='number_check'),
    path('login/', views.login, name='login'),
    path('add_cartoon/', views.add_cartoon, name='add_cartoon'),
    path('add_cartoon_info/', views.add_cartoon_info, name='add_cartoon_info'),
    path('show_info/', views.show_info, name='show_info'),
    path('all_info_from_db/', views.CartoonsList.as_view(), name='all_info_from_db'),
    path('all_info_from_db/<int:pk>', views.CartoonDetail.as_view(), name='get_info_by_id'),
]
