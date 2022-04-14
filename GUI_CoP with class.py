import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import pandas as pd
import tkinter.font as font
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class CoP:

    def __init__(self,master):

        self.master = master
        self.master.title("Center of Pressure")
        self.window_width = 850
        self.window_height = 400
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        x = (self.screen_width / 2) - (self.window_width)
        y = (self.screen_height / 2) - (self.window_height / 2)
        master.geometry(f'{self.window_width}x{self.window_height}+{int(x)}+{int(y)}')
        self.master.bind('<Escape>', lambda e: self.close_win(e))
        self.master['bg']='white'
        #Create a menu bar
        self.my_menu = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.my_menu)
        self.master.config(menu=self.my_menu)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Load data for 1 plate", command=self.Select_data_from_memory_for_1_force_plate)
        self.file_menu.add_command(label="Load data for 2 plates", command=self.Select_data_from_memory_for_2_force_plates)
        self.file_menu.add_separator()  # add._separator adds a line between New... and Exit (just a nice touch)
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        #Create stuff
        self.Force_Plate_image = ImageTk.PhotoImage(Image.open("This Platform for GUI Small.PNG"))
        self.label_Force_Plate_image = tk.Label(root, image=self.Force_Plate_image)
        # Put the image on the screen
        self.label_Force_Plate_image.config(bg="white")
        self.label_Force_Plate_image.grid(row=1, rowspan=10, column=0)
        # Create and Put on screen: the X, Y labels and their Entries and the Select Data button
        self.Width_and_Hight_label = tk.Label(root, text="Please insert the height and the width of the force platform.")
        self.Width_and_Hight_label.config(bg="orange", foregroun="black")
        self.Width_and_Hight_label.grid(row=2, rowspan=2, column=1, columnspan=2)
        self.label_X = tk.Label(text="X = ", font=10)
        self.label_Y = tk.Label(text="Y = ", font=10)
        self.label_X.config(bg="white")
        self.label_Y.config(bg="white")
        self.label_X.grid(row=4, rowspan=2, column=1)
        self.label_Y.grid(row=6, rowspan=2, column=1)
        self.Entry_X = tk.Entry(root, relief="sunken", foregroun="black", width=30)
        self.Entry_Y = tk.Entry(root, relief="sunken", foregroun="black", width=30)
        self.Entry_X.insert(0, 120)
        self.Entry_Y.insert(0, 260)
        self.Entry_X.grid(row=4, rowspan=2, column=2)
        self.Entry_Y.grid(row=6, rowspan=2, column=2)


        self.f = font.Font(weight="bold")
        self.Select_Data_Button_1_plate = tk.Button(root, borderwidth=4, text="Select Data for 1 Force Plate", cursor="hand2",
                                            background="black", foregroun="orange", relief="groove", font=30,
                                            activebackground="orange", activeforeground="black", width=30, height=3,
                                            command=self.Select_data_from_memory_for_1_force_plate)
        self.Select_Data_Button_1_plate['font'] = self.f
        self.Select_Data_Button_1_plate.grid(row=8, rowspan=1, column=1, columnspan=2)
        self.Select_Data_Button_2_plates = tk.Button(root, borderwidth=4, text="Select Data for 2 Force Plates", cursor="hand2",
                                             background="black", foregroun="orange", relief="groove", font=30,
                                             activebackground="orange", activeforeground="black", width=30, height=3,
                                             command=self.Select_data_from_memory_for_2_force_plates)
        self.Select_Data_Button_2_plates['font'] = self.f
        self.Select_Data_Button_2_plates.grid(row=9, rowspan=1, column=1, columnspan=2)
        self.Save_data = tk.Button(root, borderwidth=4, text="Save", cursor="hand2",
                           background="black", foregroun="orange", relief="groove", font=30,
                           activebackground="orange", activeforeground="black", width=30, height=3,
                           command=self.Save_Into_xlsx)
        self.Save_data['font'] = self.f
        self.Save_data.grid(row=10, rowspan=1, column=1, columnspan=2)

    def Select_data_from_memory_for_1_force_plate(self):
        if self.Entry_Y.get() and self.Entry_X.get():
            self.root.filename = filedialog.askopenfilename(initialdir="C:\\",
                                                       # initioaldir = "Which directory will the program open",
                                                       title="Select CSV File",
                                                       # title = "Title",
                                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            # filetypes = (("name files", "*.name")) <--- which types of file should the program see
            # if you choose the csv file you will see that the text that it returns is the path of the file
            # Therefore we can use it like this
            self.df = pd.read_csv(root.filename,
                             delimiter=',',
                             decimal='.',
                             thousands=',',
                             skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                             header=None)
            print(self.df)
            self.X = int(self.Entry_X.get())
            self.Y = int(self.Entry_Y.get())

            self.list_X_coordinates = []
            self.list_Y_coordinates = []
            for i in range(len(self.df[1])):
                self.F_all = self.df[1][i] + self.df[2][i] + self.df[3][i] + self.df[4][i]
                self.x_coordinate = ((self.X) / 2) * (1 + (((self.df[2][i] + self.df[3][i]) - (self.df[1][i] + self.df[4][i])) / self.F_all))
                self.list_X_coordinates.append(self.x_coordinate)
                self.y_coordinate = ((self.Y) / 2) * (1 + (((self.df[4][i] + self.df[3][i]) - (self.df[1][i] + self.df[2][i])) / self.F_all))
                self.list_Y_coordinates.append(self.y_coordinate)
            plt.plot(self.list_X_coordinates, self.list_Y_coordinates, label='CoP')
            plt.legend()
            plt.show()
            self.total_distance_right_leg = self.travel_distance(self.list_X_coordinates,self.list_Y_coordinates)

        else:
            def change_color():
                self.Width_and_Hight_label.config(bg="black", foregroun="orange")

            def original_color():
                self.Width_and_Hight_label.config(bg="orange", foregroun="black")

            self.Select_Data_Button_1_plate.after(0, change_color)
            self.Select_Data_Button_1_plate.after(150, original_color)
            self.Select_Data_Button_1_plate.after(300, change_color)
            self.Select_Data_Button_1_plate.after(450, original_color)
            self.Select_Data_Button_1_plate.after(600, change_color)
            self.Select_Data_Button_1_plate.after(750, original_color)

    def Select_data_from_memory_for_2_force_plates(self):
        if self.Entry_Y.get() and self.Entry_X.get():
            root.filename = filedialog.askopenfilename(initialdir="C:\\",
                                                       # initioaldir = "Which directory will the program open",
                                                       title="Select CSV File",
                                                       # title = "Title",
                                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            # filetypes = (("name files", "*.name")) <--- which types of file should the program see
            # if you choose the csv file you will see that the text that it returns is the path of the file
            # Therefore we can use it like this
            self.df = pd.read_csv(root.filename,
                             delimiter=',',
                             decimal='.',
                             thousands=',',
                             skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                             header=None)
            print(self.df)
            self.X = int(self.Entry_X.get())
            self.Y = int(self.Entry_Y.get())

            self.list_X_coordinates_left_plate = []
            self.list_Y_coordinates_left_plate = []
            for i in range(len(self.df[1])):
                self.F_all = self.df[1][i] + self.df[2][i] + self.df[3][i] + self.df[4][i]
                self.x_coordinate = ((self.X) / 2) * (1 + (((self.df[2][i] + self.df[3][i]) - (self.df[1][i] + self.df[4][i])) / self.F_all))
                self.list_X_coordinates_left_plate.append(self.x_coordinate)
                self.y_coordinate = ((self.Y) / 2) * (1 + (((self.df[4][i] + self.df[3][i]) - (self.df[1][i] + self.df[2][i])) / self.F_all))
                self.list_Y_coordinates_left_plate.append(self.y_coordinate)


            self.list_X_coordinates_right_plate = []
            self.list_Y_coordinates_right_plate = []
            for i in range(len(self.df[1])):
                self.F_all = self.df[6][i] + self.df[7][i] + self.df[8][i] + self.df[9][i]
                self.x_coordinate = ((self.X) / 2) * (1 + (((self.df[7][i] + self.df[8][i]) - (self.df[6][i] + self.df[9][i])) / self.F_all))
                self.list_X_coordinates_right_plate.append(self.x_coordinate)
                self.y_coordinate = ((self.Y) / 2) * (1 + (((self.df[9][i] + self.df[8][i]) - (self.df[6][i] + self.df[7][i])) / self.F_all))
                self.list_Y_coordinates_right_plate.append(self.y_coordinate)


            self.list_X_coordinates_both_plates = []
            self.list_Y_coordinates_both_plates = []
            for i in range(len(self.list_X_coordinates_right_plate)):
                self.list_X_coordinates_both_plates.append(
                    (self.list_X_coordinates_left_plate[i] + self.list_X_coordinates_right_plate[i]) / 2)
                self.list_Y_coordinates_both_plates.append(
                    (self.list_Y_coordinates_left_plate[i] + self.list_Y_coordinates_right_plate[i]) / 2)

            root2 = tk.Tk()

            fig = Figure(figsize=(8, 3), dpi=100)
            self.plot1 = fig.add_subplot(111)
            self.plot1.plot(self.list_X_coordinates_both_plates, self.list_Y_coordinates_both_plates, label='Both legs')
            self.canvas = FigureCanvasTkAgg(fig, master=root2)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=0, column=0)



            # plt.plot(self.list_X_coordinates_right_plate, self.list_Y_coordinates_right_plate, label='Rigth leg')
            # plt.plot(self.list_X_coordinates_left_plate, self.list_Y_coordinates_left_plate, label='Left leg')
            # plt.plot(self.list_X_coordinates_both_plates, self.list_Y_coordinates_both_plates, label='Both legs')
            # plt.legend()
            # plt.show()

            root2.mainloop()


            self.total_distance_right_leg = self.travel_distance(self.list_X_coordinates_right_plate,self.list_Y_coordinates_right_plate)
            self.total_distance_left_leg = self.travel_distance(self.list_X_coordinates_left_plate,self.list_Y_coordinates_left_plate)
            self.total_distance_both_legs = self.travel_distance(self.list_X_coordinates_both_plates,self.list_Y_coordinates_both_plates)


        else:
            def change_color():
                self.Width_and_Hight_label.config(bg="black", foregroun="orange")

            def original_color():
                self.Width_and_Hight_label.config(bg="orange", foregroun="black")

            self.Select_Data_Button_2_plates.after(150, original_color)
            self.Select_Data_Button_2_plates.after(300, change_color)
            self.Select_Data_Button_2_plates.after(450, original_color)
            self.Select_Data_Button_2_plates.after(600, change_color)
            self.Select_Data_Button_2_plates.after(750, original_color)

    def travel_distance(self,data_X,data_Y):
        total_distance = 0
        for i in range(len(data_X)):
            try:
                distance = math.sqrt((data_X[i + 1] - data_X[i]) ** 2) + ((data_Y[i + 1] - data_Y[i]) ** 2)
                total_distance += distance
                # print(self.total_distance_left_leg)
            except:
                pass
        return total_distance

    def close_win(self,e):
        self.master.destroy()

    def Save_Into_xlsx(self):
        if self.list_X_coordinates_right_plate:
            self.Dictionary_CoP = {'X coordinates of Right plate': self.list_X_coordinates_right_plate,
                              'Y coordinates of Right plate': self.list_Y_coordinates_right_plate,
                              'X coordinates of Left plate': self.list_X_coordinates_left_plate,
                              'Y coordinates of Left plate': self.list_Y_coordinates_left_plate,
                              'X coordinates of Both plates': self.list_X_coordinates_both_plates,
                              'Y coordinates of Both plates': self.list_Y_coordinates_both_plates}
            self.df_CoP = pd.DataFrame.from_dict(self.Dictionary_CoP)
            self.df_CoP.to_excel('myexcel.xlsx')
        else:
            self.Dictionary_CoP = {'X coordinates': self.list_X_coordinates, 'Y coordinates': self.list_Y_coordinates}
            self.df_CoP = pd.DataFrame.from_dict(self.Dictionary_CoP)
            self.df_CoP.to_csv('mycsv.csv')

    # def matplotcanvas(self):




if __name__ == "__main__":
    root = tk.Tk()
    my_gui = CoP(root)
    root.mainloop()