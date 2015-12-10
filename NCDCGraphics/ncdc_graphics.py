# coding: utf-8
#!usr/bin/python3.4

import sqlite3

import numpy 
from matplotlib import pyplot 

from ncdc_downloader import NcdcDownloader


class NcdcGraphics:
    '''The class that build the graph for ncdc archive'''
    
    def __init__(self, table_name, parameter):
        self.parameter = parameter
        self.table_name = table_name
        
    def moving_average(self, a, n=10) :
        '''The method calculates the moving average'''
        
        res = numpy.cumsum(a, dtype=float)
        res[n:] = res[n:] - res[:-n]
        return res[n - 1:] / n
        
    def ncdc_graphics(self, table_name=None, parameter=None):
        ''' The method builds the graphics for different parameters'''
        
        try: 
            
            parameter = self.parameter
            table_name = self.table_name
            
            conn = sqlite3.connect('ncdc.db')
            self.c = conn.cursor()
            
            
#----------------------TEMPERATURES-------------------------------------
                  
            if parameter == 'Temperature':
                
                self.c.execute(("SELECT temp FROM '%s'") % self.table_name)
                temp_array_F = numpy.array(self.c.fetchall())
               
                temp_array_C = numpy.array([(5/9)*(i-32) for i in temp_array_F])
                temp_mask = numpy.ma.array(temp_array_C, mask=(temp_array_F>100),\
                                          copy=True)
                temp_filter = self.moving_average(temp_mask)
                mean_temp = float(numpy.mean(temp_mask))
                
                self.c.execute(("SELECT max FROM '%s'") % self.table_name)
                max_array_F = numpy.array(self.c.fetchall())
                max_array_C = numpy.array([(5/9)*(i-32) for i in max_array_F])
                max_mask = numpy.ma.array(max_array_C, mask=(max_array_C>100),\
                                          copy=True)
                
                max_filter = self.moving_average(max_mask) 
                max_value = float(numpy.max(max_mask))
                
                self.c.execute(("SELECT min FROM '%s'") % self.table_name)
                min_array_F = numpy.array(self.c.fetchall())
                
                min_array_C = numpy.array([(5/9)*(i-32) for i in min_array_F])
                min_mask = numpy.ma.array(min_array_C, mask=(min_array_C>100),\
                                          copy=True)
                min_filter = self.moving_average(min_mask) 
                min_value = float(numpy.min(min_mask))
                
                
                pyplot.plot(temp_mask, 'g--',\
                            label = 'Mean daily temperature [C]')
                pyplot.plot(max_mask, 'r--',\
                            label = 'Max daily temperature [C]')
                pyplot.plot(min_mask, 'b--',\
                            label = 'Min daily temperature [C]')
                
                pyplot.plot(temp_filter, 'g', linewidth = 2,\
                            label = 'Mean daily temperature filter [C]')
                pyplot.plot(max_filter, 'r', linewidth = 2,\
                            label = 'Max daily temperature filter [C]')
                pyplot.plot(min_filter, 'b', linewidth = 2,\
                            label = 'Min daily temperature filter [C]')
                
                pyplot.axis([1, 366, int(min_value)-2, int(max_value)+2]) 
                pyplot.xlabel('DOY')
                pyplot.ylabel('C')
                pyplot.title('Mean, maximum and minimum temperature')
                pyplot.grid(True)
                
                temp_lst = [str(round(mean_temp, 1)), 
                            str(round(max_value,1)), 
                            str(round(min_value,1))]
                
                
                pyplot.text (50, max_value-1, 
                            'Mean & max & min temperature = ' + \
                            ((' & ').join(temp_lst)) + ' C',\
                             bbox={"facecolor": "yellow", 
                            "boxstyle": "sawtooth"})
    
                pyplot.legend(loc='lower center', prop={'size':7})
                pyplot.show()
    
    
