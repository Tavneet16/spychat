print 'Let\'s get Started....'
spy_name = raw_input('What is your name ? ')

if len(spy_name) > 0 :
    spy_salutation = raw_input("What should we call you ? ")
    spy_name = spy_salutation + ' ' + spy_name
    print 'Welcome ' + spy_name + ' Glad to see you...'


else:
    print 'please enter a valid name.'
spy_age = raw_input('what is your age ? ')


if spy_age > 12 and spy_age < 50 :
    spy_rating = raw_input('what is your spy rating ? ')
else:
    print"sorry you are not eligible to be a spy"