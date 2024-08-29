# nfl-sim

## Introduction

## Contents

1. [Simulation](#simulation)
   - [Game Progression](#game-progression)
   - [Plays](#plays)
     - [Pass](#pass)
     - [Rush](#rush)
     - [Field Goal](#field-goal)
     - [Kickoff](#kickoff)
     - [Punt](#punt)
     - [Extra Point](#extra-point)
     - [2 Point Conversion](#2-point-conversion)
     - [Saftey Punt](#saftey-punt)
2. [Models](#models)
   - [Field Goal Model](#field-goal-model)
   - [Extra Point Model](#extra-point-model)
3. [Attributes](#attributes)
   - [Passer](#passer)
     - [Decision Making](#decision-making)
     - [Control](#control)
     - [Scrambling](#scrambling)
     - [Throwing](#throwing)
   - [Rusher](#rusher)
   - [Receiver](#receiver)
   - [Pressure Protector](#pressure-protector)
   - [Defender - Passing](#defender---passing)
   - [Defender - Rushing](#defender---rushing)
   - [Special Teams - Kicking](#special-teams---kicking)
     - [Kicker](#kicker)
     - [Returner](#returner)
     - [Kick Defender](#kick-defender)
     - [Return Blocker](#return-blocker)
   - [Special Teams - Punting](#special-teams---punting)
     - [Punter](#punter)
     - [Returner](#returner-1)
     - [Punt Defender](#punt-defender)
     - [Return Blocker](#return-blocker-1)

## Simulation

### Game Progression

### Plays

#### Pass

#### Rush

#### Field Goal

1. Use the [field goal model](#field-goal-model) to determine whether the FG is good and how much time to deduct from the playclock.

#### Kickoff

1. [Kick Distance Model](#kick-distance-model)
2. [Kick Return Decision Model](#kick-return-decision-model)

   If `return == True`

   1. [Kick Return Yards Model](#kick-return-yards-model)

      If `td == True`

      1. Add `6` points to the returning team's score
      2. Deduct `time` from the playclock

      Else if `fumble == True`

      1. [Kick Return Fumble Model](#kick-return-fumble-model)

         If `td == True`

         1. Add `6` points to the kicking team's score

         Else

         1. Place the ball at the appropriate yard line (`65 - model_kd()->distance + model_kry()->yards - model_krf()->yards`)

      2. Deduct `model_kry()->time + model_krf()->time` from the playclock

      Else

      1. Place the ball at the appropriate yard line (`65 - model_kd()->distance + model_kry()->yards`)
      2. Deduct the `time` from the playclock

   Else

   1. Place the ball at the appropriate yard line per the NFL rules for the current (or simulated) year
   2. No time is dedeucted from the playclock

#### Punt

1. [Punt Model]
2. 

#### Extra Point

1. [Extra Point Model](#extra-point-model)
2. No time is deducted from the playclock

#### 2-Point Conversion

#### Saftey Punt

## Models

### Punt Model

`model_p()`

#### Parameters:

#### Returns:

``

### Field Goal Model

`model_fg()`

#### Parameters:

#### Returns:

&emsp;`made`: _bool_

&emsp;&emsp;A boolean indicator for if the field goal was made.

&emsp;`time`: _float_

&emsp;&emsp;The time in seconds used during the field goal play.

### Extra Point Model

`model_ep()`

#### Parameters:

#### Returns:

&emsp;`made`: _bool_

&emsp;&emsp;A boolean indicator for if the extra point was made.

### Kick Distance Model

`model_kd()`

#### Parameters:

#### Returns:

&emsp;`distance`: _float_

&emsp;&emsp;The distance in yards the ball was kicked.

### Kick Return Decision Model

`model_krd() -> return (bool)`

#### Parameters:

#### Returns:

&emsp;`return`: _bool_

&emsp;&emsp;A boolean indicator for if the kick was returned.

### Kick Return Yards Model

`model_kry()`

#### Parameters:

#### Returns:

&emsp;`yards`: _float_

&emsp;&emsp;The distance in yards the ball was returned.

&emsp;`td`: _bool_

&emsp;&emsp;A boolean indicator for if the ball was returned for a touchdown.

&emsp;`time`: _float_

&emsp;&emsp;The time used during the kick return.

&emsp;`fumble`: _bool_

&emsp;&emsp;A boolean indicator for if the ball was fumbled and lost.

### Kick Return Fumble Model

`model_krf() -> yards (float), td (bool), time (float)`

#### Parameters:

#### Returns:

&emsp;`yards`: _float_

&emsp;&emsp;Distance in yards the fumble was returned by kicking team.

&emsp;`td`: _bool_

&emsp;&emsp;A boolean indicator for if the kicking team returned the fumble for a touchdown.

&emsp;`time`: _float_

&emsp;&emsp;The time used during the fumble return.

## Attributes

### Passer

#### Decision Making

`p_pass`: Probability a passer will attempt to pass

`p_rush`: Probability a passer will attempt to rush

`p_handoff`: Probability a passer will hand-off to another rusher

#### Control

`p_sack`: Probability a passer will get sacked

`p_fumb`: Probability a passer will lose a fumble will attempting to pass (not including scrambling)

`p_scram`: Probability a passer will scramble

#### Scrambling

`yards`: Distribution of yards a passer gains/loses while scrambling

`p_fumb`: Probability a passer will lose a fumble while scrambling:

#### Throwing

`yards`: Distribution of yards a passer will attempt to complete

`p_comp(yards)`: Probability a passer completed a pass of `yards` attempted

### Rusher

### Receiver

### Pressure Protector

### Defender - Passing

### Defender - Rushing

### Special Teams - Kicking

#### Kicker

#### Returner

#### Kick Defender

#### Return Blocker

### Special Teams - Punting

#### Punter

#### Returner

#### Punt Defender

#### Return Blocker
