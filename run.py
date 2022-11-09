from flask import Flask
from flask import Response
from flask import request

# from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
import json

fcape = open('./cape_map.geojson')
fki = open('./ki_map.geojson')
fli = open('./li_map.geojson')

pelatihan_ibf_app = Flask(__name__)
# run_with_ngrok(pelatihan_ibf_app) #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku  

@pelatihan_ibf_app.route('/cape')
def send_cape():
    return Response(response=json.dumps(json.load(fcape)),
                    status=200,
                    mimetype="application/json")
    
@pelatihan_ibf_app.route('/ki')
def send_ki():
    return Response(response=json.dumps(json.load(fki)),
                    status=200,
                    mimetype="application/json")
    
@pelatihan_ibf_app.route('/li')
def send_json_data_other_two():
    return Response(response=json.dumps(json.load(fki)),
                    status=200,
                    mimetype="application/json")
    
# @pelatihan_ibf_app.route('/query')
# def send_json_data_other_query():
#     value = request.args.get('value')
#     key = request.args.get('key')

#     dataquery = [p for p in geodata if p[key] == int(value)] #perhatikan jenis variable

#     return Response(response=json.dumps(dataquery),
#                     status=200,
#                     mimetype="application/json")


if __name__ == '__main__':
    pelatihan_ibf_app.run()