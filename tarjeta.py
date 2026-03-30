import flet as ft
# ─── Widget: Tarjeta de Anuncio ───────────────────────────────────────────────


def actualizar_card(nueva_data,page: ft.Page,lista,funcion_alerta):
        # Reemplazamos los controles viejos por las tarjetas nuevas
        lista.controls = [crear_tarjeta(m, page, funcion_alerta) for m in nueva_data]
        page.update() # Refresca solo esta parte de la pantalla

def crear_tarjeta(anuncio: dict, page: ft.Page,al_activar):





    alarm_icon = ft.IconButton(
        icon=ft.icons.Icons.ALARM_ADD_OUTLINED,
        icon_color=ft.Colors.with_opacity(0.4, ft.Colors.ON_SURFACE),
        icon_size=20,
        tooltip="Alarma",
    )

    def toggle_alarm(e):
        anuncio["alarm"] = not anuncio["alarm"]
        alarm_icon.icon = ft.icons.Icons.ALARM if anuncio["alarm"] else ft.icons.Icons.ALARM_ADD_OUTLINED
        alarm_icon.icon_color = ft.Colors.RED_400 if anuncio["alarm"] else ft.Colors.with_opacity(0.4, ft.Colors.ON_SURFACE)
        if anuncio["alarm"]:
            al_activar(e)
            #obtener_datos(e)
        page.update()

    alarm_icon.on_click = toggle_alarm



    ##############################
    ##############################

    # ── Ratio riesgo/beneficio (solo visible si selecciona Profit) ──
    campo_total   = ft.TextField(label="Total ($)",    width=110, keyboard_type=ft.KeyboardType.NUMBER, dense=True)

   
    #campo_beneficio.on_change = calcular_ratio

    seccion_ratio = ft.Container(
        visible=False,
        margin=ft.Margin.only(top=8),
        padding=ft.Padding.all(12),
        border_radius=12,
        bgcolor=ft.Colors.with_opacity(0.06, "#006E1C"),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.2, "#006E1C")),
        content=ft.Column(
            spacing=8,
            controls=[
                ft.Text("📈 Monto", size=12, weight=ft.FontWeight.W_600,
                        color=ft.Colors.with_opacity(0.7, ft.Colors.ON_SURFACE)),
                ft.Row(controls=[campo_total], spacing=8)
            ],
        ),
    )





    # ── Estado seleccionado ──
    resultado_seleccionado = ft.Text("", size=12, weight=ft.FontWeight.W_600)
    estado_actual = [None]
    popup_visible = [False]

    def hacer_btn_opcion(label, color, icono, key):
        def on_click(e):
            estado_actual[0] = key
            resultado_seleccionado.value = f"{icono} {label}"
            resultado_seleccionado.color = color
            seccion_ratio.visible = (key == "profit" or key =="perdida")
            if key != "profit" and key !="perdida":
                campo_total.value = ""
            popup_visible[0] = False
            popup_container.visible = False
            #btn_ver.text = "Ver más"
            page.update()



        return ft.Button(
            content=ft.Row(
                controls=[ft.Icon(icono, size=16, color=color), ft.Text(label, size=13, color=color)],
                spacing=6,
                tight=True,
            ),
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.with_opacity(0.08, color),
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                elevation=0,
            ),
            on_click=on_click,
        )

    popup_container = ft.Container(
        visible=False,
        margin=ft.Margin.only(top=6),
        padding=ft.Padding.all(10),
        border_radius=12,
        bgcolor=ft.Colors.SURFACE,
        border=ft.Border.all(1, ft.Colors.with_opacity(0.15, ft.Colors.OUTLINE)),
        shadow=ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.with_opacity(0.12, ft.Colors.SHADOW),
            offset=ft.Offset(0, 4),
        ),
        content=ft.Column(
            spacing=6,
            controls=[
                ft.Text("¿Cómo resultó esta operación?", size=11,
                        color=ft.Colors.with_opacity(0.55, ft.Colors.ON_SURFACE)),
                ft.Row(
                    spacing=6,
                    wrap=True,
                    controls=[
                        hacer_btn_opcion("Profit",   "#006E1C", ft.icons.Icons.TRENDING_UP,            "profit"),
                        hacer_btn_opcion("Pérdida",  "#B3261E", ft.icons.Icons.TRENDING_DOWN,           "perdida"),
                        hacer_btn_opcion("No Operé", "#6750A4", ft.icons.Icons.REMOVE_CIRCLE_OUTLINE,   "no_opere"),
                    ],
                ),
            ],
        ),
    )

    btn_ver = ft.IconButton(
    icon=ft.icons.Icons.ADD,
    icon_color=ft.Colors.PRIMARY, # Resalta usando el color principal de la app
    icon_size=24,                 # Aumentar un poco el tamaño ayuda
    tooltip="Añadir Comentario",
)

    def toggle_popup(e):
        popup_visible[0] = not popup_visible[0]
        popup_container.visible = popup_visible[0]
        btn_ver.text = "Cerrar" if popup_visible[0] else "Ver más"
        page.update()

    btn_ver.on_click = toggle_popup

    es_señal = anuncio.get("etiqueta", "").lower() in ['señal']
    etiqueta='Anuncio'
    if es_señal:
        etiqueta='Señal 📈📉'

    fila_entradas = ft.Row(
        spacing=16,
        visible=es_señal,
        controls=[
            ft.Text("E1: ", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)),
            ft.Text(anuncio.get("entrada1", ""), size=13, weight=ft.FontWeight.W_600, color=anuncio["color"]),
            ft.Text("E2: ", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)),
            ft.Text(anuncio.get("entrada2", ""), size=13, weight=ft.FontWeight.W_600, color=anuncio["color"]),
        ],
    )

    fila_sl_tp = ft.Row(
        spacing=16,
        visible=es_señal,
        controls=[
            ft.Text("SL: ", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)),
            ft.Text(anuncio.get("sl", ""), size=13, weight=ft.FontWeight.W_600, color=ft.Colors.RED_400),
            ft.Text("TP: ", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE)),
            ft.Text(anuncio.get("tp", ""), size=13, weight=ft.FontWeight.W_600, color="#006E1C"),
        ],
    )


    ##################################################
    ##################################################
    ##################################################
    try:
        active= "Trade Historico" if anuncio["active"] == 0 else "Trade Activo"
        active=anuncio['autor'] if anuncio['etiqueta']=='Anuncio' else active
    except:active=anuncio['autor']
    if anuncio['icono']=='TRENDING_UP':
        color_='#006E1C'
    elif anuncio['icono']=='TRENDING_DOWN':
        color_='#B1416B'
    elif anuncio['icono']=='BUILD_OUTLINED':
        color_="#EB9D0E"
    else:
        color_='#4169E1'

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
                    ft.Row(
                        controls=[
                            ft.Container(
                                width=42, height=42, border_radius=12,
                                bgcolor=ft.Colors.with_opacity(0.12, color_),
                                content=ft.Icon(getattr(ft.icons.Icons,anuncio["icono"], ft.icons.Icons.HELP_OUTLINE), color=color_, size=22),

                                #content=getattr(ft.icons,anuncio["icono"], ft.icons.HELP_OUTLINE),
                                alignment=ft.alignment.Alignment.CENTER,
                            ),
                            ft.Container(width=0),
                            ft.Column(
                                spacing=2, expand=True,
                                controls=[
                                    ft.Text(active, size=12, weight=ft.FontWeight.W_600,
                                            color=ft.Colors.with_opacity(0.6, ft.Colors.ON_SURFACE)),
                                    ft.Text(anuncio["fecha"], size=11,
                                            color=ft.Colors.with_opacity(0.45, ft.Colors.ON_SURFACE)),
                                ],
                            ),
                            alarm_icon,
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    
                    ##################################################
                    ##################################################
                    ft.Container(height=10),
                    ft.Text(anuncio["titulo"], size=15, weight=ft.FontWeight.W_600, color=ft.Colors.ON_SURFACE),
                    ft.Container(height=6),
                    
                    ft.Container(
                        height=180,
                        border_radius=12,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Image(
                            src=anuncio["imagen"],
                            fit="cover",
                            width=float("inf"),
                        ),
                    ) if anuncio.get("imagen") else ft.Container(),
                    ft.Container(height=8),
                    
                    ft.Text(
                        anuncio["descripcion"],
                        max_lines=2,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        size=13,
                        color=ft.Colors.with_opacity(0.7, ft.Colors.ON_SURFACE),
                    ),
                    

                    ft.Container(height=6),

                
                    
                    fila_entradas,fila_sl_tp,


                    ##################################################
                    ##################################################
                    ft.Container(height=8),
                    ft.Row(
                        controls=[
                            ft.Container(
                                padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                                border_radius=20,
                                bgcolor=ft.Colors.with_opacity(0.1, color_),
                                content=ft.Text(etiqueta, size=15, weight=ft.FontWeight.W_800, color=color_),
                            ),
                            ft.Container(width=8),
                            resultado_seleccionado,
                            ft.Row(expand=True),
                            btn_ver,
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    popup_container,
                    seccion_ratio,
                ],
            ),
        ),
    )
    return ft.Container(content=card, margin=ft.Margin.only(bottom=12))