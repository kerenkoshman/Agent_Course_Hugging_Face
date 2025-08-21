# Agent Course - Hugging Face

This repository contains materials and examples for an AI agents course using Hugging Face tools and local LLMs.

## Setup

### Prerequisites

1. **Python 3.10+** (we're using Python 3.11)
2. **Ollama** installed and running
3. **smolagents** with litellm support

### Installation

1. Install Python 3.11 (if not already installed):
   ```bash
   brew install python@3.11
   ```

2. Install smolagents with litellm support:
   ```bash
   pip3.11 install 'smolagents[litellm]'
   ```

3. Install and run Ollama:
   ```bash
   # Pull the model
   ollama pull qwen2:7b
   
   # Start the server (if not already running)
   ollama serve
   ```

## Examples

### Working Smolagents + Ollama Integration

See `smolagents_ollama_example.py` for a complete working example that demonstrates:

- ✅ Correct way to use smolagents with Ollama
- ✅ Single-turn conversations
- ✅ Multi-turn conversations
- ❌ Common mistakes to avoid

### Quick Start

```python
from smolagents import LiteLLMModel

# Initialize the model
model = LiteLLMModel(
    model_id="ollama/qwen2:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

# Use the client directly (recommended)
response = model.client.completion(
    model="ollama/qwen2:7b",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=100
)
print(response.choices[0].message.content)
```

## Course Structure

This repository will be organized into lessons covering:

1. **Basic Setup** - Getting started with local LLMs and smolagents
2. **Agent Fundamentals** - Understanding agent architecture
3. **Tool Integration** - Adding external tools to agents
4. **Advanced Patterns** - Complex agent workflows
5. **Deployment** - Taking agents to production

## Status

- ✅ Environment setup complete
- ✅ Ollama integration working
- ✅ smolagents configured
- 🔄 Course content in development

## Requirements

- Python 3.11+
- Ollama with qwen2:7b model
- smolagents[litellm]
- 8GB+ RAM recommended for local model inference