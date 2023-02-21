from django import forms


class SumDoubleForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


class Diff21Form(forms.Form):
    a = forms.IntegerField()


class SleepInForm(forms.Form):
    Weekday = forms.BooleanField(required=False)
    Vacation = forms.BooleanField(required=False)


class Left2Form(forms.Form):
    str = forms.CharField(max_length=40, label="String")


class CountHiForm(forms.Form):
    str = forms.CharField(max_length=100, label="Word/Phrase/String of letters")


class StringMatchForm(forms.Form):
    a = forms.CharField(max_length=100, label="First String")
    b = forms.CharField(max_length=100, label="Second String")


class RoundSumForm(forms.Form):
    a = forms.IntegerField(label="First Number")
    b = forms.IntegerField(label="Second Number")
    c = forms.IntegerField(label="Third Number")
