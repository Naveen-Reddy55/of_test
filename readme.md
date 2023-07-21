

# Procedure

![flowchart](https://github.com/Naveen-Reddy55/of_test/assets/71924097/ab6a9209-37b9-45c8-8c0d-65cd56ae02b3)



# Model Performance
![example](https://github.com/Naveen-Reddy55/of_test/assets/71924097/8d87b613-f34a-436c-a19f-6fff85337594)


# AI Junior Developer (Intern) Test 
Welcome! and thank you for applying! 

## Requirement
The current project has the blueprint structure of an AI App. 

Your mission is to implement an 💬NLP chatbot **answering questions about science**. 

You will add your logic to the `main.py` file inside the `execute` function. 
```python
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:        
        response = '' # <<< --Your magic goes here
        output.append(response)

    return SimpleText(dict(text=output))
```
## Constraints and restrictions
You are free to use any package or library you see feet as long as you follow these rules:
* 👎 You can't call any external service (e.g. chatGPT) 
* 👎 You can't copy and paste from other peoples work 

## Run
The application can be executed in two different ways:
* locally by running the `start.sh` 
* on in a docker container using `Dockerfile` 

## Submission
Your solution must be uploaded on GitHub, and submit us the link in **max 1 week** after receiving the task.

## Note
Keep in mind that this is the project that will be used to evaluate your skills.
So we do expect you to make sure that the app is fully functional and doesn't have any obvious missing pieces.
