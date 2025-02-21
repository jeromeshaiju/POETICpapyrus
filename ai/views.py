import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import ailogic  

def firstview(request):
    return render(request, 'ai/first.html')

def process_input_view(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        
        # Save the uploaded file to the media directory
        fs = FileSystemStorage()
        file_path = fs.save(pdf_file.name, pdf_file)
        
        # Construct the full file path within MEDIA_ROOT
        full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        
        # Process the uploaded PDF file
        ai_response = ailogic.process_input_with_pdf(full_file_path)
        
        # Delete the uploaded file from the media directory
        fs.delete(file_path)
        
        return render(request, 'ai/first.html', {'ai_response': ai_response})
    
    return render(request, 'ai/first.html')