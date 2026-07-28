from flask import Blueprint, render_template, request

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

        protein_per_dollar = protein / price if price != 0 else None
        calorie_per_dollar = calories / price if price != 0 else None
               
    return render_template('index.html', protein_per_dollar=protein_per_dollar, calorie_per_dollar=calorie_per_dollar, product_name=product_name, price=price, calories=calories, protein=protein)


