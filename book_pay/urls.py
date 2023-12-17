from django.urls import path
from . import views

app_name = "kakaopay"

urlpatterns = [
    path('', views.pay, name='pay'),
    # path('test/', views.test),
    path('/kakaoLoginLogic/', views.kakaoLoginLogic, name='kakaoLoginLogic'),
    path('/kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name='kakaoLoginLogicRedirect'),
    path('/kakaoLogout/', views.kakaoLogout, name='kakaoLogout'),
    path('/kakaoPay/', views.kakaoPay, name='kakaoPay'),
    path('/kakaoPayLogic/', views.kakaoPayLogic, name='kakaoPayLogic'),
    path('/paySuccess', views.paySuccess, name='paySuccess'),
    path('/payFail', views.payFail, name='payFail'),
    path('/payCancel', views.payCancel, name='payCancel'),
    # FLutter & Django
    # path('kakaoPayLogic2/', views.kakaoPayLogic2),
    # path('paySuccess2/', views.paySuccess2),
    # GET | POST - Methods / Params | QueryString
    # path('methodsCheck/<int:id>', views.methodsCheck),
]