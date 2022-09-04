name = str(input('Enter your Name '))
age = int(input('Enter your Age '))


def valid_user_for_policy(name, age, mobile):
    print('Namaste,', name, 'You are eligible to buy policy')
    if age > 45:
        high_risk_policy = ['SBI Lite', 'Pnb MetLife']
        print('Please choose any policy', high_risk_policy[0], high_risk_policy[0])
    else:
        print('Purchase HDFC plan')


if age > 18:
    mobile = str(input('Enter your Mobile'))
    valid_user_for_policy(name, age, mobile)
else:
    print('Sorry, You are not eligible to buy any Policy, Thank You !')