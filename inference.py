import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_model_response(prompt, model_name, temperature=0.7):
    """Get response from the fine-tuned model"""
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error getting model response: {e}")
        return None

def main():
    # Using base model until fine-tuning is complete
    model_name = "gpt-3.5-turbo"
    
    # Test prompts
    test_prompts = [
        "User: Yaar, aaj office se early leave mil gaya!\nAssistant:",
        "User: Weekend pe Goa jaana hai, koi tips do\nAssistant:",
        "User: New job offer mila hai, confused hoon\nAssistant:"
    ]
    
    print("Testing model on new prompts:\n")
    
    for prompt in test_prompts:
        print(f"Prompt: {prompt}")
        response = get_model_response(prompt, model_name)
        if response:
            print(f"Response: {response}\n")
        else:
            print("Failed to get response\n")

if __name__ == "__main__":
    main()