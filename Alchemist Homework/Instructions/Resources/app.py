from flask import Flask, jsonify
import sqlalchemy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import datetime as dt
import seaborn as sns


engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#Table References
Measurements = Base.classes.measurements
Stations = Base.classes.station

# Create session 
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

##################################################
#Routes
# #################################################3
# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     f

@app.route("/api/v1.0/precipitation")
def precipitation():
        precip_2016 =session.query(Measurements.date,Measurements.prcp).\
        filter(Measurements.date.between('2016-01-01','2016-12-31')).all()

        all_precip = list(np.ravel(precip_2016))

        return jsonify(all_precip)


@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Stations.station).all()

    all_stations = list((stations))

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
     Stationshigh_obervations = session.query(Measurements.date,Measurements.tobs,Measurements.station).\
     filter(Measurements.date.between('2016-01-01','2016-12-31')).order_by(Measurements.date).all()

     all_stations_obs = list(Stationshigh_obervations)

     return jsonify(all_stations_obs)
    


if __name__ == '__main__':
    app.run(debug=True)



