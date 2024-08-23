# fantasy-football

## Player/Team Attributes

### Passers

$P_P\in(0,1):$ Tendency for a passer to attempt a pass

$P_R\in(0,1):$ Tendency for a passer to rush

$P_H\in(0,1):$ Tendency for a passer to hand-off to another rusher

$Y_A(Y_L):$ Yards attempted; a random variable dependent on yard line

$t_T(Y_A):$ Time to throw; a random variable dependent on yards attempted

$P_S:$ Probability of a sack given there was pressure from the defense

$P_F:$ Probability of a fumble lost

$P_C(Y_A,\ P):$ Probability of completing a pass; a function of attempted yards and pressure from the defense

$P_I(Y_A,\ P):$ Probability of an interception; a random variable dependent on attempted yards and pressure from the defense

### Rushers

$P_R\in(0,1):$ Tendency for a rusher to receive a hand-off

$Y_R(Y_L):$ Yards gained/lost; a random variable dependent on yard line

$t_R(Y_R):$ Play length in seconds; a random variable dependant on yards gained/lost

$P_F:$ Probability of a fumble lost

### Receivers

$P_C:$ Probability of catching a target

$Y_{AC}(Y_L):$ Yards after catch; a random variable dependent on yard line

$t_P(Y_A,\ Y_{AC}):$ Play length after time to throw; a random variable dependant on yards attempted and yards after catch

$P_F:$ Probability of a fumble lost

### O-Lines

$P_P(t_T):$ Probability of allowing pressure to the QB; a function of time to throw

### Defenses

$P_P(t_T):$ Probability of pressuring the QB; a function of time to throw

$P_I(Y_A,\ P)$ Probability of intercepting a pass; a function of yards attempted and pressure

$P_C(Y_A,\ P):$ Probability of completing a pass; a function of attempted yards and pressure from the defense

$P_S:$ Probability of a sack given there was pressure from the defense

$P_{PF}:$ Probability of forcing a passing fumble lost

$P_{RSF}:$ Probability of forcing a rushing fumble lost

$P_{RCF}:$ Probability of forcing a receiving fumble lost

$Y_R(Y_L):$ Return yards on a turnover; a random variable dependent on yard line

### Special Teams - Kicking/Punting

$P_{KR}:$ Probability of allowing a return on a kickoff

$Y_{KR}:$ Yards allowed on a kick return; a random variable

$P_{PR}:$ Probability of allowing a return on a punt

$Y_{KR}(Y_L):$ Yards allowed on a punt return; a random variable dependent on yard line

### Special Teams - Returning

$P_{KR}:$ Probability of returning a kickoff

$Y_{KR}:$ Yards gained on a kick return; a random variable

$t_{KR}(Y_{KR}):$ Length of kick return play in seconds; a random variable dependent on kick return yards

$P_{PR}:$ Probability of returning a punt

$Y_{PR}(Y_L):$ Yards on a punt return; a random variable dependent on yard line

$t_{PR}(Y_{PR}):$ Length of punt return play in seconds; a random variable dependent on punt return yards

### Kickers

$P_{EX}:$ Probability of making an extra point

$P_{FG}(Y):$ Probability of making a FG; a function of yards

$t_{FG}(Y):$ Clock time used for a field goals; random variable dependent on yards

### Decision Making

## Simulation Procedure

### Plays

1. Use $P_P$, $P_R$, and $P_H$ to determine what the passer will do

   If passing play

   1. Go to [Passing Play](#passing-play)

   If passer rushes

   1. Go to [Rushing Play](#rushing-play)

   If passer hands off to another rusher

   1. Use $P_R$ to determine which rusher will receive the hand-off

      *Example*: if a team has two rushers A and B with $P_R$ values $a$ and $b$, then assign the probability of A receiving the hand-off as ${a}\over{a+b}$ and $B$ as ${b}\over{a+b}$

   2. Go to [Rushing Play](#rushing-play)

### Passing Play

### Rushing Play

1. Use
2. Use $Y_R(Y_L)$ to determine the yards gained or lost
3. Use

### Kickoffs

1. Use $P_{KR}$ to determine whether the kick is returned or caught for a touchback

   If returned:

   1. Use $Y_{KR}$ to determine the return yards
   2. Use $t_{KR}(Y_{KR})$ to determine the time to deduct from the playclock

   If touchback:

   1. Ball is placed at the 25 yard line and the playclock remains unchanged

### Punts

1. Use $P_{PR}$ to determine whether the punt is returned or caught for a fair catch

   If returned:

   1. Use $Y_{PR}$ to determine the return yards
   2. Use $t_{PR}(Y_{PR})$ to determine the time to deduct from the playclock

   If fair catch:

   1. Ball is placed at the spot of the fair catch
   2. Use $t_{PR}(0)$ to determine the time to deduct from the playclock

### Field Goals

1. Use $P_{FG}(Y)$ to determine whether the field goal is good
2. Use $t_{FG}(Y)$ to determine the time to deduct from the playclock

Note: Missed field goal returns are excluded from the simulation

### Extra Points

1. Use $P_{EX}$ to determine whether the extra point is made
2. No time is deducted from the playclock
