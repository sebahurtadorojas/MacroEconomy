import flet as ft
from data import CAT_LABELS
from colors_app import color_por_icono

def crear_macro_card(metadatos:dict,page: ft.Page,mostrar_detalle) -> ft.Container:
    
    #filter_labels = ["Todos", "Inflación", "Empleo", "Tasas", "PIB", "Comercio"]
    #active_filter = ft.Ref[str]()
    #active_filter.current = "Todos"
 
    #filter_row = ft.Ref[ft.Row]()

    panel_detalle = ft.Container(
        visible=False,
        margin=ft.Margin.only(top=8),
        padding=ft.Padding.all(12),
        border_radius=10,
        bgcolor=ft.Colors.with_opacity(0.06, metadatos['badge_color']),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.18, metadatos['badge_color'])),
        content=ft.Text(
            metadatos["description"],
            size=12,
            color=ft.Colors.with_opacity(0.75, ft.Colors.ON_SURFACE),
            selectable=True,
        ),
    )

    abierto = [False]
    
    btn_ver=ft.TextButton(
        content=ft.Row(
            controls=[
                ft.Text(
                    "Ver más",
                    size=12,
                    weight=ft.FontWeight.W_600,
                    color="#333333",),
                ft.Icon(
                    ft.Icons.KEYBOARD_ARROW_DOWN,
                    size=16,
                    color="#333333",),],
            spacing=2,
            tight=True,
        ),
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=8),
            side=ft.BorderSide(1, "#DDDDDD"),
            padding=ft.padding.symmetric(horizontal=12, vertical=6),),)
    
                    #on_click=lambda e: toggle(e,abierto,panel_detalle))
                               
    #btn_ver.on_click = lambda e:toggle_detalle(e)

    def badge(text: str, color: str, bg: str) -> ft.Container:
        icon = "↑ " if "Alta" in text or "Positivo" in text or "Expansión" in text else ""
        icon = "↓ " if (("Baja" in text) or ("Déficit" in text) and icon =="") else icon
        return ft.Container(
            content=ft.Text(
                f"{icon}{text}",
                size=12,
                weight=ft.FontWeight.W_600,
                color=color,
            ),
            bgcolor=bg,
            padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border_radius=12,
            )
    
    
    card= ft.Container(
        content=ft.Column(
            controls=[
                # Top bar: category + badge
                ft.Row(
                    controls=[
                        ft.Text(
                            metadatos['category'].upper(),
                            size=11,
                            weight=ft.FontWeight.W_600,
                            color="#888888",
                            #sp=1.2,
                        ),
                        badge(metadatos['badge_text'], metadatos['badge_color'], metadatos['badge_bg']),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=6),
                # Big value
                ft.Row(
                    controls=[
                        ft.Text(
                            metadatos['value'],
                            size=48,
                            weight=ft.FontWeight.W_700,
                            color="#111111",),],),
                ft.Text(metadatos['unit'], size=12, color="#666666"),
                ft.Container(height=6),
                # Title
                ft.Text(
                    metadatos['titulo'],
                    size=14,
                    weight=ft.FontWeight.W_600,
                    color="#111111",
                ),
                # Description
                ft.Text(
                    metadatos['description'],
                    size=12,
                    color="#555555",
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
                ft.Container(height=4),
                ft.Text(
                    f"{metadatos['previous_label']}: {metadatos['previous_value']}",
                    size=11,
                    color="#888888",
                ),
                ft.Divider(height=16, color="#EEEEEE"),
                # Footer: date + button
                ft.Row(
                    controls=[
                        ft.Text(metadatos['date'], size=11, color="#AAAAAA"),
                        btn_ver
                                ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,),],
            spacing=2,
        ),
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        padding=16,
        border=ft.border.Border(
            top=ft.border.BorderSide(3, metadatos['badge_color']),
            left=ft.border.BorderSide(1, "#EEEEEE"),
            right=ft.border.BorderSide(1, "#EEEEEE"),
            bottom=ft.border.BorderSide(1, "#EEEEEE"),
        ),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=8,
            color=ft.Colors.with_opacity(0.06, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        ),
        expand=True,
        on_click=lambda e: mostrar_detalle(e,metadatos)
    )

    return ft.Container(content=card, margin=ft.Margin.only(bottom=12))

"""ft.TextButton(
                            content=ft.Row(
                                controls=[
                                    ft.Text(
                                        "Ver más",
                                        size=12,
                                        weight=ft.FontWeight.W_600,
                                        color="#333333",),
                                    ft.Icon(
                                        ft.Icons.KEYBOARD_ARROW_DOWN,
                                        size=16,
                                        color="#333333",),],
                                spacing=2,
                                tight=True,
                            ),
                            style=ft.ButtonStyle(
                                bgcolor=ft.Colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=8),
                                side=ft.BorderSide(1, "#DDDDDD"),
                                padding=ft.padding.symmetric(horizontal=12, vertical=6),),),"""