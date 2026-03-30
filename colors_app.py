def color_por_icono(icono: str) -> str:
    mapa = {
        "TRENDING_UP":             "#006E1C",
        "TRENDING_DOWN":           "#B1416B",
        "BUILD_OUTLINED":          "#EB9D0E",
        "ACCOUNT_BALANCE_OUTLINED":"#4169E1",
        "PEOPLE_OUTLINE":          "#1D9E75",
        "BAR_CHART":               "#1D9E75",
        "SWAP_HORIZ":              "#7F77DD",
    }
    return mapa.get(icono, "#4169E1")

