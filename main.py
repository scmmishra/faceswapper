import sys
import flask
from flask import send_file
from faceswap import faceswap

# faceswap(sys.argv[1], sys.argv[2])

@app.route("/swap", methods=['POST'])
def my_webservice():
    name = request.form['employee_name']
    file = request.files['image']
    #
    name_of_output = faceswap(file, "head.jpg", name)
    return url_for('static', filename=name_of_output)

app.run(host="0.0.0.0", port=5000)