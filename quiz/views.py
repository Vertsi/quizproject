from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1, 
		"name": "Epic places",	
		"description": "The 12 most epic places to visit in Barcelona"
	},
	{
		"quiz_number": 2, 
		"name": "Famous persons",	
		"description": "The 10 most famous persons in Barcelona"
	},
	{
		"quiz_number": 3, 
		"name": "Hidden gems",	
		"description": "The 11 hidden gems you need to know in Barcelona"
	},
]

def startpage (request):
	context = {
		"quizzes": quizzes, 
	}
	return render(request, "start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number": quiz_number, 
	}
	return render(request, "quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
		"question": "Barcelona is the third largest tourist destination in Europ after Paris and London - but how many tourists visit the city every year?",
		"answer1": "20 million",
		"answer2": "15 million",
		"answer3": "8 million",
		"quiz_number": quiz_number,
	}
	return render(request, "question.html", context)

def completed(request, quiz_number):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_number": quiz_number,
		"quizzes": quizzes, 
	}
	return render(request, "results.html", context)