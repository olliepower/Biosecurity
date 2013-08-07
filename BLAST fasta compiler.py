#    This program will create one large text file made up of multiple FASTA files contained in multiple folders 
# inside one large folder and also generates a text file with the descriptions of all the sequences in that database

#  This program WILL NOT create a BLAST searchable database.  To create a BLAST searchable database, take the 
# text file created by this script which contains the compiled fasta files and use the makeblastdb application which
# is included in the BLAST+ package.  More information about the BLAST+ package and the makeblastdb code can be found
# here: http://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download
# and
# here: http://www.ncbi.nlm.nih.gov/books/NBK1763/


####This program is unfinished as of 8/7/2013.####
# The portion which creates a protein searchable database is not finished.



#Things included in the description text file
# How many FASTA files are in the new database
# Number of bases or amino acids in each file
# Whether the database is a nucleotide or a protein database 
# Number of total bases or amino acids in the database
# Number the FASTA descriptions for easy retrieval
#   Something like "1  >fasta description..."
#                  "    Number of bases= 123





def asks_if_your_new_database_is_nt_or_protein(): 
    print "What kind of database are you creating today?"
    my_var = raw_input ("Type \"nt\" for a nucleotide database or \"protein\" for a protein database: ")

    # Just in case you type wrong string is entered. 
    # note: OR boolean won't work here because my_var can't be 2 things at once.        
    if my_var != "nt" and my_var != "protein": 
        print  "You didn't type \"nt\" or \"protein\".  Try again."
        print " "
        return asks_if_your_new_database_is_nt_or_protein()        
    else:
        return my_var 

def asks_what_the_name_of_the_db_will_be():
    the_name_of_the_db = raw_input("What do you want the name of your database to be?: ")
    return the_name_of_the_db









#  This function creates a text file containing a summary of the information in the large, compiled fasta file.
def creates_text_file(name_of_database, which_type_of_db):  

    new_database = open(name_of_database + ".txt", "w")  #Create text file
    #new_database.write("The number of FASTA files in this database: "+ "0" + "\n")  This will be prepended later
    if which_type_of_db == "nt":
        new_database.write("The database contains: Nucleotide sequences \n")
    else:
        new_database.write("The database contains: Protein sequences \n")        
    
    #new_database.write("The total number of bases or amino acids in this database is: " + "0" + "\n") this will be prepended later
    new_database.write("\n")
    new_database.write("\n")
    new_database.write("----------------------------------------------------------------------------------------------------" + "\n")
    new_database.write("\n")
    new_database.write("\n")
    new_database.write("\n")
    new_database.write("Index of files in the database" + "\n")
    new_database.write("\n")
    new_database.write("\n")      
	
	
	
    if which_type_of_db == "nt":    #iterates through each fasta file and run each of the below functions (for nucleotide files)
        import os
		
        base_counter = 0
        amino_acid_counter = 0
        total_nt_or_aa_counter = 0
        first_line = ""
        number_of_fasta_files_counter = 0	

		
        os.chdir("C:/Users/Evan/Desktop/Biosecurity_Stuff/test_genomes_for_database_maker")                #This code can open a file in a folder within a folder
        for files in os.walk('.').next()[1]:                                                               #
            os.chdir("C:/Users/Evan/Desktop/Biosecurity_Stuff/test_genomes_for_database_maker/" + files)   #   
            for files_in_files in os.listdir("."):                                                         #
                if files_in_files.endswith(".fna"):                                                        #
                    print files_in_files                   
                    base_counter = number_of_bases_counter(files, files_in_files)
                    total_nt_or_aa_counter = total_nt_or_aa_counter + base_counter
                    first_line = fasta_first_line_grabber(files, files_in_files)
                    number_of_fasta_files_counter = number_of_fasta_files_counter + 1
                                            
                    #Turn things to strings
                    number_of_fasta_files_counter_as_string = str(number_of_fasta_files_counter)
                    base_counter_as_string = str(base_counter)
                                            
                                            
                    #Things need to be strings to concatonate in a text file
                    new_database.write( number_of_fasta_files_counter_as_string + "   " + first_line + "\n")
                    new_database.write( "    " + "The total number of bases in this sequence is: " + base_counter_as_string + "\n")
                    new_database.write("\n")

        print total_nt_or_aa_counter
        
        new_database.close
         
                   
                                    
	
	
	
	


    elif which_type_of_db == "protein":   #iterates through each fasta file and run each of the below functions (for protein files)
        print "meh"			
    
			

    ### number_of_total_nucleotides_writer(name_of_database, blah) ######  Won't work for some reason here, but works in main()  WHY?!  #####

    ### number_of_fasta_files_prepender(name_of_database, number_of_fasta_files_counter)
    
    return total_nt_or_aa_counter, number_of_fasta_files_counter


