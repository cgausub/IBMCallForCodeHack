from flask import Flask, make_response, request
import requests
from flask import render_template
from flask import jsonify
from flask import Flask,request
import warnings
import csv
import requests, json
import urllib3
import base64
from watson_developer_cloud import VisualRecognitionV3

app = Flask(__name__)




def read_csv_as_list_map(filepath):
    output_list=[]
    with open(filepath) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            output_list.append(row)
    return output_list
def convert_url_to_byte_data(url):
    response = http.request('GET', url).data
    data = base64.b64encode(response)
    return data


@app.route('/')
def form():
    return render_template('index.html')



@app.route('/process', methods=["POST"])
def transform_view():
    output_response=[]
    print('hi')
    content = request.get_json()
    print(content)
    f=open('current.csv','wb')
    f.write(request.files['file'].read())
    f.close()
    file_path='current.csv'
    file_as_list=read_csv_as_list_map(file_path)
    for image in file_as_list:
        image_url=image['image_name']
        lat=image['lat']
        lng=image['long']
        landmark=image['landmark']
        data=convert_url_to_byte_data(image_url)
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.decodebytes(data))
        classes=None
        with open('imageToSave.png', 'rb') as images_file:
            classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
                owners=["me"]).get_result()
        prediction=dict(classes)['images'][0]['classifiers'][0]['classes'][0]['class']
        image_data_add={}
        image_data_add['lat']=float(lat)
        image_data_add['lng']=float(lng)
        image_data_add['landmark']=landmark
        print(prediction)
        if(prediction=='No Damage'):
            image_data_add['damage']=0
        else:
            image_data_add['damage']=1
        output_response.append(image_data_add)
    json_string =jsonify(output_response)
   
    return json_string

    #return jsonify([{'lat':28.6562,'lng':77.2410,'damage':'1','landmark':'CP'},{'lat':28.6362,'lng':77.2610,'damage':'0','landmark':'India Gate'}])


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    http = urllib3.PoolManager()
    visual_recognition = VisualRecognitionV3(
    version='2018-09-15',
    iam_apikey='3iQXX7o_K1_y-J4ERM6LnDFGwPkAP37RuFZJbmQi1VyE'
    )
    app.run(host='0.0.0.0', port=5014)

    