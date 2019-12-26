# The script of the game goes in this file.

define days = [ { 'title': 'Day 1',
                  'song' : '/music/devilmuzik!!s.mp3'
                },
                { 'title': 'Day 2',
                  'song' : '/music/devilmuzik!!s.mp3'
                },
                { 'title': 'Day 3',
                  'song' : '/music/devilmuzik!!s.mp3'
                },
                { 'title': 'Day 4',
                  'song' : '/music/devilmuzik!!s.mp3'
                },
                { 'title': 'Day Five',
                  'song' : '/music/devilmuzik!!s.mp3'
                }
              ]

init python:
  if persistent.votes is None:
     persistent.votes = [ 0 for i in range(14) ]

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    call screen musicScreen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
