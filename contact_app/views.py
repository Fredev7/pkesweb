from django.shortcuts import redirect, render

from .forms import ContactForm

from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    Contact_Form=ContactForm()

    if request.method=="POST":
        Contact_Form=ContactForm(data=request.POST)
        if Contact_Form.is_valid():
            name=request.POST.get("name")  #revisar name y message
            email=request.POST.get("email")
            message=request.POST.get("message") 


            email=EmailMessage("Mensaje desde App Django",
            "El Cliente con nombre {} y direccion de correo {} dice\n\n {}".format(name,email,message),
            "",["pequesctg@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contact/?valido") 
            except: 
                return redirect("/contact/?novalido")


    return render(request, 'contact.html', {'myForm':Contact_Form})

