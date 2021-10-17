from tkinter import *
from tkinter import messagebox
from pytube import YouTube

#------ Window -------
YT_Window = Tk()
YT_Window.title("Youtube Video Downloader")
YT_Window.resizable(width=False, height= False) 
YT_Window.config(padx=40, pady=20) 
#--------------------


#---- Functions ----
def DownloadVideo():
    if Link_Input.get() == "": # or FileName_Input.get() == "":
                   return 0
 
    vid_link = Link_Input.get()
    vid_Save = FileName_Input.get()

    try: 
       Video = YouTube(vid_link)
    except:
        messagebox.showerror(title="Youtube Video Error", message="Enter a valid youtube video link")
    else:
        Video_Resolution = Video.streams.filter(only_audio=True)
        
        
        Video_Details = f"Video Details:\n\nTitle: {Video.title}\nChannel: {Video.author}"
        
        Download_Message = messagebox.askokcancel(title="Youtube Video Details", message=Video_Details)

        if Download_Message:
                try: 
                    Video_Resolution.download(vid_Save)
                except: 
                    messagebox.showerror(title="Youtube Video Error", message="Something Went Wrong")
    

#---------- Window GUI --------------

# ------- Logo -----------
YT_Logo = Canvas(width=100, height=100)
YT_Logo.grid(row=0, column=1)
YT_Logo_Image = PhotoImage(file="logo2.png")
YT_Logo.create_image(50, 50, image=YT_Logo_Image)
#--------------------------

#------- Labels ----------
Link = Label(text="Video Link:")
Link.grid(row=2, column=0)
FileName = Label(text="Save Location:")
FileName.grid(row=3, column=0)
#------------------------------

#---------- Entries ------------
Link_Input = Entry(width=25)
Link_Input.grid(row=2, column=1)
FileName_Input = Entry(width=25)
FileName_Input.grid(row=3, column=1)
#--------------------------------

#-------- Buttons ------------
Download = Button(text="Download", bg='lightgreen', command=DownloadVideo)
Download.grid(row=4, column=1)
#-----------------------------

#------ Window GUI Ends ------



#--- Display Window --
YT_Window.mainloop()