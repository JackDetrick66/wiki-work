from flask import render_template

from . import main_bp

@main_bp.route('/contentListing')
def contentListing():
    return render_template('contentListing.html')
    
