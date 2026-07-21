import os
import xml.etree.ElementTree as ET
import pickle
import requests
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/download")
def download():
    filename = request.args.get("file")
    return send_file(f"/data/{filename}")

@app.route("/parse", methods=["POST"])
def parse_xml():
    xml_data = request.data
    tree = ET.fromstring(xml_data)
    return {"root": tree.tag}

@app.route("/fetch")
def fetch():
    url = request.args.get("url")
    response = requests.get(url, timeout=5)
    return response.text

@app.route("/restore", methods=["POST"])
def restore():
    data = request.data
    obj = pickle.loads(data)
    return {"restored": str(obj)}
