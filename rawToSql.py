import sqlite3
import csv

#connect with db
print("Connecting with db...")
connection = sqlite3.connect("database/drs.db")
cursor = connection.cursor()
print("Connection successfull!")

#SQL command to create the Exercise table
createExerciseTable = """CREATE TABLE EXERCISE(
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
)"""

#SQL command to create the Ingredients table
createIngredientsTable = """CREATE TABLE INGREDIENTS(
    NDB_No INT,
    Shrt_Desc TEXT,
    Water_(g) FLOAT,
    Energ_Kcal INT,
    Protein_(g) FLOAT,
    Lipid_Tot_(g) FLOAT,
    Ash_(g) FLOAT,
    Carbohydrt_(g) FLOAT,
    Fiber_TD_(g) FLOAT,
    Sugar_Tot_(g) FLOAT,
    Calcium_(mg) FLOAT,
    Iron_(mg) FLOAT,
    Magnesium_(mg) FLOAT,
    Phosphorus_(mg) FLOAT,
    Potassium_(mg) FLOAT,
    Sodium_(mg) FLOAT,
    Zinc_(mg) FLOAT,
    Copper_mg) FLOAT,
    Manganese_(mg) FLOAT,
    Selenium_(µg) FLOAT,
    Vit_C_(mg) FLOAT,
    Thiamin_(mg) FLOAT,
    Riboflavin_(mg) FLOAT,
    Niacin_(mg) FLOAT,
    Panto_Acid_mg) FLOAT,
    Vit_B6_(mg) FLOAT,
    Folate_Tot_(µg) FLOAT,
    Folic_Acid_(µg) FLOAT,
    Food_Folate_(µg) FLOAT,
    Folate_DFE_(µg) FLOAT,
    Choline_Tot_ (mg) FLOAT,
    Vit_B12_(µg) FLOAT,
    Vit_A_IU FLOAT,
    Vit_A_RAE FLOAT,
    Retinol_(µg) FLOAT,
    Alpha_Carot_(µg) FLOAT,
    Beta_Carot_(µg) FLOAT,
    Beta_Crypt_(µg) FLOAT,
    Lycopene_(µg) FLOAT,
    Lut+Zea_ (µg) FLOAT,
    Vit_E_(mg) FLOAT,
    Vit_D_µg FLOAT,
    Vit_D_IU FLOAT,
    Vit_K_(µg) FLOAT,
    FA_Sat_(g) FLOAT,
    FA_Mono_(g) FLOAT,
    FA_Poly_(g) FLOAT,
    Cholestrl_(mg) FLOAT,
    GmWt_1 FLOAT,
    GmWt_Desc1 TEXT,
    GmWt_2 FLOAT,
    GmWt_Desc2 TEXT,
    Refuse_Pct FLOAT 
)"""

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
        cursor.execute("INSERT INTO INGREDIENTS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
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