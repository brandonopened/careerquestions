import openai 

openai.api_key = "<YOUR API KEY HERE>"

user_input = input("What does your resume look like? ")
career_q = "What skills do you see in the following experience statement; write the skills as a numbered list"

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": career_q + user_input },
    ],
    temperature=.5,
)

p1 = print(response['choices'][0]['message']['content'])
print(p1)

user_input2 = input("Which skills would you like to explore further as a career track? List the skills by title:  ")
career_q2 = "Based on the following selected skills, pick 3 careers that would be a perfect match for those skills. Show median salary, career progression and basic description of the career"

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": career_q2 + user_input2 },
    ],
    temperature=.5,
)

print(response['choices'][0]['message']['content'])
