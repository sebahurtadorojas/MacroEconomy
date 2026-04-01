import flet as ft
from tarjetas_learn import *


def pantalla_blog(page: ft.Page,metadata:dict):

# Definimos los estilos para que sea visualmente jerárquico
    titulo = ft.Text(
        value=metadata['titulo'],
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700
    )
    
    meta_descripcion = ft.Text(
        value=metadata['meta_description'],#"Publicado el 30 de marzo, 2026 • Categoría: Desarrollo",
        italic=True,
        size=14,
        color=ft.Colors.GREY_700
    )
    
    descripcion = ft.Text(
        value=metadata['description'],
        
        
        size=16,
        text_align=ft.TextAlign.JUSTIFY
    )

    # Retornamos el contenedor con padding para que no pegue a los bordes
    return ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                meta_descripcion,
                ft.Divider(height=10, color="transparent"), # Espacio sutil
                descripcion,
            ],
            scroll=ft.ScrollMode.AUTO, # Por si la descripción es muy larga
            spacing=10
        ),
        padding=20,
        expand=True
    )