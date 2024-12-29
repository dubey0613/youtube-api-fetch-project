## Project Title
YouTube API Integration Project

## Description
This project integrates with the YouTube API to call it continuously in background (async) with an interval of 10 seconds for fetching the latest videos for a predefined search query (here, cricket) and should store the data of videos in a database. It is designed to be simple to set up and run locally for development purposes.

## Table of Contents
- [Clone the Repository](#clone-the-repository)
- [Environment Variables](#environment-variables)
- [Setup Instructions](#setup-instructions)
- [Starting the Project](#starting-the-project)
- [API Usage](#api-usage)

## Clone the Repository
To clone this repository, follow these steps:

1. Open your terminal.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
   ```bash
   git clone https://github.com/dubey0613/youtube-api-fetch-project.git
   ```

## Environment Variables
You need to create a `.env` file in the root directory of the project. This file will contain sensitive information such as API keys and database URLs.

1. Create a new file named `.env`.
2. Add the following lines to your `.env` file:
   ```
   YOUTUBE_API_KEY=your_youtube_api_key
   DATABASE_URL=postgresql://youtube_api_user:0olDIQ2EEBJgtgjfYFEQzLKM15oppVeY@dpg-ctogkdtumphs73ce7hv0-a.oregon-postgres.render.com/youtube_api
   ```

## Setup Instructions
Before starting the project, you need to set up a virtual environment and install the required dependencies.

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Requirements**:
   Install the necessary packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Starting the Project
Once you have set up your environment and installed the requirements, you can start using the APIs in your application.

1. Ensure your virtual environment is activated.
2. Run your application with:
   ```bash
   python main.py
   ```