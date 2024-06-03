import flet
from flet import Column,Row,Container,margin
class pagina:
    def __init__(self,page:flet.Page):
        self.page=page
        self.page.window_height=1000
        self.page.window_width=1000
        #caselar el cambio de tamaño
        self.page.window_resizable=False
        self.page.title="no estacionario"
        
        self.fecha=flet.TextField(label="Fecha")
       
        self.componentes()
        self.page.update()
        
    def componentes(self):
        self.page.add(Column([
            flet.Text("Proceso Estocástico no Estacionario en Divisas Euro/US", text_align=flet.TextAlign.CENTER)]))
        
        # Crear un contenedor y agregar los controles dentro de él
        self.contenedor1 = Container(content=Column([Row([self.fecha,
                                                     flet.TextField(label="Cierre"),flet.ElevatedButton(text="Agragar")]),flet.Text(value="model"),
                                                     Row([flet.TextField(label="P"),flet.TextField(label="D"),flet.TextField(label="Q")]),
                                                     flet.Container(content=Column([Row([
                                                                                flet.DataTable(columns=[
                                                                                    flet.DataColumn(flet.Text("Fecha")),
                                                                                    flet.DataColumn(flet.Text("Cierre"))
                                                                                ],
                                                                                rows=[]
                                                                                )
                                                                            ])
                                                         
                                                                        ]),
                                                                        margin=margin.only(0,25),
                                                                        padding=10,
                                                                        alignment=flet.alignment.center,
                                                                        width=950,
                                                                        height=450,
                                                                        border_radius=10,
                ),]),                   
                    margin=10,
                    width=920,
                    height=450,
                    )
        self.contenedor1.margin = margin.all(20)

        self.page.add(Row([self.contenedor1]))



