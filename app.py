from flask import Flask, render_template, request, redirect
import numpy as np
import pickle

app = Flask(__name__)

locations = ['Whitefield', 'Sarjapur  Road', 'Electronic City', 'Haralur Road',
       'Marathahalli', 'Raja Rajeshwari Nagar', 'Bannerghatta Road',
       'Hennur Road', 'Uttarahalli', 'Thanisandra', 'Electronic City Phase II',
       'Hebbal', '7th Phase JP Nagar', 'Yelahanka', 'Kanakpura Road',
       'KR Puram', 'Sarjapur', 'Rajaji Nagar', 'Bellandur', 'Kasavanhalli',
       'Begur Road', 'Kothanur', 'Banashankari', 'Hormavu', 'Harlur',
       'Akshaya Nagar', 'Electronics City Phase 1', 'Jakkur', 'Varthur',
       'Chandapura', 'Hennur', 'Ramamurthy Nagar', 'HSR Layout',
       'Kaggadasapura', 'Ramagondanahalli', 'Kundalahalli', 'Koramangala',
       'Budigere', 'Hulimavu', 'Hoodi', 'Malleshwaram', 'Gottigere',
       'Hegde Nagar', 'JP Nagar', 'Yeshwanthpur', '8th Phase JP Nagar',
       'Bisuvanahalli', 'Channasandra', 'Indira Nagar', 'Vittasandra',
       'Kengeri', 'Old Airport Road', 'Brookefield', 'Vijayanagar',
       'Hosa Road', 'Sahakara Nagar', 'Bommasandra', 'Green Glen Layout',
       'Balagere', 'Kudlu Gate', 'Panathur', 'Old Madras Road', 'Rachenahalli',
       'Kadugodi', 'Talaghattapura', 'Jigani', 'Ambedkar Nagar', 'Mysore Road',
       'Thigalarapalya', 'Yelahanka New Town', 'Dodda Nekkundi', 'Devanahalli',
       'Frazer Town', 'Attibele', 'Kanakapura', '5th Phase JP Nagar',
       'Lakshminarayana Pura', 'Nagarbhavi', 'Ananth Nagar', 'TC Palaya',
       'CV Raman Nagar', 'Jalahalli', 'Kengeri Satellite Town', 'Kudlu',
       'Kalena Agrahara', 'Horamavu Agara', 'Bhoganhalli', 'Doddathoguru',
       'Subramanyapura', 'Hebbal Kempapura', 'Vidyaranyapura', 'Hosur Road',
       'BTM 2nd Stage', 'Mahadevpura', 'Horamavu Banaswadi', 'Tumkur Road',
       'Domlur']
values = ['location_'+ var for var in locations]

@app.route('/')
def home():
    return render_template('index.html', locations=locations, values=values)

@app.route("/price", methods = ['GET', 'POST'])
def print_price():
    if request.method == "POST":
        location = request.form['location']
        
        list_of_data = [request.form['bath'],request.form['balcony'],request.form['total_sqft'],request.form['bhk'],request.form['price_per_sqft']]

        for area in ['area_type_Super built-up  Area','area_type_Built-up  Area','area_type_Plot  Area']:
            if area == request.form['area_type']:
                list_of_data.append(1)
            else:
                list_of_data.append(0)

        list_of_data.append(request.form['availability'])

        for loc in values:
            if loc == request.form['location']:
                list_of_data.append(1)
            else:
                list_of_data.append(0)

        model = pickle.load(open('static/Price_model', 'rb'))
        predicted_value = model.predict(np.array([list_of_data]))
        return render_template('show_price.html', location=predicted_value[0].round())

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)