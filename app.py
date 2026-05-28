from flask import Flask, render_template
from models.db import create_tables
# from controllers.auth_controller import auth_controller
# from controllers.staff_controller import staff_controller

app = Flask(__name__)
app.secret_key = "laundrify-secret-key-2026"

# Tatawagin natin ito para automatic na gumawa ng laundrify.db kapag nag-run ang app
create_tables()

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)