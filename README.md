# fantasy-football

## Player/Team Attributes

### Passers

$P_P\in(0,1):$ Tendency for a passer to attempt a pass

$P_R\in(0,1):$ Tendency for a passer to rush

$P_H\in(0,1):$ Tendency for a passer to hand off to another rusher

$Y_A(Y_L):$ Yards attempted; a random variable dependent on yard line

$t_T(Y_A):$ Time to throw; a random variable dependent on yards attempted

$P_S:$ Probability of a sack given there was pressure from the defense

$P_F:$ Probability of a fumble lost

$P_C(Y_A,\ P):$ Probability of completing a pass; a function of attempted yards and pressure from the defense

$P_I(Y_A,\ P):$ Probability of an interception; a random variable dependent on attempted yards and pressure from the defense

### Rushers

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

$P_F:$ Probability of forcing a fumble lost

$Y_R(Y_L):$ Return yards on a turnover; a random variable dependent on yard line

### Special Teams - Kicking/Punting

$P_{KR}:$ Probability of allowing a return on a kickoff

$Y_{KR}:$ Yards allowed on a kick return; a random variable

$P_{PR}:$ Probability of allowing a return on a punt

$Y_{KR}(Y_L):$ Yards allowed on a punt return; a random variable dependent on yard line

### Special Teams - Returning

$P_{KR}:$ Probability of returning a kickoff

$Y_{KR}:$ Yards gained on a kick return; a random variable

$t_{KR}(Y_{KR}):$ Length of return in seconds; a random variable dependent on return yards

$P_{PR}:$ Probability of returning a punt

$Y_{KR}(Y_L):$ Yards on a punt return; a random variable dependent on yard line

### Kickers

$P_{EX}:$ Probability of making an extra point

$P_{FG}(Y):$ Probability of making a FG; a function of yards

$t_{FG}(Y):$ Clock time used for a field goals; random variable dependent on yards

### Decision Making

## Simulation Procedure

### Plays

### Kickoffs

1. Use $P_{KR}$ to determine whether the kick is returned or caught for a touchback

If returned:
1. Use $Y_{KR}$ to determine the return yards
2. Use $t_{KR}(Y_{KR})$ to determine the time to deduct from the playclock

If touchback:
1. Ball is placed at the 25 yard line and the playclock remains unchanged

### Punts

### Field Goals
