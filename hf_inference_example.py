import os
from huggingface_hub import InferenceClient

# You need a token from https://hf.co/settings/tokens, ensure that you select 'read' as the token type. 
# If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". 
# Make sure to call it "HF_TOKEN"
HF_TOKEN = os.environ.get("HF_TOKEN")

# Initialize the client
client = InferenceClient(model="meta-llama/Llama-4-Scout-17B-16E-Instruct")

# Test the connection
try:
    if HF_TOKEN:
        print("✅ HF_TOKEN found in environment variables")
        # Set the token for the client
        client.token = HF_TOKEN
    else:
        print("⚠️  HF_TOKEN not found in environment variables")
        print("   You can set it with: export HF_TOKEN='your_token_here'")
        print("   Or get a token from: https://hf.co/settings/tokens")
    
    print(f"✅ InferenceClient initialized with model: meta-llama/Llama-4-Scout-17B-16E-Instruct")
    
    # Test a simple prompt
    if HF_TOKEN:
        print("\n🧪 Testing inference...")
        response = client.text_generation(
            "Hello! Can you tell me a short joke?",
            max_new_tokens=100,
            temperature=0.7
        )
        print(f"Response: {response}")
    else:
        print("\n⚠️  Skipping inference test - no token available")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure you have a valid HF_TOKEN and the model is accessible")
