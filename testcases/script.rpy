init:
    # Set up the size of the screen.
    $ config.screen_width = 800
    $ config.screen_height = 600

    # Positions of things on the screen.
    $ left = Position(xpos=0.0, xanchor='left')
    $ right = Position(xpos=1.0, xanchor='right')
    $ center = Position()

    # Backgrounds.
    image whitehouse = Image("whitehouse.jpg")

    # Character pictures.
    image eileen happy = Image("9a_happy.png")
    image eileen vhappy = Image("9a_vhappy.png")
    image eileen concerned = Image("9a_concerned.png")

    # Character objects.
    $ e = Character('Eileen', color=(200, 255, 200, 255))


label start:
    
    scene whitehouse
    show eileen happy

    e "Welcome to the Ren'Py testcases."

    # say

    "Single-argument say. (Expect no label)"

    e "Two-argument say with object. (Expect label 'Eileen:')"

    "Neighbor" "Two-argument say with string. (Expect label 'Neighbor:')"

    ("Other" + " " + "Neighbor") "Complicated two-argument say."


    # menu

    e "This is the menu torture test. You shouldn't be allowed to leave
       until you've picked each choice once. Each choice can only be picked
       once, and the beach can't be picked before shopping."

    $ menu_set = [ ]
    $ have_swimsuits = False

    menu torture_test:
        set menu_set
        
        "Where should we go today?"

        "The movies.":
            "We went to the movies."
            jump torture_test

        "Shopping at the mall.":
            "We went shopping, and the girls bought themselves swimsuits."
            $ have_swimsuits = True
            jump torture_test

        "Swimming at the beach." if have_swimsuits:
            "We went swimming, and I got to see the girls in their new
             swimsuits."

            jump torture_test


    # call, jump, if, $, python, python hide

    "Now testing control structures and python."

    $ n = 0

    call test_sub

    python:
        n += 1

    jump after_sub

    $ n += 1

label test_sub:

    $ n += 1

    return

label after_sub:

    python hide:
        n += 1

    # Unconventional, to test else clause.
    if n != 2:
        $ raise Exception("Control problems")
    else:
        pass


    # While, if clause, elif clause.
    
    $ n = 0

    while n < 3:
        $ n += 1

    if n > 3:
        $ raise Exception("Control problems.")
    elif n == 3:
        pass
    else:
        $ raise Exception("Control problems.")


    e "Done with control tests."

    hide whitehouse

    e "Testing hide. I should be on a black background."

    show whitehouse

    e "Testing show. I should be hidden behind the white house."

    show eileen vhappy at left

    e "Testing show/replace. I should still be hidden."

    hide eileen
    show eileen vhappy at right
    
    e "Testing hide/show. I should now be on the right side of the screen."

    show eileen happy at center


    init:
        python:
            class MyClass(object):
                def __init__(self, val):
                    self.val = val

                def __repr__(self):
                    return "<myclass " + self.val + ">"

    python:
        a = 0
        b = [ 0 ]
        c = { 'foo': 0 }
        d = MyClass(0)
        
    e "Start of rollback test. Don't rollback past here."

    python:
        a += 1
        b[0] += 1
        b.append(1)

        c['foo'] += 1
        c['bar'] = 1

        d.val = 1

    e "No matter how many times you rollback to the previous line, the
       following values shouldn't change, and should all be 1.
       \n%(a)r %(b)r %(c)r %(d)r"

    e "That's all for now. Later."

    
