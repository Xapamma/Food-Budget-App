'''
This project will create a python flask application that will allow users to import food information to create a food 
database. The application will allow users to add, view, and search for food items based on various attributes such as 
name, category, and nutritional information. The application will also provide an API for external applications to 
access the food database. It will calculate the cost per meal based on serving size and price of the food items.

'''

from flask import Flask, render_template, request
from routes.home import home_bp
from routes.about import about_bp
from routes.products import products_bp
from routes.stores import stores_bp

app = Flask(__name__)

# Add each page to the app using blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(products_bp)
app.register_blueprint(stores_bp)









if __name__ == '__main__':
    app.run(debug=True)