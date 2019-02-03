#purpose of the program is to ask for votes, tally them and calculate wjp wins

class Error(Exception):
    pass
class NotRange(Error):
    pass

def question():
    print()
    print("the presidential nominees are:")
    print ("1. Mickey Mouse")
    print ("2. Donald Duck")
    print( "3. Minnie Mouse")
    print ("4. Goofy")
    print ("Type 0 to quit")

#everything starts off at 0, add to corresponding vote getter
Mic=0
Don=0
Min=0
goof=0
tot_votes=0
question()

while True:
   
    try:
        vote_inp=int(input("Please input corresponding number to nominee to vote: "))
        if vote_inp==1:
            Mic+=1
            tot_votes+=1

        elif vote_inp==2:
            Don+=1
            tot_votes+=1

        elif vote_inp==3:
            Min+=1
            tot_votes+=1

        elif vote_inp==4:
            goof=1
            tot_votes+=1

        elif vote_inp==0:
            print (tot_votes)
            break

        else:
            raise NotRange
            

    except NotRange:
        print("This value is not available!")
    except ValueError:
        print("this is not a value")


if Mic>Don and Mic>Min and Mic>goof:
    print (("Mic is the winner with {:0.2f} percent of the vote!").format(Mic/tot_votes *100))

elif Don> Min and Don>goof:
    print (("Don is the winner with {:0.2f} percent of the vote!").format(don/tot_votes *100))

elif  Min> goof:
    print (("Min is the winner with {:0.2f} percent of the vote!").format(Min/tot_votes *100))

else:
    print (("goof is the winner with {:0.2f} percent of the vote!").format(goof/tot_votes *100))
