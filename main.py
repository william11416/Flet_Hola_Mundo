import flet as ft

def main(page: ft.Page):
    # Opcional: configurar el título de la página
    page.title = "Mi App Flet"
    
    texto = ft.Text("")
    
    def cambiar(e):
        texto.value = "Hola Mundo"
        page.update()
        
    # En Flet 1.x se utiliza ft.ElevatedButton correctamente
    boton = ft.ElevatedButton("Click Aquí", on_click=cambiar)
    
    page.add(texto, boton)

if __name__ == "__main__":
    ft.app(target=main)
