# PythonAIAgent
PythonAIAgent Tutorial from Tech with Tim - USING RAG
# What are we doing?
- - Query over pandas data - read our csv file - query on top of it - ask questions based on that data source using kind of a streamline agent
- create a query engine , which allows us to ask specific questions about the pandas data source - `pip install llama-index-experimental`
# Commands & setup Info
- Firstly create a virtual environment - `python3 -m venv ai` here ai is the name of the virtual env folder 
- Then activate the virtual env - Windows : `source ai/scripts/activate`
- Installing LlamaIndex allowing us to ingest these different data sources.
- Install a library for reading the pdfs , env(loading env files) , pandas(to read csv file)
- `pip install llama-index pypdf python-dotenv pandas`
- `pip freeze > requirements.txt` - loads the libraries we've installed
- Create a .env file - to store our open-ai api key - to interact with an ai model - we use openAI - get the key from - `https://platform.openai.com/api-keys`
- Activate our env file


# Data Sources
### Data folder
Kaggle - https://www.kaggle.com/datasets/joebeachcapital/world-population-by-country-2023 - rename it to population.csv
About Canada from Wikipedia - https://en.wikipedia.org/wiki/Canada - Tools > Download as PDF 
Create a notes.txt file - which will store different notes
# Concepts/tools/frameworks to Understand
- LlamaIndex - https://docs.llamaindex.ai/en/stable/ - LlamaIndex is a framework for building context-augmented generative AI applications with LLMs including agents and workflows.