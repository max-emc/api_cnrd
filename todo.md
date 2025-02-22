# Paramètres

- [ ] Icone
- [ ] Image au lancement
- [ ] Nom du jeu
- [ ] Activer l'anti-crénelage
- [ ] Modifier les moteurs de rendu
- [ ] Texte du personnage et règles du jeu



# Jeu

- [ ] Configuration de l'environnement + image

- [ ] Animation au survole du joueur

- [ ] Scènes

- [ ] Jeux

<center>
	<h3>
        <u>Progression du jeu</u>
    </h3>
</center>

| Index | Scène | État |          Jeu           | État |
| :---: | :---: | :--: | :--------------------: | :--: |
|   1   | Plage |  ✅   |      Débarquement      |   ❎ tutoriel + recherches   |
|   2   | Ville |  ✅   | Libération de la ville | ❎ tutoriel + audio + recherches |
|   3   |   ❓   |  ❌   |           ❓            |  ❌   |
|   4   |   ❓   |  ❌   |           ❓            |  ❌   |
|   5   |   ❓   |  ❌   |           ❓            |  ❌   |
|   6   |   ❓   |  ❌   |           ❓            |  ❌   |
|   7   |   ❓   |  ❌   |           ❓            |  ❌   |
|   8   |   ❓   |  ❌   |           ❓            |  ❌   |
|   9   |   ❓   |  ❌   |           ❓            |  ❌   |

<center>
	<h3>
        <u>Scènes et jeu non indexés</u>
    </h3>
</center>

|          Scène           | État |            Jeu             |              État               |
| :----------------------: | :--: | :------------------------: | :-----------------------------: |
|            ❓             |  ❌   | Reconstruction de la ville | ❎ tutoriel + audio + recherches |
| Symbole de la République |  🔄️   |            Quiz            | ❎ tutoriel + audio + recherches |



## Débogage

- [ ] Vider la console de débogage
- [ ] Enlever les messages dans la console

|        Fichier         | Console |
| :--------------------: | :-----: |
|          Main          |    ✅    |
|      Débarquement      |    ✅    |
| Libération de la ville |    ✅    |
|          Quiz          |    ✅    |
|           ❓            |    ❌    |
|           ❓            |    ❌    |
|           ❓            |    ❌    |
|           ❓            |    ❌    |
|           ❓            |    ❌    |

# Recherches



### <u>Libération des villes de France</u> :

*Rechercher les principales villes françaises libérée, la date et quelques informations.*

**Format**: `bbcode` + `json`

**Exemple** : 

```json
{
    "Paris": {
        "latitude": 48.856613,
        "longitude": 2.352222,
        "liberation": "1944-08-25T00:00:00Z",
        "description": [
            "Explication rapide et formatage en [b]BBcode[/b]"
        ]
    },
    "Ville_2": {
        "latitude": 12.345,
        "longitude": 67.890,
        "liberation": "1944-01-01T00:00:00Z",
        "description": [
            "Explication rapide en [b]BBcode[/b] pour Ville_2"
        ]
    }
}
```



**Utilisation dans Godot** :

```js
var json_date = "2025-02-23T14:30:00Z"
var date = Time.get_datetime_dict_from_datetime_string(json_date, true)
var formatted_date = "%02d-%02d-%04d" % [date.day, date.month, date.year]
print(formatted_date)
```
