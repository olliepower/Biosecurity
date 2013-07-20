#This program will query the BLAST database in chunks of nucleotides 

# All you need is a genome sequence and this program will query BLAST
# 160 NT at a time.  Remeber to put the genome in fasta format.  Name it
# my_genome.txt

from Bio.Blast import NCBIWWW

def Open_the_XML_file():  #works
    import os
    os.startfile("C:/Users/Evan/Desktop/overload_genome.xml")
    return

def main():
    my_string_to_use = open("C:/Users/Evan/Desktop/Biosecurity_Stuff/Genomes/test_gene.txt","r")


    line_one = ""   #This program searches 2 lines, the strings here will hold them during the for loop
    line_two = ""
    counter = 0     #this is used in the for loop 
    blast_counter = 1 #this counts the number of blast searches performed
    for lines in my_string_to_use:
        if counter == 0:
            counter = counter + 1
            #print "pear"  #These random print statements were used for troubleshooting
        elif counter%2 == 1:  #used if the counter is odd, it saves the line of nucleotides for later
            line_one = lines
            counter = counter+1
            #print "apple"
        elif counter%2 == 0:  # if the counter is even, it will blast search both lines and clear the temporary lines
            line_two = lines
            result_handle = NCBIWWW.qblast("blastn", "nt", line_one + line_two)
            #print "purple"
            print result_handle  #This tells you in the python terminal if a blast search was performed
            save_file = open("C:/Users/Evan/Desktop/overload_genome.xml", "w")
            save_file.write(result_handle.read())
            save_file.close()
            result_handle.close()
            print "Blast search number: ", blast_counter

            blast_counter = blast_counter + 1
            counter = counter + 1
        
        #print lines
        
    my_string_to_use.close()
    
    Open_the_XML_file()
main()

