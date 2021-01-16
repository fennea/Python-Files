from npyi import npi


# NPPES Review
# *********************************************************************************************************************


def from_nppes(practitioner_data):

    for row in practitioner_data[1:]:

                npi_number = row[11]

                try:
                    response = npi.search(search_params={'number': npi_number})
                except:
                    row[0] += "INPI Error"
                else:

                    try:
                        #data comes back in a multi dimensional format.
                        row[45] = response['results'][0]['taxonomies'][1]['code']
                    except IndexError:
                        try:
                            row[45] = response['results'][0]['taxonomies'][0]['code']
                        except IndexError:
                            # This point in the process basically says, I tried my best, you'll need to check manually
                            row[0] += "Taxonomy Error"

    return practitioner_data

practitioner_data = []

from_nppes(practitioner_data)