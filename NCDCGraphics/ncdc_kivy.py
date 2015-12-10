# coding: utf-8
#!usr/bin/python3.4

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from ncdc_downloader import NcdcDownloader
from ncdc_graphics import NcdcGraphics


class NcdcKivyApp (App):
    ''' The class that create application'''
    
    def build(self):
        ''' The main method that builds layouts and
            binds the other classes methods'''
             
        box_major = BoxLayout()
        box_left = BoxLayout(orientation='vertical', size_hint=(0.35,1))
        box_right = BoxLayout(orientation='vertical')
        
        box_major.add_widget(box_left)
        box_major.add_widget(box_right)
        
        emblem = Image(source=\
                      './emblem/National_Climatic_Data_Center_logo.png')
                      
        label_title = Label(text='NCDC Graphics', font_size=25)
        label_st_number = Label(text='Input station number (USAF)')
        label_year = Label(text='Input year')
        

        self.text_st_number = TextInput(multiline=False, font_size=100)
        self.text_year = TextInput(multiline=False, font_size=100)
        
        self.st_number = self.text_st_number.text
        self.year = self.text_year.text
        
        box_right_inside = BoxLayout(orientation='horizontal')
        box_graphics = BoxLayout(size_hint=(0.5,1), orientation='vertical')
        
        box_left.add_widget(emblem)
        box_left.add_widget(label_st_number)
        box_left.add_widget(label_year)
        
        box_right.add_widget(label_title)
        box_right.add_widget(self.text_st_number)
        box_right.add_widget(box_right_inside)
        
        box_right_inside.add_widget(self.text_year)
        box_right_inside.add_widget(box_graphics)
        
        but_temperature = Button(text='Temperature')
        but_pressure = Button(text='Pressure')
        but_humidity = Button(text='Humidity')
        but_wind_speed = Button(text='Wind speed')
        but_snow_depth = Button(text='Snow depth')
        but_precipitation = Button(text='Precipitation')
        
        but_lst = [but_temperature, but_pressure, but_humidity,\
                   but_wind_speed, but_snow_depth, but_precipitation]
                   
        for button in but_lst:
            box_graphics.add_widget(button)
            
        for button in but_lst:
            button.bind(on_press=self.callback)
        
        return box_major
        
    def callback(self, button):
        ''' The method that is called when a button is pressed'''
        
        parameter = button.text
        st_number = self.text_st_number.text
        year = self.text_year.text
        
        ncdc_down = NcdcDownloader(st_number, year)
        ncdc_down.ncdc_url_to_sqlite()
        
        ncdc_graph = NcdcGraphics(ncdc_down.table_name, parameter)
        ncdc_graph.ncdc_graphics()
        
                
if __name__ == '__main__':
    NcdcKivyApp().run()
