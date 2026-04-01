import flet as ft
from pantallas.aprender import pantalla_learn
from pantallas.ideas import pantalla_ideas
from pantallas.perfil import pantalla_perfil
from pantallas.detalle_learn import pantalla_blog
from pantallas.macros import pantalla_macros

def main(page: ft.Page):
    page.title = "Economy App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="#6750A4", use_material3=True)
    page.padding = 0


    def mostrar_detalle(e,metadata:dict):
        cuerpo.content = pantalla_blog(page,metadata)
        page.update()

    def toggle_detalle_macro(e,abierto: list,panel_detalle:ft.Container):
            abierto[0] = not abierto[0]
            panel_detalle.visible = abierto[0]
            text_="Ver menos ↑" if abierto[0] else "Ver más ↓"
            e.tooltip = text_
            print(text_)
            
            page.update()

    # --- Contenedor del cuerpo ---
    cuerpo = ft.Container(expand=True)

    pantallas = {
        0: lambda: pantalla_learn(page,mostrar_detalle),
        1: lambda: pantalla_macros(page,mostrar_detalle), # Si ideas usa tarjetas, pasa mostrar_alarma también
        2: lambda: pantalla_ideas(page),
    }

    indice_actual = [0]

    def cambiar_pantalla(index):
        indice_actual[0] = index
        cuerpo.content = pantallas[index]()
        nav.selected_index = index
        page.update()

    

    # --- Barra de navegación inferior ---
    nav = ft.NavigationBar(
        selected_index=0,
        on_change=lambda e: cambiar_pantalla(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.Icons.BOOK_OUTLINED,
                selected_icon=ft.icons.Icons.BOOK,
                label="Aprender",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.Icons.AREA_CHART_OUTLINED,
                selected_icon=ft.icons.Icons.AREA_CHART,
                label="Macroeconomia",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.Icons.LIGHTBULB_OUTLINED,
                selected_icon=ft.icons.Icons.LIGHTBULB,
                label="Ideas",
            ),
        ],
    )

    # Cargar pantalla inicial
    cuerpo.content = pantallas[1]()

    # Organización de la página
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                cuerpo,
                nav,
            ],
        )
    )
    
    # Asignamos el FAB a la página
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        tooltip="Nuevo",
        on_click=lambda e: None,
        offset=ft.Offset(0, -1)
    )
    page.update()

if __name__ == "__main__":
    ft.run(main)