#Modules
from keras.preprocessing import image 
from tkinter import *
from tkinter import filedialog as fd
from keras.models import load_model
import tkinter as tk
import numpy as np

#Load Model
model = load_model('dataset.h5')

#Main function
def menu():

    #Inputting Image
    adr=fd.askopenfilename(title="Select Image file:", filetypes=[("png","*.png")])
    img=PhotoImage(file=adr)
    
    lblNewImg=Label(image=img)
    lblNewImg.Image=img
    lblNewImg.grid(row=2, column=0, columnspan=2, rowspan=5, sticky=N + W, padx=5, pady=5)

    #Pixelating
    test_img=image.load_img(adr,target_size=(32,32))
    test_image=image.img_to_array(test_img)
    test_image=np.expand_dims(test_image,axis=0)

    #Predicted Result
    result=model.predict(test_image)
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    print(result)

    #Classification
    m=0
    text_output=""
    flag = 0
    for i in range(0,10):
        if(result[0][i]>=result[0][m]):
            m=i
            flag=1
        else:
            pass

    #Error in Classification
    if flag == 0:
        text_output = 'The image could not be classified'
        
    else:
        text_output=class_names[m]

    #Final Output
    print(text_output)
    lblTextOp=Label(text=text_output)
    lblTextOp.grid(row=7,column=0, columnspan=2, rowspan=5, sticky=N + W, padx=5, pady=5)


#GUI   
root=Tk()
root.geometry('430x300')
root.configure(background='white')
title = Label(root, text="Image Recognition", bg="white", font=("bold", 30))
title.grid(row=0,column=0)      
btn=tk.Button(text='Input Image',command=menu,padx=5,pady=5)
btn.grid(row=1,column=0)

#Loop
tk.mainloop()
