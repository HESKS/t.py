from twitter import *
import time

print("Twitter Frindship checker")

consumer_key= "y6uUKdqy6gmcCNbDFas3x5mnB"
consumer_secret= "crQwjhDPFWiu94Rgmi7BCwmbzPlnS0wlW1kEfs8ZOX6sidFA9U"
access_key= "296957600-omM1TEe0HtJenx7gL73oK7dUHqcxWq2XKgET1TTT"
access_secert= "cS5lCfG5FDLaWRXUCroO57CxrN37AbpcLXtnWPQu5YhVK"

twitter = Twitter(auth = 0Auth(access_key,
                               access_secert,
                               consumer_key,
                               consumer_secret))

source = "_H_E_S"
target = "alsalt77"

result = twitter.friendships.show(source_screen_name = source, target_screen_name = target)

following = result["relationship"]["target"]["following"]
follows = result["relationship"]["target"]["followed+by"]

print (str(source)+ "follows" + str(target) + " : " +str(follows))
print(target + "follows" + str(source) + " : " + str(following))
