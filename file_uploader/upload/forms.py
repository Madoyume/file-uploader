from django import forms
from .models import File

class ImageUploadForm(forms.Form):
    name = forms.CharField(max_length=100, \
        widget = forms.TextInput(attrs={'class':'form-control'}))
    file = forms.FileField()

    def save(self, commit=True):
        # アップロードされたファイルをバイナリデータに変換
        image_file = self.cleaned_data['file']
        instace = File(
            name=self.cleaned_data['name'],
            file=image_file.read()
        )
        instace.save()
        return instace