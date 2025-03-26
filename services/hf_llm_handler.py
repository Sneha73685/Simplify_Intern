from transformers import pipeline

# Load an LLM pipeline for question-answering (QA)
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-large")

def query_hf_llm(user_query, csv_data):
    """
    Uses a Hugging Face model to analyze CSV data and return an intelligent response.
    """
    try:
        # Convert CSV data to text format
        formatted_csv = "\n".join([", ".join(map(str, row.values())) for row in csv_data])

        # Construct the input text
        input_text = f"Given the following CSV data:\n\n{formatted_csv}\n\nAnswer the question: {user_query}"

        response = qa_pipeline(input_text, max_length=200)
        
        return response[0]["generated_text"]
    
    except Exception as e:
        return f"Error querying Hugging Face model: {str(e)}"
