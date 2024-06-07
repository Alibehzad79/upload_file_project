from django import forms


class UploadForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"},
        ),
        label="Title",
        required=True,
        max_length=50,
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={"class": "form-control"},
        ),
        label="Image",
        required=True,
    )

    file = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control"}),
        label="File",
        required=True
    )


    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image.size / 1000 > 50:   # convert byte to KB
            raise forms.ValidationError("Image size most be < 50 KB") 
        
        # You can change image name with 'image.name = "example name"' :) and good by

        return image