import flet as ft
from pantallas.mensajes import pantalla_mensajes
from pantallas.ideas import pantalla_ideas
from pantallas.perfil import pantalla_perfil

def main(page: ft.Page):
    page.title = "Trading App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed="#6750A4", use_material3=True)
    page.padding = 0

    titulo_ref = ft.Ref[ft.TextField]()
    entrada1_ref = ft.Ref[ft.TextField]()
    entrada2_ref = ft.Ref[ft.TextField]()
    sl_ref = ft.Ref[ft.TextField]()
    tp_ref = ft.Ref[ft.TextField]()
    icon_ref = ft.Ref[ft.Dropdown]()
    tipo_ref = ft.Ref[ft.Dropdown]()



    def guardar_trade(e):
        # Aquí procesarás la lógica de guardado
        print(f"Título: {titulo_ref.current.value}")
        print(f"Icono: {icon_ref.current.value}")
        print(f"Tipo: {tipo_ref.current.value}")
        cerrar_popup(None)
    def cerrar_popup(e):
            dlg_modal.open = False
            page.update()
    # --- Estructura del Diálogo ---
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Nueva Operación / Notificación"),
        content=ft.Column(
            tight=True,
            controls=[
                ft.TextField(ref=titulo_ref, label="Título de la señal", autofocus=True),
                ft.Row([
                    ft.TextField(ref=entrada1_ref, label="Entrada 1", expand=True),
                    ft.TextField(ref=entrada2_ref, label="Entrada 2", expand=True),
                ]),
                ft.Row([
                    ft.TextField(ref=sl_ref, label="Stop Loss (SL)", expand=True),
                    ft.TextField(ref=tp_ref, label="Take Profit (TP)", expand=True),
                ]),
                ft.Dropdown(
                    ref=icon_ref,
                    label="Icono Visual",
                    options=[
                        ft.dropdown.Option("TRENDING_UP"),
                        ft.dropdown.Option("TRENDING_DOWN"),
                        ft.dropdown.Option("WARNING"),
                        ft.dropdown.Option("NOTIFICATIONS"),
                    ],
                ),
                ft.Dropdown(
                    ref=tipo_ref,
                    label="Categoría",
                    options=[
                        ft.dropdown.Option("Anuncio"),
                        ft.dropdown.Option("Trades"),
                        ft.dropdown.Option("Mantención"),
                    ],
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=cerrar_popup),
            ft.Button("Publicar", on_click=guardar_trade),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.overlay.append(dlg_modal)

    
    # --- Configuración del FAB ---
    def abrir_popup(e):
        page.dialog = dlg_modal
        print("aca")
        dlg_modal.open = True
        page.update()








    # --- Lógica de la Alarma (Dialog) ---
    def cerrar_alarma(e):
        alarma_dialog.open = False
        page.update()

    alarma_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("¡Alerta de Trading!", weight=ft.FontWeight.BOLD),
        content=ft.Text("Se ha alcanzado el nivel de precio configurado en tu tarjeta."),
        actions=[
            ft.TextButton("Entendido", on_click=cerrar_alarma),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Agregamos el diálogo al overlay para que sea accesible
    page.overlay.append(alarma_dialog)

    def mostrar_alarma(e):
        alarma_dialog.open = True
        page.update()

    # --- Contenedor del cuerpo ---
    cuerpo = ft.Container(expand=True)

    # Pasamos 'mostrar_alarma' a las pantallas que necesiten activar el diálogo
    pantallas = {
        0: lambda: pantalla_mensajes(page),
        1: lambda: pantalla_ideas(page,mostrar_alarma), # Si ideas usa tarjetas, pasa mostrar_alarma también
        2: lambda: pantalla_perfil(page),
    }

    indice_actual = [0]

    def cambiar_pantalla(index):
        indice_actual[0] = index
        cuerpo.content = pantallas[index]()
        nav.selected_index = index
        page.update()

    # --- FAB (Botón Flotante) ---
    # Usamos ft.Offset(0, -1) para subirlo y que no choque con la Nav
    
    """fab = ft.FloatingActionButton(
        icon=ft.Icons.ADD, # Siguiendo la jerarquía ft.icons.NOMBRE
        tooltip="Nuevo",
        on_click=abrir_popup,#lambda e: None,
        # El primer valor es X (0), el segundo es Y (-0.5 sube un poco)
        offset=ft.Offset(0, -1), 
    )"""

    # --- Barra de navegación inferior ---
    nav = ft.NavigationBar(
        selected_index=0,
        on_change=lambda e: cambiar_pantalla(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.Icons.INBOX_OUTLINED,
                selected_icon=ft.icons.Icons.INBOX,
                label="Trades",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.Icons.LIGHTBULB_OUTLINED,
                selected_icon=ft.icons.Icons.LIGHTBULB,
                label="Ideas",
            ),
            ft.NavigationBarDestination(
                icon=ft.icons.Icons.PERSON_OUTLINE,
                selected_icon=ft.icons.Icons.PERSON,
                label="Perfil",
            ),
        ],
    )

    # Cargar pantalla inicial
    cuerpo.content = pantallas[0]()

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