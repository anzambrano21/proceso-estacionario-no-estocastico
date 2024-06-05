import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

class divisasEURUS:
    def __init__(self):
        self.coti={'dif':[], 'cierre':[], 'fech':[],}
    def appendCierre(self,cier):
        self.coti["cierre"].append(cier)
    def appendFecha(self,fech):
        self.coti["fech"].append(fech)
    def setCierre(self,id,cierre):
        self.coti["cierre"][id]=cierre
    def setfecha(self,id,cierre):
        self.coti["fech"][id]=cierre
    def deletRegi(self,id):
        self.coti["cierre"].pop(id)
        self.coti["fech"].pop(id)
    def model(self,p,d,q):
        order = (p, d, q)  # Orden (p, d, q)
        model = sm.tsa.ARIMA(self.coti['Diff'].dropna(), order=order)
        self.results = model.fit()
    def prediccion(self):
        forecast_steps = 10
        forecast, stderr, conf_int = self.results.forecast(steps=forecast_steps)
    


