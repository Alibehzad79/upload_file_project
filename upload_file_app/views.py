from django.shortcuts import render, redirect
from django.contrib import messages
from upload_file_app.models import Upload
from upload_file_app.forms import UploadForm

# Create your views here.

def upload_view(request):
    template_name = "index.html"
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            image = form.cleaned_data.get("image")
            file = form.cleaned_data.get("file")

            # print upload size's
            print(f"Image size: {image.size / 1000} KB \n Image Name: {image.name}")
            print(f"File size: {image.size / 1000} KB \n File Name: {file.name}")
            ###############

            new_upload = Upload.objects.create(title=title, image=image, file=file)
            if new_upload is not None:
                new_upload.save()
                messages.add_message(request, messages.SUCCESS, message="Uploaded successfuly.")
                return redirect("/")
            else:
                form.add_error("file", "somthing wraong! please try again.")
    else:
        form = UploadForm()
    context = {
        'form': form
    }

    return render(request, template_name, context)