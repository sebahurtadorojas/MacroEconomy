import flet as ft
# ─── Widget: Tarjeta de Anuncio ───────────────────────────────────────────────


def actualizar_card_learn(nueva_data,page: ft.Page,lista):
    # Reemplazamos los controles viejos por las tarjetas nuevas
    lista.controls = [crear_card_learn(m, page) for m in nueva_data]
    page.update() # Refresca solo esta parte de la pantalla



def crear_card_learn(anuncio: dict, page: ft.Page):
    if anuncio["icono"] == "TRENDING_UP":
        color_ = "#006E1C"
    elif anuncio["icono"] == "TRENDING_DOWN":
        color_ = "#B1416B"
    elif anuncio["icono"] == "BUILD_OUTLINED":
        color_ = "#EB9D0E"
    else:
        color_ = "#4169E1"
    

    
    card = ft.Card(
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=16),
        content=ft.Container(
            padding=ft.Padding.all(16),
            bgcolor=ft.Colors.with_opacity(0.05, color_),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.2, color_)),#ft.Colors.with_opacity(0.2, ft.Colors.OUTLINE)),
            border_radius=16,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(height=10),
                    ft.Text(anuncio["titulo"], size=15, 
                            weight=ft.FontWeight.W_600,
                            align=ft.Alignment.CENTER,
                            color=ft.Colors.ON_SURFACE),
                    ft.Container(height=6),
                    
                    ft.Text(
                        anuncio["descripcion"],
                        max_lines=2,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        size=13,
                        color=ft.Colors.with_opacity(0.7, ft.Colors.ON_SURFACE),
                    ),
                    ft.Container(height=6),
                    ft.Button(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.KEYBOARD_ARROW_DOWN_ROUNDED, color=color_),
                                ft.Text("Ver más", size=13, weight=ft.FontWeight.W_500),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,
                        ),
                        style=ft.ButtonStyle(
                            color=color_,
                            
                            #bgcolor=ft.Colors.with_opacity(0.1, color_),
                            overlay_color=ft.Colors.with_opacity(0.15, color_),
                            shape=ft.RoundedRectangleBorder(radius=12),
                        ),
                        height=35,
                        #width=120,
                        on_click=lambda e: page.push_route('ideas.py')       # click en null
                    )
                    ])))
 
    return ft.Container(content=card, margin=ft.Margin.only(bottom=12))
