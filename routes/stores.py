from flask import Blueprint, render_template

stores_bp = Blueprint("stores", __name__)

@stores_bp.route('/stores')

def stores():
    return render_template('stores.html')