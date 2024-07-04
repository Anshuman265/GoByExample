import pandas as pd
from tkinter import Tk, filedialog, Label, Button

def convert_csv_to_excel(csv_path, excel_path):
    df = pd.read_csv(csv_path)
    df.to_excel(excel_path, index=False)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        excel_path = file_path.replace('.csv', '.xlsx')
        convert_csv_to_excel(file_path, excel_path)
        print(f"File converted and saved to {excel_path}")

root = Tk()
root.title("File Converter")
Label(root, text="File Converter").pack()
Button(root, text="Upload File", command=open_file).pack()
root.mainloop()
