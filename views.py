from django.shortcuts import render
from .forms import PredictionForm, DatasetUploadForm
import joblib
import numpy as np
import pandas as pd

# Load the model
model = joblib.load('path/to/mental_health_predictor_model.pkl')

def predict_view(request):
    prediction_result = None
    dataset_results = None
    if request.method == 'POST':
        # Handle live prediction form
        if 'live_predict' in request.POST:
            form = PredictionForm(request.POST)
            dataset_form = DatasetUploadForm()
            if form.is_valid():
                # Extract data from form
                screen_time = form.cleaned_data['screen_time']
                num_calls = form.cleaned_data['num_calls']
                message_frequency = form.cleaned_data['message_frequency']
                social_media_usage = form.cleaned_data['social_media_usage']
                gaming_frequency = form.cleaned_data['gaming_frequency']
                sleeping_hours = form.cleaned_data['sleeping_hours']
                
                # Prepare and predict
                input_data = np.array([[screen_time, num_calls, message_frequency, social_media_usage, gaming_frequency, sleeping_hours]])
                prediction_result = model.predict(input_data)[0]

        # Handle dataset prediction form
        elif 'dataset_predict' in request.POST:
            dataset_form = DatasetUploadForm(request.POST, request.FILES)
            form = PredictionForm()
            if dataset_form.is_valid():
                # Process uploaded dataset
                file = dataset_form.cleaned_data['file']
                dataset = pd.read_csv(file)
                
                # Ensure dataset has the required columns
                required_columns = {'screen_time', 'num_calls', 'message_frequency', 'social_media_usage', 'gaming_frequency', 'sleeping_hours'}
                if required_columns.issubset(dataset.columns):
                    X = dataset[list(required_columns)]
                    dataset['prediction'] = model.predict(X)
                    dataset_results = dataset[list(required_columns) + ['prediction']]
                else:
                    dataset_results = "Uploaded dataset does not have the required columns."

    else:
        form = PredictionForm()
        dataset_form = DatasetUploadForm()

    return render(request, 'predictor/predict.html', {
        'form': form,
        'dataset_form': dataset_form,
        'prediction_result': prediction_result,
        'dataset_results': dataset_results
    })
