# Online-Health-Prediction-using-Django

## Introduction

This project proposes **Django-based Online Health Prediction platform**. This platform utilizes machine learning models to provide online predictions for various health conditions, including **mental disorders, polycystic ovary syndrome (PCOS), and obesity**. These predictions stem from trained models using datasets sourced from **Kaggle**. In addition to offering predictive health analysis, the platform allows users to have the option to download their online health reports generated from the predictions. Moreover, they can conveniently schedule appointments with healthcare professionals by providing their contact details and sending messages directly through the platform. For healthcare professionals, the platform offers the capability to register and manage appointments. Doctors can view and accept appointment requests sent by users.

## Table of Contents

* [Introduction](#Introduction)
* [Features](#Features)
* [Setup](#Setup)
* [About files and folders](#Structure)
* [Tech-Stack](#Tech-Stack)
* [Results](#Results)

## Features

* **Online Health Predictions:** The project has the ability to provide online predictions for mental disorders, PCOS, and obesity based on machine learning models trained on Kaggle datasets.
* **Health Report Download:** The project allows users to download their online health reports generated from the predictions.
* **Appointment Scheduling:** It allows users to schedule appointments with healthcare professionals directly through the platform by providing their contact details and sending messages.
* **User Registration:** This project allows users to register themselves on the platform so that they can predict their health, generate reports and fix appointments with doctors.
* **Doctor Registration:** This project allows healthcare professionals to register themselves on the platform, enabling them to accept appointment requests from users.
* **Appointment Management:** This project allows registered doctors to view and manage appointment requests sent by users, streamlining the appointment scheduling process.

## Setup

* Change the directory to Project

```
cd <directory to this folder>
```

* Install Dependencies

```
pip install -r requirements.txt
```

* Intall libraries or packages: If not installed, follow this

```
pip install <module>
```

* Database setup – Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

* Run application: start development server

```
python manage.py runserver
```

* Run application: Start development server

```
Navigate to http://127.0.0.1:8000/ in your browser
```

## Structure

Here is the breakdown of Django project structure:

* **predictHealth (Folder)**
  > This is the main root directory of Django project. It contains manage.py file, which is the primary script for managing this Django application.

* **home (Folder):**
  > This is a Django app. Django apps are reusable components that contain models, views, and other logic specific to a particular functionality.

* **static (Folder)**: This folder stores static files that are served directly by the web server without being processed by Django. This folder contains: 
  > CSS files, Images
  > CSV files: Dataset used for training models (source: kaggle)
  > encoders: Folder containing encoders for prediction models.
  > models for prediction: This folder contains saved models for prediction/
  > templates (Folder): This folder contains HTML template files.
  > requirements.txt: This file is for managing dependencies. It lists all the required Python packages and libraries needed for this project to function.

## Tech-Stack

* Frontend: HTML, CSS, Bootstrap
* Backend: Python, Django, Sqlite3

## Django Version
> Django Version: 5.0.2

## Results

This section shows the results (Screenshots and Videos)

### Video Results

Check
