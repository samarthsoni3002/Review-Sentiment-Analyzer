# Amazon Review Score Predictor

This project scrapes reviews from the Amazon site and uses a TensorFlow model to predict scores for each review. It then calculates the average score based on the input product URL.

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
The Amazon Review Score Predictor allows users to input a product URL from Amazon, from which reviews are scraped. Each review is analyzed using a trained machine learning model that predicts a score. The project culminates in displaying the average score of all the reviews, providing users with insights into product performance based on user feedback.

## Technologies Used

- **Model Training**: TensorFlow
- **Frontend**: HTML, CSS
- **Backend**: Flask
- **Scraping**: Beautiful Soup, Requests
