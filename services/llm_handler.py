import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_llm(user_query, csv_data):
    """
    Uses OpenAI GPT to analyze CSV data and return an intelligent response.
    """
    try:
        # Convert CSV data into a structured text format
        formatted_csv = "\n".join([", ".join(map(str, row.values())) for row in csv_data])

        # Construct the prompt
        prompt = f"You are a CSV data assistant. Here is the data:\n\n{formatted_csv}\n\nUser Query: {user_query}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You analyze CSV data and answer queries."},
                {"role": "user", "content": prompt}
            ]
        )

        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"Error querying LLM: {str(e)}"
