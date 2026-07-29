from flask import Blueprint, render_template, request
from services.calculations import calculate_protein_per_dollar, calculate_calorie_per_dollar
from database.database import add_product, get_products

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET", "POST"])
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

        protein_per_dollar = calculate_protein_per_dollar(protein, price)
        calorie_per_dollar = calculate_calorie_per_dollar(calories, price)

        add_product(product_name, price, calories, protein)

    products = get_products()

    return render_template(
                            'index.html', 
                            protein_per_dollar=protein_per_dollar, 
                            calorie_per_dollar=calorie_per_dollar, 
                            product_name=product_name, 
                            price=price, 
                            calories=calories, 
                            protein=protein,
                            products=products
                            )


