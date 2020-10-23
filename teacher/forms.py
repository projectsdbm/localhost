from django import forms
from student.models import StudentModel


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        Class = cleaned_data.get('Class')
        phone_no = cleaned_data.get('phone_no')
        year = cleaned_data.get('year')

        if Class not in ['A','B','C','D','E']:
            self.add_error('Class','Enter Valid Class Section')

        if len(phone_no) !=10 or phone_no.isdigit()!=True:
            self.add_error('phone_no','Enter Valid Phone Number')

        if year not in [1,2,3,4]:
            self.add_error('year','Enter Valid Year')
