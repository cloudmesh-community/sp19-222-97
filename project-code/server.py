from flask import jsonify
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints of communication
app.add_api("swagger.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Tetris Score Analyzer"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
