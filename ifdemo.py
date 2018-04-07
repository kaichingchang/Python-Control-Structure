import tkinter as tk

class IfDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("分數檢測")

        self.label = tk.Label(self)
        self.label["text"] = "請輸入分數："
        self.label.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=0, sticky=tk.N+tk.W)

        self.button = tk.Button(self)
        self.button["text"] = "檢測"
        self.button["command"] = self.testing
        self.button.grid(row=2, column=0, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = "結果是..."
        self.result.grid(row=3, column=0, sticky=tk.N+tk.W)

    def testing(self):
        score = int(self.entry.get())
        if score <= 100 and score >= 90:
            self.result["text"] = "很棒！"
        elif score < 90 and score >= 60:
            self.result["text"] = "不錯！"
        elif score < 60 and score >= 0:
            self.result["text"] = "加油！"
        else:
            self.result["text"] = "未知成績！！"

if __name__ == '__main__':
   root = tk.Tk()
   app = IfDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：ifdemo.py
# 功能：示範 if-elif-else 陳述
# 作者：張凱慶
