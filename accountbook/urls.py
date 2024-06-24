from django.urls import path

from accountbook import views

app_name = 'accountbook'

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name = 'category_list'),
    path('list/', views.AccountbookListView.as_view(), name = 'accountbook_list'),
    path('create/', views.AccountbookCreateView.as_view(), name = 'accountbook_create'),
    path('update/<int:pk>/', views.AccountbookUpdateView.as_view(), name = 'accountbook_update'),
    path('delete/<int:pk>/', views.AccountbookDeleteView.as_view(), name = 'accountbook_delete'),
    path('', views.dashboard_accountbook, name = 'accountbook_dashboard'),
]