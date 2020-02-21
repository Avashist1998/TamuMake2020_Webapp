from flask import Flask, render_template, jsonify, request,json
from fetcher import get_file
import pandas as pd 
app = Flask(__name__)

# Data sturction
class DataStore():
    botton = None
data1 = DataStore
data2 = DataStore
#df1 = pd.read_csv('static/Main_Hack_2020Final_data.csv')
#df2 = pd.read_csv('static/state_population')

@app.route("/",methods=["GET", "POST"])
def index():
#    if request.method == 'GET':
#        base_data.botton = 0
        df3 = pd.read_csv('static/Number_of_accidents.csv')
        df3['average'] = df3['average']*100 
        chart_data = df3.to_dict(orient= 'records')
        chart_data = json.dumps(chart_data,indent = 2)
        data = {'chart_data':chart_data}
        return render_template('index.html', data=data)
#    else:
#        if 'average' in request.form:
#            base_data.botton = 0
#        elif 'percentage' in request.form:
#            base_data.botton = 1
#        return render_template('index.html',base_data=df3[(['Index','percentage'])].to_json)



if __name__ == '__main__':
    app.run(debug= True)