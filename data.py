import flet as ft
import requests
import json
import os,hashlib


def cargar_cache_local(endpoint):
    """Lee el caché instantáneamente. Devuelve (hash_local, datos_cacheados)"""
    cache_file = f'cache_{endpoint}.json'
    try:
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='utf-8') as f:
                local_cache = json.load(f)
                return local_cache.get('hash'), local_cache.get('data')
    except (json.JSONDecodeError, KeyError):
        pass
    
    return None, None

def verificar_mensajes(msg,callback_actualizar_ui):
    mensajes= json.dumps(msg)
    callback_actualizar_ui(mensajes)

def verificar_api_en_segundo_plano(endpoint, local_hash, callback_actualizar_ui):
    """Consulta la API sin congelar la app y avisa si hay cambios."""
    cache_file = f'cache_{endpoint}.json'
    url = f" http://127.0.0.1:8000/{endpoint}" 
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error de red silencioso: {e}")
        return # Si falla el internet, simplemente no hacemos nada y la UI se queda con el caché

    server_text = response.text
    server_hash = hashlib.md5(server_text.encode('utf-8')).hexdigest()

    if local_hash == server_hash:
        print("La info en la API es idéntica al caché. No se mueve la UI.")
    else:
        print("¡Info nueva detectada! Actualizando caché y UI...")
        new_data = response.json()
        
        # Guardamos el nuevo caché
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump({'hash': server_hash, 'data': new_data}, f)
        
        # Llamamos a la función que redibuja la interfaz con los datos nuevos
        callback_actualizar_ui(new_data)


def get_data_with_hash_check(endpoint):
    cache_file = f'cache_{endpoint}.json'
    try:
        if os.path.exists(cache_file):
            with open(cache_file, 'r', encoding='utf-8') as f:
                local_cache = json.load(f)
                local_hash = local_cache.get('hash')
                cached_data = local_cache.get('data')
        else:
            local_hash = None
            cached_data = None
    except (json.JSONDecodeError, KeyError):
        local_hash = None
        cached_data = None


    url = f"https://tradingapp-eeix.onrender.com/{endpoint}" 
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza error si la API falla (ej. error 500 o 404)
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        # Si falla el internet o la API, devolvemos el caché si existe
        return cached_data if cached_data else []



    # 3. Crear un hash a partir del texto crudo que llegó del servidor
    server_text = response.text
    # Usamos MD5 para crear una firma única y corta de todo el texto
    server_hash = hashlib.md5(server_text.encode('utf-8')).hexdigest()
    print(server_hash)
    print(server_text)
    if local_hash == server_hash and cached_data is not None:
        print("La info es idéntica a la del caché. No se actualiza UI.")
        return cached_data
    else:
        print("Info distinta o caché vacío. Actualizando...")
        new_data = response.json() # Convertimos a diccionario/lista de Python
        
        # Guardamos el nuevo hash y la nueva data
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump({'hash': server_hash, 'data': new_data}, f)
            
        return new_data
    






blog = [
    {   "id":1,
        "titulo": "1. Los 10 Principios de la Economía",
        "meta_description":"Mankiw comienza su obra estableciendo 10 principios que rigen cómo las personas toman decisiones y cómo funciona la economía en su conjunto. Los últimos tres son los pilares de la",
        "description": 
        
        """macroeconomía:

Principio 8: El nivel de vida de un país depende de su capacidad para producir bienes y servicios (Productividad).
Principio 9: Cuando el gobierno imprime demasiado dinero, los precios se incrementan (Inflación).
Principio 10: La sociedad enfrenta a corto plazo una disyuntiva entre inflación y desempleo (Curva de Phillips)."""
        
        ,
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "color": "#6750A4",
        "etiqueta": "Anuncio",
    },
    {
        "id":2,
        "titulo": '2. Identidades y "Leyes" Clave en el Texto',
        "meta_description":"nosonosoands",
        "description": "Nos complace anunciar el inicio del nuevo ciclo de actividades. Esperamos contar con su participación activa en todos los eventos programados este trimestre.",
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "color": "#6750A4",
        "etiqueta": "Anuncio",
    },{
        "id":3,
        "titulo": "3. El Modelo de Oferta y Demanda Agregada",
        "meta_description":"nosonosoands",
        "description": "Nos complace anunciar el inicio del nuevo ciclo de actividades. Esperamos contar con su participación activa en todos los eventos programados este trimestre.",
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "color": "#6750A4",
        "etiqueta": "Anuncio",
    },
    ]
