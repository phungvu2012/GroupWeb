from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm
from home.models import Account
from django.forms import ModelForm
from django.contrib.auth import views as auth_views

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': ' Fist Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': ' Last Name'}),
        }
    CHOICES = [(True, 'Male'), (False, 'Female')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    dateOfBirth = forms.DateField(widget=DateInput)
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
        avatarUserDefault = 'female.png'
        coverPhotoDefault = 'gray_background.jpg'
        if self.cleaned_data['gender']:
            avatarUserDefault = '/male.jpg'
        
        newUser = User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'])
        Account.objects.create(user = newUser, gender=self.cleaned_data['gender'], dateOfBirth=self.cleaned_data['dateOfBirth'], avatar=avatarUserDefault, coverPhoto=coverPhotoDefault)






















# class RegistrationForm(forms.Form):
    # username = forms.CharField(label='Tài khoản', max_length=30)
    # email = forms.EmailField(label='Email')
    # password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    # password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    # def clean_password2(self):
    #     if 'password1' in self.cleaned_data:
    #         password1 = self.cleaned_data['password1']
    #         password2 = self.cleaned_data['password2']
    #         if password1 == password2 and password1:
    #             return password2
    #     raise forms.ValidationError("Mật khẩu không hợp lệ")

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.match(r'^\w+$', username):
    #         raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
    #     try:
    #         User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         return username
    #     raise forms.ValidationError("Tài khoản đã tồn tại")
    # def save(self):
    #     User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])

# class ProfileForm(forms.ModelForm):
#         gender = forms.BooleanField(label='isMale')
#         dateOfBirth = forms.DateField(label='Sinh nhật')
#         hobby = forms.Textarea()
#         avatar = forms.ImageField()
#         coverPhoto = forms.ImageField()

#         def clean_password2(self):
#             if 'dateOfBirth' in self.cleaned_data:
#                 return 1
#             raise forms.ValidationError("Mật khẩu không hợp lệ")

#         def save(self):
#             Account.objects.create(gender=self.cleaned_data['gender'], dateOfBirth=self.cleaned_data['dateOfBirth'], hobby=self.cleaned_data['hobby'], avatar=self.cleaned_data['avatar'], hobby=self.cleaned_data['hobby'])

# class ExtendedUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=45)
#     last_name = forms.CharField(max_length=150)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name', "password1", "password2")
#     def save(self., commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data["email"]
#         user.first_name = self.cleaned_data["first_name"]
#         user.last_name = self.cleaned_data["last_name"]
#         if commit:
#             user.save()
#         return user

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ('gender', 'dateOfBirth', 'hobby', 'avatar', 'coverPhoto')
