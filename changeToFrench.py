# coding=utf-8
import re
import fileinput
import sys

dict = {
	# 'TODDLER GIRL': 	'TOUTE-PETITE FILLE',
	# 'TODDLER BOY': 	'TOUT-PETIT GARÇON', 
	'TODDLER GIRLS': 	'Toute-petite Fille',
	'TODDLER BOYS': 	'Tout-petit Garçon', 
	'Exclusions & Details': 'Exclusions et détails',

	'SHOP SALE':		'Magasiner Le Solde', 
	'SHOP NOW':			'Magasiner Maintenant', 
	'SHOP CLEARANCE':	'Magasiner Les Articles En Liquidation',
	'SHOP NEW ARRIVALS':'Magasiner Les Nouveautés', 
	'SHOP OUTERWEAR':	'Magasiner les vêtements d\'extérieur', 
	'SHOP OUTDOOR':		'Magasiner les vêtements d\'extérieur', 
	'SHOP DRESSES':		'Magasiner Les Robes', 
	'SHOP FLEECE':		'Magasiner Le Molleton', 
	'SHOP SWEATERS':	'Magasiner Les Chandails', 
	'SHOP PANTS':		'Magasiner Les Pantalons', 
	'SHOP HOODIES':		'Magasiner les hauts à capuchon', 
	'SHOP JEANS':		'Magasiner les jeans', 
	'SHOP TEES':		'Magasiner les T-shirts', 
	'SHOP SHIRTS':		'Magasiner les chemises',
	'SHOP SHOES':		'Magasiner les chaussures',
	'SHOP ACCESSORIES':	'Magasiner les accessoires',
	'SHOP TOPS':		'Magasiner Les Hauts',
	'SHOP SHORTS':		'Magasiner les shorts',
	'SHOP TANKS':		'Magasiner les débardeurs',
	'SHOP SWIMWEAR':	'Magasiner les baignade',
	'SHOP GRAPHIC TEES':'Magasiner les t-shirts graphiques',
	'SHOP UNIFORMS':	'Magasiner les uniformes',
	'SHOP ROMPERS':		'Magasiner les Barboteuses',

	'SHOP MEN': 		'Magasiner Pour Homme',
	'SHOP WOMEN':		'Magasiner Pour Homme',
	'FOR HER':			'pour elle',
	'FOR HIM':			'pour lui'

}

dict2 = {
	'WOMEN':			'Femme', 
	'MATERNITY':		'Maternité',
	'MEN': 				'Homme', 
	# 'GIRL': 			'FILLE', 
	# 'BOY': 			'GARÇON', 
	'GIRLS': 			'Fille', 
	'BOYS': 			'Garçon', 
	'BABY':				'Bébé', 

	'&':				'et', 

	'SHOP':				'Magasiner', 
	'NEW ARRIVALS':		'Nouveautés', 
	'OUTERWEAR':		'Vêtements d’extérieur', 
	'DRESSES':			'Robes', 
	'FLEECE':			'Molleton', 
	'SWEATERS':			'Chandails', 
	'PANTS':			'Pantalons', 
	'ACTIVEWEAR':		'La Mode Sport', 
	'HOODIES':			'hauts à capuchon',
	'TEES':				'T-shirts', 
	'SHOES':			'chaussures', 
	'ACCESSORIES': 		'accessoires', 
	'BODY SUITS':		'Cache-couches' , 
	'TOPS':				'hauts', 
	'ONE-PIECES':		'Une-pièces',
	'TANKS':			'débardeurs',
	'SWIMWEAR':			'Collection baignade',
	'GRAPHIC TEES':		'T-shirts imprimés',
	'UNIFORMS':			'uniformes',
	'ROMPERS':			'barboteuses',
	'SHIRTS':			'chemises', 
}

def repl1(m):
	inner_word = m.group(2)
	return m.group(1) + "".join(dict[inner_word.upper()]) + m.group(3)
def repl2(m):
	inner_word = m.group(2)
	return m.group(1) + "".join(dict2[inner_word.upper()]) + m.group(3)

with open(sys.argv[-1], 'r') as file :
  filedata = file.read()
  for key in dict:
	  str_replaced = re.sub(r"(\W)("+str(key)+")(\W)", repl1, filedata, flags=re.I)
	  filedata = str_replaced
  for key in dict2:
	  str_replaced = re.sub(r"(\W)("+str(key)+")(\W)", repl2, filedata, flags=re.I)
	  filedata = str_replaced


with open(sys.argv[-1], 'w') as file:
  file.write(filedata)