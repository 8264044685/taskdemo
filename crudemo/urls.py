from django.urls import path
from django.conf.urls import url
from . import views
from taskdemo import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('crudemo/add_data/', views.add_data, name='add_data'),
    path('crudemo/status/', views.user_status, name='user_status'),
    path('crudemo/view/<int:id>/', views.view_user, name='view_user'),
    path('crudemo/edit/<int:id>/', views.edit_user, name='edit_user'),
    path('crudemo/delete/<int:id>/', views.delete_user, name='delete_user'),
    path('crudemo/pdf/view/', views.ViewPDF, name='ViewPDF'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)