# import libraries
import google.generativeai as genai
import yaml
import json

# --- Configuration ---
api_key = None
CONFIG_PATH = r"config.yaml"

# Load the API key from the config file
with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['GOOGLE_API_KEY']

# Configure the Gemini API with your key
genai.configure(api_key=api_key)


def ats_extractor(resume_data: str) -> dict:
    """
    Extracts structured information from resume text using the Gemini API.

    Args:
        resume_data: A string containing the text from a resume.

    Returns:
        A dictionary with the extracted information.
    """
    
    # --- Prompt Definition ---
    # The prompt now includes the resume data directly.
    prompt = f'''
    You are an expert AI system designed for parsing resumes.
    Please extract the following details from the resume text provided below and return the output strictly in JSON format.

    1. full_name
    2. email_id
    3. github_portfolio_url
    4. linkedin_url
    5. employment_details
    6. technical_skills
    7. soft_skills
    
    --- RESUME TEXT ---
    {resume_data}
    '''

    # --- Model and Generation Configuration ---
    
    # Initialize the Generative Model
    model = genai.GenerativeModel('gemini-1.5-flash') # or 'gemini-pro'

    # Set generation config to ensure JSON output
    # This is a key advantage of the Gemini API for this task.
    generation_config = {
        "temperature": 0.0,
        "response_mime_type": "application/json",
    }
    
    # --- API Call ---
    
    # Generate content using the model
    response = model.generate_content(
        prompt,
        generation_config=generation_config
    )
      
    # --- Response Handling ---
    
    # The API, when used with response_mime_type="application/json",
    # returns a JSON string in response.text. We parse it into a Python dict.
    try:
        extracted_data = json.loads(response.text)
        return extracted_data
    except (json.JSONDecodeError, IndexError) as e:
        print(f"Error decoding JSON from model response: {e}")
        print(f"Raw Response: {response.text}")
        return {"error": "Failed to parse JSON response from the model."}

# --- Example Usage (Optional) ---
# if __name__ == '__main__':
#     # Create a dummy resume string to test the function
#     sample_resume = """
#     John Doe
#     john.doe@email.com | linkedin.com/in/johndoe | github.com/johndoe
    
#     Experience:
#     - Software Engineer at Tech Corp (2022 - Present)
#       Developed web applications using Python and React.
    
#     Skills:
#     - Technical: Python, JavaScript, React, SQL, Docker
#     - Soft Skills: Communication, Teamwork, Problem-solving
#     """
    
#     # Call the function and print the result
#     extracted_info = ats_extractor(sample_resume)
#     print(json.dumps(extracted_info, indent=2))