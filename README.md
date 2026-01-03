# AI_Devops_Deployment
AI-Driven DevOps for Smarter Deployments:-

Problem Statement:-
Automate the code review process using GenAI to analyze code changes, approve or reject them based on quality and automatically trigger deployments to Google Cloud Run when the code is approved.

Workflow:- 

GitHub repository monitoring:- when we push the code , a query is sent to a Generative AI model (Gemini) to review the code.
Code analysis using GenAI:- The LLM analyzes the code files from the repository and gives a status of “APPROVE” or “REJECT.”
Conditional pipeline trigger:- Based on the GenAI’s response, if the status is “APPROVE,” GitHub Actions deploy the code to Google Cloud Run.


Step 1: Sending Requests to GenAI
Step 2: Creating the Cloud Function for Code Analysis
Step 3: GitHub Actions Workflow
Step 4: Dockerizing the Application
