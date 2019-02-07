from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    #los request normalmente se hacen mediante peticiones GET, pero en formularios por ejemplo, se hace con peticiones POST (ocultas)
    print("Tipo de peticion: {}".format(request.method))
    #sacaremos la plantilla vacia a la web con un request GET usual(ya que sera la primera llamada a contact)
    contact_form = ContactForm()
    #una vez hayamos dado al boton enviar el request será tipo POST y entraremos al IF para procesarla
    if request.method == "POST":
        #rellenaremos de nuevo el formulario para que nos aparezca impreso en la pagina web por si ha habido algun error al introducir datos
        #y no tengamos que introducirlos todos de nuevo
        contact_form = ContactForm(data=request.POST)
        #validamos si todos los datos son correctos, en este caso:
        #que todos los campos esten rellenados y que el email sea correcto
        if contact_form.is_valid():
            #si todo es correcto guardamos todos los datos almacenados en las siguientes variables
            #si no hay ningun valor que nos devuelva una cadena vacia ''
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #suponemos que todo ha ido bien, redireccionamos
            #enviamos el correo y redireccionamos
            email = EmailMessage(
                "La caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["rafelquetglascoll@gmail.com"],
                reply_to=[email],
            )

            try:
                #enviamos el e-mail
                email.send()
                #todo ha ido bien todo OK
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien, intentalo mas tarde
                return redirect(reverse('contact')+"?fail")
            

    return render(request, "contact/contact.html", {'form':contact_form})