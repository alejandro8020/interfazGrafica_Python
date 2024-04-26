import tkinter as tk
from tkinter import font 
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL,COLOR_CUERPO_PRINCIPAL,COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img


class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo_sameep.png",(300,136))
        self.perfil = util_img.leer_imagen("./imagenes/logo_sameep.png",(150,100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        #Configuracion inicial de ventana
        self.title('Scada - Sameep')
        self.iconbitmap("./imagenes/logo_sameep.ico")
        w, h = 1024,660
        util_ventana.centrar_ventana(self,w,h)
        

    def paneles(self):
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50, )
        self.barra_superior.pack(side=tk.TOP,fill='both')

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT,fill='both', expand=False)

        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def controles_barra_superior(self):
        #Configuracion de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        #Etiqueta de titulos
        self.labelTitulo = tk.Label(self.barra_superior, text="Sameep")
        self.labelTitulo.config(fg="#fff", font=("Roboto",15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        #Boton del menu lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(self.barra_superior, text="SCADA")
        self.labelTitulo.config(fg="#fff", font=("Roboto",10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        #Configuracion del menu lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome =  font.Font(family='FontAwesome', size=15)
        #Etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        #Boton del menu lateral
        self.buttonDashboard = tk.Button(self.menu_lateral)
        self.buttonProfile = tk.Button(self.menu_lateral)
        self.buttonPicture = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)
        self.buttonSettings = tk.Button(self.menu_lateral)

        button_info = [
            ("Dashboard", '\uf109', self.buttonDashboard),
            ("Profile", "\uf006", self.buttonProfile),
            ("Picture", "\uf03e", self.buttonPicture),
            ("Info", "\uf129",self.buttonInfo),
            ("Settings", "\uf013",self.buttonSettings)
        ]
        for text, icon, button in button_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo, bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f"{icon}  {text}", anchor="w", font=font_awesome,
                     bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        #Asociar eventos enter y leave con la funcion.
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self,event,button):
        #Cambia el estilo al pasar el raton por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')
    def on_leave(self, event, button):
        #Restaurar estilo al salir el raton
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        #Altera visibilidad del menu lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')


