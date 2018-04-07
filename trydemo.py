import tkinter as tk

class TryDemo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.winfo_toplevel().title("計算測試")

        self.button1 = tk.Button(self)
        self.button1["text"] = "測試1/0"
        self.button1["width"] = 15
        self.button1["command"] = self.testing1
        self.button1.grid(row=0, column=0, sticky=tk.N+tk.W)

        self.button2 = tk.Button(self)
        self.button2["text"] = "測試1/1"
        self.button2["width"] = 15
        self.button2["command"] = self.testing2
        self.button2.grid(row=0, column=1, sticky=tk.N+tk.W)

        self.result = tk.Label(self)
        self.result["text"] = "結果是..."
        self.result["width"] = 30
        self.result.grid(row=1, column=0, columnspan=2, sticky=tk.N+tk.W)

    def testing1(self):
        self.result["text"] = "結果是"
        try:
            r = 1 / 0
            self.result["text"] += str(r) + "。"
        except ZeroDivisionError:
            self.result["text"] += "除數不能為0！"
        except:
            self.result["text"] += "發生其他錯誤！"
        else:
            self.result["text"] += "錯誤沒有發生！"
        finally:
            self.result["text"] += "測試結束。"

    def testing2(self):
        self.result["text"] = "結果是"
        try:
            r = 1 / 1
            self.result["text"] += str(r) + "。"
        except ZeroDivisionError:
            self.result["text"] += "除數不能為0！"
        except:
            self.result["text"] += "發生其他錯誤！"
        else:
            self.result["text"] += "錯誤沒有發生！"
        finally:
            self.result["text"] += "測試結束。"

if __name__ == '__main__':
   root = tk.Tk()
   app = TryDemo(master=root)
   app.mainloop()

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：trydemo.py
# 功能：示範 try-except-finally-else 陳述
# 作者：張凱慶
