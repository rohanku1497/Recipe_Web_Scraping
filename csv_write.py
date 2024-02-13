import csv 
    
# field names 
fields = ['Recipe Name','Description','Cook time','Image', 'Grocery Item Names/quantity/quantity_types', 'instructions','ingredients list','Serving size','nutrients'] 

# name of csv file 
filename = "receipe_scarpe.csv"

def main(rows):   
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)
        