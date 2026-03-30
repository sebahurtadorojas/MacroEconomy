import flet as ft
from data import cargar_cache_local, verificar_mensajes,mensajes
from tarjetas_learn import *
import threading


def pantalla_mensajes(page: ft.Page):
    """local_hash, cached_data = cargar_cache_local('learn')
    datos_iniciales = cached_data if cached_data else []"""



    lista_tarjetas=ft.ListView(
                expand=True,
                padding=ft.Padding.symmetric(horizontal=16),
                controls=[crear_card_learn(m, page) for m in mensajes],
            )
    
    
    def puente_actualizar(nueva_data):
        actualizar_card_learn(nueva_data, page, lista_tarjetas)
    """hilo = threading.Thread(
            target=verificar_mensajes,
            args=(mensajes,puente_actualizar)
        )
    hilo.start()"""



    return ft.Column(
        expand=True,
        controls=[
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=12),
                content=ft.Row(
                    controls=[
                        ft.Text("Mensajes", size=28, weight=ft.FontWeight.BOLD),
                        ft.Row(expand=True),
                        ft.IconButton(ft.icons.Icons.SEARCH, tooltip="Buscar"),
                        ft.IconButton(ft.icons.Icons.FILTER_LIST, tooltip="Filtrar"),
                    ]
                ),
            ),
            lista_tarjetas,
        ],
    )