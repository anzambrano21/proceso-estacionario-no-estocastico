import pandas as pd
import numpy as np
import statsmodels.api as sm
#clace de los calculos para la predicion 
class DivisasEURUS:
    def __init__(self):
        self.coti = {'dif': [], 'cierre': [], 'fech': [], "media":[], "varianza":[], 'cierre_normalized':[]}
        self.results = None

    def appendCierre(self, cier):
        self.coti["cierre"].append(cier)
        self.coti["dif"].append(np.nan)  # Inicializar la diferencia como NaN
        self.coti["media"].append(np.nan)
        self.coti["varianza"].append(np.nan)
        self.coti["cierre_normalized"].append(np.nan)
        
    def appendFecha(self, fech):
        self.coti["fech"].append(fech)

    def setCierre(self, id, cierre):
        self.coti["cierre"][id] = cierre

    def setFecha(self, id, fecha):
        self.coti["fech"][id] = fecha

    def deleteRegistro(self, id):
        self.coti["cierre"].pop(id)
        self.coti["fech"].pop(id)

    def fitARIMA(self, p, d, q):
        self.Ce = pd.DataFrame(self.coti)
        # Normaliza los datos de cierre
        self.Ce['cierre_normalized'] = (self.Ce['cierre'] - self.Ce['cierre'].mean()) / self.Ce['cierre'].std()
        self.Ce['media'] = self.Ce['cierre'].mean()
        self.Ce['varianza'] = self.Ce['cierre'].var()
        self.X = self.Ce[['cierre_normalized', 'media', 'varianza']]

        self.Ce['dif'] = self.Ce['cierre'].diff().dropna()
        order = (int(p), int(d), int(q))
        model = sm.tsa.ARIMA(self.Ce['dif'], order=order, exog=self.X)
        self.results = model.fit()
        

    def forecast(self, steps=10):
        if self.results:
            forecast = self.results.forecast(steps=steps, exog=self.X.iloc[-10:])

            return forecast
        else:
            return None
    def add_linear_trend(self):
        # Agregar una tendencia lineal a los valores de cierre
        n = len(self.coti["cierre"])
        trend = np.linspace(0, 1, n)  # Tendencia lineal
        self.coti["cierre"] = [c + t for c, t in zip(self.coti["cierre"], trend)]
