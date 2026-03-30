import flet as ft
from data import CAT_LABELS
from colors_app import color_por_icono

def crear_macro_card(item: dict, page: ft.Page) -> ft.Container:
    item=item[0]
    color_ = color_por_icono(item["icono"])

    # Panel "Ver más" — arranca oculto
    panel_detalle = ft.Container(
        visible=False,
        margin=ft.Margin.only(top=8),
        padding=ft.Padding.all(12),
        border_radius=10,
        bgcolor=ft.Colors.with_opacity(0.06, color_),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.18, color_)),
        content=ft.Text(
            item["detalle"],
            size=12,
            color=ft.Colors.with_opacity(0.75, ft.Colors.ON_SURFACE),
            selectable=True,
        ),
    )

    btn_ver = ft.TextButton(
        tooltip="Ver más ↓",
        style=ft.ButtonStyle(
            color=ft.Colors.PRIMARY,
            padding=ft.Padding.all(0),
            overlay_color=ft.Colors.TRANSPARENT,
        ),
    )
    abierto = [False]

    def toggle_detalle(e):
        abierto[0] = not abierto[0]
        panel_detalle.visible = abierto[0]
        btn_ver.text = "Ver menos ↑" if abierto[0] else "Ver más ↓"
        page.update()

    btn_ver.on_click = toggle_detalle

    # ── Panel izquierdo: NÚMERO ──────────────────────────────────────────────
    panel_izq = ft.Container(
        width=100,
        bgcolor=ft.Colors.with_opacity(0.10, color_),
        border_radius=ft.BorderRadius(
            top_left=14, bottom_left=14,
            top_right=0,  bottom_right=0,
        ),
        padding=ft.Padding.symmetric(horizontal=10, vertical=16),
        alignment=ft.alignment.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            controls=[
                ft.Container(
                    width=36, height=36,
                    border_radius=10,
                    bgcolor=ft.Colors.with_opacity(0.15, color_),
                    alignment=ft.alignment.Alignment.CENTER,
                    content=ft.Icon(
                        getattr(ft.icons.Icons, item["icono"], ft.icons.Icons.HELP_OUTLINE),
                        color=color_, size=20,
                    ),
                ),
                ft.Container(height=8),
                ft.Text(
                    item["numero"],
                    size=24,
                    weight=ft.FontWeight.W_800,
                    color=color_,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    item["numero_label"],
                    size=10,
                    weight=ft.FontWeight.W_500,
                    color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=8),
                ft.Container(
                    padding=ft.Padding.symmetric(horizontal=6, vertical=3),
                    border_radius=20,
                    bgcolor=ft.Colors.with_opacity(0.15, item["badge_color"]),
                    content=ft.Text(
                        item["badge"],
                        size=9,
                        weight=ft.FontWeight.W_700,
                        color=item["badge_color"],
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
            ],
        ),
    )

    # ── Panel derecho: Título + Descripción + Footer ─────────────────────────
    panel_der = ft.Container(
        expand=True,
        bgcolor=ft.Colors.with_opacity(0.04, color_),
        border_radius=ft.BorderRadius(
            top_left=0, bottom_left=0,
            top_right=14, bottom_right=14,
        ),
        padding=ft.Padding.all(14),
        content=ft.Column(
            spacing=0,
            expand=True,
            controls=[

                # Categoría + fecha
                ft.Row(
                    controls=[
                        ft.Container(
                            padding=ft.Padding.symmetric(horizontal=8, vertical=2),
                            border_radius=20,
                            bgcolor=ft.Colors.with_opacity(0.10, color_),
                            content=ft.Text(
                                CAT_LABELS.get(item["cat"], item["cat"]),
                                size=10,
                                weight=ft.FontWeight.W_700,
                                color=color_,
                            ),
                        ),
                        ft.Row(expand=True),
                        ft.Text(
                            item["fecha"],
                            size=10,
                            color=ft.Colors.with_opacity(0.45, ft.Colors.ON_SURFACE),
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),

                ft.Container(height=8),

                # Título
                ft.Text(
                    item["titulo"],
                    size=14,
                    weight=ft.FontWeight.W_700,
                    color=ft.Colors.ON_SURFACE,
                ),

                ft.Container(height=6),

                # Descripción
                ft.Container(
                    padding=ft.Padding.all(10),
                    border_radius=8,
                    bgcolor=ft.Colors.with_opacity(0.05, color_),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.10, color_)),
                    content=ft.Text(
                        item["descripcion"],
                        size=12,
                        color=ft.Colors.with_opacity(0.75, ft.Colors.ON_SURFACE),
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                ),

                ft.Container(height=6),

                # Panel detalle expandible
                panel_detalle,

                # Footer: dato anterior + botón
                ft.Row(
                    controls=[
                        ft.Text(
                            item["anterior"],
                            size=11,
                            color=ft.Colors.with_opacity(0.4, ft.Colors.ON_SURFACE),
                        ),
                        ft.Row(expand=True),
                        btn_ver,
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
        ),
    )

    # Borde exterior de la card completa
    card = ft.Card(
        elevation=0,
        shape=ft.RoundedRectangleBorder(radius=16),
        content=ft.Container(
            border=ft.Border.all(1, ft.Colors.with_opacity(0.2, color_)),
            border_radius=16,
            content=ft.Row(
                spacing=0,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[panel_izq, panel_der],
            ),
        ),
    )

    return ft.Container(content=card, margin=ft.Margin.only(bottom=12))