#This function works		
def number_of_bases_counter(the_folder_name, the_file_name):  #counts the number of bases a fasta file, returns a number
    purple = open("C:/Users/Evan/Desktop/Biosecurity_Stuff/test_genomes_for_database_maker/" + the_folder_name + "/" + the_file_name)

    line_counter = 0
    base_counter = 0

    for lines in purple:
        if line_counter == 0:
            line_counter = line_counter + 1
        else:  #Each line has an extra space attached to it: they're 70 characters long, not 71.  Even the last one has an extra chracter attached to it.
            base_counter = (len(lines) - 1) + base_counter
            line_counter = line_counter + 1

        
        

    purple.close

    apple = base_counter
    return apple
            
            
            

##def number_of_amino_acid_counter(the_file_name): #counts amino acids in a fasta file, returns a number
##





def number_of_total_nucleotides_writer(name_of_database, total_number):  #prepends the text file with the total number of bases
    
    total_number_as_a_string = str(total_number)
    with file("C:/Users/Evan/Desktop/" + name_of_database + ".txt", 'r') as original: data = original.read()
    with file("C:/Users/Evan/Desktop/" + name_of_database + ".txt", 'w') as modified: modified.write("The total number of bases or amino acids in this database is: " + total_number_as_a_string + "\n" + data)
    
    return
    

    
##def number_of_total_amino_acids(the_file_name):
##

def number_of_fasta_files_prepender(name_of_database, fasta_number):
    fasta_number_as_a_string = str(fasta_number)
    with file("C:/Users/Evan/Desktop/" + name_of_database + ".txt", 'r') as original: data = original.read()
    with file("C:/Users/Evan/Desktop/" + name_of_database + ".txt", 'w') as modified: modified.write("The number of FASTA files in this database is: " + fasta_number_as_a_string + "\n" + data)
    
    return


def fasta_first_line_grabber(the_folder_name, the_file_name):  #takes all the first line in a fasta file and returns them, needs to take only up until the last lowercase letter
    green = open("C:/Users/Evan/Desktop/Biosecurity_Stuff/test_genomes_for_database_maker/" + the_folder_name + "/" + the_file_name)
    apple = green.readline()
    green.close
    return apple


def Open_the_text_file_description(the_name_of_the_file):  
    import os
    os.startfile("C:/Users/Evan/Desktop/" + the_name_of_the_file + ".txt")
    return

def main():

    which_type_of_db = asks_if_your_new_database_is_nt_or_protein()
    name_of_database = asks_what_the_name_of_the_db_will_be()

    if which_type_of_db == "nt":
	    #creates_nucleotide_database(what_name)  #Still needs to be made
	    
            #These create the text document that contains the index of the new database
            
            total_number_of_stuff, total_fasta_files = creates_text_file(name_of_database, which_type_of_db)   # For some reason, I can't get the total nt writer to work in the create_text_file
            number_of_total_nucleotides_writer(name_of_database, total_number_of_stuff)                        # function.  Really wierd.
            number_of_fasta_files_prepender(name_of_database, total_fasta_files)                               #


            Open_the_text_file_description(name_of_database)
    
    
    
main()



