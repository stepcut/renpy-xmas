screen musicScreen():
    default listenTo = 0
    vbox:
       for i,day in enumerate(days):
          hbox:
           textbutton day['title'] action [SetScreenVariable('listenTo', i), Play ('music', day['song'])]
           showif (listenTo == i):
             textbutton "upvote" action [SetDict(persistent.votes,i, persistent.votes[i]+1)]
           text (" - " + str(persistent.votes[i]))

