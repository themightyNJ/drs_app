import sqlite3
import csv

#connect with db
print("Connecting with db...")
connection = sqlite3.connect("database/drs.db")
cursor = connection.cursor()
print("Connection successfull!")

#Dropping any previous versions of table
try:
    cursor.execute("DROP TABLE EXERCISE")
    cursor.execute("DROP TABLE INGREDIENTS")
except:
    print("No previous table.")

#SQL command to create the Exercise table
createExerciseTable = '''CREATE TABLE EXERCISE (
    Date TEXT,
    Calories FLOAT,
    Steps FLOAT,
    Distance FLOAT,
    floors INT,
    Minutes_sitting FLOAT,
    Minutes_of_slow_activity INT,
    Minutes_of_moderate_activity INT,
    Minutes_of_intense_activity INT,
    Calories_Activity FLOAT
)'''

#SQL command to create the Ingredients table
createIngredientsTable = '''CREATE TABLE INGREDIENTS (
    NUM INT,
    NDB_No INT,
    Shrt_Desc TEXT,
    Water_ FLOAT,
    Energ_Kcal INT,
    Protein_ FLOAT,
    Lipid_Tot_ FLOAT,
    Ash_ FLOAT,
    Carbohydrt_ FLOAT,
    Fiber_TD_ FLOAT,
    Sugar_Tot_ FLOAT,
    Calcium_ FLOAT,
    Iron_ FLOAT,
    Magnesium_ FLOAT,
    Phosphorus_ FLOAT,
    Potassium_ FLOAT,
    Sodium_ FLOAT,
    Zinc_ FLOAT,
    Copper_ FLOAT,
    Manganese_ FLOAT,
    Selenium_ FLOAT,
    Vit_C_ FLOAT,
    Thiamin_ FLOAT,
    Riboflavin_ FLOAT,
    Niacin_ FLOAT,
    Panto_Acid_ FLOAT,
    Vit_B6_ FLOAT,
    Folate_Tot_ FLOAT,
    Folic_Acid_ FLOAT,
    Food_Folate_ FLOAT,
    Folate_DFE_ FLOAT,
    Choline_Tot_ FLOAT,
    Vit_B12_ FLOAT,
    Vit_A_IU FLOAT,
    Vit_A_RAE FLOAT,
    Retinol_ FLOAT,
    Alpha_Carot_ FLOAT,
    Beta_Carot_ FLOAT,
    Beta_Crypt_ FLOAT,
    Lycopene_ FLOAT,
    Lut_Zea_ FLOAT,
    Vit_E_ FLOAT,
    Vit_D_µg FLOAT,
    Vit_D_IU FLOAT,
    Vit_K_ FLOAT,
    FA_Sat_ FLOAT,
    FA_Mono_ FLOAT,
    FA_Poly_ FLOAT,
    Cholestrl_ FLOAT,
    GmWt_1 FLOAT,
    GmWt_Desc1 TEXT,
    GmWt_2 FLOAT,
    GmWt_Desc2 TEXT,
    Refuse_Pct FLOAT 
)'''

#executing the create Exercise table command
print("Creating Exercise table.")
cursor.execute(createExerciseTable)
print("Exercise Table created successfully!")

#commiting all the changes
print("Commiting all the changes...")
connection.commit()
print("Commited successfully!")

#executing the create Ingredients table command
print("Creating Ingredients table.")
cursor.execute(createIngredientsTable)
print("Ingredients Table created successfully!")

#commiting all the changes
print("Commiting all the changes...")
connection.commit()
print("Commited successfully!")

#reading the exercise.csv raw file and inserting it into the drs.db in Exercise table
print("Reading exercise.csv file...")
print("Inserting values in db...")
with open("raw_datasets/exercise.csv") as exerciseFile:
    e_num_records = 0
    for row in exerciseFile:
        cursor.execute("INSERT INTO EXERCISE VALUES(?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        e_num_records += 1
    print("Inserted all the values in db!")

#reading the ingredients.csv raw file and inserting it into the drs.db in Ingredients table
print("Reading ingredients.csv file...")
print("Inserting values in db...")
with open("raw_datasets/ingredients.csv") as ingredientsFile:
    
    i_num_records = 0
    for row in ingredientsFile:
        cursor.execute("INSERT INTO INGREDIENTS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        i_num_records += 1
    print("Inserted all the values in db!")

#close the connection from db
print("Disconnecting from the db...")
connection.close()
print("Disconnected from the db!")
print("""Successfully transfered:
    {} Records in Exercise table and 
    {} Records in Ingredients table!""".format(e_num_records, i_num_records))