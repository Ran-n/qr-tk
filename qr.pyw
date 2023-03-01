import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import pyperclip

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        self.input_text = tk.StringVar()
        self.input_text.set(pyperclip.paste())
        self.input_entry = tk.Entry(self.master, textvariable=self.input_text, text=self.input_text, width=40)
        self.input_entry.pack(pady=10)
        self.input_entry.bind('<KeyRelease>', self.generate_qr_code)

        self.master.bind('<Escape>', self.close)
        self.master.bind('<FocusOut>', self.close)

        self.qr_code_label = tk.Label(self.master)
        self.generate_qr_code()

    def generate_qr_code(self, event=None):
        if self.input_text.get():
            self.qr_code_label.pack()
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(self.input_text.get())
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(img)
            self.qr_code_label.config(image=self.img_tk)
        else:
            self.qr_code_label.pack_forget()

    def close(self, event):
        self.master.destroy()

def run():
    root = tk.Tk()
    QRCodeGenerator(root)
    root.focus_force()
    root.mainloop()

run()
