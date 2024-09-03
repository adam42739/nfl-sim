# Models

## Contents

1.  [Extra Point Model](#extra-point-model)
2.  [Field Goal Model](#field-goal-model)
3.  [Kick Distance Model](#kick-distance-model)
4.  [Kick Return Decision Model](#kick-return-decision-model)
5.  [Kick Return Fumble Model](#kick-return-fumble-model)
6.  [Kick Return Yards Model](#kick-return-yards-model)
7.  [Passer Fumble Return Model](#passer-fumble-return-model)
8.  [Passer Scramble Fumble Model](#passer-scramble-fumble-model)
9.  [Passer Scramble Model](#passer-scramble-model)
10. [Passer Throw Model](#passer-throw-model)
11. [Pass Play Branch Model](#pass-play-branch-model)
12. [Pass Play Sack Model](#pass-play-sack-model)
13. [Punt Block Model](#punt-block-model)
14. [Punt Model](#punt-model)
15. [Punt Return Decision Model](#punt-return-decision-model)
16. [Punt Return Fumble Model](#punt-return-fumble-model)
17. [Punt Return Yards Model](#punt-return-yards-model)
18. [Receiver YAC Model](#receiver-yac-model)

## Extra Point Model

`model_xp()`

### Returns:

**`made`: _bool_**

**`penalty`: _bool_**

**`penalty_yards`: _float_**

## Field Goal Model

`model_fg()`

### Returns:

**`made`: _bool_**

**`penalty`: _bool_**

**`penalty_yards`: _float_**

**`time`: _float_**

## Kick Distance Model

`model_kd()`

### Returns:

**`distance`: _float_**

**`penalty`: _bool_**

**`penalty_yards`: _float_**

## Kick Return Decision Model

`model_krd()`

### Returns:

**`ret`: _bool_**

## Kick Return Fumble Model

`model_krf()`

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`penalty`: _bool_**

**`penalty_yards`: _float_**

**`time`: _float_**

## Kick Return Yards Model

`model_kry()`

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`penalty`: _bool_**

**`penalty_yards`: _float_**

**`time`: _float_**

**`fumble`: _bool_**

## Passer Fumble Return Model

`model_pfr()`

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`time`: _float_**

## Passer Scramble Fumble Model

`model_ppscrmf()`

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`time`: \_float**

## Passer Scramble Model

`model_ppscrm()`

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`fumble`: _bool_**

**`time`: _float_**

## Passer Throw Model

`model_ppt()`

### Returns:

**`yards`: _float_**

**`complete`: _bool_**

**`td`: _bool_**

**`int`: _bool_**

**`time`: _float_**

## Pass Play Branch Model

`model_ppbrnch()`

### Returns:

**`sack`: _bool_**

**`fumble`: _bool_**

**`scramble`: _bool_**

## Pass Play Sack Model

`model_ppsck()`

### Returns:

**`safety`: _bool_**

**`yards`: _float_**

**`time`: _float_**

## Punt Block Model

`model_pntb()`

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`time`: _float_**

## Punt Model

`model_pnt()`

### Returns:

**`blocked`: _bool_**

**`distance`: _float_**

**`touchback`: _bool_**

**`time`: _float_**

## Punt Return Decision Model

`model_pntrd()`

### Returns:

**`_return`: _bool_**

## Punt Return Fumble Model

### Returns:

**`yards`: _float_**

**`td`: _bool_**

**`time`: _float_**

## Punt Return Yards Model

`model_pntry()`

### Returns:

**`yards`: _float_**

**`fumble`: _bool_**

**`time`: _float_**

## Receiver YAC Model

`model_ryac()`

### Returns:
