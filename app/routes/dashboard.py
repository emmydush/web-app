from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@dashboard_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
