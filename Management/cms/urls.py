from django.urls import path
from cms import views

app_name = 'cms'

urlpatterns = [
    # Habit
    path('habit/', views.habit_list, name='habit_list'),
    path('habit/add/', views.habit_edit, name='habit_add'),
    path('habit/mod/<int:habit_id>/', views.habit_edit, name='habit_mod'),
    path('habit/del/<int:habit_id>/', views.habit_del, name='habit_del'),

    # Small Goal

]
