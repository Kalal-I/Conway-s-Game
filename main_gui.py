import customtkinter as ctk
import random

class conwayGame:
    lst=[[0 for i in range(10)] for j in range(10)]
    def __init__(self, root):
        # 1. Store the main window
        self.root = root
        self.root.title("Conway's Game")
        self.root.geometry("1000x900")
        
        # A list of hex color codes
        
        self.main_frame=ctk.CTkFrame(self.root,width=300,height=300)
        self.main_frame.place(x=350,y=150)
        # 2. Create the button and assign it to an instance variable (self.button)
        self.button=[[0 for i in range(10)] for j in range(10)]
        for i in range(10):
            for j in range(10):
                self.button[i][j] = ctk.CTkButton(
                    self.main_frame, 
                    text=' ',
                    width=30,
                    height=30,
                    corner_radius=0,
                    fg_color="grey",
                    hover_color="#FF0000",
                    command=lambda r=i, c=j: self.change_color(r, c) # Notice we use self.change_color here
                )
                
                # 3. Place the button
                self.button[i][j].place(x=30*i,y=j*30)
        self.next_iteration=ctk.CTkButton(self.root,text="Next Iteration",command=self.next_val)
        self.next_iteration.place(x=450,y=500)
    def next_val(self):
        self.next_iter(conwayGame.lst)
        for i in range(10):
            for j in range(10):
                if(conwayGame.lst[i][j]==0):
                    self.button[i][j].configure(fg_color='grey',hover_color='Red')
                else:
                    self.button[i][j].configure(fg_color='red',hover_color="#FF7F7F")
    def change_color(self,i,j):
        color=self.button[i][j].cget("fg_color")
        if(color=='grey'):
            
            self.button[i][j].configure(fg_color='red',hover_color="#FF7F7F")
            conwayGame.lst[i][j]=1
        else:
            
            self.button[i][j].configure(fg_color='grey',hover_color='Red')
            conwayGame.lst[i][j]=0
    def next_iter(self,lst):
    
        cols=len(lst[0])
        rows=len(lst)

        
        new_lst=[[0 for x in range(cols)]for x in range(rows)]
        print(lst)
        for i in range(1,len(lst)-1):
            for j in range(1,len(lst[0])-1):
                
                sum1=sum(lst[i-1][j-1:j+2])+sum(lst[i+1][j-1:j+2])+lst[i][j-1]+lst[i][j+1]
                if(sum1<2 or sum1>3):
                    new_lst[i][j]=0
                elif((sum1==2 and lst[i][j]==1) or sum1==3):
                    new_lst[i][j]=1
                else:
                    new_lst[i][j]=0
                
        for i in range(1,len(lst[0])-1):
            sum1=sum(lst[1][i-1:i+2])+lst[0][i-1]+lst[0][i+1]
            if(sum1<2 or sum1>3):
                new_lst[0][i]=0
            elif((sum1==2 and lst[0][i]==1) or sum1==3):
                new_lst[0][i]=1
            else:
                new_lst[0][i]=0
        
        for i in range(1,len(lst[0])-1):
            sum1=sum(lst[len(lst)-2][i-1:i+2])+lst[len(lst)-1][i-1]+lst[len(lst)-1][i+1]
            if(sum1<2 or sum1>3):
                new_lst[len(lst)-1][i]=0
            elif((sum1==2 and lst[len(lst)-1][i]==1) or sum1==3):
                
                new_lst[len(lst)-1][i]=1
                
            else:
                new_lst[len(lst)-1][i]=0
            
        
        for i in range(1,len(lst)-1):
            sum1=lst[i-1][1]+lst[i][1]+lst[i+1][1]+lst[i-1][0]+lst[i+1][0]
            
            if(sum1<2 or sum1>3):
                new_lst[i][0]=0
            elif((sum1==2 and lst[i][0]==1) or sum1==3):
                new_lst[i][0]=1
            else:
                new_lst[i][0]=0
        
        for i in range(1,len(lst)-1):
            sum1=lst[i-1][len(lst[0])-2]+lst[i][len(lst[0])-2]+lst[i+1][len(lst[0])-2]+lst[i-1][len(lst[0])-1]+lst[i+1][len(lst[0])-1]
            if(sum1<2 or sum1>3):
                new_lst[i][len(lst[0])-1]=0
            elif((sum1==2 and lst[i][len(lst[0])-1]==1) or sum1==3):
                new_lst[i][len(lst[0])-1]=1
            else:
                new_lst[i][len(lst[0])-1]=0
        sum1=lst[0][1]+lst[1][0]+lst[1][1]
        if(sum1<2 or sum1>3):
            new_lst[0][0]=0
        elif((sum1==2 and lst[0][0]==1) or sum1==3):
            new_lst[0][0]=1
        else:
            new_lst[0][0]=0
        sum1=lst[0][len(lst[0])-2]+lst[1][len(lst[0])-1]+lst[1][len(lst[0])-2]
        if(sum1<2 or sum1>3):
            new_lst[0][len(lst[0])-1]=0
        elif((sum1==2 and lst[0][len(lst[0])-1]==1) or sum1==3):
            new_lst[0][len(lst[0])-1]=1
        else:
            new_lst[0][len(lst[0])-1]=0
        sum1=lst[len(lst)-2][0]+lst[len(lst)-1][1]+lst[len(lst)-2][1]
        if(sum1<2 or sum1>3):
            new_lst[len(lst)-1][0]=0
        elif((sum1==2 and lst[len(lst)-1][0]==1) or sum1==3):
            new_lst[len(lst)-1][0]=1
        else:
            new_lst[len(lst)-1][0]=0
        
        sum1=lst[len(lst)-1][len(lst[0])-2]+lst[len(lst)-2][len(lst[0])-1]+lst[len(lst)-2][len(lst[0])-2]
        if(sum1<2 or sum1>3):
            new_lst[len(lst)-1][len(lst[0])-1]=0
        elif((sum1==2 and lst[len(lst)-1][len(lst[0])-1]==1) or sum1==3):
            new_lst[len(lst)-1][len(lst[0])-1]=1
        else:
            new_lst[len(lst)-1][len(lst[0])-1]=0
        print(new_lst)
        conwayGame.lst[:]=new_lst 
if __name__=="__main__":
    main_window=ctk.CTk()
    app=conwayGame(main_window)
    main_window.mainloop()