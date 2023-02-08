import mtgsdk as mtg
import csv


with open('core2020_data.csv', "w+", encoding="utf-8") as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csv_writer.writerow(["name", "types", "Legendary", "mana_cost", "rarity"])
	cards = mtg.Card.where(set="M20").all()

	for c in cards:
		try:
			csv_writer.writerow([c.name, c.types, 0 if c.supertypes is None or 'Legendary' not in c.supertypes else 0, c.mana_cost, c.rarity])
		except:
			print(c.name + " Failed")
			pass