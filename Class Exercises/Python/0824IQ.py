# A movie review app tracks how well a movie is liked on emoji submissions
# from users. Given a list, keep track of how of the movies likeability is
# going using the emojis provided. A thumbs up emoji is +1, starry face +2, thumbs
# down -1, vomit -2 points. Write a function that returns both the percentage
# of people that liked the movie in general as well as the overall +/- point total.

from collections import Counter

givenList = ["\U0001F44D", "\N{thumbs up sign}",  "\N{Face with Open Mouth Vomiting}", "\U0001F44D", 
"\U0001f929", "\N{thumbs down sign}", "\U0001F44E", "\U0001F92E", "\U0001f929", 
"\N{thumbs down sign}", "\N{thumbs up sign}", "\U0001F44D", "\U0001F44D", 
"\N{Face with Open Mouth Vomiting}", "\N{thumbs down sign}", "\U0001F44D", 
"\U0001f929", "\U0001F44D", "\N{thumbs down sign}", "\N{thumbs down sign}"]

thumbsup1 = givenList.count('\U0001F44D')
thumbsup2 = givenList.count('\N{thumbs up sign}')
thumbsdown1 = givenList.count('\U0001F44E')
vomitface1 = givenList.count('\U0001F92E')
vomitface2 = givenList.count('\N{Face with Open Mouth Vomiting}')
starryface = givenList.count('\U0001f929')
print('# of Thumbs up 1 : ' + str(thumbsup1))
print('# of Thumbs up 2: ' + str(thumbsup2))
print('# of Thumbs down 1: ' + str(thumbsdown1))
print('# of Vomit Face 1: ' + str(vomitface1))
print('# of Vomit Face 2: ' + str(vomitface2))
print('# of Starry Face ' + str(starryface))

# def movieLikeability:

totalLikes = thumbsup1 + thumbsup2 + starryface
print(totalLikes)
totalDislikes = thumbsdown1 + vomitface1 + vomitface2
print(totalDislikes)
print(len(givenList))
likesPercent = (totalLikes/len(givenList)) * 100
roundedPercent = round(likesPercent)


print('The percentage of movie-goers who enjoyed the movie is ' + str(roundedPercent) + "%")
print('Total Likes Points: ' + str(totalLikes))
print('Total Dislikes Points: ' + str(thumbsdown1 - ((vomitface1 + vomitface2) * 2)))









