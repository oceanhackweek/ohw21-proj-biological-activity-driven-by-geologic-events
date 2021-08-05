from flask import Flask, render_template, request, url_for, session
from forms import QueryInputForm
from erddapy import ERDDAP
import pandas as pd
from datetime import datetime,timedelta
import numpy as np
import os
import json
import plotly
import plotly.express as px

app = Flask(__name__)
app.secret_key = 'random_key!'

server = "https://erddap.dataexplorer.oceanobservatories.org/erddap"
e = ERDDAP(server=server, protocol="tabledap")

e_databases = {
    'iespres': 'ooi-rs03axbs-lj03a-05-hpiesa301',
    'mass_concentration_of_chlorophyll_a_in_sea_water': 'ooi-rs03axps-pc03a-4c-flordd303',
    'sea_water_ph_reported_on_total_scale': 'ooi-rs03axps-pc03a-4b-phsena302',
    'sea_water_temperature': 'ooi-rs03axps-pc03a-4a-ctdpfa303',
    'sea_water_practical_salinity': 'ooi-rs03axps-pc03a-4a-ctdpfa303',
    'mole_concentration_of_dissolved_molecular_oxygen_in_sea_water': 'ooi-rs03axps-pc03a-4a-ctdpfa303',
    'sea_water_density': 'ooi-rs03axps-pc03a-4a-ctdpfa303',
    'sea_water_pressure': 'ooi-rs03axps-pc03a-4a-ctdpfa303'
}


@app.route('/', methods = ['GET', 'POST'])
def index():
    query_form = QueryInputForm(request.form)

    if request.method == 'POST':
        if 'start_date' in request.form and query_form.validate_on_submit():
            start_date = request.form['start_date'] + "T00:00:00Z"
            end_date = request.form['end_date'] + "T23:59:59Z"
            select_var = request.form['select_var']
            database = e_databases[select_var]

            e.dataset_id = database
            e.constraints = {
                "time>=": start_date,
                "time<=": end_date 
            }
            e.variables = ['time', select_var]

            print(start_date, end_date, select_var, database, e)
            df = e.to_pandas()
            df['time (UTC)'] = pd.to_datetime(df['time (UTC)'])

            print(df.head())

            

    return render_template('index.html', query_form = query_form)


def fix_date(da):
    da = da.assign(time=([datetime(1970,1,1) + timedelta(seconds=second) for second in da.time.data]))
    return da


if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 5000)