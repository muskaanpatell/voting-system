# first we will take input of what nominee what we want to keep
nominee1 = input("enter the name of first nominee: ")
nominee2 = input("enter the name of second nominee: ")
# initially vote count for both must be 0
nm1_votes = 0
nm2_votes = 0
voter_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_of_voter = len(voter_id)
while True:
    if voter_id == []:  # to cjheck when voter list is complete
        print("voting session is over!!!")
    if nm1_votes > nm1_votes:
        percent = (nm1_votes/no_of_voter)*100
        print(nominee1, "has won the election with", percent, "% of votes!!!")
        break
    elif nm2_votes > nm1_votes:
        percent = (nm2_votes/no_of_voter)*100
        print(nominee2, "has won the election with", percent, "% of votes!!!")
        break
    else:
        print("Both have equal number of votes!! The government will decide who will rule.")
        break
voter = int(input("Enter your voter id: "))
if voter in voter_id:
    print("You are a voter")
    # we will remove recent voter so that there is no possibility of same voter's vote
    voter_id.remove(voter)
print("-------------------------")
print("To give vote", nominee1, "press 1")
print("To give vote", nominee2, "press 2")
print("-------------------------")
vote = int(input("Enter your previous Vote: "))
if vote == 1:
    nm1_votes += 1
    print(nominee1, "Thank you to give your important vote to them !!!")
elif vote == 2:
    nm2_votes += 1
    print(nominee2, "Thank you to give your important vote to them !!!")
elif vote > 2:
    print("check your pressed key!!!")
else:
    print("You are not a voter OR you have already voted..")
