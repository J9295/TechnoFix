def centrar_ventana(ventana,appwidth,appheight):
    screen_ancho = ventana.winfo_screenwidth()
    screen_largo = ventana.winfo_screenheight()
    x = int((screen_ancho/2) - (appwidth/2))
    y = int((screen_largo/2) - (appheight/2))
    return ventana.geometry(f"{appwidth}x{appheight}+{x}+{y}")