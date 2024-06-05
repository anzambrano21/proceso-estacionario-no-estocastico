import flet
from flet import Column,Row,Container,margin
from no_estocastico import DivisasEURUS
import pandas as pd
import matplotlib.pyplot as plt
Style_Frame:dict={
    "expand": True,
    "border_radius":10,
    "padding":20
}
class grafica:
    def __init__(self):
        
        data_1=[flet.LineChartData(
                data_points=[

                ],
                stroke_width=5,
                color=flet.colors.CYAN,
                curved=False,
                stroke_cap_round=True,
                gradient=flet.LinearGradient([flet.colors.CYAN,flet.colors.WHITE]) 
            )]
        
        self.content=flet.LineChart(
            data_series=data_1,
            border=flet.border.all(3,flet.colors.with_opacity(0.2,flet.colors.BLACK)),
            horizontal_grid_lines=flet.ChartGridLines(interval=1),
            vertical_grid_lines=flet.ChartGridLines(interval=1),
            left_axis=flet.ChartAxis(
                labels=[
                    flet.ChartAxisLabel(
                        value=2,
                        label=flet.Container(
                            flet.Text(
                                "2",
                                size=16,
                                color=flet.colors.with_opacity(0.8,flet.colors.BLACK)
                            ),
                            margin=flet.margin.only(top=10),
                        ),
                    ),
                    flet.ChartAxisLabel(
                        value=6,
                        label=flet.Container(
                            flet.Text(
                                "4",
                                size=16,
                                color=flet.colors.with_opacity(0.8,flet.colors.BLACK)
                            ),
                            margin=flet.margin.only(top=10),
                        ),
                    ),
                    flet.ChartAxisLabel(
                        value=6,
                        label=flet.Container(
                            flet.Text(
                                "6",
                                size=16,
                                color=flet.colors.with_opacity(0.8,flet.colors.BLACK)
                            ),
                            margin=flet.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            bottom_axis=flet.ChartAxis(
                labels=[
                    flet.ChartAxisLabel(
                        value=2,
                        label=flet.Container(
                            flet.Text(
                                "2",
                                size=16,
                                color=flet.colors.with_opacity(0.8,flet.colors.BLACK)
                            ),
                            margin=flet.margin.only(top=10),
                        ),
                    ),
                    flet.ChartAxisLabel(
                        value=6,
                        label=flet.Container(
                            flet.Text(
                                "4",
                                size=16,
                                color=flet.colors.with_opacity(0.8,flet.colors.BLACK)
                            ),
                            margin=flet.margin.only(top=10),
                        ),
                    ),
                    flet.ChartAxisLabel(
                        value=6,
                        label=flet.Container(
                            flet.Text(
                                "6",
                                size=16,
                                color=flet.colors.with_opacity(0.8,flet.colors.BLACK)
                            ),
                            margin=flet.margin.only(top=10),
                        ),
                    ),
                ],
                labels_size=32,
            ),
            tooltip_bgcolor=flet.colors.with_opacity(0.8,flet.colors.BLACK),
            min_y=-1,
            max_y=10,
            min_x=0,
            max_x=30,
            expand=True
        )
        
class pagina:
    def __init__(self,page:flet.Page):
        self.calculos=DivisasEURUS()
        self.page=page
        self.page.window_height=1000
        self.page.window_width=985
        #caselar el cambio de tamaño
        self.page.window_resizable=False
        self.page.window_full_screen=False
        self.page.title="no estacionario"   
        #componentes
        self.fecha=flet.TextField(label="Fecha")
        self.cierre=flet.TextField(label="Cierre")
        self.pe=flet.TextField(label="P")
        self.de=flet.TextField(label="D")
        self.qu=flet.TextField(label="Q")
        self.botonAgre=flet.ElevatedButton(text="Agragar",on_click=self.agregarvalor,visible=True)
        self.edit=flet.ElevatedButton(text="Editar Valor",bgcolor="orange",color="white",on_click=self.editSave,visible=False)
        self.delet=flet.ElevatedButton(text="Delet",bgcolor="red",color="white",on_click=self.remover,visible=False)
        self.id=0
        self.Cal=flet.ElevatedButton("Calcular",on_click=self.Operar,visible=True,disabled=False)
        self.tabla=flet.DataTable(columns=[flet.DataColumn(flet.Text("ID")),
                                            flet.DataColumn(flet.Text("Fecha")),
                                            flet.DataColumn(flet.Text("Cierre"))
                                           ],
                                  rows=[]
                                  )
        self.grafica=grafica()
        self.componentes()
        self.page.update()
    def remover(self,e):
        del self.tabla.rows[self.id]
        self.calculos.deleteRegistro(self.id)      
        self.page.snack_bar = flet.SnackBar(
        flet.Text("Eliminacion Exitosa"),
        bgcolor = "red"
        )
        self.page.snack_bar.open = True
        self.ordenar()
        self.botonAgre.visible=True
        self.Cal.visible=True
        self.edit.visible=False
        self.delet.visible=False
        self.fecha.value=""
        self.cierre.value=""
        self.page.update()
    def ordenar(self):
        for i in range(len(self.tabla.rows)):
            self.tabla.rows[i].cells[0].content=flet.Text(i)
    def editText(self,f,e,r):
        self.id=int(f)
        self.fecha.value=e
        self.cierre.value=r
        self.botonAgre.visible=False
        self.Cal.visible=False
        self.edit.visible=True
        self.delet.visible=True
        self.page.update()
    def editSave(self,e):     
        fecha=None
        num=None
        try:
            num=float(self.cierre.value)
            fecha=pd.to_datetime(self.fecha.value,format='%d-%m-%Y')
        except:
            
            self.page.snack_bar = flet.SnackBar(
                flet.Text("Valor invalido"),
                 bgcolor = "red"
                )
            self.page.snack_bar.open = True
            self.page.update() 
            return
        self.tabla.rows[self.id].cells[1].content=flet.Text(self.fecha.value)
        self.tabla.rows[self.id].cells[2].content=flet.Text(self.cierre.value)
        self.botonAgre.visible=True
        self.Cal.visible=True
        self.edit.visible=False
        self.delet.visible=False
        self.calculos.setCierre(num)
        self.calculos.setFecha(fecha)
        self.fecha.value=""
        self.cierre.value=""
        self.page.update()
    def agregarvalor(self,e):
        fecha=None
        num=None
        try:
            num=float(self.cierre.value)
            fecha=pd.to_datetime(self.fecha.value)
        except:
            
            self.page.snack_bar = flet.SnackBar(
                flet.Text("Valor invalido"),
                 bgcolor = "red"
                )
            self.page.snack_bar.open = True
            self.page.update() 
            return
        self.calculos.appendCierre(num)
        self.calculos.appendFecha(fecha)
        self.tabla.rows.append(
            flet.DataRow(
                cells=[
                    flet.DataCell(flet.Text(len(self.tabla.rows))),
                    flet.DataCell(flet.Text(self.fecha.value)),
                    flet.DataCell(flet.Text(self.cierre.value))
                ],
                on_select_changed=lambda e:self.editText(e.control.cells[0].content.value,e.control.cells[1].content.value,e.control.cells[2].content.value)
            )
        )
        self.fecha.value=""
        self.cierre.value=""
        
        self.page.update()   
    def Operar(self,e):
        pasos=len(self.calculos.coti["cierre"])
        self.calculos.fitARIMA(self.pe.value,self.de.value,self.qu.value)
        self.calculos.add_linear_trend()
        forecast= self.calculos.forecast(steps=pasos)
        print(forecast)
        puntos=[]
        for i in range(len(self.calculos.coti["cierre"])):

            puntos.append(flet.LineChartDataPoint(i, self.calculos.coti["cierre"][i]/100))
        for valor in forecast :
            puntos.append(flet.LineChartDataPoint(len(puntos)-1, valor/1000))                 
        print(len(puntos))
        data_1=[flet.LineChartData(
                data_points=puntos,
                stroke_width=5,
                color=flet.colors.CYAN,
                curved=False,
                stroke_cap_round=True,
                gradient=flet.LinearGradient([flet.colors.CYAN,flet.colors.WHITE]) 
            )]
        
        self.grafica.content.data_series=data_1
        self.page.update()

        

    def componentes(self):
        self.page.add(Column([
            flet.Text("Proceso Estocástico no Estacionario en Divisas Euro/US", text_align=flet.TextAlign.CENTER)]))
        # estructura de la pagina
        self.contenedor1 = Container(content=Column([Row(
            [self.fecha,
                                                     self.cierre,self.botonAgre,self.edit,self.delet,self.Cal]),flet.Text(value="model"),
                                                     Row([self.pe,self.de,self.qu]),Column([Row([
                                                         flet.Container(content=Column([
                                                                                self.tabla,
                                                                                
                                                                                
                                                                        ]),
                                                                        margin=margin.only(0,25),
                                                                        padding=10,
                                                                        alignment=flet.alignment.center,
                                                                        width=265,
                                                                        height=450,                                                                        
                                                                    ),
                                                                    
                                                    flet.Container(content=Column([Row([
                                                                                self.grafica.content
                                                                            ])
                                                                        ]),
                                                                        margin=margin.only(15,25),
                                                                        padding=10,
                                                                        alignment=flet.alignment.center,
                                                                        width=650,
                                                                        height=450, 
                                                                    )
                                                     ])]),
                                                     ]),                   
                                                    margin=10,
                                                    width=920,
                                                    height=450,
                    )
        self.contenedor1.margin = margin.all(20)
        self.page.add(Row([self.contenedor1]))
        self.page.update()


