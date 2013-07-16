# This program will demonstrate how to take a sequence imputed from the user
# and run a BLAST serach against a local database and return the resuts as an
# XML file.


from Bio.Blast.Applications import NcbiblastnCommandline


def Gets_User_Query():   #This works
    My_Query = raw_input("Enter your DNA query: ")
    
    return My_Query

def Gets_User_Database_Name(): #this works
    my_db = raw_input("Enter your Database name: ")

    return my_db

def Puts_the_query_in_a_text_doc_so_BLAST_can_use_it(My_Query):  #This works

    my_stuff = open("temporary_file.txt", "w")
    my_stuff.write(My_Query)
    my_stuff.close
    return "temporary_file.txt"

def Deletes_the_temporary_file(): #This deletes the temporary_file.txt file
    import os
    os.remove("C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/temporary_file.txt")

    return

def Runs_BLAST_Search(My_Query, Which_Database):

    Puts_the_query_in_a_text_doc_so_BLAST_can_use_it(My_Query) #Create text file
    #print "1"
    
    blastncline = NcbiblastnCommandline(query= "temporary_file.txt", db = "C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/Test_DB_of_ebola_proteins", out = "C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/My_pathogen_blast.xml")
    #NcbiblastnCommandline doesn't like python variables, only strings.  The only input is temporary_file.txt anyway
    blastncline()
    #print "2"
    Deletes_the_temporary_file() #Deletes the temporary text file
    #print "3"
    return

def Open_the_XML_file():  #works
    import os
    os.startfile("C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/My_pathogen_blast.xml")
    return

##def The_GUI_Maker():
##    from Tkinter import *
##    my_GUI = Tk()
##    my_GUI.geometry('750x500+300+100')
##    my_GUI.title("Biosecurity Proof of Concept Program")
##
##    label_one = Label(text="Enter Query Here").place(x=30, y=10)
##
##    that_query_from_GUI = StringVar()
##    t = Text(my_GUI, Variable = that_query_from_GUI)
##    t.place(x=20, y=30)
##
##    my_db = "meh" #this is a placeholder for now
##    my_button = Button(text="Run BLAST", Command = Runs_BLAST_Search(that_query_from_GUI, my_db ).place(x=30,y=450)
##
##    my_GUI.mainloop()
##    Open_the_XML_file()
##    
##
##The_GUI_Maker()

def main():
    the_query = Gets_User_Query()
    my_db = "meh" #Gets_User_Database_Name()    #This isn't needed since we only have one database

    Runs_BLAST_Search(the_query, my_db)

    #The_GUI_Maker()
                       
    Open_the_XML_file()
main()
