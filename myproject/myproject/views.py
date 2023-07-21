from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'index.html')
def tailwind(request):
    return render(request, 'tailwind.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to a file
        with open('data.txt', 'a') as file:
            file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")

        # Send email
        # subject = 'Feedback from Contact Us Form'
        # message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        # from_email = 'your-email@example.com'  # Replace with your email address
        # to_email = 'neerajgupta5963@gmail.com'  # Replace with your email address

        # send_mail(subject, message, from_email, [to_email])

        message = "Success! Your feedback has been received. We will reply shortly!"
        data = {
            'name': name,
            'email': email,
            'message': message
        }
    else:
        data = {}

    return render(request, 'contactus.html', data)

def aboutus(request):
    return render(request, 'aboutus.html')

#def search(request):
    #return render(request, 'index.html')
#def poem_detail(request):
    #return render(request, 'poem_detail.html')