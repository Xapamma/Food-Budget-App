'''
This project will create a python flask application that will allow users to import food information to create a food 
database. The application will allow users to add, view, and search for food items based on various attributes such as 
name, category, and nutritional information. The application will also provide an API for external applications to 
access the food database. It will calculate the cost per meal based on serving size and price of the food items.

'''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    protein_per_dollar = None
    calorie_per_dollar = None
    product_name = None
    price = None
    calories = None
    protein = None

    if request.method == 'POST':
        product_name = request.form['product_name']
        price = float(request.form['price'])
        calories = float(request.form['calories'])
        protein = float(request.form['protein'])

        protein_per_dollar = protein / price if price != 0 else None
        calorie_per_dollar = calories / price if price != 0 else None
               
    return render_template('index.html', protein_per_dollar=protein_per_dollar, calorie_per_dollar=calorie_per_dollar, product_name=product_name, price=price, calories=calories, protein=protein)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/stores')
def stores():
    return render_template('stores.html')





if __name__ == '__main__':
    app.run(debug=True)