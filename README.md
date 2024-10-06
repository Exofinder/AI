# 2024 NASA Space Apps Challenge

---

## Theme: Navigator for the Habitable Worlds Observatory (HWO): Mapping the Characterizable Exoplanets in our Galaxy

---

## Implements

### Machine Learning-Based Approach for Identifying Habitable Exoplanets
I have focused on developing a machine learning-based system to analyze specific characteristics of exoplanets and compute the Goldilocks Zone to evaluate habitability. The core process consists of two main steps:

1. **Goldilocks Zone Calculation**
Exoplanets are identified within the Goldilocks Zone by calculating the distance from their host star. The Goldilocks Zone is the region around a star where liquid water can exist, which is a crucial condition for sustaining life.

2. **Habitability Assessment Based on Earth Similarity**
After filtering exoplanets within the Goldilocks Zone, the model computes a habitability score to evaluate how similar each exoplanet is to Earth. This score is used to determine the likelihood of the exoplanet supporting life.

Two key variables are used in this analysis:

Density: The density of an exoplanet is compared to Earth's density, providing insights into the internal composition of the planet and evaluating the likelihood of a rocky surface similar to Earth's.

Eccentricity: The orbital eccentricity helps assess the climate stability of an exoplanet. A lower eccentricity indicates a more consistent climate, which is an important factor for sustaining life.

The machine learning model integrates these factors to generate a similarity score, which serves as an indicator of the exoplanet’s potential habitability based on Earth-like characteristics.

Technical Implementation
Data Preprocessing: Exoplanet data was preprocessed to ensure clean and accurate inputs for analysis. Missing data was handled appropriately, and relevant features necessary for distance and similarity calculations were selected.

Goldilocks Zone Calculation: The Goldilocks Zone was determined using established astrophysical models, based on the characteristics of the star and the distance from the star.

Machine Learning Model for Similarity Analysis: The model uses density and eccentricity to generate a habitability index. This similarity score represents the likelihood of the exoplanet maintaining life-supporting conditions comparable to those on Earth.

This methodology allows for a systematic identification and evaluation of exoplanets that are most likely to be habitable, providing a valuable tool for future astrobiological studies.
     
---

## Tech Stack

- Build & Bundler: `AWS Elastic Beanstalk`
- Framework: `Spring Boot`
- Language: `Java`
- CSV Reader: `OpenCSV`
- Database: `AWS RDS`
- CORS Configuration: `WebMvcConfigurer`
- Deploy: `AWS`

---
