from django import forms
from app2.models import *

class ReligionForm(forms.ModelForm):
    class Meta:
        model = Religion
        fields = "__all__"

class CasteForm(forms.ModelForm):
    class Meta:
        model = Caste
        fields = "__all__"

class SuplHeadForm(forms.ModelForm):
    class Meta:
        model = SuplHead
        fields = "__all__"

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = "__all__"

class DesignatureForm(forms.ModelForm):
    class Meta:
        model = Designature
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class TypeTranForm(forms.ModelForm):
    class Meta:
        model = TypeTran
        fields = "__all__"

class MainDeptForm(forms.ModelForm):
    class Meta:
        model = MainDept
        fields = "__all__"

class MainDesignation(forms.ModelForm):
    class Meta:
        model = MainDesignation
        fields = "__all__"

class Staff(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

class Scale(forms.ModelForm):
    class Meta:
        model = Scale
        fields = "__all__"






#crud operations

class EmployeeInformationForm(forms.ModelForm):
    class Meta:
        model = EmployeeInformation
        fields = "__all__"

 
        widgets = {
            'INCREMENT_DATE': forms.DateInput(attrs={'type': 'date'}),
            'DATE_OF_BIRTH': forms.DateInput(attrs={'type': 'date'}),
            'DATE_OF_JOINING': forms.DateInput(attrs={'type': 'date'}),
            'DATE_OF_RETIREMENT': forms.DateInput(attrs={'type': 'date'}),
            'TA':forms.RadioSelect,
            'PT':forms.RadioSelect,
            'QUARTER':forms.RadioSelect,
            'RENT_FREE':forms.RadioSelect,
            'HANDICAP':forms.RadioSelect,
            'SENIOR_CITIZEN':forms.RadioSelect,
            'PAY_STATUS':forms.RadioSelect,
            'GENDER': forms.Select(attrs={'size': '1'}),
            'TITLE':forms.Select(attrs={'size': '1'}),
            'DESIGNATION':forms.Select(attrs={'size': '1'}),
            'DEPARTMENT':forms.Select(attrs={'size': '1'}),
            'STAFF_TYPE':forms.Select(attrs={'size': '1'}),
            'APPOINTMENT':forms.Select(attrs={'size': '1'}),
            'VACATIONAL':forms.Select(attrs={'size': '1'}),
            'BANK_NAME':forms.Select(attrs={'size': '1'}),
            'UNDER':forms.Select(attrs={'size': '1'}),
            'LEVEL':forms.Select(attrs={'size': '1'}),
            'RULE':forms.Select(attrs={'size': '1'})
        }