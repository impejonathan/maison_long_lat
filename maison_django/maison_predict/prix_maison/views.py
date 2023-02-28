from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import HousePredictionForm
# from .models import HousePricePrediction
import joblib
import pandas

def index(request):
    """
    Affiche la page d'accueil.
    """
    return render(request, 'prix_maison/index.html')

def formulaire(request):
    """
    Gère le formulaire de prédiction de prix de maison.
    """
    if request.method == 'POST':
        form = HousePredictionForm(request.POST)
        if form.is_valid():
            # Récupère les données du formulaire
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            sqft_living = form.cleaned_data['sqft_living']
            sqft_lot = form.cleaned_data['sqft_lot']
            floors = form.cleaned_data['floors']
            waterfront = form.cleaned_data['waterfront']
            view = form.cleaned_data['view']
            grade = form.cleaned_data['grade']
            sqft_basement = form.cleaned_data['sqft_basement']
            yr_renovated = form.cleaned_data['yr_renovated']
            # zipcode = form.cleaned_data['zipcode']
            lat = form.cleaned_data['lat']
            long = form.cleaned_data['long']

            # Effectue la prédiction
            model = joblib.load('prix_maison/models/knn_model_maison.pkl')
            data = pandas.DataFrame({
                'bedrooms': [bedrooms],
                'bathrooms': [bathrooms],
                'sqft_living': [sqft_living],
                'sqft_lot': [sqft_lot],
                'floors': [floors],
                'waterfront': [waterfront],
                'view': [view],
                'grade': [grade],
                'sqft_basement': [sqft_basement],
                'yr_renovated': [yr_renovated],
                # 'zipcode': [zipcode],
                'lat': [lat],
                'long': [long],
            })
            predicted_price = model.predict(data)[0]
                        

            # Affiche la page de résultat avec la prédiction
            return render(request, 'prix_maison/prediction_result.html', {'predicted_price': predicted_price})
    else:
        form = HousePredictionForm()
    
    # Render the prediction form
    return render(request, 'prix_maison/predict_price.html', {'form': form})


# def prediction_result(request, prediction_id):
#     prediction = get_object_or_404(HousePricePrediction, id=prediction_id)
#     context = {'predicted_price': prediction.predicted_price}
#     return render(request, 'prix_maison/prediction_result.html', context)



# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from .forms import HousePredictionForm
# from .models import HousePricePrediction
# import joblib
# import pandas as pd


# def index(request):
#     """
#     Affiche la page d'accueil.
#     """
#     return render(request, 'prix_maison/index.html')


# def formulaire(request):
#     """
#     Gère le formulaire de prédiction de prix de maison.
#     """
#     if request.method == 'POST':
#         form = HousePredictionForm(request.POST)
#         if form.is_valid():
#             # Récupère les données du formulaire
#             bedrooms = form.cleaned_data['bedrooms']
#             bathrooms = form.cleaned_data['bathrooms']
#             sqft_living = form.cleaned_data['sqft_living']
#             sqft_lot = form.cleaned_data['sqft_lot']
#             floors = form.cleaned_data['floors']
#             waterfront = form.cleaned_data['waterfront']
#             view = form.cleaned_data['view']
#             grade = form.cleaned_data['grade']
#             sqft_basement = form.cleaned_data['sqft_basement']
#             yr_renovated = form.cleaned_data['yr_renovated']
#             # zipcode = form.cleaned_data['zipcode']
#             lat = form.cleaned_data['lat']
#             long = form.cleaned_data['long']

#             # Chargement du fichier de mapping pour les codes postaux
#             zip_map = pd.read_csv("prix_maison/data/zip_code_map.csv")
#             zip_map = zip_map.astype({"zip_code": str, "zip_code_map": str})
#             zip_map = zip_map.set_index("zip_code")

#             # Transformation du code postal entré en code postal normalisé
#             try:
#                 zipcode = zip_map.loc[zipcode]["ZipCodeType"]
#             except KeyError:
#                 pass

#             # Effectue la prédiction
#             model = joblib.load('prix_maison/models/knn_model_maison.pkl')
#             predicted_price = model.predict([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, grade, sqft_basement, yr_renovated, zipcode]])[0]  #, lat, long

#             # Enregistre la prédiction dans la base de données
#             prediction = HousePricePrediction.objects.create(
#                 bedrooms=bedrooms, 
#                 bathrooms=bathrooms, 
#                 sqft_living=sqft_living,
#                 sqft_lot=sqft_lot, 
#                 floors=floors, 
#                 waterfront=waterfront,
#                 view=view, 
#                 grade=grade, 
#                 sqft_basement=sqft_basement,
#                 yr_renovated=yr_renovated,
#                 # zipcode=zipcode, 
#                 lat=lat, 
#                 long=long,
#                 predicted_price=predicted_price
#             )

#             # Affiche la page de résultat avec la prédiction
#             return render(request, 'prix_maison/prediction_result.html', {'predicted_price': predicted_price})
#     else:
#         form = HousePredictionForm()
    
#     # Render the prediction form
#     return render(request, 'prix_maison/predict_price.html', {'form': form})


# def prediction_result(request, prediction_id):
#     prediction = get_object_or_404(HousePricePrediction, id=prediction_id)
#     context = {'predicted_price': prediction.predicted_price}
#     return render(request, 'prix_maison/prediction_result.html', context)
