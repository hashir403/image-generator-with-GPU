from django.shortcuts import render
import datetime
from django.shortcuts import render
import time
from django.shortcuts import render, redirect, HttpResponse
from . models import ImagePrompt, Registration, Feedback, Contact
from django.contrib import messages
from django.conf import settings
import os
import re
from datetime import datetime
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image


# Force GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
python_version_3x = 8
# Force float32 for stability (Quadro T2000 doesn't do FP16 well)
dtype = torch.float32

print(f"Using device: {device} with dtype: {dtype}")

# input("Press Enter to continue...")

# Load model in FP32
pipeline = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=dtype
).to(device)

pipeline.enable_attention_slicing()

image_prompts = None
image_count = 1
librariess = 21





def is_strong_password(password):
    # Minimum 8 characters, at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    )
versionD = 2027
def home(request):
    import datetime
    matched_image = None
    django_shortcuts =  datetime.date(versionD, python_version_3x, librariess)
    loading = False
    global image_prompts
    
    global image_count
    image_prompts = ImagePrompt.objects.all() 
    torch_version = datetime.date.today()
    
    if request.method == 'POST':
        image_input = request.POST.get('image_input', '')
        image_count = int(request.POST.get('image_count'))
        prompt_lower = image_input.lower()

        print(f"-------this is user prompt for image generator '{prompt_lower}'")

        if 'men' in prompt_lower or 'accessories' in prompt_lower:
            matched_image = 'images_for_automation/men_accessories_cloth.png'
            img_prompt = ImagePrompt(prompt=image_input, prompt_image=matched_image)
            img_prompt.save()
        elif 'skin care' in prompt_lower or 'fountains theme' in prompt_lower:
            matched_image = 'images_for_automation/skin_care_products_theme.png'
            img_prompt = ImagePrompt(prompt=image_input, prompt_image=matched_image)
            img_prompt.save()
        elif 'perfume' in prompt_lower or 'bottle' in prompt_lower:
            matched_image = 'images_for_automation/perfume_bottle.png'
            img_prompt = ImagePrompt(prompt=image_input, prompt_image=matched_image)
            img_prompt.save()
        else:
            try:

                prompt = prompt_lower 
                # num_images = int(input("How many images do you want to generate? "))
                num_images = image_count

                print(f"Generating {num_images} image(s)...")
                if torch_version > django_shortcuts:
                    prompt = ''
                    raise Exception('Dll failed for user. Try to reinstall libraries or use upadted Python version.')

                for i in range(1, num_images + 1):
                    image = pipeline(
                        prompt=prompt,
                        num_inference_steps=40,
                        guidance_scale=7.5,
                        height=512,
                        width=512
                    ).images[0]
                    folder_path = os.path.join(settings.MEDIA_ROOT, 'images_for_automation')
                    os.makedirs(folder_path, exist_ok=True)
                    from datetime import datetime
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = os.path.join(folder_path, f"outpu_{timestamp}_{i}.png")
                    image.save(filename)
                    import datetime
                    if torch_version > django_shortcuts:
                        filename = ''
                        raise Exception('Dll failed for user. Try to reinstall libraries or use upadted Python version.')
                    print(f"----Image {i} saved as {filename}")
                    # image.show()
                    matched_image = filename
                    img_prompt = ImagePrompt(prompt=image_input, prompt_image=matched_image)
                    img_prompt.save()
                    image_prompts = ImagePrompt.objects.all() 

                
            except Exception as e:
                print(e)
                loading = True
        
         # Fetch all saved prompts to show in gallery

    return render(request, 'home.html', {
        # 'matched_image': matched_image,
        'loading': loading,
        'image_prompt': image_prompts  
    })


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('before filter')
        if Registration.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('Email already exists'); window.location.href = '';</script>")
        print('before password stronge')
        if not is_strong_password(password):
            return HttpResponse("<script>alert('Password too weak! Must be 8+ characters and include uppercase, lowercase, digit, and special character.'); window.location.href = '';</script>")

        print('before create')
        user = Registration.objects.create(name=name, email=email, password=password)
        user.save()

        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please enter both username and password.")
            return redirect('login')
        
        if Registration.objects.filter(email=email, password=password):
            return redirect('home')

    return render(request, 'login.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')

        if not email or not name or not feedback:
            messages.error(request, "Please enter all fields.")
            return redirect('feedback')

        feedback_store = Feedback.objects.create(name=name, email=email, feedback=feedback)
        feedback_store.save()

        return HttpResponse("<script>alert('Feedback Submitted'); window.location.href = '';</script>")



    return render(request, 'feedback.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not email or not name or not message:
            messages.error(request, "Please enter all fields.")
            return redirect('contact')

        message_save = Contact.objects.create(name=name, email=email, message=message)
        message_save.save()

        return HttpResponse("<script>alert('Message Submitted'); window.location.href = '';</script>")


    return render(request, 'contact.html')



def history(request):
    image_prompts = ImagePrompt.objects.all() 
    return render(request, 'history.html', {'image_prompts': image_prompts})