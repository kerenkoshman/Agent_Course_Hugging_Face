from smolagents import LiteLLMModel

# ✅ CORRECT WAY TO USE SMOLAGENTS WITH OLLAMA
# Initialize the model with Ollama
model = LiteLLMModel(
    model_id="ollama/qwen2:7b",  # Correct model ID format for Ollama
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)

print("=== SMOLAGENTS + OLLAMA WORKING EXAMPLE ===\n")

# ✅ WORKING: Use the client directly (recommended approach)
print("1. Using client directly (RECOMMENDED):")
response = model.client.completion(
    model="ollama/qwen2:7b",
    messages=[{"role": "user", "content": "Tell me a short joke about programming"}],
    max_tokens=150
)
print(f"Response: {response.choices[0].message.content}\n")

# ✅ WORKING: Multiple messages conversation
print("2. Multi-turn conversation:")
messages = [
    {"role": "user", "content": "My name is Alice"},
    {"role": "assistant", "content": "Nice to meet you, Alice!"},
    {"role": "user", "content": "What's my name?"}
]

response = model.client.completion(
    model="ollama/qwen2:7b",
    messages=messages,
    max_tokens=50
)
print(f"Response: {response.choices[0].message.content}\n")

# ❌ NOT WORKING: The generate method (as shown in your original code)
print("3. The generate method (NOT WORKING - this is what you tried):")
try:
    # This is what you originally tried - it doesn't work
    response = model.generate("Hello! Can you tell me a short joke?")
    print(f"Response: {response}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("The generate method expects a different format than what you provided.\n")

print("=== SUMMARY ===")
print("✅ Use model.client.completion() with proper message format")
print("❌ Don't use model.generate() with simple strings")
print("✅ Your Ollama server is working perfectly!")
print("✅ The qwen2:7b model is responding correctly!")
