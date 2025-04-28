import os
import openai
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def upload_dataset():
    """Upload the dataset file to OpenAI"""
    try:
        # Upload the dataset file
        file = client.files.create(
            file=open("dataset.jsonl", "rb"),
            purpose="fine-tune"
        )
        print(f"Dataset uploaded successfully. File ID: {file.id}")
        return file.id
    except Exception as e:
        print(f"Error uploading dataset: {e}")
        return None

def start_fine_tuning(file_id):
    """Start the fine-tuning job"""
    try:
        # Start fine-tuning job
        # Using gpt-3.5-turbo as base model for better cost-effectiveness and faster training
        # 2 epochs chosen to balance between learning and overfitting
        fine_tune = client.fine_tuning.jobs.create(
            training_file=file_id,
            model="gpt-3.5-turbo",  # Using base model that supports fine-tuning
            hyperparameters={
                "n_epochs": 2,
                "batch_size": 1,
                "learning_rate_multiplier": 0.1
            }
        )
        print(f"Fine-tuning job started successfully. Job ID: {fine_tune.id}")
        return fine_tune.id
    except Exception as e:
        print(f"Error starting fine-tuning: {e}")
        return None

def main():
    # Upload dataset
    file_id = upload_dataset()
    if not file_id:
        return
    
    # Start fine-tuning
    job_id = start_fine_tuning(file_id)
    if not job_id:
        return
    
    print("\nFine-tuning process started!")
    print("You can check the status of your fine-tuning job using the job ID above.")
    print("The process may take some time to complete.")

if __name__ == "__main__":
    main() 