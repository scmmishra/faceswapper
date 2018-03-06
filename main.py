import sys
import random
from flask import (Flask, request, Response)
# install using
import jsonpickle
from flask import send_file
from faceswap import faceswap

# faceswap(sys.argv[1], sys.argv[2])
app = Flask(__name__)

@app.route("/swap", methods=['POST'])
def my_webservice():
    data = request.get_json()
    name = data['employee_name']
    image_url = data['image']
    img_data = requests.get(image_url).content
    temp_name = str(time.time())[4:10] + '.jpg'
    with open(temp_name, 'wb') as handler:
        handler.write(img_data)
    # Uses faceswap to change image
    name_of_output = faceswap(temp_name, "head.jpg", name)

    response = {'image': '{}'.format(url_for(filename=name_of_output))}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

def main():
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()
