def can_abhimanyu_cross_chakravyuha(p, a, b, powers):
    current_power = p
    skip_left = a
    recharge_left = b
    defeated = False
    
    for i in range(11):
        if skip_left > 0 and current_power < powers[i]:
            skip_left -= 1
            continue
        
        current_power -= powers[i]
        
        if current_power <= 0:
            if recharge_left > 0:
                current_power = p
                recharge_left -= 1
            else:
                defeated = True
                break
        
        if i == 3 or i == 7:
            regen_power = powers[i-1] // 2
            current_power -= regen_power
            
            if current_power <= 0:
                if recharge_left > 0:
                    current_power = p
                    recharge_left -= 1
                else:
                    defeated = True
                    break
    
    return not defeated

# Test Cases
test_cases = [
    # case 1
    {
        "p": 60,
        "a": 3,
        "b": 2,
        "powers": [10, 15, 25, 10, 15, 30, 20, 25, 25, 10, 5]
    },
    #  case 2
    {
        "p": 40,
        "a": 1,
        "b": 1,
        "powers": [5, 10, 20, 10, 5, 25, 10, 15, 10, 5, 5]
    }
]

for i, test in enumerate(test_cases):
    result = can_abhimanyu_cross_chakravyuha(test["p"], test["a"], test["b"], test["powers"])
    print(f"For Test Case {i+1}: {'Can Cross the chakravyuha' if result else 'Cannot Cross the chakravyuha'}")
