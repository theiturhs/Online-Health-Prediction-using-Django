from django import forms
from .models import Appointment, AppointmentData, obesityDisorder

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date']

from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date']

from .models import mentalDisorder, pcosDisorder

class AppointmentDataForm(forms.ModelForm):
    class Meta:
        model = AppointmentData
        fields = '__all__'
        exclude = ['user', 'doctor', 'status']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control col-md-12'}),
            'phone': forms.TextInput(attrs={'class': 'form-control col-md-12'}),
            'appointmentDate': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

class MentalDisorderForm(forms.ModelForm):
    class Meta:
        model = mentalDisorder
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-12'})
            if isinstance(field.widget, forms.Select):
                field.empty_label = "Choose one"

class pcosDisorderForm(forms.ModelForm):
    class Meta:
        model = pcosDisorder
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-12'})
            if isinstance(field.widget, forms.Select):
                field.empty_label = "Choose one"
                
class obesityDisorderForm(forms.ModelForm):
    class Meta:
        model = obesityDisorder
        fields = '__all__'
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-12'})
            if isinstance(field.widget, forms.Select):
                field.empty_label = "Choose one"