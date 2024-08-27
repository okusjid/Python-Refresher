from django.urls import path
from . import views

urlpatterns = [
    path('<str:month>/', views.monthy_challenges),
    path('<int:month>/', views.monthly_challenge_by_number),
    
    # path["feb", views.feb],
    # path["mar", views.mar],
    # path["apr", views.apr],
]