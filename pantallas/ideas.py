import flet as ft
from data import cargar_cache_local,verificar_api_en_segundo_plano
from tarjeta import crear_tarjeta,actualizar_card
import threading

def pantalla_ideas(page: ft.Page,funcion_alerta):


    

    local_hash, cached_data = cargar_cache_local('ideas')
    datos_iniciales = cached_data if cached_data else []
    lista_tarjetas=ft.ListView(
                expand=True,
                padding=ft.Padding.symmetric(horizontal=16),
                controls=[crear_tarjeta(i, page,funcion_alerta) for i in datos_iniciales],
            )


    def puente_actualizar(nueva_data):
        actualizar_card(nueva_data, page, lista_tarjetas, funcion_alerta)
    hilo = threading.Thread(
            target=verificar_api_en_segundo_plano,
            args=('ideas', local_hash, puente_actualizar)
        )
    hilo.start()
    
    return ft.Column(
        expand=True,
        controls=[
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=12),
                content=ft.Row(
                    controls=[
                        ft.Text("Ideas", size=28, weight=ft.FontWeight.BOLD),
                        ft.Row(expand=True),
                        ft.IconButton(ft.icons.Icons.SEARCH, tooltip="Buscar"),
                    ]
                ),
            ),
            lista_tarjetas,
        ],
    )

