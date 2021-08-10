import sqlite3
from sqlite3 import connect

DB_FILEPATH = '/Users/youssefalyakoob/Downloads/rpg_db.sqlite3'
connection = sqlite3.connect(DB_FILEPATH)

cursor = connection.cursor()

'''Total Characters'''
query = '''SELECT COUNT(name) FROM charactercreator_character'''
result = cursor.execute(query).fetchone()
print('Total number of characters:')
print(f'{result[0]} \n')

'''Total Characters in each  Subclass'''
query2 = '''SELECT * FROM
    (SELECT COUNT(DISTINCT character_ptr_id) as cleric FROM charactercreator_cleric), 
    (SELECT COUNT(DISTINCT character_ptr_id) as fighter FROM charactercreator_fighter),
    (SELECT COUNT(DISTINCT character_ptr_id) as mage FROM charactercreator_mage),
    (SELECT COUNT(DISTINCT mage_ptr_id) as necromancer FROM charactercreator_necromancer),
    (SELECT COUNT(DISTINCT character_ptr_id) as thief FROM charactercreator_thief)
	'''
result2 = cursor.execute(query2).fetchone()
print(result2)
print(f'Total number of clerics are {result2[0]}')
print(f'Total number of fighters are {result2[1]}')
print(f'Total number of mages are {result2[2]}')
print(f'Total number of necromancers are {result2[3]}')
print(f'Total number of thieves are {result2[4]}')

'''Total Items'''
query3 = '''SELECT COUNT(item_id) FROM armory_item'''
result3 = cursor.execute(query3).fetchone()
print(f'Total number of items are {result3[0]}')

'''Number of Items That are Weapons and Non Weapons'''
query4 = '''SELECT * FROM
    (SELECT COUNT(item_ptr_id) AS weapons FROM armory_weapon),
    (SELECT COUNT(item_id) - 37 AS nonweapons FROM armory_item)'''
result4 = cursor.execute(query4).fetchone()
print(result4)
print(f'Total number of weapons are {result4[0]}')
print(f'Total number of non weapons are {result4[1]}')

'''Number of Items Each Character Has(first 20 characters)'''
query5 = ''' SELECT character_id AS characters, COUNT(*) AS items FROM  charactercreator_character_inventory
GROUP BY character_id LIMIT 20 '''
results5 = cursor.execute(query5).fetchall()
print(f'Number of items each character has {results5}')

'''Number of Weapons Each Character Has(first 20 characters)'''
query6 = '''SELECT character_id AS char_id, COUNT(*) AS weapons FROM charactercreator_character_inventory AS characters, armory_weapon as armory
 WHERE characters.item_id = armory.item_ptr_id
 GROUP BY character_id LIMIT 20 '''
result6 = cursor.execute(query6).fetchall()
print(f'Number of weapons each character has {result6}')

'''Average Items per Character'''
query7 = '''SELECT AVG(items.COUNT) FROM (
SELECT COUNT(*) AS count FROM charactercreator_character_inventory
 GROUP BY character_id) AS items'''
result7 = cursor.execute(query7).fetchone()
print(f'The average number of items per character is {result7[0]}')

'''Average Weapons per Character'''
query8 = ''' SELECT AVG(weapons.count) FROM (
SELECT COUNT(*) AS count FROM charactercreator_character_inventory AS character_inv, armory_weapon AS armory
WHERE character_inv.item_id = armory.item_ptr_id
GROUP BY character_id) AS weapons '''
result8 = cursor.execute(query8).fetchone()
print(f'The average number of weapons per character is {result8[0]}')