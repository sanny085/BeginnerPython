import policyModule as Store
from policyModule import high_risk_policy
from policyModule import low_risk_policy
from policyModule import fetchPolicy

print("All Store Dir: ", dir(Store))
# Getting user information
name = str(input('Enter your Name : '))
age = int(input('Enter your Age : '))


def valid_user_for_policy(name, age, mobile):
    print('Namaste,', name, 'You are eligible to buy policy')
    if age > 45:
        # For high_risk_policy plan details (Getting from modules)
        print('High Risk Policy : ', fetchPolicy(high_risk_policy))
        user_policy = input('Choose your policy : ')
        if user_policy in fetchPolicy(high_risk_policy):
            Store.currentPlanDetails(user_policy, high_risk_policy)
        else:
            print('Invalid plan! Please Enter valid plan')
            return
    else:
        # For high_risk_policy + low_risk_policy plan details (Getting from modules)
        allPolicy = []
        for policy_type in [high_risk_policy, low_risk_policy]:
            allPolicy.extend(policy_type)
        print('Low risk available policy 3 : ', fetchPolicy(allPolicy))

        user_policy = input('Choose your policy : ')
        if user_policy in fetchPolicy(allPolicy):
            Store.currentPlanDetails(user_policy, allPolicy)
        else:
            print('Invalid plan! Please Enter valid plan')
            return


if age > 18:
    mobile = str(input('Enter your Mobile : '))
    valid_user_for_policy(name, age, mobile)
else:
    print('Sorry, You are not eligible to buy any Policy, Thank You !')