#----------------------PRESSURE-----------------------------------------
    
            if parameter == 'Pressure':
                
                self.c.execute(("SELECT slp FROM '%s'") % self.table_name)
                slp_array = numpy.array(self.c.fetchall())
                slp_mask = numpy.ma.array(slp_array, mask=(slp_array>9998),\
                                          copy=True)
                
                slp_filter = self.moving_average(slp_mask)
                mean_value = round(float(numpy.mean(slp_mask)),1)
                max_value = round(float(numpy.max(slp_mask)),1)
                min_value = round(float(numpy.min(slp_mask)),1)
                
                pyplot.plot(slp_mask, 'k--',\
                            label = 'Pressure on Sea level [mbar]')
                
                pyplot.plot(slp_filter, 'k', linewidth = 2,\
                            label = 'Pressure on Sea level filter [mbar]')
                
                pyplot.axis([1, 366, int(min_value-2), int(max_value+2)])
                pyplot.xlabel('DOY')   
                pyplot.ylabel('mbar')   
                pyplot.title('Pressure on Sea level') 
                pyplot.grid(True)
                pyplot.legend(loc='lower center', prop={'size':7})
                
                pressure_lst = [str(mean_value), str(max_value),\
                                str(min_value)]
                
                pyplot.text (30, max_value-3, 
                            'Mean & max & min pressure = ' + \
                            ((' & ').join(pressure_lst)) + ' mbar',\
                             bbox={"facecolor": "yellow", 
                            "boxstyle": "sawtooth"})
                pyplot.show()
                
                
#----------------------HUMIDITY-----------------------------------------
                
            if parameter == 'Humidity':
                
                self.c.execute(("SELECT dewp FROM '%s'") % self.table_name)
                dewp_array_F = numpy.array(self.c.fetchall())
                dewp_array_C = numpy.array([(5/9)*(i-32) for i in dewp_array_F])
                dewp_mask = numpy.ma.array(dewp_array_C, mask=(dewp_array_C>100),\
                                          copy=True)
                                          
                self.c.execute(("SELECT temp FROM '%s'") % self.table_name)
                temp_array_F = numpy.array(self.c.fetchall())
                temp_array_C = numpy.array([(5/9)*(i-32) for i in temp_array_F])
                temp_mask = numpy.ma.array(temp_array_C, mask=(temp_array_C>100),\
                                          copy=True)
                
                rh_array = numpy.array([100*(1-0.05*(temp - dewp)) for temp, dewp\
                                      in zip (temp_mask, dewp_mask)])
                
                
                rh_filter = self.moving_average(rh_array)
                mean_value = round(float(numpy.mean(rh_array)),1)
                max_value = round(float(numpy.max(rh_array)),1)
                min_value = round(float(numpy.min(rh_array)),1)
                
                pyplot.plot(rh_array, 'b--',\
                            label = 'Relative humidity [%]')
                
                pyplot.plot(rh_filter, 'b', linewidth = 2,\
                            label = 'Relative humidity filter [%]')
                
                pyplot.axis([1, 366, int(min_value-2), int(max_value+2)])
                pyplot.xlabel('DOY')   
                pyplot.ylabel('%')   
                pyplot.title('Relative humidity') 
                pyplot.grid(True)
                pyplot.legend(loc='lower center', prop={'size':7})
                
                rh_lst = [str(mean_value), str(max_value),\
                                str(min_value)]
                
                pyplot.text (30, max_value-2, 
                            'Mean & max & min relative humidity = ' + \
                            ((' & ').join(rh_lst)) + ' %',\
                             bbox={"facecolor": "yellow", 
                            "boxstyle": "sawtooth"})
                pyplot.show()
                
                
