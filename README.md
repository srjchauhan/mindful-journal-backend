# Mindful Journal Backend Service 

This backend service empowers you to create a personalized wellness journaling experience using the power of FastAPI and Large Language Models (LLMs).

# Key Features:
### 1. User Management:
    
Streamlined user signup and signin processes for secure access.

### 2. Journal Entry Prompts:

Leverage the insights of LLMs to generate insightful and personalized journal prompts based on user responses to targeted questions. This fosters deeper self-reflection and exploration of emotions.

### 3. Journal Entry Storage

Safely store and retrieve journal entries, allowing users to revisit past experiences and track their progress over time.

# Getting Started:

### 1. Run in Development
    
#### Pre-requisites : Install python in system
```shell
python -m venv venv
source activate venv/bin/activate
pip install -r requirements.txt
```

### 2. Run in Docker

```shell
docker build -t mindfull-backend-service:latest .
docker run -d --name mindfull-backend -p 8000:8000 mindfull-backend-service:latest
```

