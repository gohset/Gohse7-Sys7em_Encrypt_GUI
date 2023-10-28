#!/usr/bin/python
#-*- coding: latin-1 -*-
import tkinter
from tkinter import *

import customtkinter
from customtkinter import *
from tkinter import messagebox as msg
import os
from playsound import playsound

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from smtplib import SMTP
import socket
from email import encoders
import smtplib
import email.mime.multipart
import email.mime.base
#####################################################################
###################### DIRECTORIOS DE IMAGENES ######################
#####################################################################

directorio_principal = os.path.dirname(__file__)
carpeta_sonido = os.path.join(directorio_principal, "sonido")
carpeta_imagenes = os.path.join(directorio_principal, "imagen")
carpeta_iconos = os.path.join(directorio_principal, "iconos")

#####################################################################
####################### CONFIGURACION VENTANA #######################
#####################################################################
negro = "#010101"
ventana = CTk()
###################### LADO LATERAL HIZQUIERDO #####################
miFrame = CTkFrame(ventana, width=30, height=450, fg_color= negro)
miFrame.grid(column=0, row = 0, sticky='nsew',padx=10, pady =40)

################################ CENTRO #############################
miFrame2 = CTkFrame(ventana, width=400, height=450, fg_color="lime")
miFrame2.grid(column=1, row = 0, sticky='nsew',padx=10, pady =40)
############################## BARRA DE TAREA #######################
miFrame_barra_tarea = CTkFrame(ventana, width=400, height=40, fg_color="lime")
#miFrame_barra_tarea.grid(row=1, column=1)

################## LADO LATERAL DERECHA DESPLEGABLE #################
miFrame4 = CTkFrame(ventana, width=30, height=450, fg_color=negro)
miFrame3 = CTkFrame(ventana, width=30, height=450, fg_color=negro)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.resizable(False,False)
ventana.iconbitmap(os.path.join(carpeta_iconos, "Bird.ico"))
ventana.title("Gohse7-Sys7em")

#####################################################################
########################## CARGAR IMAGENES ##########################
#####################################################################

logo = PhotoImage(file= os.path.join(carpeta_imagenes, "logo4.png"))
img_config = PhotoImage(file= os.path.join(carpeta_imagenes, "x.png"))
img_buscar = PhotoImage(file= os.path.join(carpeta_imagenes, "buscar.png"))
img_executar = PhotoImage(file= os.path.join(carpeta_imagenes, "executar.png"))
img_xx = PhotoImage(file= os.path.join(carpeta_imagenes, "imgxx.png"))
img_xx3 = PhotoImage(file= os.path.join(carpeta_imagenes, "rancid.png"))
img_configuracion = PhotoImage(file= os.path.join(carpeta_imagenes, "config.png"))
img_correo = PhotoImage(file= os.path.join(carpeta_imagenes, "hotmail.png"))
img_gmail = PhotoImage(file= os.path.join(carpeta_imagenes, "gmail.png"))
img_hotmail = PhotoImage(file= os.path.join(carpeta_imagenes, "hotmail.png"))
#####################################################################
def logo():
    texto.configure(state="normal")
    texto.configure(font = ("Consolas", 8))
    a10 = " "
    a1 = "      @@@@@@@@               @@                                                    "
    a2 = "   @@                        @@                            @@                       "
    a3 = "  @@              @@@@@@    @@@@@@@@    @@@@@@    @@@@  @@@@@@@ @@@@@@@@@  @@@@@@@@@"
    a4 = "   @@    @@@@@@  @@    @@    @@    @@    @@      @@    @@  @@          @@         @@"
    a5 = "   II        II  II    II    II    II    IIIIII  IIIIIIII  II         II         II"
    a6 = "   IIII      II  II    II    II    II        II  II        II        II         II  "
    a7 = "       IIIIIIII  IIIIIIII    II    II    IIIIII    IIIIII  IIIIII    II        II  "
    a8 = "                                                                    II        II  "
    a9 = "                                                                    II        II  "
    texto.insert("0.0", "\n" + a9)
    texto.insert("0.0", "\n" + a8)
    texto.insert("0.0", "\n" + a7)
    texto.insert("0.0", "\n" + a6)
    texto.insert("0.0", "\n" + a5)
    texto.insert("0.0", "\n" + a4)
    texto.insert("0.0", "\n" + a3)
    texto.insert("0.0", "\n" + a2)
    texto.insert("0.0", "\n" + a1)
    texto.insert("0.0", "\n\n\n\n\n\n\n\n\n" + a10)
    texto.configure(state="disabled")


