import flet
from flet import Column,Row,Container,margin
class pagina:
    def __init__(self,page:flet.Page):
        self.page=page
        self.page.window_height=1000
        self.page.window_width=900
        #caselar el cambio de tamaño
        self.page.window_resizable=False
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
        self.tabla=flet.DataTable(columns=[flet.DataColumn(flet.Text("ID")),
                                            flet.DataColumn(flet.Text("Fecha")),
                                            flet.DataColumn(flet.Text("Cierre"))
                                           ],
                                  rows=[]
                                  )

       
        self.componentes()
        self.page.update()
    def remover(self,e):
        del self.tabla.rows[self.id]
        self.page.snack_bar = flet.SnackBar(
        flet.Text("Eliminacion Exitosa"),
        bgcolor = "red"
        )
        self.page.snack_bar.open = True
        self.ordenar()
        self.page.update()
    def ordenar(self):
        for i in range(len(self.tabla.rows)):
            self.tabla.rows[i].cells[0].content=flet.Text(i)
    def editText(self,f,e,r):
        self.id=int(f)
        self.fecha.value=e
        self.cierre.value=r
        self.botonAgre.visible=False
        self.edit.visible=True
        self.delet.visible=True
        self.page.update()
    def editSave(self,e):
        self.tabla.rows[self.id].cells[1].content=flet.Text(self.fecha.value)
        self.tabla.rows[self.id].cells[2].content=flet.Text(self.cierre.value)
        self.page.update()
    def agregarvalor(self,e):
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
    def componentes(self):
        self.page.add(Column([
            flet.Text("Proceso Estocástico no Estacionario en Divisas Euro/US", text_align=flet.TextAlign.CENTER)]))
        
        # estructura de la pagina
        self.contenedor1 = Container(content=Column([Row([self.fecha,
                                                     self.cierre,self.botonAgre,self.edit,self.delet]),flet.Text(value="model"),
                                                     Row([self.pe,self.de,self.qu]),
                                                     flet.Container(content=Column([Row([
                                                                                self.tabla
                                                                            ])
                                                         
                                                                        ]),
                                                                        margin=margin.only(0,25),
                                                                        padding=10,
                                                                        alignment=flet.alignment.center,
                                                                        width=950,
                                                                        height=450,
                                                                        border_radius=10,
                                                                    )
                                                    ]),                   
                                                    margin=10,
                                                    width=920,
                                                    height=450,
                    )
        self.contenedor1.margin = margin.all(20)

        self.page.add(Row([self.contenedor1]))



