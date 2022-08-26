# A movie review app tracks how well a movie is liked on emoji submissions
# from users. Given a list, keep track of how of the movies likeability is
# going using the emojis provided. A thumbs up emoji is +1, starry face +2, thumbs
# down -1, vomit -2 points. Write a function that returns both the percentage
# of people that liked the movie in general as well as the overall +/- point total.

from collections import Counter

def movieLikeability(givenList):
    totalLikes = (givenList.count('\U0001F44D')) + (givenList.count('\U0001f929'))
    # totalDislikes =(givenList.count('\U0001F44E')) + (givenList.count('\U0001F92E'))
    likesPercent = (totalLikes/len(givenList)) * 100
    roundedPercent = round(likesPercent)
    print('The percentage of movie-goers who enjoyed the movie is ' + str(roundedPercent) + "%")
    print('Total Likes Points: ' + str(givenList.count('\U0001F44D') + (givenList.count('\U0001f929') * 2)))
    print('Total Dislikes Points: ' + str((givenList.count('\U0001F44E') + (givenList.count('\U0001F92E') * 2)) * -1))

givenList = ["\U0001F44D", "\N{thumbs up sign}",  "\N{Face with Open Mouth Vomiting}", "\U0001F44D", "\U0001f929", "\N{thumbs down sign}", "\U0001F44E", "\U0001F92E", "\U0001f929", "\N{thumbs down sign}", "\N{thumbs up sign}", "\U0001F44D", "\U0001F44D", "\N{Face with Open Mouth Vomiting}", "\N{thumbs down sign}", "\U0001F44D", "\U0001f929", "\U0001F44D", "\N{thumbs down sign}", "\N{thumbs down sign}"]
movieLikeability(givenList)








