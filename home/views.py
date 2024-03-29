from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .models import ObesityData

import pandas as pd
from datetime import date

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import AppointmentForm, MentalDisorderForm, pcosDisorderForm, AppointmentDataForm, obesityDisorderForm
from .models import Receipt, UserProfile, userHistory, DoctorUser, AppointmentData
from django.contrib.auth.models import User
from django import forms


import pandas as pd
import joblib
import tensorflow as tf
import numpy as np
from django.utils import timezone
import json

from django.contrib import messages

mental_disorder_model = joblib.load('static/models/mental_disorder_prediction.pkl')
mental_disorder_encoder = joblib.load('static/encoders/mental_disorder_encoder.pkl')
mental_disorder_output_encoder = joblib.load('static/encoders/mental_disorder_output_encoder.pkl')
mental_disorder_df = pd.read_csv('static/mentalDisorder.csv')

pcos_model = joblib.load('static/models/pcos_prediction.pkl')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for CSS Properties
        self.fields['username'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-10 form-control'})

        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['email'].help_text = '<span class="text-muted">Required. Inform a valid email address.</span>'
        self.fields['password2'].help_text = '<span class="text-muted">Enter the same password as before, for verification.</span>'
        self.fields['password1'].help_text = '<span class="text-muted"><ul class="small"><li class="text-muted">Your password can not be too similar to your other personal information.</li><li class="text-muted">Your password must contain at least 8 characters.</li><li class="text-muted">Your password can not be a commonly used password.</li><li class="text-muted">Your password can not be entirely numeric.</li></ul></span>' 

class DoctorRegistrationForm(UserRegistrationForm):
    
    phone = forms.CharField(max_length=20)
    specialization = forms.CharField(max_length=100)
    hospital = forms.CharField(max_length=255)
    city = forms.CharField(max_length = 100)
    state = forms.CharField(max_length = 100)
    country = forms.CharField(max_length = 100)
    about = forms.CharField(max_length = 1000)
    education = forms.CharField(max_length = 1000)
    experience = forms.CharField(max_length = 1000)
    languages = forms.CharField(max_length = 1000)
    expertise = forms.CharField(max_length = 1000)

    class Meta:
        model = DoctorUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 
                'phone', 'specialization', 'hospital', 'city', 'state', 'country',
                'about', 'education', 'experience', 'languages', 'expertise']
        db_table = 'doctor_user'

    DoctorUser.groups.field.related_name = 'doctor_groups'
    DoctorUser.user_permissions.field.related_name = 'doctor_user_permissions'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for CSS Properties
        self.fields['username'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['specialization'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['hospital'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['city'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['state'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['country'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['about'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['education'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['experience'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['languages'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['expertise'].widget.attrs.update({'class': 'col-md-10 form-control'})

        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['email'].help_text = '<span class="text-muted">Required. Inform a valid email address.</span>'
        self.fields['password2'].help_text = '<span class="text-muted">Enter the same password as before, for verification.</span>'
        self.fields['password1'].help_text = '<span class="text-muted"><ul class="small"><li class="text-muted">Your password can not be too similar to your other personal information.</li><li class="text-muted">Your password must contain at least 8 characters.</li><li class="text-muted">Your password can not be a commonly used password.</li><li class="text-muted">Your password can not be entirely numeric.</li></ul></span>' 
        
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                return redirect('login')
        except:
            form = UserRegistrationForm()
            messages.error(request, "Something went wrong. Try again!")
            
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        form2 = UserRegistrationForm(request.POST)
        
        try:
            if form.is_valid():
                form.save()
                form2.save()
                return redirect('doctor_login')
        except:
            form = DoctorRegistrationForm()
            messages.error(request, "Something went wrong. Try again!")
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Something went wrong. Try again!")
    return render(request, 'login.html')


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                if DoctorUser.objects.get(username = user.username).phone == phone:
                    login(request, user)
                    return redirect('doctor_dashboard')
            except:
                messages.error(request, "Something went wrong. Try again!")
        else:
            messages.error(request, "Something went wrong. Try again!")
    return render(request, 'doctor_login.html')


@login_required
def complete_profile(request):
    if UserProfile.objects.filter(user=request.user).exists():
        # If profile exists, redirect to the dashboard profile page
        return redirect('dashboard')
    
    if request.method == 'POST':
        user_profile = UserProfile.objects.create(
            user=request.user,
            dob=request.POST['dob'],
            gender=request.POST['gender'],
            height=request.POST['height'],
            weight=request.POST['weight'],
            profession=request.POST['profession']
        )
        return redirect('dashboard')
    return render(request, 'profile.html', {'user_name': request.user.first_name + " " + request.user.last_name})

@login_required
def user_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'user_dashboard.html', {'user_name': request.user.first_name + " " + request.user.last_name, 
                                                'user_profile': user_profile, 
                                                'user_username': request.user.username
                                                })

@login_required
def doctor_dashboard(request):
    doctor_detail = DoctorUser.objects.get(username = request.user)
    return render(request, 'doctor_dashboard.html', {'doctor': doctor_detail, 'user_name': request.user.first_name + " " + request.user.last_name})


@login_required
def health_prediction(request):
    return render(request, 'health_test.html', {'user_name': request.user.first_name + " " + request.user.last_name})

@login_required
def fix_appointment(request):
    form = AppointmentDataForm()
    doctors = DoctorUser.objects.all()
    if request.method == 'POST':
        form = AppointmentDataForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            doctor_id = request.POST.get('doctor')
            doctor = DoctorUser.objects.get(id=doctor_id)
            appointment.doctor = doctor
            appointment.save()
            return redirect('appointmentHistory')
    return render(request, 'fix_appointment.html', {'form': form, 'user_name': request.user.first_name + " " + request.user.last_name, 'doctors': doctors})

@login_required
def appointmentHistory(request):
    appointment = AppointmentData.objects.filter(user=request.user)
    return render(request, 'appointment_history.html', {'user_name': request.user.first_name + " " + request.user.last_name, 'appointment': appointment})

def update_status(request, appointment_id):
    appointment = AppointmentData.objects.get(pk=appointment_id)
    appointment.status = 'Scheduled'
    appointment.save()
    return redirect('appointmentRequest')

@login_required
def appointmentRequest(request):
    doctor = DoctorUser.objects.get(username=request.user.username)
    appointment = AppointmentData.objects.filter(doctor=doctor, status='Pending')
    print(appointment)
    return render(request, 'appointment_request.html', {'user_name': request.user.first_name + " " + request.user.last_name, 'appointment': appointment})

@login_required
def appointmentScheduled(request):
    doctor = DoctorUser.objects.get(username=request.user.username)
    appointment = AppointmentData.objects.filter(doctor=doctor, status='Scheduled')
    print(appointment)
    return render(request, 'appointment_scheduled.html', {'user_name': request.user.first_name + " " + request.user.last_name, 'appointment': appointment})

@login_required
def mental_disorder(request):
    if request.method == 'POST':
        form = MentalDisorderForm(request.POST)
        if form.is_valid():
            # Retrieve user-entered data from the form
            sadness = form.cleaned_data['sadness']
            euphoric = form.cleaned_data['euphoric']
            exhausted = form.cleaned_data['exhausted']
            sleep_disorder = form.cleaned_data['sleep_disorder']
            mood_swing = form.cleaned_data['mood_swing']
            suicidal_thoughts = form.cleaned_data['suicidal_thoughts']
            anorexia = form.cleaned_data['anorxia']
            authority_respect = form.cleaned_data['authority_respect']
            try_explanation = form.cleaned_data['try_explanation']
            aggressive_response = form.cleaned_data['aggressive_response']
            ignore_moveon = form.cleaned_data['ignore_moveon']
            nervous_breakdown = form.cleaned_data['nervous_breakdown']
            admit_mistakes = form.cleaned_data['admit_mistakes']
            overthink = form.cleaned_data['overthink']
            sexual_activity = form.cleaned_data['sexual_activity']
            concentration = form.cleaned_data['concentration']
            optimism = form.cleaned_data['optimisim']
            
            new_data = [[sadness, euphoric, exhausted, sleep_disorder,
                        mood_swing, suicidal_thoughts, anorexia, authority_respect,
                        try_explanation, aggressive_response, ignore_moveon,
                        nervous_breakdown, admit_mistakes, overthink, sexual_activity, 
                        concentration, optimism]]
            
            symp = new_data[0]
            new_data = mental_disorder_encoder.transform(new_data)
            predicted_data = mental_disorder_model.predict(new_data)
            prediction_result = mental_disorder_output_encoder.inverse_transform((np.array(predicted_data)).reshape(-1, 1))
            
            print(prediction_result)
            
            my_instance = userHistory(
                user=request.user,
                test_type='Mental Disorder Test',
                symptoms=json.dumps(symp),  # Convert list to JSON string
                result=prediction_result[0][0],  # Set result as needed
                date=timezone.now()  # Set current date and time
            )
            my_instance.save()

            return render(request, 'mental_disorder_prediction.html', {'form': form, 'prediction_result': prediction_result[0][0]})
    else:
        form = MentalDisorderForm()
    return render(request, 'mental_disorder_prediction.html', {'form': form, 'user_name': request.user.first_name + " " + request.user.last_name})


obesity_encoder = joblib.load('static/encoders/obesity_encoder.pkl')
obesity_output_encoder = joblib.load('static/encoders/obesity_output_encoder.pkl')
obesity_model = joblib.load('static/models/obesity_prediction.pkl')

@login_required
def obesity(request):
    user_data = UserProfile.objects.get(user=request.user)
    weight, height, bmi, gender = user_data.weight, user_data.height, user_data.bmi, user_data.gender.capitalize()
    age = date.today().year - user_data.dob.year - ((date.today().month, date.today().day) < (user_data.dob.month, user_data.dob.day))
    
    if request.method == 'POST':
        
        form = obesityDisorderForm(request.POST)
        if form.is_valid():
            activityLevel = form.cleaned_data['activityLevel']
            
            new_data = [[age, gender, height, weight, bmi, int(activityLevel)]]
            new_data[0][1] = obesity_encoder.transform(np.array(new_data[0][1]).reshape(-1, 1))[0][0]
            predicted_data = obesity_model.predict(new_data)
            predicted_output = obesity_output_encoder.inverse_transform((np.array(predicted_data)).reshape(-1, 1))[0][0]
            
            symp = [int(activityLevel)]
            
            my_instance = userHistory(
                user=request.user,
                test_type='Obesity Test',
                symptoms=json.dumps(symp),
                result=predicted_output,
                date=timezone.now()
            )
            my_instance.save()
            
            return render(request, 'obesity.html', {'age': age, 'user_data': user_data, 'form': form, 'prediction_result': predicted_output, 'user_name': request.user.first_name + " " + request.user.last_name})
    else:
        form = obesityDisorderForm()

    return render(request, 'obesity.html', {'age': age, 'user_data': user_data, 'form': form, 'user_name': request.user.first_name + " " + request.user.last_name})

@login_required
def pcos(request):
    user_data = UserProfile.objects.get(user=request.user)
    print(user_data, user_data.dob, user_data.weight, user_data.height)
    age = date.today().year - user_data.dob.year - ((date.today().month, date.today().day) < (user_data.dob.month, user_data.dob.day))
    
    if request.method == 'POST':
        form = pcosDisorderForm(request.POST)
        if form.is_valid():
            # Retrieve user-entered data from the form
            period_frequency = form.cleaned_data['period_frequency']
            gained_weight = form.cleaned_data['gained_weight']
            body_hair_growth = form.cleaned_data['body_hair_growth']
            skin_dark = form.cleaned_data['skin_dark']
            hair_problem = form.cleaned_data['hair_problem']
            pimples = form.cleaned_data['pimples']
            fast_food = form.cleaned_data['fast_food']
            exercise = form.cleaned_data['exercise']
            mood_swing = form.cleaned_data['mood_swing']
            mentrual_regularity = form.cleaned_data['mentrual_regularity']
            duration = form.cleaned_data['duration']
            blood_grp = form.cleaned_data['blood_grp']
            
            new_data = [[age, user_data.weight, user_data.height, period_frequency, int(gained_weight),
                        int(body_hair_growth), int(skin_dark), int(hair_problem),
                        int(pimples), int(fast_food), int(exercise), int(mood_swing),
                        int(mentrual_regularity), int(duration), int(blood_grp)]]
            
            prediction_result = pcos_model.predict(new_data)[0]
            
            print(prediction_result)
            
            if prediction_result == 1:
                prediction_result = 'PCOS Positive'
            else:
                prediction_result = 'PCOS Negative'
            
            print(prediction_result)
            
            ch = {1: "YES", 0: "NO"}
            blood_group = {11: 'A+',
                            12: 'A-',
                            13: 'B+',
                            14: 'B-',
                            15: 'O+',
                            16: 'O-',
                            17: 'AB+',
                            18: 'AB-'}
            
            symp = [period_frequency, ch[int(gained_weight)],
                        ch[int(body_hair_growth)], ch[int(skin_dark)], ch[int(hair_problem)],
                        ch[int(pimples)], ch[int(fast_food)], ch[int(exercise)], ch[int(mood_swing)],
                        ch[int(mentrual_regularity)], int(duration), blood_group[int(blood_grp)]]
            
            my_instance = userHistory(
                user=request.user,
                test_type='PCOS Test',
                symptoms=json.dumps(symp),  # Convert list to JSON string
                result=prediction_result,  # Set result as needed
                date=timezone.now()  # Set current date and time
            )
            my_instance.save()

            return render(request, 'pcos.html', {'age': age, 'height': user_data.height, 'weight': user_data.weight,  'form': form, 'prediction_result': prediction_result, 'user_name': request.user.first_name + " " + request.user.last_name})
    else:
        form = pcosDisorderForm()
    return render(request, 'pcos.html', {'age': age, 'height': user_data.height, 'weight': user_data.weight, 'form': form, 'user_name': request.user.first_name + " " + request.user.last_name})


@login_required
def report(request):
    user_data = userHistory.objects.last()
    
    user_info = {}
    user_info['test_type'] = user_data.test_type
    user_info['result'] = user_data.result
    user_info['date'] = user_data.date
    
    user_profile = UserProfile.objects.get(user=user_data.user)

    user_info['dob']= user_profile.dob
    user_info['gender'] = user_profile.gender
    user_info['height'] = user_profile.height
    user_info['weight'] = user_profile.weight
    user_info['profession'] = user_profile.profession
    
    given_list = user_data.get_symptoms()
    
    if user_data.test_type == 'Mental Disorder Test':
        attributes = mental_disorder_df.columns[1:]
    
    elif user_data.test_type == 'PCOS Test':
        attributes = ['Period Frequency', 'Gained Weight', 'Excessive body/facial hair growth',
                    'Noticed skin darkening', 'Hair Loss/ Hair Thinning/ Baldness', 'Pimples/Acne',
                    'Fast Food Consumption', 'Exercise Regularity', 'Mood Swings', 'Menstrual Regularity',
                    'Duration of Menstrual Periods', 'Blood Group']
    
    elif user_data.test_type == 'Obesity Test':
        attributes = ['Activity Level (1-4)']
    
    attributes_values = {}
    for i in range(len(given_list)):
        attributes_values[attributes[i]] = given_list[i]
    
    if user_data.test_type == 'Mental Disorder Test':
        advice = {
            'Bipolar Type-2': "A comprehensive treatment plan combining mood stabilizers, therapy, and lifestyle adjustments is key to managing the cyclical nature of bipolar type-2 disorder. Regular monitoring and open communication with healthcare providers are essential for maintaining stability.",
            "Depression": "Effective treatment for depression often involves a combination of therapy and medication tailored to individual needs. Engaging in regular physical activity, maintaining a healthy lifestyle, and seeking support from loved ones can also play a crucial role in managing symptoms.",
            "Bipolar Type-1": "Treatment for bipolar type-1 typically involves mood stabilizers, antipsychotic medications, and psychotherapy. Developing coping strategies, adhering to medication regimens, and fostering a strong support network are vital for stabilizing mood swings and preventing relapses.",
            "Normal": "For individuals experiencing normal fluctuations in mood, maintaining a balanced lifestyle, practicing stress management techniques, and prioritizing self-care activities such as adequate sleep, healthy eating, and regular exercise can contribute to overall well-being and resilience."
        }
    
    elif user_data.test_type == 'PCOS Test':
        advice = {'PCOS Positive': "Implement healthy habits like balanced eating, regular exercise, and stress management to alleviate symptoms and improve overall well-being.",
                'PCOS Negative': "Maintain a balanced lifestyle including nutritious eating and regular exercise to support overall health and potentially reduce the risk of developing PCOS-related symptoms."}
    
    elif user_data.test_type == 'Obesity Test':
        advice = {
            'Normal weight': 'Maintain your healthy lifestyle habits, including balanced nutrition and regular exercise, to support overall well-being.',
            'Obese': 'Seek professional guidance to develop a personalized weight management plan focusing on sustainable changes in diet and physical activity.',
            'Overweight': 'Implement small, gradual changes such as portion control and incorporating more fruits and vegetables into your diet to achieve a healthier weight.',
            'Underweight': 'Consult with a healthcare provider to identify potential underlying causes and develop a nutrition plan to reach and maintain a healthy weight.'
        }
    
    user_info['advice'] = advice[user_data.result]
    
    return render(request, 'report.html', {'user_info': user_info, 'attributes_values': attributes_values, 'user_name': request.user.first_name + " " + request.user.last_name})


@login_required
def test_history(request):
    user_medical_history = userHistory.objects.filter(user=request.user)
    return render(request, 'test_history.html', {'user_name': request.user.first_name + " " + request.user.last_name,
                                                'user_medical_history': user_medical_history})

@login_required
def download_receipt(request):
    receipt = Receipt.objects.get(user=request.user)
    # Logic to generate/download receipt file
    return redirect('dashboard')  # Redirect to dashboard or any other page

@login_required
def appointment_success(request):
    return render(request, 'appointment_success.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html')

