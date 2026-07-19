import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.minsize(250, 300)
window.maxsize(250, 400)

#Height Section

height_discription_label = tk.Label(padx=1, pady=1,width=30,height=2)
height_discription_label.grid(row=0, column=0)
height_discription_label.config(anchor='center', fg='black',font=('Arial', 10, 'bold'),text='Boy Bilgisini Giriniz (cm).')
height_discription_label.pack(anchor='center')

height_input_text = tk.Text(padx=1, pady=1,width=20,height=2)
height_input_text.pack(anchor='center')


#Weight Section

weight_discription_label = tk.Label(padx=1, pady=1,width=25,height=2)
weight_discription_label.config(anchor='center', fg='black',font=('Arial', 10, 'bold'),text='Kilo Bilgisini Giriniz.')
weight_discription_label.pack(anchor='center')


weight_input_text = tk.Text(padx=1, pady=1,width=20,height=2)
weight_input_text.pack(anchor='center')

#Calculation Function

def calculate_BMI():
    weight=weight_input_text.get('1.0',tk.END)
    height=height_input_text.get('1.0',tk.END)
    
    try:
        weight=float(weight)
        height=float(height)/100
        if weight <= 0 or height <= 0:
            tk.messagebox.showerror("Error", "Girilen degerler Negatif olamaz")
        else:
            tk.messagebox.showinfo("Sonuc", "Vucut Kitle Indeksiniz: "+str(round(weight/pow(height,2),2)))
    except ValueError:
        tk.messagebox.showerror("Error", "Sadece pozitif tam sayi degerleri girilebilir, hic bir alan bos birakilamaz")
#Button and Calculation Section

submit_button = tk.Button(command=calculate_BMI,padx=1,pady=1,text="Hesapla",fg='black',font=('Arial', 10, 'bold'),width=20,height=2)
submit_button.place(x=122,y=200,anchor='center')

window.mainloop()
