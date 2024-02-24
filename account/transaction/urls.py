from django.urls import path
from . import views


urlpatterns = [
        path('transactions/', views.create_account.as_view()),
        path('account/', views.create_account.as_view()),
        path('withdraw/', views.create_withdraw.as_view()),
        path('deposit/', views.create_deposit.as_view()),
        ]
