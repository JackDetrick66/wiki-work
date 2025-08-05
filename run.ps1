& "venv\Scripts\Activate.ps1"
$env:FLASK_APP = "app.py"
$env:FLASK_DEBUG = "1"
flask run