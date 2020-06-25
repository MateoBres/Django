from django import forms


class FormularioRemeras(forms.Form):
  marca = forms.CharField(label="Marca", max_length=30)
  TALLE = (
    (1, "XS"),
    (2, "S"),
    (3, "M"),
    (4, "L"),
    (5, "XL"),
    (6, "XXL")
  )
  talle = forms.ChoiceField(label = "Talle", choices = TALLE)
  color = forms.CharField(label="Color", max_length=30)
  lisa = forms.BooleanField(label = "Lisa", required = False)
  GENERO = (
    (1, "Hombre"),
    (2, "Mujer"),
    (3, "Unisex")
  )
  genero = forms.ChoiceField(label = "Genero", choices = GENERO)
