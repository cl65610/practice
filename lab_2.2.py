def areasquare(l):
    areasquare = float(l)**2
    print 'The area of the square is %.2f units squared.' % areasquare
    return



def arearec(l,h):
    arearec = l*h
    print 'The area of the rectangle is %.2f units squared.' % arearec
    return

def areacuboid(l,h,d):
    areacuboid = 2*(l*h+l*d+h*d)
    print 'The area of the cuboid is %.2f units squared.' % areacuboid
    return



choices = ['s', 'r', 'c', 'q']
choice = str(raw_input("""
Press 's' to find the area of a square.
Press 'r' to find the area of a rectangle.
Press 'c' to find the area of a cuboid.
If you're not interested in that, press 'q' to quit.
"""))

def choose_shape(choice):
    if choice not in choices:
        print 'That\'s not a valid choice.'
        try_again = raw_input('Would you like to try again? y or n? ')
        if try_again == 'y':
            choice = str(raw_input("""
Press 's' to find the area of a square.
Press 'r' to find the area of a rectangle.
Press 'c' to find the area of a cuboid.
If you're not interested in that, press 'q' to quit."""))
            choose_shape(choice)
        else:
            return
    elif choice == 's':
        l = float(raw_input('How long is the bottom of the shape? '))
        areasquare(l)
        return
    elif choice == 'r':
        l = float(raw_input('How long is the bottom of the shape? '))
        h = float(raw_input('How tall is the shape? '))
        arearec(l,h)
        return
    elif choice == 'c':
        l = float(raw_input('How long is the bottom of the shape? '))
        h = float(raw_input('How tall is the shape? '))
        d = float(raw_input('How deep is the shape? '))
        areacuboid(l,h,d)
        return
    elif choice == 'q':
        print 'You want to quit? Fine, get out of here.'
        return
    else:
        return
choose_shape(choice)
print 'Thank you for your interest in shapes.'
