# deep_learning2_exam
Détection Automatique de Sentiment dans des Appels Vocaux à l’aide de Wav2Vec 2.0 et BERT

# 🎙️ Audio Sentiment Analysis (French)

## Description

Ce projet est une application d'Intelligence Artificielle permettant d'analyser le sentiment exprimé dans un fichier audio en français.

Le système fonctionne en deux étapes :

1. **Transcription de la parole en texte** grâce à un modèle **Wav2Vec2** pré-entraîné.
2. **Analyse de sentiment** du texte obtenu grâce à un modèle **BERT**.

L'application fournit :

* la transcription de l'audio ;
* le sentiment détecté (Positive, Neutre ou Négative) ;
* le score de confiance associé.

Le projet propose également :

* une interface graphique avec **Gradio** ;
* une API REST avec **FastAPI** ;
* une architecture modulaire facilitant la maintenance et l'évolution.

---

# Objectifs

L'objectif est de construire une chaîne complète de traitement capable de :

* recevoir un fichier audio ;
* le prétraiter ;
* reconnaître automatiquement la parole ;
* analyser le sentiment du texte transcrit ;
* retourner le résultat à l'utilisateur.

---

# Architecture du projet

```text
                    Audio (.wav)
                         │
                         ▼
             Prétraitement audio
                         │
                         ▼
                 Wav2Vec2 (ASR)
                         │
                         ▼
              Transcription du texte
                         │
                         ▼
                Modèle BERT
        (Analyse de sentiment)
                         │
                         ▼
         Positive / Neutre / Négative
                         │
             Score de confiance
```

---

# Structure du projet

```text
deep_learning2_exam/

│
├── models/
│   ├── asr.py
│   ├── sentiment.py
│   └── __init__.py
│
├── utils/
│   ├── audio.py
│   ├── pipeline.py
│   └── __init__.py
│
├── test_audio/
│   ├── audio1.wav
│   ├── audio2.wav
│   └── audio3.wav
│
├── uploads/
│
├── api.py
├── app.py
├── main.py
│
├── test_audio.py
├── test_asr.py
├── test_sentiment.py
├── test_pipeline.py
│
├── requirements.txt
├── pyproject.toml
├── poetry.lock
│
├── Dockerfile
├── README.md
└── .gitignore
```

---

#  Description des fichiers

## models/asr.py

Implémente la reconnaissance vocale.

Responsabilités :

* charger le modèle Wav2Vec2 ;
* convertir l'audio en texte ;
* retourner la transcription.

---

## models/sentiment.py

Implémente l'analyse de sentiment.

Responsabilités :

* charger le modèle BERT ;
* tokenizer le texte ;
* effectuer la classification ;
* convertir les prédictions en trois classes.

---

## utils/audio.py

Prétraitement audio.

Fonctions :

* chargement du fichier audio ;
* conversion mono ;
* rééchantillonnage à 16 kHz ;
* normalisation.

---

## utils/pipeline.py

Cœur de l'application.

Enchaîne automatiquement :

Audio

↓

Prétraitement

↓

Wav2Vec2

↓

Texte

↓

BERT

↓

Résultat final

---

## api.py

Expose le modèle sous forme d'API REST avec FastAPI.

Retourne un JSON contenant :

* transcription
* sentiment
* score

---

## app.py

Interface utilisateur Gradio.

Permet de tester facilement le système depuis un navigateur.

---

## main.py

Point d'entrée principal du projet.

Permet de lancer :

* Gradio
* FastAPI

---

#  Modèles utilisés

## 1. Reconnaissance vocale (ASR)

**Nom :**

```
jonatasgrosman/wav2vec2-large-xlsr-53-french
```

Description :

Modèle Wav2Vec2 pré-entraîné pour la reconnaissance automatique de la parole en français.

Lien Hugging Face :

https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-french

---

## 2. Analyse de sentiment

**Nom :**

```
nlptown/bert-base-multilingual-uncased-sentiment
```

Description :

Modèle BERT multilingue permettant de classifier un texte selon cinq niveaux de sentiment.

Dans ce projet, les cinq classes sont regroupées en trois :

| Classe originale | Classe finale |
| ---------------- | ------------- |
| 1 étoile         | Négative      |
| 2 étoiles        | Négative      |
| 3 étoiles        | Neutre        |
| 4 étoiles        | Positive      |
| 5 étoiles        | Positive      |

Lien Hugging Face :

https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment

---

#  Technologies utilisées

* Python 3.12
* PyTorch
* TorchAudio
* Transformers
* Hugging Face
* Wav2Vec2
* BERT
* FastAPI
* Gradio
* Poetry

---

# ⚙️ Installation

## Cloner le projet

```bash
git clone <repository_url>

cd deep_learning2_exam
```

---

## Installer les dépendances

Avec Poetry :

```bash
poetry install
```

Ou avec pip :

```bash
pip install -r requirements.txt
```

---

# Utilisation

## Lancer Gradio

```bash
python app.py
```

Puis ouvrir :

```
http://127.0.0.1:7860
```

---

## Lancer l'API

```bash
uvicorn api:app --reload
```

Documentation :

```
http://127.0.0.1:8000/docs
```

---

# Exemple de sortie

```json
{
  "transcription": "je suis très heureux aujourd'hui",
  "sentiment": "positive",
  "score": 0.97
}
```

---

#  Tests

Tester le prétraitement :

```bash
python test_audio.py
```

Tester Wav2Vec2 :

```bash
python test_asr.py
```

Tester BERT :

```bash
python test_sentiment.py
```

Tester le pipeline complet :

```bash
python test_pipeline.py
```

---

#  Points importants

* Les modèles sont téléchargés automatiquement lors de la première exécution.
* Une connexion Internet est nécessaire uniquement pour ce premier téléchargement.
* Les modèles sont ensuite mis en cache localement par Hugging Face.

---

# 📈 Améliorations possibles

* Fine-tuning des modèles sur un jeu de données spécifique.
* Détection des émotions (joie, colère, tristesse, peur, etc.).
* Traitement en temps réel via microphone.
* Déploiement sur le cloud.
* Ajout d'une base de données pour l'historique des analyses.

---

#  Auteur

**Adama Sarr**

Master 2 Intelligence Artificielle

Projet réalisé dans le cadre de l'examen de Deep Learning.

---

#  Références

* PyTorch
* TorchAudio
* Transformers
* Hugging Face
* FastAPI
* Gradio

