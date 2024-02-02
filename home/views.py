from django.http import JsonResponse
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    return text

def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_path = uploaded_image.image.path
            extracted_text = extract_text_from_image(image_path)

            # Delete the image file after processing
            os.remove(image_path)

            # Check if the request is AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Handle AJAX request; return JSON response
                return JsonResponse({'status': 'success', 'message': 'Image uploaded successfully', 'extracted_text': extracted_text})

            # For regular form submissions, render template with context
            return render(request, 'home/index.html', {
                'form': form,
                'extracted_text': extracted_text
            })

        # If form is invalid and request is AJAX, return error as JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Form is not valid'}, status=400)

    else:
        form = ImageUploadForm()

    return render(request, 'home/index.html', {'form': form})
