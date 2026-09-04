\# Git and GitHub Assignment



\## Project Overview



This project is a Flask-based To-Do application integrated with MongoDB.



\## Technologies Used



\- Python

\- Flask

\- MongoDB Atlas

\- PyMongo

\- HTML

\- Git and GitHub



\## Features



\- To-Do form with Item Name and Item Description

\- Item ID, Item UUID and Item Hash fields

\- POST API endpoint `/submittodoitem`

\- MongoDB storage for submitted To-Do items

\- Git branching, merging, soft reset and rebase operations



\## MongoDB Configuration



The MongoDB connection string is stored in a `.env` file using the `MONGO\_URI` variable.



The `.env` file is excluded from Git using `.gitignore` so that credentials are not committed to the repository.



\## Running the Application



Install the required packages:



```bash

pip install flask pymongo python-dotenv

