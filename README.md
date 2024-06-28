## ApplyMate:  Your AI companion for job applications          
This project focuses on developing a conversational AI chatbot designed to enhance the job application process by effectively answering common candidate queries and guiding users through the various stages of applying for a job. Leveraging Natural Language Processing (NLP), the chatbot can understand and respond to user inputs with accuracy and relevance. The aim is to streamline the job application process for candidates, making it more efficient and user-friendly through the use of advanced conversational AI technologies.

The chatbot is designed to collect and store applicant details in a structured manner. The collected information includes the applicant's full name, mobile number, email address, and a link to their resumes. This information is stored in a CSV file, making it easy to manage and review applicant data.

## Features
1. **Candidate Query Handling:** 
    The chatbot can respond to frequently asked questions from candidates, such as inquiries about job openings, application status, and company information.


2. **Guided Application Process:** 
    The chatbot assists candidates through the job application process, providing step-by-step guidance and collecting necessary information like full name, mobile number, email, and resume.


3. **Natural Language Processing:** 
    Utilizing NLP, the chatbot can interpret user inputs and provide appropriate responses, ensuring a seamless and intuitive interaction experience.

4. **Custom Actions:** 
    Includes tailored responses and actions such as greeting users, providing job descriptions, and offering company information.

5. **Applicant Details Storage**:
   The chatbot collects applicant details (full name, mobile number, email, and resume link or PDF) and stores them in a CSV file for easy access and management.

## Technologies Used
1. **Rasa:** For building and deploying the conversational AI.

2. **Streamlit:** To create a user-friendly frontend interface.

3. **Python:** For implementing custom actions and handling backend logic.

4. **Requests:** For managing HTTP requests between the frontend and the Rasa server.

## Folder Structure

<img src="https://github.com/farvath/ApplyMate-Your-AI-companion-for-job-applications-/blob/main/images/folder.jpg"  alt="alt text">
 
1. **actions/actions.py** : This directory contains your custom action code. Custom actions are Python functions that execute specific tasks, such as querying a database or performing calculations.

2. **data/nlu.yml** : Contains the training data for the Natural Language Understanding (NLU) component. This file includes example user inputs (utterances) and their corresponding intents.
3. **stories.yml**  : Contains example conversation paths (stories) that show how the bot should respond to user inputs in a multi-turn dialogue. This helps train the dialogue management model.
4. **models/**      : This directory stores the trained models. After you run `rasa train`, the trained models are saved here.
5. **config.yml**   : This file contains the configuration for your NLU pipeline and core policies. It defines how user inputs are processed and how the bot decides on responses.
6. **credentials.yml** : This file contains the credentials for various messaging platforms and channels, such as Slack, Facebook Messenger, and custom channels.
7. **domain.yml** : This file defines the domain of your assistant, including intents, entities, slots, responses, actions, and forms.
8. **endpoints.yml** : This file defines the endpoints for your action server and model server.





## implementations

1. First clone the repository :
    ```bash
        git clone https://github.com/farvath/ApplyMate-Your-AI-companion-for-job-applications-.git
    ```

2. Install Rasa:
     ```bash
        pip install rasa
    ```

3. Run the Rasa Server:
     ```bash
        rasa run actions --port 5056
    ```

4.  Test the Chatbot : open another terminal and run 
    ```bash
      rasa shell --port 5006 --endpoints endpoints.ymL
    ```

5. Train the Model (if needed):
    ```bash
        rasa train
    ```

## Ouptut
<img src="https://github.com/farvath/ApplyMate-Your-AI-companion-for-job-applications-/blob/main/images/interface.jpg"  alt="alt text">
<img src="https://github.com/farvath/ApplyMate-Your-AI-companion-for-job-applications-/blob/main/images/interface1.jpg"  alt="alt text">
