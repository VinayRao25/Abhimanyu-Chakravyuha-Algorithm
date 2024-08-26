# Abhimanyu_Chakravyuha

## Problem Statement
Imagine Abhimanyu in Chakravyuha. There are 11 circles in the Chakravyuha surrounded by different enemies. Abhimanyu is located in the innermost circle and has to cross all the 11 circles to reach Pandavas army back.
Given:
- Each circle is guarded by different enemy where enemy is equipped with k1, k2……k11 powers.
- Abhmanyu start from the innermost circle with p power, Abhimanyu has a boon to skip fighting enemy a times.
- Abhmanyu can recharge himself with power b times.
- Battling in each circle will result in loss of the same power from Abhimanyu as the enemy. If
- Abhmanyu enter the circle with energy less than the respective enemy, he will lose the battle.
- k3 and k7 enemies are endured with power to regenerate themselves once with half of their initial power and can attack Abhimanyu from behind if he is battling in iteratively next circle.

# Write an algorithm to find if Abhimanyu can cross the Chakravyuha and test it with two sets of test cases. 

### Conditions:
1. Abhimanyu loses power equal to the enemy's power if he chooses to fight.
2. If Abhimanyu's power is less than the enemy's power when entering a circle, he will lose.
3. Enemies in circles 3 (`k3`) and 7 (`k7`) can regenerate once with half of their initial power and attack from behind when Abhimanyu battles in the next circle.

### Objective:
Determine if Abhimanyu can cross all 11 circles and survive.

## Algorithm Explanation

The algorithm simulates Abhimanyu's journey through the Chakravyuha by iterating through each of the 11 circles, taking into account his power level, the ability to skip battles, recharge options, and the regeneration of certain enemies.

### Steps:
1. **Initialization**:
   - Abhimanyu starts with `P` power.
   - Track the number of skips (`a`) and recharges (`b`) available.

2. **Battle Simulation**:
   - For each circle:
     - **Skip**: If skipping is an option and Abhimanyu's power is less than the enemy's power, he skips the battle.
     - **Fight**: If not skipping, Abhimanyu fights the enemy, losing power equal to the enemy's power.
     - **Recharge**: If Abhimanyu's power is depleted after a battle, and recharges are available, he recharges.
     - **Regeneration Check**: If Abhimanyu is battling in circles 4 or 8, check if enemies `k3` or `k7` regenerate and attack again with half their original power.

3. **Outcome**:
   - If Abhimanyu survives all 11 circles, he wins. Otherwise, he loses.

###Code: 
The code implementation is provided in the [abhimanyu_chakravyuha.py](abhimanyu_chakravyuha.py) file.

