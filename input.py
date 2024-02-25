

class makeQuestions:
    def __init__(self, questions: dict) -> None:
        self.questions:None = questions
        print("Could you please answer the following questions, please?")
        print(self.questionsList())
        
    def questionsList(self)-> list:
        setCounter:int = len(self.questions)
        counter:int = 0
        answers:list =[]
        while counter < setCounter:    
            try:
                answer:None = self.questions[counter]["type"](input(self.questions[counter]["question"]))
            except ValueError:
                print("Please make sure to respond to the question correctly")
            else:
                answers.append(answer) 
                counter = counter + 1 
        return answers

questions:dict = {
            "questions":[{
                "question":"What is your name? ",
                "type":str
            },
            {
                "question":"What is your last name? ",
                "type":str
            },
            {
                "question":"How old are you? ",
                "type":int
            }]
        }
    
startQuestions:None = makeQuestions(questions["questions"])