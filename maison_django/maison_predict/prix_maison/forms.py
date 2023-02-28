from django import forms

class HousePredictionForm(forms.Form):
    BEDROOM_CHOICES = [(i, str(i)) for i in range(0, 16)]
    bedrooms = forms.ChoiceField(label="Nombre de chambres", choices=BEDROOM_CHOICES, 
                                 error_messages={'required': "Veuillez indiquer le nombre de chambres"})
    
    BATHROOM_CHOICES = [(i, str(i)) for i in range(0, 16)]
    bathrooms = forms.ChoiceField(label="Nombre de salles de bain", choices=BATHROOM_CHOICES, 
                                  error_messages={'required': "Veuillez indiquer le nombre de salles de bain"})
    
    sqft_living = forms.IntegerField(label="Surface à vivre (en pieds carrés)" ,initial=0)
    
    sqft_lot = forms.IntegerField(label="Surface du terrain (en pieds carrés)" ,initial=0)
    
    FLOOR_CHOICES = (
        (0.0, '0.0'), (0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'), (3, '3'), (3.5, '3.5'), (4, '4')
    )

    floors = forms.ChoiceField(label="Nombre d'étages", choices=FLOOR_CHOICES, error_messages={'required': "Veuillez indiquer le nombre d'étages"})

    
    waterfront = forms.BooleanField(label="Vue sur le lac", required=False)
        
    VIEW_CHOICES = [(i, str(i)) for i in range(5)]
    view = forms.ChoiceField(label="Qualité de la vue (de 0 à 4)", choices=VIEW_CHOICES, initial=0, 
                            error_messages={'required': "Veuillez indiquer la qualité de la vue"})

    GRADE_CHOICES = [(i, str(i)) for i in range(14)]
    grade = forms.ChoiceField(label="Qualité de la construction (de 0 à 13)", choices=GRADE_CHOICES, initial=0, 
                            error_messages={'required': "Veuillez indiquer la qualité de la construction"})

    
    sqft_basement = forms.IntegerField(label="Surface du sous-sol (en pieds carrés)", min_value=0, required=False, initial=0,)
    
    yr_renovated = forms.IntegerField(label="Années depuis la rénovation ou la construction", required=False, initial=0,)
    
    # zipcode = forms.CharField(max_length=5, label="Code postal",
    #                           error_messages={'required': "Veuillez indiquer le code postal",
    #                                           'max_length': "Le code postal doit comporter exactement 5 caractères"})
    
    lat = forms.DecimalField(label="Latitude", max_digits=10, decimal_places=6, initial=0,)
    long = forms.DecimalField(label="Longitude", max_digits=10, decimal_places=6, initial=0,)
