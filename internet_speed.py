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


root.mainloop()
