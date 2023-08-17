from prettytable import PrettyTable

pokemons=["Pikachu","Squirtle","Charmander"]
types=["Electric","Water","Fire"]

table=PrettyTable()
table.add_column("Pokemon name",pokemons)
table.add_column("Type",types)

#table.header=True
table.align="l"
print(table)