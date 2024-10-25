# PythonAIAgent

PythonAIAgent Tutorial from Tech with Tim - USING RAG

# What are we doing?

- - Query over pandas data - read our csv file - query on top of it - ask questions based on that data source using kind of a streamline agent
- create a query engine , which allows us to ask specific questions about the pandas data source - `pip install llama-index-experimental`
- Things to do to make it work a little bit better and to optimize it's performance
  - Pass an Instruction string that specifies what it should be doing
  - Then we want to give it a template on how the prompt should be handled when we start querying some information from it
  - we specified two things - `an instruction_string and a new prompt`
  - using gemini API key - `pip install llama-index google-generativeai` , `pip install llama-index-llms-gemini`
  - https://aistudio.google.com/apikey

### Outputs

- `population_query_engine.query("What is the population of Canada?")` gives us below output

```
    python main.py
> Pandas Instructions:
```

df[df['Country'] == 'Canada']['Population2023'].values[0]

```
> Pandas Output: 38781291
```

- `population_query_engine.query("What is the population of India?")`

```
abhis@Tinku MINGW64 ~/Desktop/AIAgents/PythonAIAgent (main)
$ python main.py
> Pandas Instructions:
```

df[df['Country'] == 'India']['Population2023'].values[0]

```
> Pandas Output: 1428627663
(ai)
```

### Next

- Upto now we're quering directly using the source(population.csv) but what's really going to happen is our `agent` is going to be use this tool , where it will get that output & then it will pass that output with anything else that it needs & then give us a more `human readable response`

# Building Agent Capabilities

Now we have both tools - pandasQueryENgine using prompts and Note_engine to save notes in a file

- now we specify a pipeline here of different tools that the agent has access to & then it will choose which one it needs to use

### agent in Action with the tools provided

```
abhis@Tinku MINGW64 ~/Desktop/AIAgents/PythonAIAgent (main)
$ python main.py
WARNING:llama_index.core.agent.react.formatter:ReActChatFormatter.from_context is deprecated, please use `from_defaults` instead.
ReActChatFormatter.from_context is deprecated, please use `from_defaults` instead.
Enter a prompt (or 'exit' to quit): can u save a note for me saying "I love Rebel Star Prabhas"
> Running step 83d21bfe-674c-4a58-a577-ac0729ff57a1. Step input: can u save a note for me saying "I love Rebel Star Prabhas"
Thought: The current language of the user is: english. I need to use a tool to help me answer the question.
Action: note_saver
Action Input: {'note': AttributedDict([('title', 'Note'), ('type', 'string')])}
Observation: Error saving note: unsupported operand type(s) for +: 'AttributedDict' and 'str'
> Running step 3ae74ad2-8edc-4565-9f4c-f7966c21d0d9. Step input: None
Thought: The current language of the user is: english. I need to use a tool to help me answer the question.
Action: note_saver
Action Input: {'note': AttributedDict([('title', 'Note'), ('type', 'string')])}
Observation: Error saving note: unsupported operand type(s) for +: 'AttributedDict' and 'str'
> Running step 7af1090d-9965-4965-8270-7af1929b1599. Step input: None
Thought: The current language of the user is: english. I need to use a tool to help me answer the question.
Action: note_saver
Action Input: {'note': 'I love Rebel Star Prabhas'}
Observation: Note saved successfully!
> Running step 98abb136-2582-4849-bf2e-3ebc858e4aee. Step input: None
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: Ok, I've saved the note.
Ok, I've saved the note.
Enter a prompt (or 'exit' to quit): what is the population of vatican city
> Running step 4fb53027-0243-48a1-9128-c6f8abac6811. Step input: what is the population of vatican city
Thought: The current language of the user is: english. I need to use a tool to help me answer the question.
Action: population_data
Action Input: {'input': 'vatican city'}
> Pandas Instructions:
```

df.query("Country == 'Vatican City'")

```
> Pandas Output: Empty DataFrame
Columns: [Rank, Country, Population2023, YearlyChange, NetChange, Density(P/Km²), Land Area(Km²), Migrants(net), Fert.Rate, MedianAge, UrbanPop%, WorldShare]
Index: []
Observation: Empty DataFrame
Columns: [Rank, Country, Population2023, YearlyChange, NetChange, Density(P/Km²), Land Area(Km²), Migrants(net), Fert.Rate, MedianAge, UrbanPop%, WorldShare]
Index: []
> Running step 368d9606-27df-46fe-bc4b-2fff9b2f20cc. Step input: None
Thought: I cannot answer the question with the provided tools.
Answer: I apologize, but I cannot answer your question about the population of Vatican City. The tool I used did not have any information about Vatican City.
I apologize, but I cannot answer your question about the population of Vatican City. The tool I used did not have any information about Vatican City.
Enter a prompt (or 'exit' to quit): what is the population of india
> Running step f340dd41-d07f-4a40-9933-dd353292a478. Step input: what is the population of india
Thought: The current language of the user is: english. I need to use a tool to help me answer the question.
Action: population_data
Action Input: {'input': 'india'}
> Pandas Instructions:
```

df[df['Country'] == 'India']

```
> Pandas Output:     Rank Country  Population2023 YearlyChange  ...  Fert.Rate  MedianAge  UrbanPop%  WorldShare
95     1   India      1428627663       0.81 %  ...        2.0       28.0       36 %     17.76 %

[1 rows x 12 columns]
Observation:     Rank Country  Population2023 YearlyChange  ...  Fert.Rate  MedianAge  UrbanPop%  WorldShare
95     1   India      1428627663       0.81 %  ...        2.0       28.0       36 %     17.76 %

[1 rows x 12 columns]
> Running step 9b926576-19ff-4b63-a1ea-f1edfc1ad6ed. Step input: None
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: The population of India is 1428627663.
The population of India is 1428627663.
Enter a prompt (or 'exit' to quit): exit
```

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
