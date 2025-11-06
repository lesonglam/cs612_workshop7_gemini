Create an AI Agent with Gemini

Step 0: Having a laptop/pc, with Window10/11 pre-installed 

Step 1: Install Python 3.1x 

Step 2: Installing Conda (for creating environment)

Install miniconda: https://www.anaconda.com/download

Install with default options all through the way

To get the installed path, open anaconda promt, type "conda info", something like: "C:\Users\<Username>\miniconda3"

Type in Window searchbar: "Edit Environment Variables"
In the "System variables" box, choose "Path" => "Edit" => "New"
Add the following to System Variable Path

C:\Users\<Username>\miniconda3
C:\Users\<Username>\miniconda3\Scripts
C:\Users\<Username>\miniconda3\Library\bin


Open the new terminal command, type "conda", if it popup something like:
"usage: conda-script.py [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda is a tool for managing and deploying applications, environments and packages.
.................."
It means you're successful installation process

Step 2: Installing VScode IDE
In VScode, insatll extention name "Jupyter" from  Microsoft (96,664,xxx downloads)

Step 3: Getting Gemini API key
Create a new API key from link: https://aistudio.google.com/api-keys
Save it here: GEMINI_API_KEY="your-api-key"

Step 4: Creating environment and libraries

conda create --name ws7 python=3.12
conda activate ws7

pip install -U google-generativeai
pip install -U faiss-cpu
pip install -U tiktoken
pip install -U python-dotenv
pip install notebook
pip install Flask requests python-dotenv

Clone this repo.
Inside the project folder, create a .env file with this content: GEMINI_API_KEY="your-api-key"
Open the file main.ipynb, click Run the cell "Testing environment", and Select the kernel (the environment) you had created.
If you see the "'Success!'" message, that means you're done with the setup environment.

Step 5: During class
Tip: To change directory other drive like D, type "D:"
Three runs: 
    1. Run by cell: main.ipynb
    2. Run by file: python main.py
    3. Run the web using Flask: flask --app app run
       On the browser: http://127.0.0.1:5000/


------------------------------------
Step 1001: Destroying everything

At the end of the day, If you want to delete an environment

conda deactivate
conda remove --name ENV_NAME --all







