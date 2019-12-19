
threshold = 100

input = {
    "US": 140,
    "CA": 120,
    "MX": 80,
    "GB": 70,
    "DE": 110
    }

def balance(input):
    """
    returns list of (src, dest, amount)
    """

    instructions = []
    for account_to_update, account_update_balance in input.iteritems():
        if account_update_balance >= threshold:
            continue
        
        print input
        money_needed = threshold - account_update_balance
        for account_to_pull_from, account_to_pull_from_balance in input.iteritems():
            total = account_update_balance
            if account_to_pull_from == account_to_update:
                continue
            
            # can we take from this account
            if account_to_pull_from_balance > threshold:
                # if we have more money than we need take it all
                # we need
                money_available = (account_to_pull_from_balance - threshold)
                value_transfered = 0
                if money_needed <= money_available:
                    value_transfered = money_needed
                else:
                    value_transfered = money_available

                input[account_to_pull_from] = input[account_to_pull_from] - money_available
                input[account_to_update] += money_available
                money_needed = money_needed - money_available
                instructions.append((account_to_pull_from, account_to_update, value_transfered))

            if money_needed == 0:
                break
            
    return instructions



def test(input, instructions):
    pass


print balance(input)
