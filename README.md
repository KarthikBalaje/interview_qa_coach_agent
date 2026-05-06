# Interview Q&A Coach Agent

Use Case: 

A user provides a job role (e.g., "Data Analyst at a fintech startup"). 
The agent generates likely interview questions and then provides model answers.

Tool 1 — generate_interview_questions

	• Input: job role and optionally a skill or domain to focus on
	• Task: Generate 8–10 realistic interview questions covering technical skills, behavioural situations, and role-specific scenarios
	• Output: A numbered list of interview questions grouped by type
  
Tool 2 — generate_model_answers

	• Input: the list of questions from Tool 1 and the job role
	• Task: Write concise, impressive model answers for each question using the STAR format (Situation, Task, Action, Result) where applicable
	• Output: Each question followed by its model answer
  
System Prompt: 

The agent acts as a career coach who prepares candidates to ace job interviews with confidence.

