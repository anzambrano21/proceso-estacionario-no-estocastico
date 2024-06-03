import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

class divisasEURUS:
    def __init__(self):
        self.coti["dif"]
        self.coti["cierre"]
        self.coti["fecha"]
    def setCierre(self,cier):
        self.coti["cierre"]=cier
    def setFecha(self,fech):
        self.coti["fech"]=fech
    def model(self,p,d,q):
        order = (p, d, q)  # Orden (p, d, q)
        model = sm.tsa.ARIMA(self.df['Diff'].dropna(), order=order)
        self.results = model.fit()
    def prediccion(self):
        forecast_steps = 10
        forecast, stderr, conf_int = self.results.forecast(steps=forecast_steps)
    


