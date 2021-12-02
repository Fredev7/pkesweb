from django.shortcuts import redirect, render

from .forms import ContactForm

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    Contact_Form=ContactForm()

    if request.method=="POST":
        Contact_Form=ContactForm(data=request.POST)
        if Contact_Form.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido") 


            email=EmailMessage("Mensaje desde App Django",
            "El Cliente con nombre {} y direccion de correo {} dice\n\n {}".format(nombre,email,contenido),
            "",["pequesctg@gmail.com"], reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido") 
            except: 
                return redirect("/contacto/?novalido")


    return render(request, 'contacto.html', {'myForm':Contact_Form})

