#this is basically a version of KBC, questions will be based on Programming


#questions below are stored in list format so that we can loop through them later. 
questions = [
    ["Which of the following is NOT a web browser?", "Chrome", "Firefox", "Edge", "Adobe Photoshop", 4],
    ["Which programming language is commonly used for developing Android apps?", "Python", "Kotlin", "Ruby", "PHP", 2],
    ["What is the name of Apple's operating system for mobile devices?", 'Windows Mobile', 'iOS', 'Android', 'Tizen', 2],
    ["What type of malware is designed to replicate itself and spread to other computers?", "Worm", "Trojan", "Spyware", 'Ransomware', 1],
    ["What does GPU stand for in computing?", "General Processing Unit", "Graphics Processing Unit", "General Power Unit", "Graphics Power Unit", 2],
    ["What is the name of the first computer virus?", "Melissa", "Brain", "ILOVEYOU", "Code Red", 2],
    ["Who is considered the father of the World Wide Web?", "Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Larry Page", 3],
    ["Which cloud computing service is provided by Microsoft?", "AWS", "Azure", "Google Cloud", "Oracle Cloud", 2],
    ["In the context of databases, what does SQL stand for?", "Simple Query Language", 'Structured Query Language', "Strong Query Language", "Standard Query Language", 2],
    ["Which programming language is used primarily for AI and machine learning?", "PHP", 'Swift', 'Python', 'COBOL', 3],
    ["Which of the following companies developed the famous programming language C?", "IBM", "Microsoft", "AT&T Bell Labs", "Google", 3],
    ["What does the acronym IoT stand for in technology?", "Internet of Technology", "Interconnected Online Things", "Internet of Things", "Interface of Technologies", 3],
    ["Which technology is used to record transactions in Bitcoin and other cryptocurrencies?", 'AI', 'Blockchain', 'Cloud Computing', 'Virtual Reality', 2],
    ["Which of the following is the main framework used for developing cross-platform mobile applications using JavaScript?", "Django", "Flutter", "React Native", 'Laravel', 3],
    ["Which one of the following is a distributed version control system?", 'Subversion', "Mercurial", "Git", "CVS", 3]
]


question_number = 1 
option_indexing = ['a)' , 'b)', 'c)' , 'd)'] 
option_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4}                 

prize_stages = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
prize_money = 0

for question in questions:                                  
    print(f"{question_number}. {question[0]}")              
    for i, option in enumerate(question[1:5]):                           
        print(f"{option_indexing[i]} {option}")

    question_number += 1                         #adds 1 to question number to ensure that the indexing is up to date


    while True:
        user_input = input('Answer (q for quit): ').lower()
        if user_input == 'q':
             print('Goodbye.')
             prize_money = prize_stages[question_number - 1]
             break
        elif user_input not in option_mapping.keys():
              print("Valid inputs are either a,b,c or d. Please try again. ")
        else:
              break
        
    if user_input == 'q':
         break
    if option_mapping[user_input] == question[-1]:
        print('Right answer!')
        prize_money = prize_stages[question_number - 2]
    else:
        print("This was not a correct answer. ")
        if question_number > 9:
             prize_money = prize_stages[9]
        elif question_number > 4:
             prize_money = prize_stages[4]
        else:
             prize_money = 0
        break

print(f"Your take home money is {prize_money}")            

