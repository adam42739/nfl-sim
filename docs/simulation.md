# nfl-sim

## Contents

1. [Game Progression](#game-progression)
2. [Plays](#plays)
   - [Pass](#pass)
   - [Rush](#rush)
   - [Field Goal](#field-goal)
   - [Kickoff](#kickoff)
   - [Punt](#punt)
   - [Extra Point](#extra-point)
   - [2 Point Conversion](#2-point-conversion)
   - [Saftey Punt](#saftey-punt)

## Game Progression

## Plays

### Pass

1. [Pass Play Branch Model](models.md#pass-play-branch-model)

   **If** `sack == True`:

   1. [Pass Play Sack Model](models.md#pass-play-sack-model)

      **If** `saftey == True`:

      1. Add `2` to the defense's score.
      2. Deduct `time` from the playclock.

      **Else**:

      1. Place the ball at the appropriate yard line.
      2. Deduct `time` from the playclock

   **Else if** `fumble == True`:

   1. [Passer Fumble Return Model](models.md#passer-fumble-return-model)

      **If** `td == True`:

      1. Add `6` to the defense's score.

      **Else**:

      1. Place the ball at the appropriate yard line.

   2. Deduct `time` from the playclock

   **Else if** `scramble == True`:

   1. [Passer Scramble Model](models.md#passer-scramble-model)

      **If** `td == True`:

      1. Add `6` to the offense's score.
      2. Deduct `time` from the playclock.

      **Else if** `fumble ==  True`:

      1. [Passer Scramble Fumble Model](models.md#passer-scramble-fumble-model)

         **If** `td == True`:

         1. Add `6` to the defense's score

         **Else**

         2. Place the ball at the appropriate yard line.

      2. Deduct `time` from the playclock.

      **Else**

      1. Place the ball at the appropriate yard line.
      2. Deduct `time` from hte playclock.

   **Else if** `throw == True`:

   1. [Passer Throw Model](models.md#passer-throw-model)

      **If** `td ==  True`:

      1. Add `6` to the offense's score.
      2. Deduct `time` from the playclock.

      **Else if** `complete == True`:

      1. [Receiver YAC Model]()

      **Else if** `int == True`:

      1. [Passing Interction Return Model]()

      **Else**:

      1. Deduct `time` from the playclock.

### Rush

### Field Goal

1. [Field Goal Model](models.md#field-goal-model).

2. Deduct `time` from the playclock.

### Kickoff

1. [Kick Distance Model](models.md#kick-distance-model).
2. [Kick Return Decision Model](models.md#kick-return-decision-model).

   **If** `_return == True`:

   1. [Kick Return Yards Model](models.md#kick-return-yards-model).

      **If** `td == True`:

      1. Add `6` points to the returning team's score.
      2. Deduct `time` from the playclock.

      **Else if** `fumble == True`:

      1. [Kick Return Fumble Model](models.md#kick-return-fumble-model).

         **If** `td == True`:

         1. Add `6` points to the kicking team's score.

         **Else**:

         1. Place the ball at the appropriate yard line.

      2. Deduct `time` from the playclock.

      **Else**:

      1. Place the ball at the appropriate yard line.
      2. Deduct the `time` from the playclock.

   **Else**:

   1. Place the ball at the appropriate yard line per the NFL rules for the current (or simulated) year.
   2. No time is deducted from the playclock.

### Punt

1. [Punt Model](models.md#punt-model).

   **If** `blocked == True`:

   1. [Punt Block Model](models.md#punt-block-model).

      **If** `td == True`:

      1. Add `6` to the returning team's score.

      **Else**:

      1. Place the ball at the appropriate yard line.

   2. Deduct `time` from the playclock.

   **Else if** `touchback == True`:

   1. Place the ball at the appropriate yard line per the NFL rules for the current (or simulated) year.
   2. Deduct `time` from the playclock.

   **Else**:

   1. [Punt Return Decision Model](models.md#punt-return-decision-model).

      **If** `_return == True`:

      1. [Punt Return Yards Model](models.md#punt-return-yards-model)

         **If** `fumble == True`:

         1. [Punt Return Fumble Model](models.md#punt-return-fumble-model)

            **If** `td == True`:

            1. Add `6` to the punting teams score.

            **Else**:

            1. Place the ball at the appropriate yard line.

         2. Deduct `time` from the playclock.

         **Else**:

         1. Place the ball at the appropriate yard line.
         2. Deduct `time` from the playclock.

      **Else**:

      1. Place the ball at the appropriate yard line.
      2. Deduct `time` from the playclock.

### Extra Point

1. [Extra Point Model](models.md#extra-point-model)
2. No time is deducted from the playclock

### 2-Point Conversion

### Saftey Punt