#----------------------WIND SPEED---------------------------------------
                
            if parameter == 'Wind speed':
                
                self.c.execute(("SELECT wdsp FROM '%s'") % self.table_name)
                wdsp_array_k = numpy.array(self.c.fetchall())
                wdsp_array_m = numpy.array([0.514444*i for i in wdsp_array_k])
                wdsp_mask = numpy.ma.array(wdsp_array_m, mask=(wdsp_array_m>998),\
                                          copy=True)
                
                wdsp_filter = self.moving_average(wdsp_mask)
                mean_value = round(float(numpy.mean(wdsp_mask)),1)
                max_value = round(float(numpy.max(wdsp_mask)),1)
                min_value = round(float(numpy.min(wdsp_mask)),1)
                
                pyplot.plot(wdsp_mask, 'k--',\
                            label = 'Mean wind speed [m/s]')
                
                pyplot.plot(wdsp_filter, 'k', linewidth = 2,\
                            label = 'Mean wind speed filter [m/s]')
                
                pyplot.axis([1, 366, int(min_value-1), int(max_value+1)])
                pyplot.xlabel('DOY')   
                pyplot.ylabel('m/s')   
                pyplot.title('Mean wind speed') 
                pyplot.grid(True)
                pyplot.legend(loc='lower center', prop={'size':7})
                
                wdsp_lst = [str(mean_value), str(max_value),\
                                str(min_value)]
                
                pyplot.text (70, max_value-0.1, 
                            'Mean & max & min wind speed = ' + \
                            ((' & ').join(wdsp_lst)) + ' m/s',\
                             bbox={"facecolor": "yellow", 
                            "boxstyle": "sawtooth"})
                pyplot.show()
                
                
#----------------------SNOW DEPTH---------------------------------------

            if parameter == 'Snow depth':
                
                self.c.execute(("SELECT sndp FROM '%s'") % self.table_name)
                sndp_array = numpy.array(self.c.fetchall())
                sndp_array[sndp_array>998] = 0
                sndp_array_mm = numpy.array([i*2.54 for i in sndp_array])
                min_value = int(min(sndp_array_mm))
                max_value = int(max(sndp_array_mm))
                sndp_len = len(sndp_array_mm)

                pyplot.axis([1, sndp_len, min_value, max_value+5])
                pyplot.bar(range(1,sndp_len+1), sndp_array_mm, color='cyan',\
                            align='center', edgecolor='cyan',\
                            label = 'Snow depth [mm]')

                pyplot.xlabel('DOY') 
                pyplot.ylabel('mm')    
                
                pyplot.title('Snow depth [mm]') 
                pyplot.grid(True)
                pyplot.legend(loc='best', prop={'size':10})
                pyplot.show()
                
                
#----------------------PRECIPITATION------------------------------------

            if parameter == 'Precipitation':
                
                self.c.execute(("SELECT prcp FROM '%s'") % self.table_name)
                prcp_array = numpy.array(self.c.fetchall())
                prcp_array[prcp_array>99] = 0
                prcp_array_mm = numpy.array([i*25.4 for i in prcp_array])
                min_value = numpy.min(prcp_array_mm)
                max_value = numpy.max(prcp_array_mm)
                prcp_sum = numpy.sum(prcp_array_mm)
                prcp_len = len(prcp_array_mm)
                
                pyplot.axis([1, prcp_len, int(min_value), int(max_value)+5])
                pyplot.bar(range(1,prcp_len+1), prcp_array_mm, color='blue',\
                          align='center', edgecolor='blue',\
                          label = 'Precipitation [mm]')
                               
                prcp_lst = [str(round(float(max_value),1)),\
                            str(round(float(prcp_sum),1))]
                
                pyplot.text (10, int(max_value), 
                            'Max & sum precipitation = ' + \
                            ((' & ').join(prcp_lst)) + ' mm',\
                             bbox={"facecolor": "yellow", 
                            "boxstyle": "sawtooth"})
                            
                pyplot.xlabel('DOY') 
                pyplot.ylabel('mm')    
                
                pyplot.title('Precipitation [mm]') 
                pyplot.grid(True)
                pyplot.legend(loc='upper right', prop={'size':10})
                pyplot.show()
                
        except Exception as e:
            
            print ('Graph are not built')
            print (e)
            
if __name__ == '__main__':
    ncdc_down_1 = NcdcDownloader(260590, 2005)     # Class test
    ncdc_down_1.ncdc_url_to_sqlite()
    
    ncdc_graph_1 = NcdcGraphics(ncdc_down_1.table_name, 'Temperature')
    ncdc_graph_1.ncdc_graphics()
