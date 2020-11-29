from django import forms
from home.models import Account
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class EditProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('userName', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']   

    CHOICES = [(True, 'Male'), (False, 'Female')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    dateOfBirth = forms.DateField(widget=DateInput)
    hobby = forms.CharField(widget=forms.Textarea, )

    def save(self, commit=False):
        editUser = self.author
        editUser.email = self.cleaned_data['email']
        editUser.first_name = self.cleaned_data['first_name'] 
        editUser.last_name = self.cleaned_data['last_name']
        editUser.save()

        accountUser = Account.objects.get(user=self.author)
        accountUser.gender = self.cleaned_data['gender']
        accountUser.dateOfBirth = self.cleaned_data['dateOfBirth']
        accountUser.hobby = self.cleaned_data['hobby']
        accountUser.save()

def clean_image(self):
    image = self.cleaned_data.get('', None) 
    if image:
        # do some validation, if it fails
        raise forms.ValidationError(u'Form error')
    return image

class EditAvatar(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('avatar', 'coverPhoto')

# class EditPassword(forms.Form):
#     def __init__(self, *args, **kwargs):
#         self.author = kwargs.pop('userPara', None)
#         super().__init__(*args, **kwargs)

#     passwordOld = forms.CharField(label='Mật khẩu cũ', widget=forms.PasswordInput())
#     password1 = forms.CharField(label='Mật khẩu mới', widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

#     def clean_checkPasswordOld(self):
#         if 'passwordOld' in self.cleaned_data:
#             passwordOld = self.cleaned_data['passwordOld']
#             password = self.author.password
#             print('passwordOld :', passwordOld)
#             print('password: ', password)
#             if passwordOld == password and passwordOld:
#                 return password
#                 # pass
#         raise forms.ValidationError("Mật khẩu cũ Không đúng")

#     def clean_password2(self):
#         print('hello')
#         if 'password1' in self.cleaned_data:
#             password1 = self.cleaned_data['password1']
#             password2 = self.cleaned_data['password2']
#             if password1 == password2 and password1:
#                 return password2
#         raise forms.ValidationError("Mật khẩu không hợp lệ")

#     def save(self):
#         editUser = self.author
#         print('password: ', editUser.password)
#         print('newpassword: ', self.cleaned_data['password1'])
#         editUser.password = self.cleaned_data['password1']
#         editUser.save()