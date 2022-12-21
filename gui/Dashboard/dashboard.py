"""
This includes the class to build
the second page of the gui.
"""


from tkinter import *
from PIL import Image, ImageTk
from gui.BaseDesk import base


class Dashboard:

    image_data_base = []


    def __init__(self, master) -> None:

        self.root = master
        self.root.config(bg='#98AFC7')
        self.root.title("Dashboard")
        self.root.geometry("960x540")

        """
            Create the lower Frame in the window
        """
        self.dashboard_frame = Frame(
            self.root,
            bg="#BCC6CC",
        )
        self.dashboard_frame.place(
            relx=0,
            rely=0,
            relheight=1,
            relwidth=1,
        )

        """
            Add the canvas layer on the lower Frame
        """
        self.bg_canvas = Canvas(
            self.dashboard_frame,
            width=960,
            height=540,
            bd=0,
            cursor='arrow',
        )
        self.bg_canvas.pack(
            side=TOP,
            anchor=W,
            padx=0,
            pady=0,
        )

        """
            Add the image to the background
        """
        self.bg_img = Image.open('./assets/imgs/Dashboard.jpg')
        self.tk_bg_img = ImageTk.PhotoImage(self.bg_img)
        self.image_data_base.append(self.tk_bg_img)
        print(self.tk_bg_img)
        print(self.image_data_base[-1])
        self.bg_canvas.create_image(
            480,
            270,
            anchor='center',
            image=self.image_data_base[0],
        )

        """
            Create the guide button
        """
        self.guide_btn_img = Image.open('./assets/imgs/Guide.png')
        self.tk_guide_btn_img = ImageTk.PhotoImage(self.guide_btn_img)
        self.image_data_base.append(self.tk_guide_btn_img)
        self.guide_btn = Button(
            self.dashboard_frame,
            image=self.image_data_base[1],
            bd=0,
            cursor='mouse',
            highlightthickness=0,
            borderwidth=0,
            command=self.__click_guide,
        )
        self.bg_canvas.create_window(
            100,
            212,
            anchor='center',
            window=self.guide_btn,
        )

        """
            Create the calculator button
        """
        self.cal_btn_img = Image.open('./assets/imgs/Calculator.png')
        self.tk_cal_btn_img = ImageTk.PhotoImage(self.cal_btn_img)
        self.image_data_base.append(self.tk_cal_btn_img)
        self.cal_btn = Button(
            self.dashboard_frame,
            image=self.image_data_base[2],
            bd=0,
            cursor='mouse',
            highlightthickness=0,
            borderwidth=0,
            command=self.__click_calculator,
        )
        self.bg_canvas.create_window(
            100,
            360,
            anchor='center',
            window=self.cal_btn,
        )

        """
            Create the background button
        """
        self.bg_btn_img = Image.open('./assets/imgs/background.png')
        self.tk_bg_btn_img = ImageTk.PhotoImage(self.bg_btn_img)
        self.image_data_base.append(self.tk_bg_btn_img)
        self.bg_btn = Button(
            self.dashboard_frame,
            image=self.image_data_base[3],
            bd=0,
            cursor='mouse',
            highlightthickness=0,
            borderwidth=0,
            command=self.__click_bg,
        )
        self.bg_canvas.create_window(
            100,
            286,
            anchor='center',
            window=self.bg_btn,
        )

        """
            Create the about us button
        """
        self.about_us_btn_img = Image.open('./assets/imgs/about_us.png')
        self.tk_about_us_btn_img = ImageTk.PhotoImage(self.about_us_btn_img)
        self.image_data_base.append(self.tk_about_us_btn_img)
        self.about_us_btn = Button(
            self.dashboard_frame,
            image=self.image_data_base[4],
            bd=0,
            cursor='mouse',
            highlightthickness=0,
            borderwidth=0,
            command=self.__click_about_us,
        )
        self.bg_canvas.create_window(
            100,
            434,
            anchor='center',
            window=self.about_us_btn,
        )

        """
            Create the log out function
        """
        self.logout_btn_img = Image.open('./assets/imgs/logout.png')
        self.tk_logout_btn_img = ImageTk.PhotoImage(self.logout_btn_img)
        self.image_data_base.append(self.tk_logout_btn_img)
        self.logout_btn = Button(
            self.dashboard_frame,
            image=self.image_data_base[5],
            bd=0,
            cursor='mouse',
            highlightthickness=0,
            borderwidth=0,
            command=self.__logoutFunc,
        )
        self.bg_canvas.create_window(
            100,
            508,
            anchor='center',
            window=self.logout_btn,
        )



    def __click_bg(self, ):

        self.__initial_dashboard()

        self.background_canvas = Canvas(
            self.dashboard_frame,
            width=620,
            height=420,
            bd=0,
            highlightthickness=0,  # No boarder anymore
            cursor='arrow',
            bg='white'
        )
        self.background_canvas.place(relx=0.27, rely=0.13, anchor=NW)

        self.background_canvas.create_text(
            80,
            40,
            text='積溫介紹',
            fill='black',
            font=('Arial', 30, 'bold italic'),
        )
        self.background_canvas.create_text(
            310,
            140,
            text='在種植農作物的過程中，能得知作物的生長時間是非常重要的，能藉由作物的生長時長得知何時種植能\n'
                 '在何時收成，更勝一步知道一年能收成多少次，推算出產量的大小。而種植時間要如何得知？這便是積\n'
                 '溫的重要性了。\n',
            fill='black',
            font=('Arial', 12),
        )
        self.background_canvas.create_text(
            306,
            180,
            text='積溫（Growing Degree Day）：為作物從種下直到收成間的每日積熱總量，要在日積月累的受熱下才\n'
                 '能累積到足夠的溫度使作物成熟。',
            fill='black',
            font=('Arial', 12),
        )
        self.background_canvas.create_text(
            250,
            215,
            text='積熱：為當日平均溫度減去基本溫度的量，為當日實際能讓植物生長的溫度量。',
            fill='black',
            font=('Arial', 12),
        )
        self.background_canvas.create_text(
            233,
            245,
            text='基本溫度：植物的生長起始溫度，當天的溫度一定要超過此值才能生長。',
            fill='black',
            font=('Arial', 12),
        )
        self.background_canvas.create_text(
            313,
            290,
            text='MGDD：為標準化的積溫，在大多數經濟作物可以有效增加生長速度的溫度區間，為 0～30℃ 的區間，\n'
                 '當日最大溫度超過 30℃ 便以 30℃ 計算，最小溫度小於 0℃ 便以 0℃ 計算。本次的\積溫計算便是用\n'
                 '此方式。',
            fill='black',
            font=('Arial', 12),
        )

    def __click_guide(self, ):

        self.__initial_dashboard()

        self.guide_canvas = Canvas(
            self.dashboard_frame,
            width=620,
            height=420,
            bd=0,
            highlightthickness=0,  # No boarder anymore
            cursor='arrow',
            bg='white'
        )
        self.guide_canvas.place(relx=0.27, rely=0.13, anchor=NW)
        self.guide_canvas.create_text(
            80,
            40,
            text='專案導覽',
            fill='black',
            font=('Arial', 30, 'bold italic'),
        )
        self.guide_canvas.create_text(
            315,
            140,
            text='在這個稻米的積溫計算器中，因為就目前所得的稻米基本溫度資料皆大約 10℃ （台農67號：12.26℃，\n'
                 '台中秈10號：7.07℃，台中109號：9.8℃），故以 10℃ 計算。而每日溫度選了近五年的資料進行平均，\n'
                 '以增加未來的每日溫度的可預報度。',
            fill='black',
            font=('Arial', 12),
        )
        self.guide_canvas.create_text(
            330,
            220,
            text='稻米為我國最重要的農作物之一，為我們的一大主食，有許多種不同的品種，大多數時候為兩穫（兩次收成），\n'
                 '分別為二～六月與七～十一月，十二月與一月為休耕的養地期，在播種後經過插秧（秧苗期，20～30 天）、\n'
                 '營養成長期（分蘗期，50 天）、升殖成長期（開花期，30 天）、成熟期（結穗期，40 天）後，即可收割，\n'
                 '第一穫因為初春到盛夏，成長期溫度偏低，故要花比較多時間；而第二穫從盛夏到秋末，\n'
                 '在台灣能說是最熱的時段，故收成時間通常比第一穫短，而何時最短便要從積溫計算才能得知了。',
            fill='black',
            font=('Arial', 12),
        )


    def __click_calculator(self, ):

        self.__initial_dashboard()

        self.calculator_canvas = Canvas(
            self.dashboard_frame,
            width=620,
            height=420,
            bd=0,
            # highlightthickness=0,  # No boarder anymore
            cursor='arrow',
            bg='white'
        )
        self.calculator_canvas.place(relx=0.27, rely=0.13, anchor=NW)
        self.calculator_canvas.create_text(
            95,
            40,
            text='積溫計算機',
            fill='black',
            font=('Arial', 30, 'bold italic'),
        )


    def __click_about_us(self, ):

        self.__initial_dashboard()

        self.about_us_canvas = Canvas(
            self.dashboard_frame,
            width=620,
            height=420,
            bd=0,
            highlightthickness=0,  # No boarder anymore
            cursor='arrow',
            bg='white'
        )
        self.about_us_canvas.place(relx=0.27, rely=0.13, anchor=NW)
        self.about_us_canvas.create_text(
            80,
            40,
            text='關於我們',
            fill='black',
            font=('Arial', 30, 'bold italic'),
        )
        self.about_us_canvas.create_text(
            215,
            140,
            text='Data: 孫維辰（資料尋搜者）\n\n'
                 'Program: 洪晨哲（接水大掌門）\n\n'
                 'Graphic User interface & data pre-solving: 林群賀（排水大將軍)',
            fill='black',
            font=('Arial', 12),
        )


    def __initial_dashboard(self, ):

        try:

            self.background_canvas.delete("all")
            self.guide_canvas.delete("all")
            self.calculator_canvas.delete("all")
            self.about_us_canvas.delete("all")
        except:

            print("no canvas to delete")
            # pass

    def __logoutFunc(self):

        self.dashboard_frame.destroy()
        base.init_base(self.root)



class ImageProgressing:

    # def __init__(self) -> None:

    def __create_canvas(self, width_, height_) -> None:

        self.canvas = Canvas(
            width=width_,
            height=height_,
            bg='violet',
            bd=0,
        )
        self.canvas.grid()


    def __embed_img(self, img_path) -> None:

        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(
            0,
            0,
            image=img,
            anchor='nw',
        )