def info():
    #carpeta_imagenes = os.path.join(directorio_principal, "imagen")
    #dr1 = "C:/Users/admin/PycharmProjects/prueba1/Documentos"
    dr1 = txtbuscar.get()
    if os.path.exists(dr1) == True:  # Si existe la carpeta pasa de largo
        try:
            texto.configure(state="normal")
            texto.configure(font=("Consolas", 11))
            texto.delete("0.0", 'end')
            for archivo in os.listdir(dr1):
                # if archivo.endswith(".docx") or archivo.endswith(".doc"):
                d = os.path.join(dr1, archivo)
                texto.insert("0.0", "\n" + d)
            texto.configure(state="disabled")
            # print(d)
        except IOError:
            pass
def executar():

    if os.path.isfile(txtbuscar.get()):
        os.system(txtbuscar.get())
    else:
        pass
def informacion():
    msg.showinfo("Listo","[*] Encriptacion / Desencriptacion completa...")
def encrp_decrip_img():

    try:

        ruta = txtbuscar.get()
        #clave = int(input("[*] Ingrese la clave de encriptacion solo 2 digitos: "))
        clave = 77

        abrir = open(ruta, "rb")

        imagen = abrir.read()
        abrir.close()

        imagen = bytearray(imagen)

        for index, values in enumerate(imagen):
            imagen[index] = values ^ clave

        abrir = open(ruta, "wb")

        abrir.write(imagen)
        abrir.close()

        informacion()
        #time.sleep(2)
        #quit()
    except Exception:
        print("Error:", Exception.__name__)
def sonido():
    s = os.path.join(carpeta_sonido, 'HighpitchedCompute.mp3')
    playsound(s, bloque=True)

#############################################################################
######################### Botones lado derecho ##############################
#############################################################################
#global miFrame3
global lblimagenx

def info_imagenx(event):
    lblimagenx.configure(text="Encriptar/Desencriptar")

def info_imagenx3(event):
    lblimagenx.configure(text="Encriptar...")

def info_imagenx2(event):
    lblimagenx.configure(text=" ")
def config2():
    sonido()
    #global miFrame4
    ocultar4()
    global miFrame3
    global lblimagenx

    miFrame3 = CTkFrame(ventana, width=30, height=450, fg_color=negro)
    miFrame3.grid(column=2, row=0, sticky='nsew', padx=10, pady=40)

    btnimagenx = CTkButton(miFrame3, fg_color="#010101", text=" ", text_color="white", border_color="lime",
                           hover_color='#008000', corner_radius=12, border_width=2, image=img_xx, command=encrp_decrip_img)
    btnimagenx.grid(row=1, column=0)

    btnimagenx3 = CTkButton(miFrame3, fg_color="#010101", text=" ", text_color="white", border_color="lime",
                           hover_color='#008000', corner_radius=12, border_width=2, image=img_xx3)
    btnimagenx3.grid(row=2, column=0)

    lblimagenx = CTkLabel(miFrame3, text=" ")
    lblimagenx.grid(row=0, column=0)
    btnimagenx.bind("<Motion>", info_imagenx)
    btnimagenx3.bind("<Motion>", info_imagenx3)
    miFrame3.bind("<Motion>", info_imagenx2)

    boton2_1()

def config1():
    sonido()
    global miFrame3
    miFrame3.destroy()
    boton1()


#############################################################################
################# Boton para ocultar lado derecho ###########################
#############################################################################

# Boton para oculta el lado derecho...
def configurar(event):
    lblinfo.configure(text="Peligro")
def configurar2(event):
    lblinfo.configure(text="Peligro")

def boton1():
    btnconfig = CTkButton(miFrame, fg_color="#010101", text=" ", text_color="white", border_color="lime",
                          hover_color='#008000', corner_radius=12, border_width=2, image=img_config, command=config2)
    btnconfig.grid(row=1, column=0)
    btnconfig.bind("<Motion>", configurar)

# Boton oculto en la misma pocision para mostrar el lado derecho...
def boton2_1():
    btnconfig2 = CTkButton(miFrame, fg_color="#010101", text=" ", text_color="white", border_color="red",
                           hover_color='#008000', corner_radius=12, border_width=2, image=img_config, command=config1)
    btnconfig2.grid(row=1, column=0)
    btnconfig2.bind("<Motion>", configurar2)
