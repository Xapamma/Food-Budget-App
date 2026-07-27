'''
This project will create a python flask application that will allow users to import food information to create a food 
database. The application will allow users to add, view, and search for food items based on various attributes such as 
name, category, and nutritional information. The application will also provide an API for external applications to 
access the food database. It will calculate the cost per meal based on serving size and price of the food items.

'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Budget Price App</h1>"

@app.route('/about')
def about():
    return "<h1>About This App</h1><p>This app helps compare grocery prices.</p>"







if __name__ == '__main__':
    app.run(debug=True)