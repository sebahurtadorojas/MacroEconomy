import flet as ft


def pantalla_perfil(page: ft.Page):
    def stat_card(valor, etiqueta, icono, color):
        return ft.Card(
            elevation=0,
            expand=True,
            content=ft.Container(
                padding=ft.padding.symmetric(vertical=16, horizontal=8),
                bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.ON_SURFACE),
                border_radius=16,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                    controls=[
                        ft.Icon(icono, color=color, size=24),
                        ft.Text(valor, size=20, weight=ft.FontWeight.BOLD),
                        ft.Text(etiqueta, size=11, color=ft.Colors.with_opacity(0.6, ft.Colors.ON_SURFACE)),
                    ],
                ),
            ),
        )

    def opcion_tile(icono, titulo, subtitulo, color=None):
        return ft.ListTile(
            leading=ft.Icon(icono, color=color or ft.Colors.ON_SURFACE),
            title=ft.Text(titulo, weight=ft.FontWeight.W_500, color=color or ft.Colors.ON_SURFACE),
            subtitle=ft.Text(subtitulo) if subtitulo else None,
            trailing=ft.Icon(ft.icons.Icons.CHEVRON_RIGHT, color=ft.Colors.with_opacity(0.4, ft.Colors.ON_SURFACE)),
            on_click=lambda e: None,
        )

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                padding=ft.padding.symmetric(horizontal=16, vertical=12),
                content=ft.Row(
                    controls=[
                        ft.Text("Perfil", size=28, weight=ft.FontWeight.BOLD),
                        ft.Row(expand=True),
                        ft.IconButton(ft.icons.Icons.SETTINGS_OUTLINED),
                    ]
                ),
            ),
            ft.Container(
                margin=ft.margin.symmetric(horizontal=16),
                padding=ft.padding.all(24),
                border_radius=20,
                bgcolor="#EAD8FF",
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.CircleAvatar(
                            content=ft.Text("MG", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            bgcolor="#6750A4",
                            radius=44,
                        ),
                        ft.Container(height=12),
                        ft.Text("María González", size=18, weight=ft.FontWeight.BOLD, color="#21005D"),
                        ft.Text("maria.gonzalez@empresa.com", size=13, color=ft.Colors.with_opacity(0.65, "#21005D")),
                        ft.Container(height=12),
                        ft.OutlinedButton("Editar perfil"),
                    ],
                ),
            ),
            ft.Container(height=16),
            ft.Container(
                margin=ft.margin.symmetric(horizontal=16),
                content=ft.Row(
                    controls=[
                        stat_card("23", "Mensajes", ft.icons.Icons.INBOX, "#6750A4"),
                        stat_card("8", "Ideas", ft.icons.Icons.LIGHTBULB, "#B1416B"),
                        stat_card("5", "Favoritos", ft.icons.Icons.FAVORITE, ft.Colors.RED_400),
                    ],
                    spacing=12,
                ),
            ),
            ft.Container(height=16),
            ft.Container(
                margin=ft.margin.symmetric(horizontal=16),
                border_radius=16,
                bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.ON_SURFACE),
                content=ft.Column(
                    spacing=0,
                    controls=[
                        opcion_tile(ft.icons.Icons.NOTIFICATIONS_OUTLINED, "Notificaciones", "Configura tus alertas"),
                        ft.Divider(height=1, trailing_indent=56),
                        opcion_tile(ft.icons.Icons.LOCK_OUTLINE, "Privacidad", "Gestiona tu privacidad"),
                        ft.Divider(height=1, trailing_indent=56),
                        opcion_tile(ft.icons.Icons.HELP_OUTLINE, "Ayuda", "Centro de soporte"),
                        ft.Divider(height=1, trailing_indent=56),
                        opcion_tile(ft.icons.Icons.LOGOUT, "Cerrar sesión", "", color=ft.Colors.RED_400),
                    ],
                ),
            ),
            ft.Container(height=24),
        ],
    )
