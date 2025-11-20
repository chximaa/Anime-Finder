# 🎌 Anime Finder — Multi-Version Anime Search & Recommendation App

Anime Finder is a fun and lightweight project built to help anime fans quickly **search**, **compare**, and **discover** anime.
I created **three versions** of the same concept:

1. **Python Console App (No GUI)** — loads anime data from JSON and interacts through terminal.
2. **Python + Flask Web App** — backend-powered anime finder served on a local website.
3. **HTML/CSS/JS Frontend Website** — a clean standalone UI that loads and filters anime using JavaScript.

---

## 🚀 Features

### ✔ Python Console Version

* 🔍 Search anime by name
* ⚔ Compare two animes by score
* 🎭 Filter by genre
* 🎲 Random anime generator
* 📊 View episodes, score, genres, synopsis, status, and release year
* 📂 All data loaded from `anime_data.json`

### ✔ Flask Web Version

* Backend powered by Python
* Loads the same JSON data
* Provides a simple web interface
* Extends the same functionalities from the console version

### ✔ HTML/CSS/JS Website Version

* Fully responsive UI
* Loads data from JSON using JavaScript
* Search, filter, and display anime with beautiful cards
* Pure frontend (no backend required)

---

## 🧠 How It Works (Python Console)

The console version uses a JSON file that contains a list of anime objects.
Key functions include:

* `get_anime_by_name(name)`
* `compare_two_animes(name1, name2)`
* `get_anime_by_genre(genre)`
* `get_random_anime()`
* `display_anime(anime)`

A simple menu system lets users select actions and interact with the database.

---

## 🛠 Technologies Used

### 🐍 Python

* JSON loading
* Console interaction
* Flask routing

### 🌐 Web

* HTML5
* CSS3
* JavaScript
* JSON data loading

---


## 🎯 Future Improvements

* Add search suggestions
* Add anime cover images in the console version
* Deploy the Flask app online
* Add advanced filtering and sorting
* Build a full GUI version with Tkinter or PyQt

---

## 🤝 Contribute

Pull requests are welcome!
For major changes, open an issue first to discuss what you want to modify.


