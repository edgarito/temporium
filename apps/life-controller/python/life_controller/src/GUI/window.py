'''
Created on Apr 24, 2014

@author: Cactus
'''
from tkinter import *
from GUI.visual_feedback import *
from GUI.button_manuel import *
from GUI.button_action import *
import time


class window(Tk):
    '''
    Principal window of the GUI
    '''
    
    

    def __init__(self,parent , current_state):
        '''
        Constructor
        '''
        Tk.__init__(self, parent)
        self.parent = parent
        self.current_state = current_state
        

        self.visual_feedback  = visual_feedback(self, self.current_state)
        self.button_manuel = button_manuel(self)
        self.button_action = button_action(self)
        
        self.refresh_after()
        
        
    def test_r (self):
        self.refresh()
        self.after_idle(self.test_r)

      
    def refresh(self) :
        """Function to call to reresh the GUI"""    
        self.visual_feedback.draw()
    
    def refresh_after(self):
        self.refresh()
        self.after(100, self.refresh_after)   
        #time.sleep(0.1)     
        #self.after_idle(self.refresh_test)


        


    
    
    


      
        