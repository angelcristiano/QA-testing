def cantidad=context.expand('${Properties#cantidadPokemons}')

def task="python /pokemon.py $cantidad".execute()
log.info (task.text)