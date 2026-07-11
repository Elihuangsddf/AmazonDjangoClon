from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage
from django.conf import settings

def contacto(request):
    formularioContacto = formularioContacto()

    if request.method == "POST":
        form = formularioContacto(data=request.POST)

        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            emailRemitente = form.cleaned_data["correo"]
            contenido = form.cleaned_data["contenido"]

            asunto = "Mensaje enviado desde contacto"
            cuerpo = (
                f"El usuario con nombre {nombre}, "
                f"con la dirección de correo {emailRemitente}, "
                f"escribe lo siguiente:\n\n{contenido}"
            )

            email = EmailMessage(
                asunto,
                cuerpo,
                settings.DEFAULT_FROM_EMAIL,
                ["elihuangeles6@gmail.com"],
                reply_to=[emailRemitente]
            )

            try:
                email.send()

                return redirect("/Contacto/?valido")

            except Exception as e:
                print(f"Error al enviar correo: {e}")

                return redirect("/Contacto/?novalido")

        else:
            return render(request, "Contacto/Contacto.html", {'formulario': form})

    return render(request, "Contacto/Contacto.html", {'formulario': formularioContacto})