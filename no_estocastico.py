import pandas as pd
import numpy as np

import statsmodels.api as sm

class DivisasEURUS:
    def __init__(self):
        self.coti = {'dif': [], 'cierre': [], 'fech': []}
        self.results = None

    def appendCierre(self, cier):
        self.coti["cierre"].append(cier)
        self.coti["dif"].append(np.nan)  # Inicializar la diferencia como NaN

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
        self.Ce = pd.DataFrame(self.coti.copy())
        self.Ce['dif'] = self.Ce['cierre'].diff().dropna()
        order = (int(p), int(d), int(q))
        model = sm.tsa.ARIMA(self.Ce['dif'], order=order)
        self.results = model.fit()

    def forecast(self, steps=10):
        if self.results:
            forecast = self.results.forecast(steps=steps)

            return forecast
        else:
            return None
    def add_linear_trend(self):
        # Agregar una tendencia lineal a los valores de cierre
        n = len(self.coti["cierre"])
        trend = np.linspace(0, 1, n)  # Tendencia lineal
        self.coti["cierre"] = [c + t for c, t in zip(self.coti["cierre"], trend)]
