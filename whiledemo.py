import tkinter as tk

class WhileDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("計算總和")

        self.label = tk.Label(self)
        self.label["text"] = "請輸入整數："
        self.label.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "計算"
        self.button["command"] = self.calculate
        self.button.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = "結果是..."
        self.result.grid(row=3, column=0, sticky=tk.N+tk.W)

    def calculate(self):
        number = int(self.entry.get())
        sum = 0
        i = 0
        while i <= number:
            sum += i
            i += 1
        else:
            self.result["text"] = str(sum)

if __name__ == '__main__':
   root = tk.Tk()
   app = WhileDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：whiledemo.py
# 功能：示範 while-else 陳述
# 作者：張凱慶
