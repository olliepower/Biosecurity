# This program will demonstrate how to take a sequence imputed from the user
# and run a BLAST serach against a local database and return the resuts as an
# XML file.

#  To get this code to work on your computer, you need to download BLAST+ and move Blastn to the file pathway you 
# specify in this code.  You'll also need to create a database using makeblastdb from a text file.  You also need to 
# change the file pathways that arein this code to the ones that are on your computer.

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
    
    
    blastncline = NcbiblastnCommandline(query= "temporary_file.txt", db = "C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/Test_DB_of_ebola_proteins", out = "C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/My_pathogen_blast.xml")
    #NcbiblastnCommandline doesn't like python variables, only strings.  The only input is temporary_file.txt anyway
    blastncline()
    
    Deletes_the_temporary_file() #Deletes the temporary text file
    
    return

def Open_the_XML_file():  #works
    import os
    os.startfile("C:/Users/Evan/Desktop/Biosecurity_Stuff/Python_biosecurity_test_program/My_pathogen_blast.xml")
    return


def main():
    the_query = Gets_User_Query()
    my_db = "meh" #Gets_User_Database_Name()    #This isn't needed since we only have one database

    Runs_BLAST_Search(the_query, my_db)

    
                       
    Open_the_XML_file()
main()
