from tkinter.filedialog import asksaveasfilename
import csv

def cool_function_name(cool_data):

    print("")

    # sometimes you help users create a usable filesytem
    print("Saving File [please type your initials + todays date | Ex: 'AAF01172020']")

    saved_file = asksaveasfilename(initialdir="C:/Users", filetypes=(('CSV File', '*.csv'),

                                                                     ('All Files', '*.*')), title='Save_files')

    saved_file_full = saved_file + "_SAVED FILE.csv"

    # The w mean write. We are writing a csv file using our variables data This data is a list.
    with open(saved_file_full, 'w') as finished:

        write_function = csv.writer(finished, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL,

                                    lineterminator='\n')

        for row in cool_data:
            write_function.writerow(row)

cool_data = []

cool_function_name(cool_data)
    