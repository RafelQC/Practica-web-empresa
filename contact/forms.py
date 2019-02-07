from django import forms

class ContactForm(forms.Form):
    #el campo required se tiene que poner en todos los campos para especificar si es un campo obligatorio o no
    #widget=forms.TextInput(attrs={'class':'form-control'} damos una configuración con bootstrap a la casilla para que se vea mejor
    name = forms.CharField(label="Nombre", required = True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribre tu nombre'}), min_length = 3, max_length=100)
    email = forms.EmailField(label="E-mail", required = True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Escribre tu e-mail'}), min_length = 3, max_length=100)
    #la diferencia con el pandel de administrador es que en un texto largo tambien utilitzamos un Charfield
    #widget=forms.Textarea hace que la casilla rellenable sea mucho más grande al ser un campo para mucho contenido
    content = forms.CharField(label="Contenido", required = True, widget=forms.Textarea(attrs={'class':'form-control','rows':4, 'placeholder':'Escribre tu comentario'}), min_length = 10, max_length=1000)