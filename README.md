# Code Challenge Solution

This submission is for the WeatherAPI backend code challenge from CheMondis.

## Overview

...This repository houses the code for a **dynamic and feature-rich Django web application** that serves as a **current weather API**. This solution exceeds the requirements of the weather API coding challenge by providing a robust, well-structured, and easily deployable application.

**Key Features:**

-   **City-Specific Weather:** Retrieve comprehensive weather data for any city, including temperature, humidity, pressure, wind, and descriptive information.
-   **Configurable Caching:** Optimize performance by caching responses for 5, 10, or 60 minutes, balancing freshness and efficiency.
-   **Multilingual Support:** Choose from English and two additional languages of your choice (e.g., English, French, German) for user-friendly experiences.
-   **Robust Error Handling:** Gracefully handle unexpected situations, ensuring a seamless user experience even when faced with API errors or invalid requests.
-   **Modern Technologies:** Leverage the power of `Django`, `Django Rest Frameowkr`, `OpenWeatherMap API`.
-   **Production-Ready:** Enjoy a well-structured architecture, clear documentation, and Docker Compose integration for effortless deployment.

## Installation

 1. Clone the repository with command: `git clone https://github.com/s-khoshdast/weather_api.git`
 2. Enter the folder of code `cd weather_api`
 3. Create a custom `apikey.yaml` file in the root folder of the project.
 4. Run the multi-containers using `docker compose` with the following command: `docker compose up -d`

## Understanding the Code

 - **Data Handling and Validation:**
	 - **Configuration:** Uses a Singleton and a YAML file to manage and validate settings like language, cache time, and API details.
	 - **City Validation:** Ensures proper city names using a regular expression pattern.
	 - **Caching:** Improves performance by caching retrieved weather data based on city and language.
 - **Weather Data Retrieval:**
	 - Builds API requests based on configuration and user-provided city name.
	 - Leverages requests library to send API calls and retrieve weather data in JSON format. Raises appropriate errors if API communication fails or invalid data is received.
 - **API Endpoint and Responses:**
	 - `WeatherView` class handles API requests for specific city weather.
	 - `Serializes` weather data into a consistent `JSON` format using custom serializers.
	 - Returns successful responses with weather details or informative error messages if necessary.

## Additional Information

 - Making things even faster with fancy techniques called `asyncio` – this is my next  adventure!
 - Perfecting the code – I know it's not perfect, and I'm always looking for ways to improve.

## Author

**Sobhan Khoshdast**
E-Mail: sobikhoschdasst@gmail.com
Mobile: +49 (0) 160 4540 - 602
