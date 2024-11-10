meme_dict = {
            "PRINT": "funcion para mostrar un obj en la consola",
            "LOL": "Una respuesta común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Esa palabra no se encuentra en la BD')
