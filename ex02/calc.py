import tkinter as tk
import tkinter.messagebox as tkm
import math
def kaijyou(x):
    
    return math.factorial(x)


def button_click(event):
    btn = event.widget
    num = btn["text"]
    print(num)
    if num == "=":
         eqn = entry.get()
         res = eval(eqn)
         entry.delete(0, tk.END)
         entry.insert(tk.END,res)
         print(res)
    if num == "x!":
        eqn1 = entry.get()
        print(eqn1)
        entry.delete(0, tk.END)
        entry.insert(tk.END,kaijyou(int(eqn1)))
    

        


    if num != "=" and num != "x!":
        entry.insert(tk.END, num)
        print(num)
        #tkm.showinfo("", f"{num}のボタンがクリックされました")
if __name__ == "__main__":

    
    r,c = 1, 0
    root = tk.Tk()
    root.title("超高機能電卓")
    #root.geometry("300x500")

    entry = tk.Entry(root, justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)
    for i,num in enumerate([i for i in range(9, -1, -1)]+["+"]+["="]):
        btn = tk.Button(root,text=f"{num}",width=4,height=2,font=("Times New Roman", 30))
        btn.bind("<1>", button_click)
        btn.grid(row=r,column=c)
        c+=1
        if (i+1)%3 == 0:
            r += 1
            c = 0
    btn = tk.Button(root,text="x!",width=4, height=2,font=("Times New Roman", 30) )
    btn.bind("<1>", button_click)
    btn.grid(row=1,column=4)
    btn = tk.Button(root,text="/",width=4, height=2,font=("Times New Roman", 30))
    btn.bind("<1>", button_click)
    btn.grid(row=2,column=4)


    root.mainloop()
        