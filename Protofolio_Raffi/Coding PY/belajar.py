
db_user = {"Prompt": []}



db = {"Menyapa": ["halo","apakabar"],"subjek" : ["bro","kawan","bang","jarvis"]}

poin = 0

user = input("You: ").lower().split()

jawaban = []

for k in range(len(user)):
    if user[k] in db["subjek"][0]:
        user.remove("bro")
    elif user[k] in db["subjek"][1]:
        user.remove("kawan")
    elif user[k] in db["subjek"][2]:
        user.remove("bang")
    elif user[k] in db["subjek"][3]:
        user.remove("jarvis")

db_user["Prompt"] = user

db_answer = {db["Menyapa"][0]: "Halo Saya senang bertemu",db["Menyapa"][1]: "Saya Baik Baik saja"}

for i in range(len(user)):
    jawaban.append(db_answer[db_user["Prompt"][i]])

j = ",".join(jawaban)

print(f"Jarvis: {j}")

