# Anime-Finder

**Anime-Finder** is an interactive application that allows users to browse, search, and explore anime series. It comes in **two versions**:

1. **Desktop GUI version** built with Python.
2. **Web GUI version** using HTML, CSS, JS, and Python for backend data handling.

Both versions use a **JSON file** to store anime data, making it easy to extend, modify, or sync across platforms.

---

## Features

* Browse a curated list of anime with details: title, episodes, genres, score, status, year, and synopsis.
* Filter anime by genre or search by name.
* View cover images for each anime.
* JSON-based data storage for easy updates and sharing.
* Two interface options:

  * Desktop GUI (Python)
  * Web GUI (HTML/CSS/JS frontend, Python backend)

---

## Screenshots

**Desktop GUI Version:**
![Desktop GUI Screenshot](screenshots/desktop_gui.png)

**Web GUI Version:**
![Web GUI Screenshot](screenshots/web_gui.png)

---

## Installation

### **1. Clone the repository**

```bash
git clone https://github.com/chximaa/Anime-Finder.git
cd Anime-Finder
```

### **2. Create a virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

> Make sure Python 3.10+ is installed.

---

## Usage

### **Desktop GUI Version**

1. Run the Python application:

```bash
python app.py
```

2. Browse anime, filter by genre, or search for your favorite titles.
3. Modify `anime_data.json` to add or update anime entries.

---

### **Web GUI Version**

1. Start the Python backend server (Flask or FastAPI, depending on your setup):

```bash
python server.py
```

2. Open your browser and navigate to `http://localhost:5000`.
3. Browse anime with a web interface, search, and filter by genre.
4. JSON data is automatically loaded for both versions.

---

## Project Structure

```
Anime-Finder/
│
├─ app.py                 # Desktop GUI Python app
├─ server.py              # Backend server for web GUI
├─ anime_data.json        # Shared data for both versions
├─ README.md              # Project documentation
├─ requirements.txt       # Python dependencies
├─ covers/                # Anime cover images
├─ web/                   # Web GUI files (HTML, CSS, JS)
└─ screenshots/           # Example screenshots
```

---

## Technologies Used

* **Python** – main language for both versions
* **JSON** – data storage
* **HTML/CSS/JavaScript** – web GUI
* **Flask/FastAPI** – Python backend for web GUI (if used)
* **Git & GitHub** – version control

---

## Contributing

Contributions are welcome! You can:

* Add new anime entries to `anime_data.json`
* Improve the desktop GUI
* Enhance the web GUI interface
* Optimize Python backend code

**Steps:**

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Commit your changes: `git commit -m "Add new feature"`
5. Push to the branch: `git push origin feature-name`
6. Create a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


This README clearly explains the **dual-version setup**, the JSON integration, and guides users to use either version easily.

---
