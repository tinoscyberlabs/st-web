from django import forms
from .models import Event_Details_Model,Event_Registration,MinistriesModel,Daily_Mass,Special_Masses,Obituary_Model,Gallery_Model,Blog_Model,Blog_News_Model



class Event_Details_Form(forms.ModelForm):
    class Meta:
        model = Event_Details_Model
        fields =  '__all__'

class MinistriesForm(forms.ModelForm):
    class Meta:
        model = MinistriesModel
        fields = '__all__'


class Daily_Mass_Form(forms.ModelForm):
    class Meta:
        model = Daily_Mass
        fields = '__all__'

class Special_Masses_Form(forms.ModelForm):
    class Meta:
        model = Special_Masses
        fields = '__all__'

class Obituary_Form(forms.ModelForm):
    class Meta:
        model = Obituary_Model
        fields = '__all__'

class Gallery_Form(forms.ModelForm):
    class Meta:
        model = Gallery_Model
        fields = '__all__'

class Blog_Form(forms.ModelForm):
    class Meta:
        model = Blog_Model
        fields = '__all__'

class Blog_News_Form(forms.ModelForm):
    class Meta:
        model = Blog_News_Model
        fields = '__all__'

class Event_Registration_form(forms.ModelForm):
    class Meta:
        model = Event_Registration
        fields =  '__all__'