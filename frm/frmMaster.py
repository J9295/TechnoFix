import tkinter as tk
from tkinter import font
from cfg import *
import util.UtilVentana as UtilVentana
import util.UtilImg as UtilImg
#import fontawesome as fa
#from fontawesome import *
from PIL import Image, ImageTk


class frmMaster(tk.Tk):

    
    
    def __init__(self):
        super().__init__()
        
        # Cargando Imagenes
        self.logo = UtilImg.read_img("./img/LogoCompleto.png",(560,250))
        self.perfil = UtilImg.read_img("./img/me.jpg",(100,100))
        sizeIconTop = 16, 16
        sizeIconSide = 30, 30
        self.wbtn = 170
        self.hbtn = 38
        
        #Cargando Iconos
        self.IconBarra = UtilImg.read_img("./icon/menu.png",(sizeIconTop))
        self.IconDash = UtilImg.read_img("./icon/analisis.png",(sizeIconSide))
        self.IconCuenta = UtilImg.read_img("./icon/cuenta.png",(sizeIconSide))
        self.IconInfo = UtilImg.read_img("./icon/informacion.png",(sizeIconSide))
        self.IconLogo = UtilImg.read_img("./icon/logo.png",(sizeIconSide))
        self.IconCfg = UtilImg.read_img("./icon/configuraciones.png",(sizeIconSide))
        
        # Configuramos Ventana
        self.cfg_windows()
        # cargamos los Paneles o Frames
        # Esqueleto de la app
        self.paneles()
        
        # cargamos controles 
        self.ctr_topbar()
        self.ctr_sidebar()
        
    def cfg_windows(self):
        # Confoguracion Inicial de la vevntana
        icono = tk.PhotoImage(file="./img/icon-16.png")
        self.iconphoto(True,icono)
        # Colocamos Titulo de Ventana
        self.title(appTitle + ' GUI')
        # Establecemos el Icono de la App en .ico
       # self.iconbitmap("img/logo.ico")
        #self.iconbitmap("./img/logo.png")
        # Establecemos Tamaño de la Ventana en pixeles
        #w, h = 1024, 768
        #self.geometry("%dx%d+0+0" % (w, h))
        UtilVentana.centrar_ventana(
            self,
            mainwidth,
            mainheight
            )
        
    def paneles(self):
        # Crear Paneles de trabajo 
        
        # Barra Superior , Menu Lateral y body
        self.topbar = tk.Frame(
            self, 
            bg = topbar_color, 
            height = topbarheight
        )
        # aplicamos pack para posicionarlo topbar
        self.topbar.pack(
            side = tk.TOP,
            fill = 'both'
        )
        
        # Creamos barra lateral sidebar
        self.sidebar = tk.Frame(
            self,
            bg = sidebar_color,
            width = sidebarwidth
        )
        # Posicionamos el sidebar a la izquierda y evitamos q expanda
        self.sidebar.pack(
            side = tk.LEFT,
            fill = 'both',
            expand = False
        )
        
        # Creamos el MainBody
        self.mainbody = tk.Frame(
            self,
            bg = mainbody_color,
            #width = mainbodywidth
        )
        
        self.mainbody.pack(
            side = 'right',
            fill = 'both',
            expand = True 
        )
        
    def ctr_topbar(self):   
        # Configuracion TopBar
        font_awesome = font.Font(family="FontAwesome", size = 12)
        
        
        # etiqueta titulo
        self.lblTitulo = tk.Label(
            self.topbar,
            text = appTitle  
            )
        # Configuramos etiqueta
        self.lblTitulo.config(
            fg = "#fff",
            font = ("Roboto", 18, ),
            bg = topbar_color,
            pady = 5,
            width = 12
        )
        # Ubicamos la etiqueta
        self.lblTitulo.pack(side = tk.LEFT)
        #icnBarra = self.IconBarra
        # img_btn = ImageTk.PhotoImage(Image.open('./img/lista.png'))
        
        # Boton topbar
        self.cmdSideMenu = tk.Button(
            self.topbar,
            bg = topbar_color,
            bd = 0,
            width = 25,
            height = 25,
            fg = topbar_color,
            font = font_awesome,
            image = self.IconBarra,
            compound = tk.CENTER,
            
            #text='',
            #command = self.toggle_panel,    
        )
        
        self.cmdSideMenu.pack(side = tk.LEFT)
        self.bindHoverEvents(self.cmdSideMenu)
        
         # etiqueta titulo1
        self.lblTitulo1 = tk.Label(
            self.topbar,
            text = "appTitle"  
            )
        # Configuramos etiqueta
        self.lblTitulo1.config(
            fg = "#fff",
            font = ("Roboto", 14 ),
            bg = topbar_color,
            padx = 18,
            width = 20
        )
        # Ubicamos la etiqueta
        self.lblTitulo1.pack(side = tk.RIGHT)
        
    def ctr_sidebar(self):
        
        anchoMenu = 35
        altoMenu = 2 
        font_awesome = font.Font(family = 'FontAwesome', size = 15)  

        
        self.lblPerfil = tk.Label(
            self.sidebar, 
            image=self.perfil,
            bg = sidebar_color 
        )
        self.lblPerfil.pack(
            side = tk.TOP,
            pady = 10
        )
        
        
        
        ### Boton DashBoard
        self.cmdDash = tk.Button(
            self.sidebar,
            bg = IconSidebarColor,
            background = sidebar_color,
            width = self.wbtn,
            height = self.hbtn,
            font = ("Roboto",16,),
            bd = 0,
            fg = sidebar_color,
            text= "DashBoard     ",
            #command = self.toggle_panel,
            )
        ### Configuramos Icono
        self.cmdDash.config(
            image = self.IconDash,
            compound = tk.LEFT,
            padx = 35
            )
        self.cmdDash.pack(side = tk.TOP)
        self.bindHoverEvents(self.cmdDash)
        
        
        ### Boton Terminados
        self.cmdCuenta = tk.Button(
            self.sidebar,
            bg = sidebar_color,
            width = self.wbtn,
            height = self.hbtn,
            font = ("Roboto",16,),
            bd = 0,
            fg = sidebar_color,
            text= "Terminados    ",
            
            #command = self.toggle_panel,
            )
        ### Configuramos Icono
        self.cmdCuenta.config(
            image = self.IconCuenta,
            compound = tk.LEFT,
            padx = 35
            )
        self.cmdCuenta.pack(side = tk.TOP)
        self.bindHoverEvents(self.cmdCuenta)
        
        ### Boton Servicio
        self.cmdPicture = tk.Button(
            self.sidebar,
            bg = sidebar_color,
            width = self.wbtn,
            height = self.hbtn,
            font = ("Roboto",16,),
            bd = 0,
            fg = sidebar_color,
            text= "Servicios       ",
            
            #command = self.toggle_panel,
            )
        ### Configuramos Icono
        self.cmdPicture.config(
            image = self.IconLogo,
            compound = tk.LEFT,
            padx = 35
            )
        self.cmdPicture.pack(side = tk.TOP)
        self.bindHoverEvents(self.cmdPicture)
        
        ### Boton Informacion
        self.cmdInfo = tk.Button(
            self.sidebar,
            bg = sidebar_color,
            width = self.wbtn,
            height = self.hbtn,
            font = ("Roboto",16,),
            bd = 0,
            fg = sidebar_color,
            text= "Informacion   ",
            
            #command = self.toggle_panel,
            )
        ### Configuramos Icono
        self.cmdInfo.config(
            image = self.IconInfo,
            compound = tk.LEFT,
            padx = 35
            )
        self.cmdInfo.pack(side = tk.TOP)
        self.bindHoverEvents(self.cmdInfo)
        
        
        ### Boton Config
        self.cmdCfg = tk.Button(
            self.sidebar,
            bg = sidebar_color,
            width = self.wbtn,
            height = self.hbtn,
            font = ("Roboto",16,),
            bd = 0,
            fg = sidebar_color,
            text= "Configuracion",
            
            #command = self.toggle_panel,
            )
        ### Configuramos Icono
        self.cmdCfg.config(
            image = self.IconCfg,
            compound = tk.LEFT,
            padx = 35
            )
        self.cmdCfg.pack(side = tk.TOP)
        self.bindHoverEvents(self.cmdCfg)
        
    def cfgcmdmenu(
        self, 
        button, 
        text, 
        icon, 
        font_awesome, 
        anchoMenu, 
        altoMenu ):
        button.config(
            text=f"  {icon}   {text}", 
            anchor="w", 
            font=font_awesome, 
            bd=0, 
            bg=sidebar_color, 
            fg="white", 
            width=anchoMenu, 
            height=altoMenu )
        button.pack(side=tk.TOP)
        self.bindHoverEvents(button)
    
    def bindHoverEvents(self, button):
        # Asociar evento enter y leave con funcion dinamica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar el estilo al pasar el mouse
        button.config(bg=rollover_color, fg = topbar_color)
        
    def on_leave(self, event, button):
        # Cambiar el estilo al pasar el mouse
        button.config(bg=sidebar_color, fg = sidebar_color)
        
    