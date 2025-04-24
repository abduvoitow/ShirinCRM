from django.db import models

class Group(models.Model):
    # Dars kunlari uchun choices
    DAYS_CHOICES = [
        ('Du, Cho, Ju', 'Du, Cho, Ju'),
        ('Se, Pa, Sha', 'Se, Pa, Sha'),
    ]

    name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    days = models.CharField(max_length=50, choices=DAYS_CHOICES, blank=True, null=True)  # Dars kunlari
    time = models.CharField(max_length=20, blank=True, null=True)  # Dars vaqti

    def __str__(self):
        return f"{self.name} - {self.course_name}"



class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    passport_series = models.CharField(max_length=10, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    jshr = models.CharField(max_length=20, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    join_date = models.DateField(auto_now_add=True)
    has_contract = models.BooleanField(default=False)   # Shartnoma bor yoki yo‘q

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Naqt', 'Naqt'),
        ('Karta', 'Karta'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='Naqt')

    def __str__(self):
        return f"{self.student.full_name} - {self.amount} ({self.payment_method})"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.full_name} - {self.date} - {'Bor' if self.is_present else 'Yo‘q'}"
