from django import forms
from home.models import Group, GroupHasAccount, GroupBelongCategory, Category
class CreateGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('userName', None)
        super().__init__(*args, **kwargs)
    class Meta:
        model = Group
        fields = ['name', 'description', 'image'] 
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    def save(self):
        new_group = Group.objects.create(name=self.cleaned_data['name'], description=self.cleaned_data['description'], image = self.cleaned_data['image'])
        print('forms: ',  self.cleaned_data['image'])
        GroupBelongCategory.objects.create(categoryName=self.cleaned_data['category'], groupId_id=new_group.id)
        GroupHasAccount.objects.create(groupId_id=new_group.id, isAdmin=True, userName_id = self.author)