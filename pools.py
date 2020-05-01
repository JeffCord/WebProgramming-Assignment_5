from flask import Flask, render_template
import requests
import gunicorn
import json
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template("index.html")

@app.route("/pools")
def show_pools():
    url_xml_data = 'https://raw.githubusercontent.com/devdattakulkarni/elements-of-web-programming' \
                   '/master/data/austin-pool-timings.xml'
    xml_to_str = requests.get(url_xml_data).text

    root = ET.fromstring(xml_to_str)


    output_data = []

    for row in root:
        row_data = {}

        for item in row:
            if item.tag == 'pool_name':
                row_data['Pool_name'] = item.text

            if item.tag == 'pool_type':
                row_data['Pool_type'] = item.text

            if item.tag == 'status':
                row_data['Status'] = item.text

            if item.tag == 'open_date':
                row_data['Open_date'] = item.text

            if item.tag == 'weekday':
                row_data['Weekday'] = item.text

            if item.tag == 'weekend':
                row_data['Weekend'] = item.text

        output_data.append(row_data)

    return json.dumps(output_data)

if __name__=='__main__':
    app.run(debug=True)
