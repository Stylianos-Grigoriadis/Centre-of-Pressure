import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pandas as pd
import tkinter.font as font

root = Tk()
root.title('CoP')
window_width = 850
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (window_width)
y = (screen_height/2) - (window_height/2)
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
root['bg']='white'

#Start the Menu widget part 1

#tell you program that you are going to put a menu
my_menu = Menu(root)
root.config(menu=my_menu)


def Select_data_from_memory_for_1_force_plate():
    if Entry_Y.get() and Entry_X.get():
        root.filename = filedialog.askopenfilename(initialdir="C:\\",
                                                   # initioaldir = "Which directory will the program open",
                                                   title="Select CSV File",
                                                   # title = "Title",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        # filetypes = (("name files", "*.name")) <--- which types of file should the program see
        # if you choose the csv file you will see that the text that it returns is the path of the file
        # Therefore we can use it like this
        df = pd.read_csv(root.filename,
                         delimiter=',',
                         decimal='.',
                         thousands=',',
                         skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                         header=None)
        print(df)
        X = int(Entry_X.get())
        Y = int(Entry_Y.get())
        print(type(X))
        global list_X_coordinates,list_Y_coordinates
        list_X_coordinates = []
        list_Y_coordinates = []
        for i in range(len(df[1])):
            F_all = df[1][i] + df[2][i] + df[3][i] + df[4][i]
            x_coordinate = ((X) / 2) * (1 + (((df[3][i] + df[4][i]) - (df[1][i] + df[2][i])) / F_all))
            list_X_coordinates.append(x_coordinate)
            y_coordinate = ((Y) / 2) * (1 + (((df[2][i] + df[4][i]) - (df[1][i] + df[3][i])) / F_all))
            list_Y_coordinates.append(y_coordinate)
        print(list_X_coordinates)
        plt.plot(list_X_coordinates, list_Y_coordinates, label='CoP')
        plt.legend()
        plt.show()
        """Dictionary_CoP = {'X coordinates':list_X_coordinates,'Y coordinates':list_Y_coordinates}
        df_CoP = pd.DataFrame.from_dict(Dictionary_CoP)
        df_CoP.to_csv('mycsv.csv')"""


    else:
            def change_color():
                Width_and_Hight_label.config(bg="black", foregroun="orange")
            def original_color ():
                Width_and_Hight_label.config(bg="orange", foregroun="black")
            Select_Data_Button.after(0, change_color)
            Select_Data_Button.after(150, original_color)
            Select_Data_Button.after(300, change_color)
            Select_Data_Button.after(450, original_color)
            Select_Data_Button.after(600, change_color)
            Select_Data_Button.after(750, original_color)

def Select_data_from_memory_for_2_force_plates():
    if Entry_Y.get() and Entry_X.get():
        root.filename = filedialog.askopenfilename(initialdir="C:\\",
                                                   # initioaldir = "Which directory will the program open",
                                                   title="Select CSV File",
                                                   # title = "Title",
                                                   filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        # filetypes = (("name files", "*.name")) <--- which types of file should the program see
        # if you choose the csv file you will see that the text that it returns is the path of the file
        # Therefore we can use it like this
        df = pd.read_csv(root.filename,
                         delimiter=',',
                         decimal='.',
                         thousands=',',
                         skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                         header=None)
        print(df)
        X = int(Entry_X.get())
        Y = int(Entry_Y.get())
        print(type(X))
        global list_X_coordinates_left_plate,\
            list_Y_coordinates_left_plate,\
            list_X_coordinates_right_plate,\
            list_Y_coordinates_right_plate,\
            list_X_coordinates_both_plates,\
            list_Y_coordinates_both_plates
        list_X_coordinates_left_plate = []
        list_Y_coordinates_left_plate = []
        for i in range(len(df[1])):
            F_all = df[1][i] + df[2][i] + df[3][i] + df[4][i]
            x_coordinate = ((X) / 2) * (1 + (((df[3][i] + df[4][i]) - (df[1][i] + df[2][i])) / F_all))
            list_X_coordinates_left_plate.append(x_coordinate)
            y_coordinate = ((Y) / 2) * (1 + (((df[2][i] + df[4][i]) - (df[1][i] + df[3][i])) / F_all))
            list_Y_coordinates_left_plate.append(y_coordinate)
        print(list_X_coordinates_left_plate)

        list_X_coordinates_right_plate = []
        list_Y_coordinates_right_plate = []
        for i in range(len(df[1])):
            F_all = df[6][i] + df[7][i] + df[8][i] + df[9][i]
            x_coordinate = ((X) / 2) * (1 + (((df[8][i] + df[9][i]) - (df[6][i] + df[7][i])) / F_all))
            list_X_coordinates_right_plate.append(x_coordinate)
            y_coordinate = ((Y) / 2) * (1 + (((df[7][i] + df[9][i]) - (df[6][i] + df[8][i])) / F_all))
            list_Y_coordinates_right_plate.append(y_coordinate)
        print(list_X_coordinates_right_plate)

        list_X_coordinates_both_plates = []
        list_Y_coordinates_both_plates = []
        for i in range(len(list_X_coordinates_right_plate)):
            list_X_coordinates_both_plates.append((list_X_coordinates_left_plate[i] + list_X_coordinates_right_plate[i]) / 2)
            list_Y_coordinates_both_plates.append((list_Y_coordinates_left_plate[i] + list_Y_coordinates_right_plate[i]) / 2)

        plt.plot(list_X_coordinates_right_plate, list_Y_coordinates_right_plate, label='Rigth leg')
        plt.plot(list_X_coordinates_left_plate, list_Y_coordinates_left_plate, label='Left leg')
        plt.plot(list_X_coordinates_both_plates, list_Y_coordinates_both_plates, label='Both legs')
        plt.legend()
        plt.show()

        """Dictionary_CoP = {'X coordinates of Right plate': list_X_coordinates_right_plate,
                          'Y coordinates of Right plate': list_Y_coordinates_right_plate,
                          'X coordinates of Left plate': list_X_coordinates_left_plate,
                          'Y coordinates of Left plate': list_Y_coordinates_left_plate,
                          'X coordinates of Both plates': list_X_coordinates_both_plates,
                          'Y coordinates of Both plates': list_Y_coordinates_both_plates}
        df_CoP = pd.DataFrame.from_dict(Dictionary_CoP)
        df_CoP.to_excel('myexcel.xlsx')"""

    else:
            def change_color():
                Width_and_Hight_label.config(bg="black", foregroun="orange")
            def original_color ():
                Width_and_Hight_label.config(bg="orange", foregroun="black")
            Select_Data_Button.after(0, change_color)
            Select_Data_Button.after(150, original_color)
            Select_Data_Button.after(300, change_color)
            Select_Data_Button.after(450, original_color)
            Select_Data_Button.after(600, change_color)
            Select_Data_Button.after(750, original_color)
def close_win(e):
   root.destroy()
root.bind('<Escape>',lambda e: close_win(e))

def Save_Into_xlsx():
    if list_X_coordinates_right_plate:
        Dictionary_CoP = {'X coordinates of Right plate': list_X_coordinates_right_plate,
                          'Y coordinates of Right plate': list_Y_coordinates_right_plate,
                          'X coordinates of Left plate': list_X_coordinates_left_plate,
                          'Y coordinates of Left plate': list_Y_coordinates_left_plate,
                          'X coordinates of Both plates': list_X_coordinates_both_plates,
                          'Y coordinates of Both plates': list_Y_coordinates_both_plates}
        df_CoP = pd.DataFrame.from_dict(Dictionary_CoP)
        df_CoP.to_excel('myexcel.xlsx')
    else:
        Dictionary_CoP = {'X coordinates': list_X_coordinates, 'Y coordinates': list_Y_coordinates}
        df_CoP = pd.DataFrame.from_dict(Dictionary_CoP)
        df_CoP.to_csv('mycsv.csv')


#Start the Menu widget part 2

#Create menu bars
file_menu = Menu(my_menu)

#Put the menu bar on screen using add_cascade()
my_menu.add_cascade(label="File",menu=file_menu)

#put a bars with comands to file_menu
file_menu.add_command(label="Load data for 1 plate", command=Select_data_from_memory_for_1_force_plate)
file_menu.add_command(label="Load data for 2 plates", command=Select_data_from_memory_for_2_force_plates)
file_menu.add_separator() #add._separator adds a line between New... and Exit (just a nice touch)
file_menu.add_command(label="Exit", command=root.quit)



Force_Plate_image = ImageTk.PhotoImage(Image.open("This Platform for GUI Small.PNG"))
label_Force_Plate_image = Label(root,image=Force_Plate_image)
#Put the image on the screen
label_Force_Plate_image.config(bg="white")
label_Force_Plate_image.grid(row=1,rowspan=10,column=0)
#Create and Put on screen: the X, Y labels and their Entries and the Select Data button
Width_and_Hight_label = Label(root,text = "Please insert the height and the width of the force platform.")
Width_and_Hight_label.config(bg="orange",foregroun="black")
Width_and_Hight_label.grid(row=2,rowspan=2,column=1,columnspan=2)
label_X = Label(text = "X = ", font=10)
label_Y = Label(text = "Y = ", font=10)
label_X.config(bg="white")
label_Y.config(bg="white")
label_X.grid(row=4,rowspan=2,column=1)
label_Y.grid(row=6,rowspan=2,column=1)
Entry_X = Entry(root,relief="sunken",foregroun="orange",width=30)
Entry_Y = Entry(root,relief="sunken",foregroun="orange",width=30)
Entry_X.grid(row=4,rowspan=2,column=2)
Entry_Y.grid(row=6,rowspan=2,column=2)
print(type(X))

f = font.Font(weight="bold")
Select_Data_Button_1_plate = Button(root,borderwidth=4,text="Select Data for 1 Force Plate",cursor="hand2",
                            background="black",foregroun="orange",relief="groove",font=30,
                            activebackground="orange",activeforeground="black",width=30,height=3,
                            command=Select_data_from_memory_for_1_force_plate)
Select_Data_Button_1_plate['font'] = f
Select_Data_Button_1_plate.grid(row=8,rowspan=1,column=1,columnspan=2)
Select_Data_Button_2_plates = Button(root,borderwidth=4,text="Select Data for 2 Force Plates",cursor="hand2",
                            background="black",foregroun="orange",relief="groove",font=30,
                            activebackground="orange",activeforeground="black",width=30,height=3,
                            command=Select_data_from_memory_for_2_force_plates)
Select_Data_Button_2_plates['font'] = f
Select_Data_Button_2_plates.grid(row=9,rowspan=1,column=1,columnspan=2)
Save_data = Button(root,borderwidth=4,text="Save",cursor="hand2",
                            background="black",foregroun="orange",relief="groove",font=30,
                            activebackground="orange",activeforeground="black",width=30,height=3,
                            command=Save_Into_xlsx)
Save_data['font'] = f
Save_data.grid(row=10,rowspan=1,column=1,columnspan=2)


root.mainloop()
#HELP for size and bold buttons f = font.Font(family='Times New Roman', size=20, weight="bold")