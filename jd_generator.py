from pydantic_extractor import retrieve_data
from tot_prompt import get_contract_prompt
import streamlit as st
from openai import AzureOpenAI


# gpt-4 turbo 128k
client = AzureOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_version= "2023-12-01-preview",
    api_key="6e9d4795bb89425286669b5952afe2fe",
    # base_url="https://danielingitaraj-gpt4turbo.openai.azure.com/"
    base_url="https://danielingitaraj-gpt4turbo.openai.azure.com/openai/deployments/GPT4Turbo/chat/completions?api-version=2023-12-01-preview"
)

# # gpt 35 turbo 16k
# client = AzureOpenAI(
#     api_version= "2023-12-01-preview",
#     api_key="c09f91126e51468d88f57cb83a63ee36",
#     base_url="https://chat-gpt-a1.openai.azure.com/openai/deployments/DanielChatGPT16k/chat/completions?api-version=2023-12-01-preview"
# )


def get_completion(messages=None,
                temperature=0.7, max_tokens=3000, top_p=0.95, frequency_penalty=0,
                presence_penalty=0, stop=None):
    # Set default values if parameters are not provided
    messages = messages or []

    # Make API call with provided parameters
    response = client.chat.completions.create(
        messages= messages,
        model="GPT4Turbo",
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop
    )
    return response.choices[0].message.content


def main():
    st.title('JOB Description Generator')
    
    # Create an empty list to store form data
    form_data = []

    with st.form(key ='jd_form'):
        job_title = st.text_input("JOB TITLE", value= "Senior Litigation Docket Specialist")
        date = st.text_input("DATE", value= "September 2022")
        department = st.text_input("DEPARTMENT", value= "Paralegals")
        flsa = st.text_input("FLSA CLASSIFICATION", value= "Non-exempt")
        report_to = st.text_input("REPORTS TO", value="Litigation Docketing Manager")
        eeo = st.text_input("EEO CLASSIFICATION", value="Administration")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            with st.spinner("Generating Job Description Document..."):

                prompt = get_contract_prompt(job_title, date, department, flsa, report_to, eeo, *retrieve_data(job_title))
                
                generated_jd = get_completion(messages=prompt)

                st.write(generated_jd)

                # with open('data.txt', 'a') as file:  # 'a' mode opens the file for appending
                #     file.write("\n".join(form_data[0]))


                # # Display form data list
                # st.write(form_data)

if __name__=='__main__':
    main()



















# title = "Applications Analyst"
# date = "September 2022"
# department = "Technology Services"
# flsa = "Exempt"
# report_to = "Enterprise Applications & Engineering Manager"
# eeo = "Professional"

# prompt = get_contract_prompt(title, date, department, flsa, report_to, eeo, *retrieve_data(title))


# # Open the file in write mode
# with open("prompt.txt", 'w', encoding='utf-8') as file:
#     file.write(prompt)
