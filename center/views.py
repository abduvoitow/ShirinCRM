from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from datetime import date
import openpyxl
from openpyxl.utils import get_column_letter
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
    return render(request, 'center/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')




# Asosiy sahifa
@login_required
def home(request):
    query = request.GET.get('q', '')
    groups = Group.objects.all().order_by('-start_date')
    
    if query:
        students = Student.objects.filter(
            Q(full_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(group__name__icontains=query)
        ).select_related('group').prefetch_related('payments')
    else:
        students = Student.objects.none()

    for group in groups:
        group_students = group.students.all()
        group.student_count = group_students.count()
        group.paid_count = group_students.filter(payments__isnull=False).distinct().count()

    return render(request, 'center/home.html', {
        'groups': groups,
        'students': students,
        'query': query
    })

# Talabalarni qidirish
def search_students(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(full_name__icontains=query).select_related('group')
        results = [{
            'full_name': student.full_name,
            'group_id': student.group.id,
        } for student in students]
    else:
        results = []
    return JsonResponse(results, safe=False)




# Guruh yaratish
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'center/create_group.html', {'form': form})
#  Guruh sahifasi
def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    students = group.students.all()
    return render(request, 'center/group_detail.html', {'group': group, 'students': students})
# Guruhni tahrirlash
def edit_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)
    return render(request, 'center/edit_group.html', {'form': form, 'group': group})
# Guruhni o‘chirish
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('home')
    return render(request, 'center/delete_group.html', {'group': group})


# Talaba qo‘shish
def add_student(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.group = group
            student.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = StudentForm()
    return render(request, 'center/add_student.html', {'form': form, 'group': group})
# Talabani tahrirlash
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=student.group.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'center/edit_student.html', {'form': form, 'student': student})
# Talabani o‘chirish
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        group_id = student.group.id
        student.delete()
        return redirect('group_detail', group_id=group_id)
    return render(request, 'center/delete_student.html', {'student': student})



# To‘lov qo‘shish
def add_payment(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.student = student
            payment.save()
            return redirect('group_detail', group_id=student.group.id)
    else:
        form = PaymentForm()
    return render(request, 'center/add_payment.html', {'form': form, 'student': student})


# Davomatlarni ko‘rish
def group_attendance(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    students = group.students.all()
    return render(request, 'center/group_attendance.html', {'group': group, 'students': students})


# Davomatlarni ko‘rish va yangilash
def attendance_view(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    students = group.students.all()
    today = date.today()

    if request.method == 'POST':
        for student in students:
            present = request.POST.get(f'attendance_{student.id}') == 'on'
            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={'is_present': present}
            )
        return redirect('attendance_view', group_id=group.id)

    # Barcha davomatlar jadvali
    attendance_data = {}
    all_dates = Attendance.objects.filter(student__group=group).values_list('date', flat=True).distinct().order_by('-date')

    for student in students:
        records = Attendance.objects.filter(student=student)
        attendance_data[student] = {record.date: record.is_present for record in records}

    return render(request, 'center/attendance.html', {
        'group': group,
        'students': students,
        'attendance_data': attendance_data,
        'all_dates': all_dates,
        'today': today
    })



#  Guruhni Excelga eksport qilish
def export_group_excel(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    students = group.students.all()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = f"{group.name} o'quvchilari"

    headers = ['№', 'F.I.SH', 'Telefon raqami', 'Seriya', 'Raqam', 'JSHSHIR', 'To‘lov',]
    for col_num, header in enumerate(headers, 1):
        col_letter = get_column_letter(col_num)
        sheet[f'{col_letter}1'] = header

    for row_num, student in enumerate(students, 2):
        sheet[f'A{row_num}'] = student.id
        sheet[f'B{row_num}'] = student.full_name
        sheet[f'C{row_num}'] = student.phone
        sheet[f'D{row_num}'] = student.passport_series
        sheet[f'E{row_num}'] = student.passport_number
        sheet[f'F{row_num}'] = student.jshr
        sheet[f'G{row_num}'] = "Bor" if student.payments.exists() else "Yo'q"

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename={group.name}_students.xlsx'
    workbook.save(response)
    return response



# Shartnoma o‘chirish yoki qo‘shish
def toggle_contract(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.has_contract = not student.has_contract
    student.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))