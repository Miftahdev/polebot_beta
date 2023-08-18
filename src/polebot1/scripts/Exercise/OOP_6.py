import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text= "POLMAN OPEN PLATFORM EDUCATIONAL ROBOT")
label2 = tkinter.Label(main_window, text= "USER INTERFACE")

tombol1 = tkinter.Button(main_window,text = " Run")
tombol2 = tkinter.Button(main_window, text= "STOP")


#method positioning 
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

#method menampilkan gui
main_window.mainloop()