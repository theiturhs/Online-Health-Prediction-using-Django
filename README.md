# Online-Health-Prediction-using-Django
==========

## Introduction
=========

This project proposes **Django-based Online Health Prediction platform**. This platform utilizes machine learning models to provide online predictions for various health conditions, including **mental disorders, polycystic ovary syndrome (PCOS), and obesity**. These predictions stem from trained models using datasets sourced from **Kaggle**. In addition to offering predictive health analysis, the platform allows users to have the option to download their online health reports generated from the predictions. Moreover, they can conveniently schedule appointments with healthcare professionals by providing their contact details and sending messages directly through the platform. For healthcare professionals, the platform offers the capability to register and manage appointments. Doctors can view and accept appointment requests sent by users.

## Table of Contents

* [Introduction](#Introduction)
* [Features](#Features)
* [Setup](#Setup)
* [Results](#Results)

## Features
========

* **Online Health Predictions:** The project has the ability to provide online predictions for mental disorders, PCOS, and obesity based on machine learning models trained on Kaggle datasets.
* **Health Report Download:** The project allows users to download their online health reports generated from the predictions.
* **Appointment Scheduling:** It allows users to schedule appointments with healthcare professionals directly through the platform by providing their contact details and sending messages.
* **User Registration:** This project allows users to register themselves on the platform so that they can predict their health, generate reports and fix appointments with doctors.
* **Doctor Registration:** This project allows healthcare professionals to register themselves on the platform, enabling them to accept appointment requests from users.
* **Appointment Management:** This project allows registered doctors to view and manage appointment requests sent by users, streamlining the appointment scheduling process.

## Setup
========

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

## About files and folders
========

The breakdown of Django project structure:

