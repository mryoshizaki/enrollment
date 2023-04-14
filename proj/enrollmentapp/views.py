from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from enrollmentapp.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'birthday']

def student_list(request, template_name='student_list.html'):
    student = Student.objects.all()
    data = {}
    data['object_list'] = student
    return render(request, template_name, data)

def student_view(request, pk, template_name='student_detail.html'):
    student= get_object_or_404(Student, pk=pk)    
    return render(request, template_name, {'object':student})

def student_create(request, template_name='student_update.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, template_name, {'form':form})

def student_update(request, pk, template_name='student_update.html'):
    student= get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, template_name, {'form':form})

def student_delete(request, pk, template_name='student_confirm_delete.html'):
    student= get_object_or_404(Student, pk=pk)    
    if request.method=='POST':
        student.delete()
        return redirect('student_list')
    return render(request, template_name, {'object':student})