from flask import render_template

from . import main_bp
#just returning the html
@main_bp.route('/contentListing')
def contentListing():
    return render_template('contentListing.html')
    
