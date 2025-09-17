def famous_births(a):
  for i in sorted(a.values(), key=lambda x: int(x['date_of_birth'])):
    print(f"{i["name"]} is a great scientist born in {i["date_of_birth"]}")
women_scientists = {"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
                    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
                    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
                    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
                }
famous_births(women_scientists)