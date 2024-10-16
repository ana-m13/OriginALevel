# from django.forms import ModelForm
from cProfile import label
from django import forms
from OriginALevel_app.models import OriginALevel_PostModel, OriginALevel_ReplyModel
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = OriginALevel_PostModel
        fields = ["title", "body"]

    title = forms.CharField(max_length=250, widget=forms.TextInput, required=False)
    body = forms.CharField(widget=forms.Textarea, required=True)
    # ratings = forms.IntegerField(widget=forms.NumberInput, required=False)
    # tags = forms.CharField(widget=forms.TextInput, required=False)
    title.widget.attrs['placeholder'] = 'Title'
    body.widget.attrs['placeholder'] = 'Body'




class ReplyForm(forms.ModelForm):
    class Meta:
        model = OriginALevel_ReplyModel
        fields = ["body"]
    body = forms.CharField(widget=forms.Textarea, required=True)
    # ratings = forms.IntegerField(widget=forms.NumberInput, required=False)
    # tags = forms.CharField(widget=forms.TextInput, required=False)

    body.widget.attrs['placeholder'] = 'reply text'













# # from django.forms import ModelForm
# from cProfile import label
# from django import forms
# from OriginALevel_app.models import OriginALevel_PostModel
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = OriginALevel_PostModel
#         title = forms.TextInput()
#         body = forms.TextInput()
#         fields = [
#                 'title',
#                 'body',
#                 'rating',
#                 'tags',
#                 ] 
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
#             'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'body'}),
#             'rating': forms.NumberInput(attrs={'class': 'form-control'}),
#             'tags': forms.TextInput(attrs={'class': 'form-control'}),
#         }

#         labels = {
#             'title': '',
#             'body': '',
#             'rating': '',
#             'tags': '',
#         }





