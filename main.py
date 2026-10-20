import flet as ft
def main(page: ft.Page):
    texto = ft.Text("")
    def cambiar(e):
        texto.value = "Hola Mundo"
        page.update()
    boton = ft.Button("Click Aquí", on_click=cambiar)
    page.add(texto, boton)
ft.run(main)
print ("hola")
