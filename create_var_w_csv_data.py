from tkinter.filedialog import askopenfilename
import csv

def fallout_files(file_title):

    fallout_file = askopenfilename(initialdir="C:/Users", filetypes=(('CSV File', '*.csv'), ('All Files', '*.*')),

                             title=file_title)

    # r means read. You are going to read teh file.
    with open(fallout_file, 'r') as infile:

        read_function = csv.reader(infile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        list_variable = list(read_function)

    return list_variable