# fantasy-football

## Player/Team Attributes

### Passers

$P_P\in(0,1):$ Tendency for a passer to attempt a pass

$P_R\in(0,1):$ Tendency for a passer to rush

$P_H\in(0,1):$ Tendency for a passer to hand-off to another rusher

$Y_A(Y_L):$ Yards attempted; a random variable dependent on yard line

$t_T(Y_A):$ Time to throw; a random variable dependent on yards attempted

$P_{FP}:$ Probability of a fumble lost given there was pressure

$P_{SP}:$ Probability of a sack given there was pressure from the defense

$P_{SCP}:$ Probability of a scramble given there was pressure

$P_F:$ Probability of a fumble lost given there was no pressure

$P_{SC}:$ Probability of a scramble given there was no pressure

$P_C(Y_A,\ P):$ Probability of completing a pass; a function of attempted yards and pressure from the defense

$P_I(Y_A,\ P):$ Probability of an interception; a random variable dependent on attempted yards and pressure from the defense

### Rushers

$P_R\in(0,1):$ Tendency for a rusher to receive a hand-off

$Y_R(Y_L):$ Yards gained/lost; a random variable dependent on yard line

$P_F:$ Probability of a fumble lost

### Receivers

$P_C:$ Probability of catching a target

$Y_{AC}(Y_L):$ Yards after catch; a random variable dependent on yard line

$P_F:$ Probability of a fumble lost

### O-Lines

$P_P(t_T):$ Probability of allowing pressure to the QB; a function of time to throw

### Defenses

$P_P(t_T):$ Probability of pressuring the QB; a function of time to throw

$P_I(Y_A,\ P)$ Probability of intercepting a pass; a function of yards attempted and pressure

$P_C(Y_A,\ P):$ Probability of completing a pass; a function of attempted yards and pressure from the defense

$P_S:$ Probability of a sack given there was pressure from the defense

$Y_R(Y_L):$ Yards allowed on a rush; a random variable dependent on yard line

$Y_{AC}(Y_L):$ Yards after catch allowed on a reception; a random variable dependent on yard line

$P_{PF}:$ Probability of forcing a passing fumble lost

$P_{RSF}:$ Probability of forcing a rushing fumble lost

$P_{RCF}:$ Probability of forcing a receiving fumble lost

$Y_{TR}(Y_L):$ Net return yards on a turnover; a random variable dependent on yard line

### Special Teams - Kicking/Punting

$P_{KR}:$ Probability of allowing a return on a kickoff

$Y_{KR}:$ Yards allowed on a kick return; a random variable

$P_{PR}:$ Probability of allowing a return on a punt

$Y_{KR}(Y_L):$ Yards allowed on a punt return; a random variable dependent on yard line

### Special Teams - Returning

$P_{KR}:$ Probability of returning a kickoff

$Y_{KR}:$ Yards gained on a kick return; a random variable

$P_{PR}:$ Probability of returning a punt

$Y_{PR}(Y_L):$ Yards on a punt return; a random variable dependent on yard line

### Kickers

$P_{EX}:$ Probability of making an extra point

$P_{FG}(Y):$ Probability of making a FG; a function of yards

### Decision Making

## General League Attributes

$t_R(Y_R):$ Time of play for a rushing play; a random variable dependant on yards gained/lost

$t_P(Y_A,\ Y_{AC}):$ Time of play after time to throw on a passing play; a random variable dependant on yards attempted and yards after catch

$t_{TR}(Y_{TR}):$ Time of play for a turnover; a random variable dependent on net return yards

$t_{KR}(Y_{KR}):$ Time of play for a kick return play in seconds; a random variable dependent on kick return yards

$t_{PR}(Y_{PR}):$ Time of play for a punt return play in seconds; a random variable dependent on punt return yards

$t_{FG}(Y):$ Time of play for a field goal; random variable dependent on yards

## Simulation Procedure

### Plays

1. Use $P_P$, $P_R$, and $P_H$ to determine what the passer will do

   If passing play:

   1. Go to [Passing Play](#passing-play)

   If passer rushes:

   1. Go to [Rushing Play](#rushing-play)

   If passer hands off to another rusher:

   1. Use $P_R$ to determine which rusher will receive the hand-off

      _Example_: If a team has two rushers A and B with $P_R$ values $a$ and $b$, then assign the probability of A receiving the hand-off as ${a}\over{a+b}$ and $B$ as ${b}\over{a+b}$

   2. Go to [Rushing Play](#rushing-play)

### Passing Play

1. Use $Y_A(Y_L)$ to determine the yard that will be attempted by the passer
2. Use $t_T(Y_A)$ to determine the time the passer will need to throw
3. Use $P_P(t_T)$ to determine whether or not the defense will pressure
4. Use passer and defensive $P_S$ to determine whether the passer will be sacked

### Rushing Play

1.  Use $P_{RSF}$ and $P_F$ to determine whether a fumble lost will occur

    _Example_: If the defense has $P_{RSF}$ value $d$ and the rusher has $P_{F}$ value $r$, then the probability of a fumble lost is ${d+r}\over{2}$.

    If fumble lost:

    1. Use $Y_{TR}(Y_L)$ to determine the net return yards by the defense
    2. Use $t_{TR}(Y_{TR})$ to determine the time to dedect from the playclock

    If no fumble lost:

    1. Use rusher and defensive $Y_R(Y_L)$ to determine the yards gained or lost

       _Example_: If $r$ is a randome sample from the rushers distribution and $d$ is a random sample from the defenses, take the yards to be $r$ with probability ${1}\over{2}$ and $d$ with probability ${1}\over{2}$

    2. Use $t_R(Y_R)$ to determine the time to deduct from the playclock.

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
