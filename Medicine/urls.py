from django.urls import path, include
from .views import *

urlpatterns = [

    path('accounts/', include('allauth.urls')),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('doctor/', DoctorViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='doctor_list'),
    path('doctor/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='doctor_detail'),

    path('medical/record/', MedicalRecordViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='medical_record_list'),
    path('medical/record/<int:pk>/', MedicalRecordViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='medical_record_detail'),

    path('appointment/', AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='appointment_detail'),

    path('medication/', MedicationViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='medication_list'),
    path('medication/<int:pk>/', MedicationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='medication_detail'),

    path('fitnessProgram/', FitnessProgramViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='fitnessProgram_list'),
    path('fitnessProgram/<int:pk>/', FitnessProgramViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='fitnessProgram_detail'),

    path('notification/', NotificationViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='notification_list'),
    path('notification/<int:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='notification_detail'),

]