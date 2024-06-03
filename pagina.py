import flet
class pagina:
    def __init__(self,page:flet.Page):
        self.page=page
        self.page.window_height=500
        self.page.window_width=500
        #caselar el cambio de tamaño
        self.page.window_resizable=False
        self.page.title="no estacionario"
        self.page.vertical_alignment = flet.MainAxisAlignment.CENTER
        self.page.update()

