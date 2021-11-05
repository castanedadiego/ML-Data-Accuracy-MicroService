from typing import Collection
from flask import Flask, json, render_template, make_response, jsonify, request
from main import *;

app= Flask(__name__, static_url_path= '/static')

PORT = 3200
HOST = "0.0.0.0"

DATA= {
    "all" : "stats unknown, upload a file to analyze",

}

#GET ENDPOINTS

@app.route("/data")
def data():
    return DATA

@app.route("/upload") #visual GUI to facilitate testing of uploading different datasets
def upload():
    return render_template('upload.html')

@app.route("/boxplot") #buggy but serves more a raw example of how further data visualization could be implemented
def boxplot():
    box= build_df("current_data.csv")["reach"].plot.box()
    box.figure.savefig("static/images/boxplot.png")
    return render_template('boxplot.html', name = 'BoxPlot', url ='/static/images/boxplot.png')


#POST ENDPOINTS

@app.route("/uploader", methods= ['POST'])
def uploader():
    if request.method == "POST":
        f = request.files['file']
        f.save('current_data.csv')

        DF= build_df("current_data.csv")
        DATA["all"]= get_data(DF) #bottleneck is here, the reach_accuracy is re-calculated before returning the HTTP request

        return 'file saved successfully'

if __name__=="__main__":
    print("Server running in port %s"%(PORT))
    app.run(host= HOST, port =PORT, debug= True)
