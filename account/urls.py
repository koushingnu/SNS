from django.contrib.admin.sites import all_sites
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.AccountSignUpView.as_view(), name='signup'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(),name='logout'),

    path('password_change/', views.AccountPasswordChangeView.as_view(),
    name='password_change'),
    path('password_change/done/', views.AccountPasswordChangeDoneView.as_view(),
    name='password_change_done'),
    path('email/change/',
    views.AccountEmailChangeView.as_view(), name='email_change'),
    path('email/change/done',
    views.AccountEmailChangeDoneView.as_view(), name='email_change_done'),
    path('email/change/complete/<str:token>',
    views.AccountEmailChangeCompleteView.as_view(), name='email_change_complete'),

    path('password_reset/',views.AccountPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done',views.AccountPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>',views.AccountPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/',views.AccountPasswordResetComplete.as_view(), name='password_reset_complete'),

    path('avator/upload/', views.AccountAvatorUploadView.as_view(), name='avator_upload'),
    path('avator/upload/done', views.AccountAvatorUploadDoneView.as_view(), name='avator_upload_done'),

    path('<int:pk>', views.AccountDetailView.as_view(),name='detail'),
]
