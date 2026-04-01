import flet as ft
from data import cargar_cache_local, verificar_api_en_segundo_plano,macros
import threading
from tarjeta_macros import crear_macro_card


def pantalla_macros(page: ft.Page,mostrar_detalle):
    local_hash, cached_data = cargar_cache_local('learn')
    datos_iniciales = cached_data if cached_data else []

    #lista = ft.Column(spacing=5,scroll=True) 



    """for i in range(0, len(macros), 2):
        fila = ft.Row(
            controls=[
                crear_macro_card(macros[i], page),
                crear_macro_card(macros[i+1], page) if i + 1 < len(macros) else ft.Container(width=0),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
    )
    controls_filas.append(fila)"""

    lista=ft.ListView(
        expand=True,
        padding=ft.Padding.symmetric(horizontal=16),
        controls=[
            ft.ResponsiveRow(
                controls=[
                ft.Container(content=crear_macro_card(macro, page,mostrar_detalle), col={"sm": 6, "md": 6, "xl": 4}) for macro in macros
                ],
                spacing=15,
                run_spacing=20,
            )
        ]
    )


    """   lista.controls = [
        ft.Row(controls=[crear_macro_card(macros[0],page),crear_macro_card(macros[1],page)]),
        ft.Row(controls=[crear_macro_card(macros[0],page),crear_macro_card(macros[1],page)])]"""
    #grid = crear_macro_card(macros[0],page)
    #grid1 = crear_macro_card(macros[1],page)

    return ft.Column(
        expand=True,
        controls=[
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=12),
                content=ft.Row(
                    controls=[
                        ft.Text("Macroeconomía", size=28, weight=ft.FontWeight.BOLD),
                        ft.Row(expand=True),
                        ft.IconButton(ft.icons.Icons.SEARCH, tooltip="Buscar"),
                        ft.IconButton(ft.icons.Icons.FILTER_LIST, tooltip="Filtrar"),
                    ]
                ),
            ),lista,
        ],
    )