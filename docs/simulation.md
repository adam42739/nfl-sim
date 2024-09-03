# nfl-sim

## Introduction



## Contents

- [nfl-sim](#nfl-sim)
  - [Introduction](#introduction)
  - [Contents](#contents)
  - [Game Progression](#game-progression)
  - [Plays](#plays)
    - [Pass](#pass)
    - [Rush](#rush)
    - [Field Goal](#field-goal)
    - [Kickoff](#kickoff)
    - [Punt](#punt)
    - [Extra Point](#extra-point)
    - [2-Point Conversion](#2-point-conversion)
    - [Saftey Punt](#saftey-punt)

## Game Progression

## Plays

### Pass

1. [Pass Play Branch Model](models.md#pass-play-branch-model)

   **If** `sack == True`:

   1. [Pass Play Sack Model](models.md#pass-play-sack-model)

   **Else if** `fumble == True`:

   1. [Passer Fumble Return Model](models.md#passer-fumble-return-model)

   **Else if** `scramble == True`:

   1. [Passer Scramble Model](models.md#passer-scramble-model)

      **If** `fumble ==  True`:

      1. [Passer Scramble Fumble Model](models.md#passer-scramble-fumble-model)

   **Else**:

   1. [Passer Throw Model](models.md#passer-throw-model)

      **If** `complete == True`:

      1. [Receiver YAC Model](models.md#receiver-yac-model)


      **Else if** `int == True`:

      2. [Passing Interction Return Model]()

### Rush

### Field Goal

1. [Field Goal Model](models.md#field-goal-model).

### Kickoff

1. [Kick Distance Model](models.md#kick-distance-model).
2. [Kick Return Decision Model](models.md#kick-return-decision-model).

   **If** `_return == True`:

   1. [Kick Return Yards Model](models.md#kick-return-yards-model).

      **If** `fumble == True`:

      1. [Kick Return Fumble Model](models.md#kick-return-fumble-model).

### Punt

1. [Punt Model](models.md#punt-model).

   **If** `blocked == True`:

   1. [Punt Block Model](models.md#punt-block-model).

   **Else**:

   1. [Punt Return Decision Model](models.md#punt-return-decision-model).

      **If** `_return == True`:

      1. [Punt Return Yards Model](models.md#punt-return-yards-model)

         **If** `fumble == True`:

         1. [Punt Return Fumble Model](models.md#punt-return-fumble-model)

### Extra Point

1. [Extra Point Model](models.md#extra-point-model)

### 2-Point Conversion

### Saftey Punt
