# hydra-ml-project

## Steps
1. create the environment and activate it 
```
python -m venv .venv
source .venv/bin/activate
```

2. Install the requirements  
`pip install -r requirements.txt`

3. Get your API key for Google models  

You can get your FREE api key from https://aistudio.google.com/apikey
Create `.env` file from `.env.template` and fill in the API keys 

4. Running the code:

Running it using default parameters (available in conf/config.yaml)
`python my_app.py query=hello`

Running it with other parameters:
`python my_app.py query=hello generator=gemini_flash_2_5`
