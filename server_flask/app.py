from flask import Flask, render_template
from routes.upload import upload_bp
from routes.machines import machines_bp
from routes.logs import logs_bp
from routes.decrypt import decrypt_bp


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# register blueprints
app.register_blueprint(upload_bp)
app.register_blueprint(machines_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(decrypt_bp)

if __name__ == '__main__':
    app.run(debug=True)