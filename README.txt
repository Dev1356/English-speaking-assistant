English Speaking Assistant - Setup & Run Instructions
-----------------------------------------------------

1. Prerequisites:
   - Python 3 installed (https://www.python.org/downloads/)
   - Internet connection
   - OpenAI API Key (get one from https://platform.openai.com/account/api-keys)

2. Setup:
   - Extract the zip folder anywhere you like.
   - Open a terminal (command prompt) in the extracted folder.
   - (Optional) Create and activate a Python virtual environment:
     Windows:
       python -m venv venv
       venv\Scripts\activate
     macOS/Linux:
       python3 -m venv venv
       source venv/bin/activate

   - Install required packages:
     pip install -r requirements.txt

3. Set your OpenAI API key as environment variable:
   Windows (cmd):
     set OPENAI_API_KEY=your_api_key_here
   Windows (PowerShell):
     $env:OPENAI_API_KEY="your_api_key_here"
   macOS/Linux:
     export OPENAI_API_KEY=your_api_key_here

4. Run the app:
   python app.py

5. Open your browser and go to:
   http://127.0.0.1:5000

6. Click "Start Speaking" and talk to the assistant.

-----------------------------------------------------
For deployment online, I can provide extra steps if needed.