##############################################################################
##############################################################################
boton1()

#############################################################################
################### Elementos del centro del programa #######################
#############################################################################
txtbuscar = CTkEntry(miFrame2, font=("Consolas", 11), width=400)
txtbuscar.grid(row=0, column=1)
txtbuscar.insert(0, directorio_principal)

texto = CTkTextbox(miFrame2, font=("Consolas", 11), width=400, height=250)
texto.grid(row=1, column=1)
texto.configure(state="disabled")

logo()
#############################################################################
##################### Boton del lado izquierdo ##############################
#############################################################################
lblinfo = CTkLabel(miFrame, text=" ")
lblinfo.grid(row=0, column=0)
btninfo = CTkButton(miFrame, fg_color="#010101", text=" ", text_color="white", border_color="lime",
                          hover_color='#008000', corner_radius=12, border_width=2, image=img_buscar, command=info)
btninfo.grid(row=2, column=0)
btnexecutar = CTkButton(miFrame, fg_color="#010101", text=" ", text_color="white", border_color="lime",
                          hover_color='#008000', corner_radius=12, border_width=2, image=img_executar, command=executar)
btnexecutar.grid(row=3, column=0)

btnconfiguracion = CTkButton(miFrame, fg_color="#010101", text=" ", text_color="white", border_color="lime",
                          hover_color='#008000', corner_radius=12, border_width=2, image=img_configuracion)
btnconfiguracion.grid(row=4, column=0)

#############################################################################
############ Eventos de los Boton del lado izquierdo ########################
#############################################################################
def info_fuera(event):
    lblinfo.configure(text=" ")
def info2(event):
    lblinfo.configure(text="Buscar")
def ejecutar(event):
    lblinfo.configure(text="Ejecutar")
def configuracion(event):
    lblinfo.configure(text="Configuracion")
def msg_correo(event):
    lblinfo.configure(text="Enviar correo")


btninfo.bind("<Motion>", info2)
btnexecutar.bind("<Motion>", ejecutar)
miFrame.bind("<Motion>", info_fuera)
btnconfiguracion.bind("<Motion>", configuracion)
#btncorreo.bind("<Motion>", msg_correo)


#############################################################################
################# Metodo de botones para Enviar correo ######################
#############################################################################

##############################################################################
#################### ENVIA POR CORREO EL ARCHIVO #############################
##############################################################################

def correo_hotmail():
    ##############################################################################
    ################ ENVIA POR CORREO EL ARCHIVO COMPRIMIDO ######################
    ##############################################################################
    try:
        #directorio_prueba = os.path.expanduser('~')  # Carpeta del usuario actual
        c = txtbuscar.get()
        #host = socket.gethostname()
        nusuario ="archovo_hotmail.txt"
        #nusuario = txtbuscar.get()

        msg = MIMEMultipart("plain")
        msg["From"] = "josedelgado7777@hotmail.com"
        msg["To"] = "gonzarias2@hotmail.com"

        msg["Subject"] = "-> ### Archivos enviado ###..."
        #archivo = MIMEBase('application', 'octect-stream') #-> Cuando son varios archovos o un .zip o .rar
        archivo = MIMEBase("multipart", "octect-stream") #-> Cuando es un solo archivo

        ##################################################################
        # -> ENVIAR UN ARCHIVO COMPRIMIDO
        ##################################################################
        archivo.set_payload(open(c, "rb").read())
        encoders.encode_base64(archivo)
        archivo.add_header('content-Disposition', "attachment; filename= %s" % nusuario)
        msg.attach(archivo)

        smtp = SMTP('smtp-mail.outlook.com', 587)
        smtp.starttls()

        smtp.login("josedelgado7777@hotmail.com", "setamercenary77")
        smtp.sendmail("josedelgado7777@hotmail.com", "gonzarias2@hotmail.com", msg.as_string())

        smtp.quit()
        mensaje_enviado()
        # Realiza la eliminacion de la carpeta creada y todos los archivos que contiene...
        #shutil.rmtree(c)
    except IOError:
        pass
        #print("no conecto1...")

