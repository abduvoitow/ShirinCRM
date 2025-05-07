from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Gurhlar sahifasi
    path("yangi-guruh", views.create_group, name='create_group'), # Qo‘shish
    path('guruh/<int:group_id>/', views.group_detail, name='group_detail'), # Sahifa
    # path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('guruh/<int:group_id>/tahrirlash/', views.edit_group, name='edit_group'), # Tahrirlash
    path("guruhni_o'chirish/<int:group_id>/", views.delete_group, name='delete_group'),

    
    # O'quvchilar sahifasi
    path("group/<int:group_id>/yangi-o'quvchi/", views.add_student, name='add_student'), # Qo‘shish
    path("o'quvchi/<int:student_id>/tahrirlash/", views.edit_student, name='edit_student'), # Tahrirlash
    path("o'quvchini-o'chirish/<int:student_id>/", views.delete_student, name='delete_student'),


    # To'lovlar sahifasi
    path("yangi-to'lov/<int:student_id>/", views.add_payment, name='add_payment'), # Qo‘shish
    path("to'lovni-tahrirlash/<int:payment_id>/", views.edit_payment, name='edit_payment'), # Tahrirlash
    path("to'lovni-o'chirish/<int:payment_id>/", views.delete_payment, name='delete_payment'), # O'chirish

    # Shartnoma sahifasi
    path("o'quvchi/<int:student_id>/shartnoma/", views.toggle_contract, name='toggle_contract'),
    
    # Davomat sahifasi
    path('guruh/<int:group_id>/davomat/', views.attendance_view, name='attendance_view'),

    # Qidirish funksiyasi
    path('qidirish/', views.search_students, name='search_students'),

    # Excel, yuklab olish
    path('guruh/<int:group_id>/yuklab-olish-excel/', views.export_group_excel, name='export_group_excel'),

    # Arxiv
    path('arxiv-guruhlar/', views.archived_groups, name='archived_groups'),
    path("guruh/<int:group_id>/arxivlash/", views.archive_group, name='archive_group'),
    path('guruh/<int:group_id>/arxivdan-chiqarish/', views.unarchive_group, name='unarchive_group'),

]


