from tkinter import *

import speedtest

def Check():
    
    try:
        
        root=speedtest.Speedtest()
        root.get_servers()

        download=str(round(root.download()/(10**6),3))+" Mbps"
        upload=str(round(root.upload()/(10**6),3))+" Mbps"

        label_download_result.config(text=download)
        label_upload_result.config(text=upload)
        
    except:
        
        print("Not connected to internet!")
        
root=Tk()

root.title("Internet Speed Test")
root.geometry("500x600")
root.config(bg="Antiquewhite")

label_heading=Label(root,text="Intenet Speed Test",font=("Arial",30,"bold"),bg="Antiquewhite",fg="Brown")
label_heading.place(x=50,y=50,height=50,width=400)

label_download=Label(root,text="Download Speed",font=("Arial",30),bg="Antiquewhite",fg="Orange")
label_download.place(x=50,y=150,height=50,width=400)

label_download_result=Label(root,text="0.0",font=("Arial",30),bg="Antiquewhite",fg="Orange")
label_download_result.place(x=50,y=200,height=50,width=400)

label_upload=Label(root,text="Upload Speed",font=("Arial",30),bg="Antiquewhite",fg="Orange")
label_upload.place(x=50,y=300,height=50,width=400)

label_upload_result=Label(root,text="0.0",font=("Arial",30),bg="Antiquewhite",fg="Orange")
label_upload_result.place(x=50,y=350,height=50,width=400)

button_check=Button(root,text="Check",font=("Arial",30),bg="Antiquewhite",fg="Red",state="normal",borderwidth=5,relief="groove",command=Check)
button_check.place(x=50,y=450,height=50,width=400)

root.mainloop()
