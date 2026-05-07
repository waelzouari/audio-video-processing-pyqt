# Détection des contours

## 📚 Description

Ce projet est une application graphique développée avec **PyQt5** et **OpenCV** permettant la détection des contours dans une image.

Ce TP fait partie du module **Computer Vision 1** (ENIS - GI1).

👉 Objectifs :

* Implémenter les filtres **Prewitt** et **Sobel**
* Calculer le **gradient d’image**
* Appliquer un **seuillage**
* Utiliser les dérivées secondes :

  * Laplacien
  * LoG (Laplacian of Gaussian)
* Implémenter l’algorithme **Canny**


---

## 🖥️ Interface

L’application permet :

* Charger une image
* Afficher en niveaux de gris
* Appliquer :

  * Prewitt / Sobel
  * Seuillage
  * Laplacien
  * LoG
  * Canny

---

## ⚙️ Technologies utilisées

* Python 3
* PyQt5
* OpenCV
* NumPy
* Matplotlib

---

## ▶️ Exécution

### 1. Cloner le projet

```bash
git clone https://github.com/waelzouari/Edge-Detection.git
cd Edge-Detection
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Lancer l’application

```bash
python main.py
```

---

## 📁 Structure du projet

```
tp3-edge-detection/
│── main.py
│── design.ui
│── README.md
│── requirements.txt
```

---

## 📌 Fonctionnalités principales

✔ Détection par dérivée première
✔ Calcul du gradient (magnitude)
✔ Seuillage des contours
✔ Détection par dérivée seconde
✔ Détection avancée avec Canny

---

## 🧑‍💻 Auteur

* Wael Zouari

---
