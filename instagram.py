#filter through each list value, and return as many redundancies as possible
def filter1(lines):
    temp = []
    for line in lines:
        if not(line=="Verified\n" or (" " in line) or (line.lower() in temp)):
            temp.append(line)
    return temp

#read in from following list and add to lin
with open("following.txt") as file:
    following = file.readlines()

with open("followers.txt") as file2:
    followers = file2.readlines()


#filter out unnecessary strings for readability
following,followers = filter1(following),filter1(followers)

#iterate through following, if that string is not in followers list - they unfollowed you, and it prints
for i in following:
    if not(i in followers):
        print(i)