# Audio & Video Processing GUI

## 📚 Description

Ce projet est une application desktop développée avec **PyQt5**, **OpenCV** et **SciPy** permettant le traitement et la compression de signaux audio et vidéo.

Ce TP fait partie du module **Computer Vision 1** (ENIS - GI1).

👉 Objectifs :

* Charger et analyser des fichiers audio
* Visualiser un signal temporel
* Effectuer le rééchantillonnage (resampling)
* Implémenter une compression audio par FFT
* Charger et analyser des vidéos
* Compresser une vidéo avec différents codecs
* Modifier la résolution et le FPS d’une vidéo

---

## 🖥️ Interface

L’application permet :

### 🎵 Audio

* Charger un fichier `.wav`
* Afficher :
  * fréquence d’échantillonnage
  * nombre d’échantillons
  * durée
  * type mono/stéréo
* Visualiser le signal temporel
* Rééchantillonner le signal :
  * Fe/2
  * Fe/4
  * Fe/8
* Compresser un signal audio avec la FFT
* Afficher le spectre fréquentiel

### 🎥 Vidéo

* Charger une vidéo
* Afficher :
  * résolution
  * FPS
  * nombre de trames
* Prévisualiser une frame
* Compresser une vidéo
* Changer :
  * résolution
  * FPS
  * codec vidéo

Codecs supportés :

* MJPG
* XVID
* mp4v

---

## ⚙️ Technologies utilisées

* Python 3
* PyQt5
* OpenCV
* NumPy
* Matplotlib
* SciPy
* FFmpeg

---

## ▶️ Exécution

### 1. Cloner le projet

```bash
git clone https://github.com/waelzouari/audio-video-processing-pyqt.git
cd audio-video-processing-pyqt
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Installer FFmpeg

#### macOS

```bash
brew install ffmpeg
```

#### Ubuntu / Debian

```bash
sudo apt install ffmpeg
```

#### Windows

Télécharger FFmpeg :
https://ffmpeg.org/download.html

---

### 4. Lancer l’application

```bash
python main.py
```

---

## 📁 Structure du projet

```text
audio-video-processing-pyqt/
│── main.py
│── design.py
│── design.ui
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 📌 Fonctionnalités principales

✔ Analyse de signaux audio  
✔ Rééchantillonnage audio  
✔ Compression audio avec FFT  
✔ Visualisation du spectre fréquentiel  
✔ Analyse vidéo  
✔ Compression vidéo  
✔ Support multi-codecs  
✔ Modification de résolution et FPS  
✔ Interface graphique PyQt5  

---

## 🧠 Concepts utilisés

### Audio

* Signal temporel
* FFT (Fast Fourier Transform)
* Compression fréquentielle
* Rééchantillonnage

### Vidéo

* Codec vidéo
* Compression
* Résolution
* FPS (Frames Per Second)

---

## 🧑‍💻 Auteur

* Wael Zouari

