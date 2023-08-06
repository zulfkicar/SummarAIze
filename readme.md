IMPORTANT: LINK TO THE OVERLEAF REPO
https://www.overleaf.com/read/rhddbxzzdvrj


######################Text Summarization Project######################################

This project aims to develop an AI-based text summarization system using various techniques and models. It allows users to automatically generate summaries of input text for efficient information retrieval and comprehension.

#############Deployment Instructions###########

To deploy the project, follow these steps:

1. Install the required dependencies. Make sure you have Python 3.7 or higher installed.
	pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run Home.py

(Ensure that the terminal is open in your root folder.

4. Access the application in your web browser at `http://localhost:8501`.

5. Use the user interface to input text and generate summaries. Choose the desired summarization technique and adjust any parameters if applicable.

############Project Structure##############

The project structure is organized as follows:

- `Home.py`: The main entry point of the Streamlit application.
- `Abstractive_Summarization_(Base_Models).py`: Contains the implementation of the abstractive text summarization using base models of BART and T5
- 'Abstractive_Summarization_(Fine-Tuned_Models).py':  Contains the implementation of the abstractive text summarization using fine-tuned models of T5 and LED fine-tuned on the BookSum dataset
- 'Extractive_Summarization_(BERT).py': Contains the implementation of the extractive text summarization using BERT

- `requirements.txt`: Lists the required dependencies for the project.

##############Additional Notes###################

- The project utilizes pretrained models for text summarization. Make sure to have a stable internet connection for downloading the models if necessary.
- The summarization techniques available include both extractive and abstractive approaches, allowing users to choose the desired method based on their requirements.
- Feel free to explore and modify the code to further enhance the project or adapt it to your specific needs.



Feel free to customize this README file based on your specific project requirements and add any additional information or sections as needed.
