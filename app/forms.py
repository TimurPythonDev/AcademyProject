from django.forms import ModelForm
from .models import CourseAddPage,SendRegistr


class ProjectForm(ModelForm):
    class Meta:
        model = CourseAddPage
        fields = ['course_name', 'course_price', 'course_discount','course_continu','image',]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['course_price'].widget.attrs.update(
            {'class': 'form-control', })



class MessageForm(ModelForm):
    class Meta:
        model = SendRegistr
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', })

        self.fields['course_name'].widget.attrs.update(
            {'class': 'form-control'})