macros = [
    {   "category":"Tasas",
        "badge_text": "Sin Cambio",
        "title":"Tasa de Interes",
        "unit": "% tasa de referencia",
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "badge_color": "#6750A4",
        "badge_bg": "#6750A4",
        "value": 4.25,
        "meta_description": "El Ba",
        "description": "El Banco Central mantuvo tasas sin cambio en su reunión de marzo, a la espera de más datos",
        "previous_label": "Dato anterior",
        "previous_value": "4.5%",
        "date": "Febrero 2026",
    },{   "category":"Tasas",
        "badge_text": "Déficit",
        "title":"Tasa de Interes",
        "unit": "% tasa de referencia",
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "badge_color": "#6750A4",
        "badge_bg": "#6750A4",
        "value": 4.25,
        "meta_description": "El Ba",
        "description": "El Banco Central mantuvo tasas sin cambio en su reunión de marzo, a la espera de más datos",
        "previous_label": "Dato anterior",
        "previous_value": "4.5%",
        "date": "Febrero 2026",
    }]
macros = [
    {
        "category": "Tasas",
        "badge_text": "Déficit",
        "titulo": "Tasa de Interés",
        "unit": "% tasa de referencia",
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "badge": "↑ Alta",
        "badge_color": "#226424",
        "badge_bg": "#72C275",
        "value": 4.25,
        "meta_description": "El Ba",
        "description": "El Banco Central mantuvo tasas sin cambio en su reunión de marzo, a la espera de más datos",
        "previous_label": "Dato anterior",
        "previous_value": "4.5%",
        "date": "Febrero 2026",
    },
    {
        "category": "Tasas",
        "badge_text": "Sin cambio",
        "titulo": "Tasa de Interés",
        "unit": "% tasa de referencia",
        "icono": ft.icons.Icons.CAMPAIGN_OUTLINED,
        "badge": "↑ Alta",
        "badge_color": "#226424",
        "badge_bg": "#72C275",
        "value": 2.25,
        "meta_description": "El Ba",
        "description": "El Banco Central mantuvo tasas sin cambio en su reunión de marzo, a la espera de más datos",
        "previous_label": "Dato anterior",
        "previous_value": "4.5%",
        "date": "Febrero 2026",
    },
    # === Los 3 nuevos datos ===

    {
        "category": "Inflación",
        "badge_text": "Baja",
        "titulo": "Inflación Mensual",
        "unit": "% variación mensual",
        "icono": ft.icons.Icons.TRENDING_UP,
        "badge": "↑ Alta",
        "badge_color": "#226424",
        "badge_bg": "#72C275",
        "value": 0.4,
        "meta_description": "El Ba",
        "description": "La inflación de marzo sorprendió al alza por el aumento en precios de alimentos y transporte",
        "previous_label": "Dato anterior",
        "previous_value": "0.2%",
        "date": "Marzo 2026",
    },
    {
        "category": "Empleo",
        "badge_text": "Positivo",
        "titulo": "Tasa de Desempleo",
        "unit": "% de la fuerza laboral",
        "icono": ft.icons.Icons.WORK_OUTLINE,
        "badge": "↑ Alta",
        "badge_color": "#226424",
        "badge_bg": "#72C275",
        "value": 8.1,
        "meta_description": "El Ba",
        "description": "La tasa de desempleo subió ligeramente debido a la desaceleración en el sector construcción",
        "previous_label": "Dato anterior",
        "previous_value": "7.8%",
        "date": "Febrero 2026",
    },
    {
        "category": "Crecimiento",
        "badge_text": "Expansión",
        "titulo": "IMACEC Mensual",
        "unit": "% variación interanual",
        "icono": ft.icons.Icons.SHOW_CHART,
        "badge": "↑ Alta",
        "badge_color": "#226424",
        "badge_bg": "#72C275",
        "value": 2.3,
        "meta_description": "El Ba",
        "description": "El IMACEC de febrero mostró un crecimiento moderado, impulsado principalmente por el sector minería",
        "previous_label": "Dato anterior",
        "previous_value": "1.9%",
        "date": "Febrero 2026",
    }
]
MACRO_DATA = [
    {
        "cat": "inflacion",
        "numero": "3.2%",
        "numero_label": "IPC anual",
        "titulo": "Inflación EE.UU. (CPI)",
        "descripcion": "El índice de precios al consumidor aumentó 3.2% interanual en febrero, impulsado por energía y servicios.",
        "detalle": "La inflación núcleo (sin alimentos ni energía) se ubicó en 3.8%. La Fed mantiene su objetivo en 2%, por lo que se espera que las tasas sigan elevadas durante 2026.",
        "anterior": "Anterior: 3.1%",
        "fecha": "Feb 2026",
        "icono": "TRENDING_UP",
        "badge": "↑ Alta",
        "badge_color": "#B3261E",
    },
    {
        "cat": "empleo",
        "numero": "151K",
        "numero_label": "nóminas no agrícolas",
        "titulo": "Nóminas EE.UU. (NFP)",
        "descripcion": "Se crearon 151,000 empleos en febrero, levemente por debajo de las expectativas de 160K.",
        "detalle": "La tasa de desempleo se mantuvo en 4.1%. El sector salud y ocio lideró las contrataciones. El salario promedio creció 0.3% mensual.",
        "anterior": "Anterior: 125K",
        "fecha": "Feb 2026",
        "icono": "PEOPLE_OUTLINE",
        "badge": "↑ Positivo",
        "badge_color": "#006E1C",
    },
    {
        "cat": "tasas",
        "numero": "4.25%",
        "numero_label": "tasa de referencia",
        "titulo": "Fed Funds Rate",
        "descripcion": "La Reserva Federal mantuvo tasas sin cambio en su reunión de marzo, a la espera de más datos.",
        "detalle": "El dot plot sugiere dos recortes posibles en 2026. La incertidumbre en inflación y mercado laboral mantiene a la Fed en pausa. Próxima reunión: mayo.",
        "anterior": "Anterior: 4.50%",
        "fecha": "Mar 2026",
        "icono": "ACCOUNT_BALANCE_OUTLINED",
        "badge": "Sin cambio",
        "badge_color": "#4169E1",
    },
    {
        "cat": "pib",
        "numero": "2.4%",
        "numero_label": "crecimiento anual",
        "titulo": "PIB EE.UU. Q4 2025",
        "descripcion": "La economía creció 2.4% en el cuarto trimestre, superando las previsiones del consenso de 2.1%.",
        "detalle": "El consumo privado aportó el mayor impulso (+2.9%), mientras que la inversión empresarial se desaceleró. El mercado de vivienda se contrajo por segundo trimestre.",
        "anterior": "Q3 2025: 3.1%",
        "fecha": "Q4 2025",
        "icono": "BAR_CHART",
        "badge": "↑ Expansión",
        "badge_color": "#1D9E75",
    },
    {
        "cat": "inflacion",
        "numero": "2.6%",
        "numero_label": "IPCA zona euro",
        "titulo": "Inflación Eurozona",
        "descripcion": "La inflación en la zona euro bajó a 2.6% en febrero, acercándose al objetivo del BCE del 2%.",
        "detalle": "La moderación fue generalizada. Alemania y Francia reportaron datos por debajo del promedio. El BCE podría realizar otro recorte en junio.",
        "anterior": "Anterior: 2.8%",
        "fecha": "Feb 2026",
        "icono": "TRENDING_DOWN",
        "badge": "↓ Bajando",
        "badge_color": "#EB9D0E",
    },
    {
        "cat": "comercio",
        "numero": "-131B",
        "numero_label": "USD balanza comercial",
        "titulo": "Déficit comercial EE.UU.",
        "descripcion": "El déficit se amplió a 131 mil millones en enero, máximo histórico, por alza de importaciones.",
        "detalle": "Las importaciones de bienes de consumo y farmacéuticos lideraron el alza. Las exportaciones de servicios tecnológicos moderaron parcialmente el impacto.",
        "anterior": "Anterior: -98B",
        "fecha": "Ene 2026",
        "icono": "SWAP_HORIZ",
        "badge": "↑ Déficit",
        "badge_color": "#7F77DD",
    },
]
 
CATEGORIAS = ["Todos", "inflacion", "empleo", "tasas", "pib", "comercio"]
CAT_LABELS = {
    "Todos": "Todos",
    "inflacion": "Inflación",
    "empleo": "Empleo",
    "tasas": "Tasas",
    "pib": "PIB",
    "comercio": "Comercio",
}