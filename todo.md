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
| Chemins en zigzag | ❌ | [state.io](https://play.google.com/store/apps/details?id=io.state.fight) | 🔄️ |


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

*Rechercher les principales villes françaises libérées après l'arrivée des Américains*

**Jeu**: Libération de la troupe, inspiré de [state.io](https://play.google.com/store/apps/details?id=io.state.fight)

**Exemple de recherche**:

```yaml
Paris:
- date: 25-08- 25 → Date de libération
- symbole: Tour Eiffel → symbole de la ville
- coordonnees: [48.856613, 2.352222]
- description: Paris a été libéré le ... par ... Après la libération... → résumé avec quelques informations
```

**Langage**: `bbcode` + `json`

**Formatage** : 

```json
{
    "Paris": {
        "latitude": 48.856613,
        "longitude": 2.352222,
        "liberation": "1944-08-25T00:00:00Z",
        "description": [
            "Explication rapide et formatage en [b]BBcode[/b]"
        ],
        "symbole": "Tour Effeil"
    },
    "Ville_2": {
        "latitude": 12.345,
        "longitude": 67.890,
        "liberation": "1944-01-01T00:00:00Z",
        "description": [
            "Explication rapide en [b]BBcode[/b] pour Ville_2",
        "symbole": "symbole 2"
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

