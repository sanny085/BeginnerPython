name = str(input('Enter your Name : '))
age = int(input('Enter your Age : '))

def policyPlanDetails(user_policy):
    hr_policy_details = [{
        'name': 'SBI Lite',
        'company': 'LIC',
        'premium': 3000,
        'isReqMedical': True,
       },
       {
            'name': 'Pnb MetLife',
            'company': 'Punjab National Bank',
            'premium': 2800,
            'isReqMedical': True,
        }
    ]
    for i in range(len(hr_policy_details)):
        if hr_policy_details[i]['name'] == user_policy:
            print(hr_policy_details[i])



def valid_user_for_policy(name, age, mobile):
    print('Namaste,', name, 'You are eligible to buy policy')
    if age > 45:
        high_risk_policy = ['SBI Lite', 'Pnb MetLife']
        print('Your are eligible for these policy :')
        for x in high_risk_policy:
            print(x)
        user_policy = input('Choose your policy :')

        # For plan details
        if user_policy in high_risk_policy:
            policyPlanDetails(user_policy)
        else:
            print('Invalid plan! Please Enter valid plan')
            return
    else:
        print('Purchase HDFC plan')


if age > 18:
    mobile = str(input('Enter your Mobile : '))
    valid_user_for_policy(name, age, mobile)
else:
    print('Sorry, You are not eligible to buy any Policy, Thank You !')