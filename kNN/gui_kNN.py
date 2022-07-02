import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import joblib
import numpy
# load the trained model to classify sign
model = joblib.load('D:/UIT/Two/Sector2/ComputerVision/Project Traffic Sign Classification/kNN/kNN_model')


# dictionary to label all traffic signs class.
classes = {1: 'Tốc độ tối đa (20km/h)',
           2: 'Tốc độ tối đa (30km/h)',
           3: 'Tốc độ tối đa (50km/h)',
           4: 'Tốc độ tối đa (60km/h)',
           5: 'Tốc độ tối đa (70km/h)',
           6: 'Tốc độ tối đa (80km/h)',
           7: 'Hết giới hạn tốc độ (80km/h)',
           8: 'Tốc độ tối đa (100km/h)',
           9: 'Tốc độ tối đa (120km/h)',
           10: 'Cấm vượt',
           11: 'Không vượt quá 3,5 tấn',
           12: 'Quyền ưu tiên tại giao lộ',
           13: 'Đường ưu tiên',
           14: 'Yield',
           15: 'Dừng',
           16: 'Cấm phương tiện',
           17: 'Cấm phương tiện >3.5 tấn',
           18: 'Cấm vào',
           19: 'Chướng ngại vật',
           20: 'Đường cong nguy hiểm bên trái',
           21: 'Đường cong nguy hiểm bên phải',
           22: 'Đường cong kép',
           23: 'Đường gập ghềnh',
           24: 'Đường trơn',
           25: 'Đường thu hẹp ở bên phải',
           26: 'Công trình đang thi công',
           27: 'Đèn tín hiệu',
           28: 'Đường đi bộ',
           29: 'Trẻ em băng qua',
           30: 'Xe đạp băng qua',
           31: 'Cẩn thận với băng, tuyết',
           32: 'Động vật hoang dã băng qua',
           33: 'Kết thúc giớn hạn tốc độ',
           34: 'Rẽ phải phía trước',
           35: 'Rẽ trái phía trước',
           36: 'Chỉ được đi thẳng',
           37: 'Đi thẳng hoặc sang phải',
           38: 'Đi thẳng hoặc sang trái',
           39: 'Đi bên phải',
           40: 'Đi bên trái',
           41: 'Đi vòng xoay',
           42: 'Kết thúc cấm vượt',
           43: 'Kết thúc cấm vượt phương tiện > 3,5 tấn'}


# initialise GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Phân loại biển báo giao thông')

top.configure(background='#FFFFE0')

# In ra kết quả dự đoán biển báo.
label = Label(top, background='#FFFFE0', font=('arial', 30, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((20, 20))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    image = image.reshape((20*20, 3))
    image = np.flip(image, axis=1)
    image = image.reshape((20, 20, 3))
    image = image.astype('float32')/255
    print(image.shape[0])
    image = image.reshape(1, 20*20*3)
    pred = (model.predict(image))[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    # Nút bấm phân loại biển báo
    classify_b = Button(top, text="Phân loại biển báo",
                        command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#FF0000',
                         foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

# Hàm tải ảnh lên


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(
            ((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


# Nút tải ảnh lên
upload = Button(top, text="Tải ảnh lên", command=upload_image, padx=10, pady=5)
upload.configure(background='#FF0000', foreground='white',
                 font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Biển Báo Giao Thông",
                pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#FFFFE0', foreground='#FF0000')
heading.pack()
top.mainloop()
