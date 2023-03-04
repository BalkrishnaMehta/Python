from fpdf import FPDF
import aspose.words as aw
import openai
# import openai_secret_manager

# assert "openai" in openai_secret_manager.get_services()
# secrets = openai_secret_manager.get_secret("openai")

# openai.api_key = "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"

# # Read the text file
# with open('questions.txt', 'r', encoding="utf8") as file:
#     text = file.read()

# # Separate the text into questions
# questions = text.split("Q")

# # Initialize an array to store the responses
# responses = []

# # Loop through each question and send it to ChatGPT
# for question in questions:
#     # Remove any leading or trailing white space
#     question = question.strip()

#     # Skip any empty questions
#     if not question:
#         continue

#     # Generate a response from ChatGPT
#     completion = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=question,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     # print(question)
#     # print(completion.choices[0].text)
#     # Store the response in the array
#     responses.append(completion.choices[0].text)

# # Write the text file
# with open('answers.txt', 'w') as file:

#     # Print the responses
#     for i, response in enumerate(responses):
#         # print(f"Question {i + 1}: {questions[i]}")
#         # print(f"Answer {i + 1}: {response}")
#         file.write("%s %s %s %s\n" % ("Question", str(i+1) ,": ", str(questions[i+1])))
#         file.write("%s %s %s %s\n" % ("Answer", str(i+1) ,": ", str(response)))
#         # file.write("Question",(i+1),": ",questions[i])
#         # file.write("Answer",(i+1),": ",response)
#         file.write("-" * 70)
#         file.write("\n")
    

# load TXT document
doc = aw.Document("answers.txt")

# save TXT as PDF file
doc.save("answer.pdf", aw.SaveFormat.PDF)

# # save FPDF() class into
# # a variable pdf
# pdf = FPDF()  
  
# # Add a page
# pdf.add_page()
  
# # set style and size of font
# # that you want in the pdf
# pdf.set_font("Arial", size = 15)
 
# # open the text file in read mode
# f = open("answers.txt", "r", encoding="latin-1")
 
# # insert the texts in pdf
# i = 1
# for x in f:
#     pdf.cell(5, 5, txt = x,ln = i, align = 'L')
#     i = i + 1
  
# # save the pdf with name .pdf
# pdf.output("answers.pdf")  

# prompt = input("Enter new prompt: ")
# completion = openai.Completion.create(
#     engine="text-davinci-003",
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )
# response = completion.choices[0].text
# print(response)

