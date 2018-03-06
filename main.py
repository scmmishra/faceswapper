import sys
from flask import Flask
from flask import send_file
from faceswap import faceswap

# faceswap(sys.argv[1], sys.argv[2])
app = Flask(__name__)

@app.route("/swap", methods=['POST'])
def my_webservice():
    name = request.form['employee_name']
    file = request.files['image']
    # Uses faceswap to change image
    name_of_output = faceswap(file, "head.jpg", name)

    # Send this `url_for('static', filename=name_of_output)` in an HTTPS respose or any other form
    return url_for(filename=name_of_output)

def main():
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()
