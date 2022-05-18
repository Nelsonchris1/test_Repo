import pandas as pd
import snscrape.modules.twitter as sntwitter
import datetime

"""
Python script to scrape twitter data of 3 tech supply chain management company

"""

# Define queries to search for, an empyt list and a limit of accumulated tweets to scrape

query = ["Lori Systems logistics", "kobo360", "sendy logistics"]
tweets = []
limit = 5500

# Create a forloop to iterate of each query and scrape twitter for data relating to each query
for qr in query:

    #Iterate over the each query and scrape data then append to the tweets list created 
    for tweet in sntwitter.TwitterSearchScraper(qr).get_items():

        if len(tweets) == limit:
            break
        else:
            tweets.append(
                [tweet.date, tweet.user.username, tweet.content]
            )
    #Include a print statement to indicate the end of each query scrapped
    print(f"Finished {qr} by {datetime.datetime.now()}")

#Convert tweets listto a dataframe
df = pd.DataFrame(tweets, columns=['Date', 'username', 'content'])

# Clean the content columns by removing link url(https://) as smiley characters
df["content"] = df["content"].str.replace(r'https?://[^\s<>"]+|www\.[^\s<>"]+', "")
replace = ['â€“',  'â€“Â', 'ðŸššðŸš', 
            '&amp;Â', 'ðŸ‘¨ðŸ¾â€ðŸ’»', 
            'ðŸ’ªðŸ¾ðŸ’ªðŸ¾', 'ðŸ‘ŠðŸ¾ðŸ‘ŠðŸ¾', 
            'ðŸ”¥ðŸ”¥ðŸ”¥' , 'ðŸ¤©ðŸ¤©ðŸššðŸšš']

for rep in replace:
    df['content'] = df['content'].str.replace(rep, "")

# Save tweets 
df.to_csv('tweets.csv', index=False)



"""
1. Snscrape cant performlive operation . Somehow its has to have a listner, 
    which after checking the github repo, there was nothing on stream or listner. 
    NOTE! it has no documentation also
2. Theres not customer online presence on any of the tech supply chain company queries,
    Most of the tweet were about news of these companies either raising funds from investors
    or patternering with other companies
3. Still thinking of a scenerio where building a live tweet scrapper will be useful because for example,
    The last time lori systems had a mention on twitter was Dec 2021
""" 