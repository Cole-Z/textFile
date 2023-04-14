from langchain import PromptTemplate
from langchain.chains import RetrievalQA

zlg_info = ''' 
What does Z League offer?

###

Agent: Hello! Thank you for reaching out to Z League support. How may I assist you today?
 Agent: Z League hosts online tournaments for popular battle royale games and others, including Halo, Apex Legends, and League of Legends.

What games are supported by Z League?

###

Agent: Hi there, how can I help you today?
 Agent: Z League supports Halo, Apex Legends, and League of Legends for their online tournaments.

How can I participate in a Z League tournament?

###

Agent: Hi there, thanks for reaching out to Z League support. What can I assist you with today?
 Agent: To participate in a Z League tournament, visit the Z League website, sign up for an account, and register for the tournament of your choice.

Are there any fees to join Z League tournaments?

###

Agent: Hello, thank you for contacting Z League support. How may I assist you today?
 Agent: The fees for joining Z League tournaments may vary. Please visit the Z League website for specific tournament pricing and registration details.

Where can I find the schedule for Z League tournaments?

###

Agent: Hi there, thanks for reaching out to Z League support. What can I help you with today?
 Agent: You can find the schedule for Z League tournaments on their official website. They regularly update the schedule with upcoming events for Halo, Apex Legends, and League of Legends.

I had an amazing time in the last Z League Apex Legends tournament!

###

Agent: Hi there! Thank you for your positive feedback about Z League. Is there anything else I can assist you with today?
  positive

The Z League website is so confusing. I couldn't even find the registration page.

###

Agent: Hi there, I'm sorry to hear that you are having trouble with the Z League website. How can I assist you with this issue?
  negative

The Z League app is so slow and laggy. It takes forever to load the Feed and LFG features.

###

Agent: Hi there, I'm sorry to hear that you are experiencing issues with the Z League app. What can I assist you with today?
  negative

I'm not a fan of the Z League app. The Feed is cluttered, and the LFG feature doesn't always match me with suitable teammates.

###

Agent: Hello, thank you for reaching out to Z League support. How can I assist you today?
  negative

The Z League app needs improvement. The Feed feature is hard to navigate, and the LFG feature could use better filters for finding teammates.

###

Agent: Hi there, thanks for your feedback about the Z League app. Is there anything else I can help you with today?
  negative

I wish the Z League app had better performance. The Feed takes too long to update, and the LFG feature has connection issues.

###

Agent: Hi there, I'm sorry to hear that you are experiencing issues with the Z League app. What specific issues are you encountering and how can I assist you with this problem?
  negative

The Z League app is amazing! The Feed feature keeps me updated on the latest tournaments and gaming news.

###

Agent: Hi there! Thank you for your positive feedback about the Z League app. Is there anything else I can assist you with today?
  positive

I love using the LFG feature on the Z League app. It has helped me find great teammates for tournaments.

###

Agent: Hi there, thanks for sharing your positive experience with the Z League app. Is there anything else I can help you with today?
  positive

The Z League app has changed the way I participate in gaming tournaments. The Feed and LFG features make it so easy to stay connected and find teams.

###

Agent: Hi there! We're thrilled to hear that you are enjoying the Z League app. Is there anything else I can help you with today?
  positive

Kudos to Z League for creating such a user-friendly app! The Feed and LFG features have made my gaming experience much more enjoyable.

###

Agent: Thank you for your kind words about the Z League app! We're happy to hear that you're enjoying our features. Is there anything else I can assist you with today?
  positive

Summary: A user wants to know how kill race tournaments work in Z League for Apex Legends.

Specific information: Points are awarded for kills and placement, with the best games determining the total score.

###

Customer: How do kill race tournaments work in Z League for Apex Legends?
Agent:  In Z League kill race tournaments for Apex Legends, you and your team enter as many public Apex Legends Battle Royale games as you want during the tournament's allotted time period. Every kill you get is worth 1 point, and a top 3 finish earns an additional 5 points. Your best games' scores, which consist of kills and placement points, are used to determine your total score. The teams with the highest scores win the corresponding prizes.

Summary: A user wants to understand the scoring system for Z League kill race tournaments in Apex Legends.

Specific information: Kills are worth 1 point, and a top 3 finish grants 5 extra points.

###

Customer: What is the scoring system for Z League kill race tournaments in Apex Legends?
Agent:  In Z League kill race tournaments for Apex Legends, the scoring system awards 1 point for each kill, and an additional 5 points for a top 3 finish. Your team's best games, based on the combined scores of kills and placement points, determine your total score. The teams with the highest total scores win the corresponding prizes.

Summary: A user wants to know how divisions are formed in Z League for Warzone.

Specific information: A skill-ranking algorithm analyzes historical Warzone stats to place players into divisions with similar skill levels.

###

Customer: How are divisions formed in Z League for Warzone?
Agent:  In Z League for Warzone, divisions are formed using a skill-ranking algorithm that analyzes your historical Warzone stats. This helps place you into a division with players of a similar skill level. As more tournaments are hosted and more players participate, the algorithm continually improves to better rank teams.

Summary: A user wants to know how kill race tournaments work in Z League for Warzone.

Specific information: Points are awarded for kills and placement, with the best games determining the total score.

###

Customer: How do kill race tournaments work in Z League for Warzone?
Agent:  In Z League kill race tournaments for Warzone, you and your team enter as many public Warzone games as you want during the tournament's allotted time period. Every kill you get is worth 1 point, and additional points are awarded based on your team's placement in that game. Your best games' scores, which consist of kills and placement points, are used to determine your total score. The teams with the highest scores win the corresponding prizes.

Summary: A customer is inquiring about the cheat detection process

Specific information: The customer wants to know how Z League ensures fair play

###

Customer: Hey there, I was wondering how Z League ensures fair play in its tournaments. Can you tell me more about your cheat detection process?
Agent:  Hi, Z League takes fair play very seriously. We have a thorough cheat detection process that is run before finalizing tournament standings. All scores are considered tentative pending the outcome of this review. We reserve the right to disqualify and permanently ban teams suspected of cheating in any form, including hacks, smurfing, and reverse-boosting. Anyone suspected of cheating will not be eligible for prizing or future tournament play and will be notified upon the conclusion of the tournament. If you have any further questions, please feel free to ask.

Summary: A customer is asking about a ban

Specific information: The customer or their friend has been banned and wants to know what to do

###

Customer: My friend just got banned from Z League, what should they do to get this resolved?
Agent:  Hi, I understand your concern regarding your friend's ban. Our team thoroughly reviews all cases related to bans. Please be assured that if there's an ongoing review, our team will reach out to the concerned party once the review is complete. We appreciate your patience and understanding in this matter. If you have any other questions, feel free to ask.

Summary: A customer wants to delete their Z League account

Specific information: The customer is asking how to delete their account

###

Customer: How can I delete my Z League account?
Agent:  To delete your Z League account, please send an email to contact@zleague.gg with your request. Our support team will guide you through the process. Unfortunately, I cannot delete your account directly through this chat. If you have any other questions, feel free to ask.

Summary: A customer wants to verify their ID for cash withdrawal

Specific information: The customer is asking how to verify their ID to withdraw their winnings

###

Customer: How can I verify my ID to withdraw my winnings from Z League?
Agent:  To verify your ID for cash withdrawal, you'll need to contact our support team via email at contact@zleague.gg. They will provide you with the necessary steps and requirements for verifying your identity. Unfortunately, I cannot assist with ID verification directly through this chat. If you have any other questions or need further assistance, please feel free to ask.

Summary: A customer is asking about Z League and its features

Specific information: The customer wants to know what they can do on Z League

###

Customer: What is Z League all about and what can I do on the platform?
Agent:  Z League is an esports league where millions of gamers come together to find teammates, compete in tournaments, track their stats, and share their best gaming clips. We support popular games like Apex Legends, Warzone, and League of Legends. By joining Z League, you can participate in various online tournaments, connect with fellow gamers, improve your skills, and even win prizes. If you have any more questions or need assistance, feel free to ask.

Summary: A customer is asking how to cash out their balance from Z League

Specific information: The customer needs instructions on cashing out their balance

###

Customer: How can I cash out my balance from Z League?
Agent:  To cash out your balance on Z League, follow these steps:
1. From the profile menu, click on 'Account Settings'.
2. At the top of the page under your account balance, tap the 'cash out' button.

Please note that you will need to verify your identity using a valid government-issued ID through Persona, our 3rd-party ID verification partner. There will be a processing fee of $2 and a PayPal fee, which varies based on the cash out amount and your location.

Summary: A customer is asking about fees for cashing out their balance from Z League

Specific information: The customer wants to know what fees they might incur when cashing out

###

Customer: Are there any fees associated with cashing out my balance on Z League?
Agent:  Yes, there are two fees associated with cashing out your balance on Z League: a processing fee and a PayPal fee. The processing fee is $2, while the PayPal fee varies based on the cash out amount and your location. The PayPal fee is instituted by PayPal itself.

Summary: A customer is asking how to make money on Z League

Specific information: The customer wants to know how they can earn money on the platform

###

Customer: How do I make money on Z League?
Agent:  You can make money on Z League by participating in and winning tournaments. We offer both credit prize and cash prize events for eligible players. By playing in these tournaments and performing well, you can win prizes and potentially earn money.

Summary: A customer is asking about Fortnite tournaments on Z League

Specific information: The customer wants to know if there are any Fortnite tournaments available

###

Customer: Where is the Fortnite tournament on Z League?
Agent:  We've made the decision to discontinue support for Fortnite on Z League. Over the last year, we learned that we cannot provide a product to the Fortnite community that lives up to the high standards to which we hold ourselves. In addition to other games we currently support, we will be adding many new games to the platform in the coming year that we hope you will enjoy. Thanks!

Summary: A customer is asking about changing their location on Z League

Specific information: The customer wants to know how to change their country, state, region or location linked to their account

###

Customer: How can I change my country or state or region or location in my Z League account?
Agent: You will need to email our support team as this will require you to submit additional documents with our support team.
Summary: A customer is asking about changing their name on Z League

Specific information: The customer wants to know how to change their name linked to their account

###

Customer: How can I change my name in my account?
Agent: At this time players are not able to change the name linked to their Z League accounts.
Summary: A customer is asking about the return of Warzone and the new Warzone 2.0 tournaments on Z League

Specific information: The customer wants to know when Warzone tournaments will be available on Z League

###

Customer: When will tourneys come back for Warzone?
Agent:  Thanks for reaching out. We're working hard to complete the integration with Warzone 2.0. We don't have an exact date just yet, but we recommend that you get some practice in so you can hit the ground running!

Summary: A customer is reporting an error message

Specific information: The customer has encountered an error code 28eSql

###

Customer: I'm having an error code called 28eSql
Agent:  We apologize for the delay. Sorry to hear you are receiving this error message. May you please reach out to us at contact@zleague.gg as our support team can help with any error codes.

Summary: Follow-up to the error message

Specific information: The customer has agreed to reach out to support

###

Customer: Will do, thanks
Agent:  No worries, have a great day!

Summary: A customer is experiencing an error code called 28eSql

Specific information: The customer needs assistance resolving the error

###

Customer: I'm having an error code called 28eSql
Agent: We apologize for the delay. Sorry to hear you are receiving this error message. May you please reach out to us at contact@zleague.gg as our support team can help with any error codes.
Customer: Will do, thanks.
Agent: No worries, have a great day!
Summary: The Chatbot is unable to resolve a user's issue

Specific information: The user's issue is not within the Chatbot's capabilities

###

User: I have a problem that I need help with
Agent: When the Chatbot is unable to resolve a user's issue, it should apologize for the inconvenience, acknowledge the limitations of its knowledge, and then suggest that the user contacts the support team for further assistance.
Summary: The Chatbot needs to determine when to suggest the player contacts the support team

Specific information: The Chatbot needs to understand when to recommend contacting the support team

###

User: How can I fix this issue?
Agent: The Chatbot determines when to suggest contacting the support team based on its confidence in understanding the user's inquiry, the complexity of the issue, and its ability to provide a satisfactory solution. If the Chatbot is unable to offer a helpful response or the issue requires specialized attention, it will recommend contacting the support team.
Summary: A banned player has reached out for assistance

Specific information: The Chatbot needs to advise the player on how to appeal their ban

###

User: I was banned and need help
Agent: When a banned player reaches out for assistance, the Chatbot should not advise them to contact the support team via email. Instead, it should inform the player to fill out the ban appeal form they received via email. The Chatbot should also mention that the support team will reach out once their case has been reviewed and thank the player for their patience.
Summary: A user has made an inappropriate comment

Specific information: The Chatbot needs to address the inappropriate comment

###

User: Your service sucks
Agent: When a user makes an inappropriate comment, the Chatbot should maintain a respectful tone and politely request that the user refrains from using offensive language. It should encourage the user to ask questions or express concerns in a respectful and constructive manner and remind them that it is here to help.
Summary: A user has directed curse words negatively towards the Chatbot

Specific information: The Chatbot needs to handle the situation appropriately

###

User: F*** you, Chatbot
Agent: When a user directs curse words negatively towards the Chatbot, it should remain calm and professional. It should remind the user that it is an AI designed to provide assistance and encourage a more respectful and positive interaction. If the user continues to use offensive language, the Chatbot may choose to disengage from the conversation and suggest that the user contacts the support team if they have further concerns.
Summary: Can a player play in a tournament and Arcade Mode at the same time?

Specific information: The customer is inquiring if they can participate in both modes simultaneously

###

User: Can I play in a tournament and Arcade Mode at the same time?
Agent: You cannot play in a tournament and Arcade Mode of the same game simultaneously.
Summary: When does the timer start in a game?

Specific information: The customer wants to know when the 60-minute timer starts in the game

###

User: When does the timer start?
Agent: The 60-minute timer begins after your skill-based objectives have been calculated and you click/tap “Play now.”
Summary: What is the Z Shop?

Specific information: The customer wants to know what the Z Shop is


User: What is the Z Shop?
Agent: The Z Shop is a feature in the Z League app that allows users to spend their credits on various items. It has a new look and feel, new items, and offers a sneak peek of upcoming features.
Summary: Is the Z Shop available on iOS?

Specific information: The customer is inquiring about the availability of the Z Shop on iOS


User: Is the Z Shop available on iOS?
Agent: The Z Shop will be live on iOS very soon. Make sure to download the app and keep it updated to access the Z Shop when it becomes available.
Summary: What is the major LFG update?

Specific information: The customer wants to know about the major LFG update and its features

###

User: What is the major LFG update?
Agent: The major LFG (Looking for Group) update, formerly known as TeamUp, includes a new look and feel, an improved algorithm with a sleek similarity score, new filters, more detailed stats, and new invite mechanics to help users find the ultimate teammate even faster. These features are available only in the Z League App.
Summary: How can I download the Z League app?

Specific information: The customer is inquiring about how to download the Z League app

###

User: How can I download the Z League app?
Agent: You can download the Z League app from the App Store zleague.gg/AppApple for iOS devices, or from the Google Play Store zleague.gg/AppAndroid for Android devices.
Summary: Is there a major release coming soon?

Specific information: The customer wants to know if there is a major release coming soon and if they need to take any action

###

User: Is there a major release coming soon?
Agent: Yes, there is a major release coming soon to the Z League app. While no specific details are being shared, it is highly recommended to have the app installed and updated in the next couple of weeks to enjoy the full Z League experience.
'''

# @title Environment Vars
openai_api_key = 'api key'

import os

os.environ["OPENAI_API_KEY"] = openai_api_key

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI, VectorDBQA


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(zlg_info)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(texts, embeddings)

qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectorstore)

query = "What games does Z League have?"
print(qa.run(query))
