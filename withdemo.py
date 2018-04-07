import tkinter as tk

class WithDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("開啟檔案")

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "開啟"
        self.button["command"] = self.loadfile
        self.button.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.result = tk.Text(self)
        self.result["width"] = 60
        self.result["height"] = 10
        self.result.grid(row=2, column=0, sticky=tk.N+tk.W)

    def loadfile(self):
        self.result.delete(1.0, tk.END)
        try:
            with open(self.entry.get(), "r", encoding="UTF-8") as file:
                for line in file:
                    self.result.insert(tk.INSERT, line)
        except:
            self.result.insert(tk.INSERT, "檔案不存在")
            self.result["state"] = "disabled"


if __name__ == '__main__':
   root = tk.Tk()
   app = WithDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：withdemo.py
# 功能：示範 with-as 陳述
# 作者：張凱慶
