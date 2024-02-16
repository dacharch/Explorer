import os
from  explorer.file import *
from pick import pick



def menu(path,suffix_list):

    if path[0] == '.' :
       path  = path[1:]
       path =  os.getcwd().replace("//", "/") +path
       
    if path:
           list_temp  =[]
           list=[]
           folder =[]
           
           for x in os.listdir(path):
               list_temp.append(x)
           
           for b in list_temp:
               if isFolder(path +b ) is True:
                  folder.append(b)
                  
           if len(suffix_list) == 0:
               list = list_temp
                      
           title = "Please Choose a and Click Enter"
           options = list
           options.append(">back<")
           options.append(">quit<") 
           selected = pick(options,title,multiselect=True,
                           min_selection_count=1)
           selected_word(selected,list,suffix_list,path)
           
    else:
        print("The path is invalid")       

def selected_word(selected,list,suffix_list,path):
    selected_name = selected[0][0] 
    selected_num = selected[0][1]
  
    if selected_num == len(list)-1:
        quit() 
    elif selected_num == len(list)- 2 :
         if get_upper_level(path) is False:
              menu(path,suffix_list)
         else:
             menu(get_upper_level(path),suffix_list)
    else:
        if isFolder(path+selected_name) is True:
            menu(path+selected_name+"/",suffix_list)
        
                     
             
             

         

    

    
   
        
            
    
            
   
    
    
               
                  
            
            
             
            
        
                   
           
                       
                  
                  
           
                  
            
                  
                  
              
           
        
           
               
       
       
    