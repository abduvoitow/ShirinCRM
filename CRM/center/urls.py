from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('group/create/', views.create_group, name='create_group'), # Guruh yaratish
    path('group/<int:group_id>/', views.group_detail, name='group_detail'), # Guruh sahifasi
    path('group/<int:group_id>/add-student/', views.add_student, name='add_student'), # Talaba qo‘shish
    path('payment/add/<int:student_id>/', views.add_payment, name='add_payment'), # To‘lov qo‘shish
    path('group/<int:group_id>/edit/', views.edit_group, name='edit_group'), # Guruhni tahrirlash
    path('group/<int:group_id>/delete/', views.delete_group, name='delete_group'), # Guruhni o‘chirish
    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'), # Talabani tahrirlash
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'), # Talabani o‘chirish
    path('group/<int:group_id>/attendance/', views.attendance_view, name='attendance_view'), # Davomat sahifasi
    path('search_students/', views.search_students, name='search_students'),  # Qidiruv uchun URL
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),  # Guruh sahifasi
    path('group/<int:group_id>/export/', views.export_group_excel, name='export_group_excel'), # Guruhni Excelga eksport qilish
    path('student/<int:student_id>/toggle_contract/', views.toggle_contract, name='toggle_contract'),  # Shartnoma o‘chirish yoki qo‘shish
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
