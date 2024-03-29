from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='home'),
    path("register", views.register, name="register"),
    path("doctor_register", views.doctor_register, name="doctor_register"),
    path("login", views.user_login, name="login"),
    path("doctor_login", views.doctor_login, name="doctor_login"),
    path("profile", views.complete_profile, name="profile"),
    path("dashboard", views.user_dashboard, name="dashboard"),
    path("doctor_dashboard", views.doctor_dashboard, name="doctor_dashboard"),
    path("health_prediction", views.health_prediction, name="health_prediction"),
    path("mental_disorder", views.mental_disorder, name="mental_disorder"),
    path("pcos", views.pcos, name="pcos"),
    path("obesity", views.obesity, name="obesity"),
    path("report", views.report, name="report"),
    path("test_history", views.test_history, name="test_history"),
    path("fix_appointment", views.fix_appointment, name="fix_appointment"),
    path("appointment_success", views.appointment_success, name="appointment_success"),
    path('logout', views.user_logout, name='logout'),
    path('appointmentHistory', views.appointmentHistory, name='appointmentHistory'),
    path('appointmentRequest', views.appointmentRequest, name='appointmentRequest'),
    path('appointmentScheduled', views.appointmentScheduled, name='appointmentScheduled'),
    path('update_status/<int:appointment_id>/', views.update_status, name='update_status'),
]