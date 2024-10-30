from django import forms

class PredictionForm(forms.Form):
    screen_time = forms.FloatField(label='Screen Time (hours)')
    num_calls = forms.IntegerField(label='Number of Calls')
    message_frequency = forms.IntegerField(label='Message Frequency')
    social_media_usage = forms.FloatField(label='Social Media Usage (hours)')
    gaming_frequency = forms.FloatField(label='Gaming Frequency (hours)')
    sleeping_hours = forms.FloatField(label='Sleeping Hours')

class DatasetUploadForm(forms.Form):
    file = forms.FileField(label='Upload CSV Dataset')
