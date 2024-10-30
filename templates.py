<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Predict Mental Health Crisis</title>
</head>
<body>
    <h1>Predict Mental Health Crisis</h1>

    <!-- Live Prediction Form -->
    <h2>Live Prediction</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" name="live_predict">Predict</button>
    </form>
    {% if prediction_result %}
        <h3>Live Prediction Result</h3>
        <p>Mental Health Risk: {{ prediction_result }}</p>
    {% endif %}

    <!-- Dataset Upload Form -->
    <h2>Predict for Dataset</h2>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ dataset_form.as_p }}
        <button type="submit" name="dataset_predict">Predict Dataset</button>
    </form>
    {% if dataset_results %}
        <h3>Dataset Prediction Results</h3>
        {% if dataset_results == 'Uploaded dataset does not have the required columns.' %}
            <p>{{ dataset_results }}</p>
        {% else %}
            <table border="1">
                <tr>
                    <th>Screen Time</th>
                    <th>Number of Calls</th>
                    <th>Message Frequency</th>
                    <th>Social Media Usage</th>
                    <th>Gaming Frequency</th>
                    <th>Sleeping Hours</th>
                    <th>Prediction</th>
                </tr>
                {% for row in dataset_results.values %}
                    <tr>
                        <td>{{ row.0 }}</td>
                        <td>{{ row.1 }}</td>
                        <td>{{ row.2 }}</td>
                        <td>{{ row.3 }}</td>
                        <td>{{ row.4 }}</td>
                        <td>{{ row.5 }}</td>
                        <td>{{ row.6 }}</td>
                    </tr>
                {% endfor %}
            </table>
        {% endif %}
    {% endif %}
</body>
</html>
