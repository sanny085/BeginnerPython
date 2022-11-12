high_risk_policy = [
    {
        'name': 'SBI Lite',
        'company': 'SBI',
        'm_premium': 3800,
        'isReqMedical': True,
    },
    {
        'name': 'LIC Life',
        'company': 'LIC',
        'm_premium': 3200,
        'isReqMedical': True,
    },
    {
        'name': 'Pnb MetLife',
        'company': 'Punjab National Bank',
        'm_premium': 2800,
        'isReqMedical': True,
    }
]
low_risk_policy = [
    {
        'name': 'HDFC Premium',
        'company': 'HDFC',
        'm_premium': 2500,
        'isReqMedical': True,
    },
    {
        'name': 'ICICI Lite',
        'company': 'ICICI',
        'm_premium': 2100,
        'isReqMedical': True,
    },
    {
        'name': 'Kotak Bank Seva',
        'company': 'Kotak Bank',
        'm_premium': 1900,
        'isReqMedical': True,
    }
]


# Get list of policy -> Return Policy Name in tuple
def fetchPolicy(available_policy):
    currentPolicy = []
    for x in available_policy:
        currentPolicy.append(x['name'])
    return tuple(currentPolicy)


# Get policy name and available list -> Return Current Policy Details
def currentPlanDetails(user_policy, available_policy):
    for policy in available_policy:
        if policy['name'] == user_policy:
            print('%s complete details is : %s' % (user_policy, policy))