def correo_gmail():
    try:
        c = txtbuscar.get()
        # host = socket.gethostname()
        nusuario = "archovo_gmail.txt"
        # nusuario = txtbuscar.get()

        # Crea la conexión SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        correo = 'cuentadeseguridades@gmail.com'
        pas = 'wvnnworrigcreboe'
        # Inicia sesión en tu cuenta de Gmail
        server.starttls()
        server.login(correo, pas)

        # Definir el remitente y destinatario del correo electrónico
        remitente = "cuentadeseguridades@gmail.com"
        destinatario = "cuentadeseguridades@gmail.com"

        # Crear el mensaje del correo electrónico
        mensaje = email.mime.multipart.MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = "Correo electrónico con archivo adjunto"

        # Añadir el cuerpo del mensaje
        cuerpo = "-> Archivos enviado satisfactoriamente..."
        mensaje.attach(email.mime.text.MIMEText(cuerpo, 'plain'))

        # Añadir el archivo Excel como adjunto
        adjunto = email.mime.base.MIMEBase('application', 'octet-stream')
        #adjunto.set_payload(open(os.path.join(c, nusuario), "rb").read())
        adjunto.set_payload(open(c, "rb").read())
        email.encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', "attachment; filename= %s" % nusuario)
        mensaje.attach(adjunto)

        # Convertir el mensaje a texto plano
        texto = mensaje.as_string()

        # Enviar el correo electrónico
        server.sendmail(remitente, destinatario, texto)
        server.quit()
        mensaje_enviado()
        # Realiza la eliminacion de la carpeta creada y todos los archivos que contiene...
        #shutil.rmtree(c)
    except IOError:
        pass
        # print("no conecto1...")

#############################################################################
######################### Botones lado derecho 2 ############################
#############################################################################
#global miFrame4
global lblimagenx4
def mensaje_enviado():
    msg.showinfo("Correo","[*] Archivo enviado...")
def msg_gmail(event):
    lblimagenx4.configure(text="Gmail")
def msg_hotmail(event):
    lblimagenx4.configure(text="Hotmail/Outlook")

def info_imagenx4(event):
    lblimagenx4.configure(text=" ")
def mostrar4():
    global miFrame3
    config1()
    global miFrame4
    global lblimagenx4

    miFrame4 = CTkFrame(ventana, width=30, height=450, fg_color=negro)
    miFrame4.grid(column=2, row=0, sticky='nsew', padx=10, pady=40)

    btngmail = CTkButton(miFrame4, fg_color="#010101", text=" ", border_color="lime",
                         hover_color='#008000', corner_radius=12, border_width=2, image=img_gmail, command=correo_gmail)
    btngmail.grid(row=1, column=0)

    btnhotmail = CTkButton(miFrame4, fg_color="#010101", text=" ", border_color="lime",
                           hover_color='#008000', corner_radius=12, border_width=2, image=img_hotmail, command=correo_hotmail)
    btnhotmail.grid(row=2, column=0)

    lblimagenx4 = CTkLabel(miFrame4, text=" ")
    lblimagenx4.grid(row=0, column=0)

    btngmail.bind("<Motion>", msg_gmail)
    btnhotmail.bind("<Motion>", msg_hotmail)
    miFrame4.bind("<Motion>", info_imagenx4)

    boton_correo2()

def ocultar4():
    global miFrame4
    miFrame4.destroy()
    boton_correo1()


#############################################################################
################# Boton para ocultar lado derecho 2 #########################
#############################################################################
# Boton para oculta el lado derecho...
def configurar4(event):
    lblinfo.configure(text="Peligro")

def boton_correo1():
    btncorreo = CTkButton(miFrame, fg_color="#010101", text=" ", border_color="lime",
                          hover_color='#008000', corner_radius=12, border_width=2, image=img_hotmail, command=mostrar4)
    btncorreo.grid(row=5, column=0)
    btncorreo.bind("<Motion>", msg_correo)

# Boton oculto en la misma pocision para mostrar el lado derecho...
def boton_correo2():
    btncorreo2 = CTkButton(miFrame, fg_color="#010101", text=" ", border_color="red",
                          hover_color='#008000', corner_radius=12, border_width=2, image=img_hotmail, command=ocultar4)
    btncorreo2.grid(row=5, column=0)
    #btncorreo2.bind("<Motion>", msg_correo)
##############################################################################
##############################################################################
boton_correo1()


#ventana.call('wm', 'iconphoto', ventana._w, logo)
ventana.mainloop()
