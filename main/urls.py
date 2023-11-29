from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.loginUser, name='main'),
    path('identities/<str:img>', views.secure, name='secure'),
    path('open', views.open, name='open'),
    path('closed', views.closed, name='closed'),
    path('overdue', views.overdue, name='overdue'),
    path('search', views.search, name='search'),
    path('logout', views.logoutUser, name='logout'),
    path('entry/<int:key>', views.openEntry, name='entry'),
    path('delete_entry/<int:key>', views.deleteEntry, name='delete_entry'),
    path('delete_inst/<int:key>', views.deleteInst, name='delete_inst'),
    path('status_entry/<int:key>', views.statusEntry, name='status_entry'),
]
