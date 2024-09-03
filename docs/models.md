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

`model_ep()`

### Parameters:

### Returns:

&emsp;**`made`: _bool_**

&emsp;&emsp;A boolean indicator for if the extra point was made.

## Field Goal Model

`model_fg()`

### Parameters:

### Returns:

&emsp;**`made`: _bool_**

&emsp;&emsp;A boolean indicator for if the field goal was made.

&emsp;**`time`: _float_**

&emsp;&emsp;The time in seconds used during the field goal play.

## Kick Distance Model

`model_kd()`

### Parameters:

### Returns:

&emsp;**`distance`: _float_**

&emsp;&emsp;The distance in yards the ball was kicked.

## Kick Return Decision Model

`model_krd() -> return (bool)`

### Parameters:

### Returns:

&emsp;**`_return`: _bool_**

&emsp;&emsp;A boolean indicator for if the kick was returned.

## Kick Return Fumble Model

`model_krf() -> yards (float), td (bool), time (float)`

### Parameters:

### Returns:

&emsp;**`yards`: _float_**

&emsp;&emsp;Distance in yards the fumble was returned by kicking team.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the kicking team returned the fumble for a touchdown.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the fumble return.

## Kick Return Yards Model

`model_kry()`

### Parameters:

### Returns:

&emsp;**`yards`: _float_**

&emsp;&emsp;The distance in yards the ball was returned.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the ball was returned for a touchdown.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the kick return.

&emsp;**`fumble`: _bool_**

&emsp;&emsp;A boolean indicator for if the ball was fumbled and lost.

## Passer Fumble Return Model

`model_pfr()`

### Parameters

### Returns

&emsp;**`yards`: _float_**

&emsp;&emsp;The net yards gained by the defense on the fumble.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the fumble resulted in a touchdown for the defense.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the fumble return play.

## Passer Scramble Fumble Model

`model_ppscrmf()`

### Parameters

### Returns

&emsp;**`yards`: _float_**

&emsp;&emsp;The yards gained by the defense on the fumble return.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the fumble return resulted in a touchdown.

&emsp;**`time`: \_float**

&emsp;&emsp;The time used during the fumble return play.

## Passer Scramble Model

`model_ppscrm()`

### Parameters

### Returns

&emsp;**`yards`: _float_**

&emsp;&emsp;The yards gained/loss by the passer.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the play resulted in a touchdown.

&emsp;**`fumble`: _bool_**

&emsp;&emsp;A boolean indicator for if the passer loses a fumble.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the scramble play.

## Passer Throw Model

`model_ppt()`

### Parameters

### Returns

&emsp;**`yards`: _float_**

&emsp;&emsp;The yards of the pass.

&emsp;**`complete`: _bool_**

&emsp;&emsp;A boolean indicator for if the pass was completed.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the completed resulted in a touchdown.

&emsp;**`int`: _bool_**

&emsp;&emsp;A boolean indicator for if the pass was intercepted.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the pass play.

## Pass Play Branch Model

`model_ppbrnch()`

### Parameters

### Returns

&emsp;**`sack`: _bool_**

&emsp;&emsp;A boolean indicator for if the play resulted in a sack.

&emsp;**`fumble`: _bool_**

&emsp;&emsp;A boolean indicator for if the play resulted in a lost fumble.

&emsp;**`scramble`: _bool_**

&emsp;&emsp;A boolean indicator for if the play resulted in a scramble.

## Pass Play Sack Model

`model_ppsck()`

### Parameters

### Returns

&emsp;**`safety`: _bool_**

&emsp;&emsp;A boolean indicator for if the sack resulted in a safety.

&emsp;**`yards`: _float_**

&emsp;&emsp;The yards sacked on the play.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the play.

## Punt Block Model

`model_pntb()`

### Parameters:

### Returns:

&emsp;**`yards`: _float_**

&emsp;&emsp;The yards returned on the punt block.

&emsp;**`td`: _bool_**

&emsp;&emsp;A binary indicator for if the punt block resulting in a touchdown.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used on the punt block play.

## Punt Model

`model_pnt()`

### Parameters:

### Returns:

&emsp;**`blocked`: _bool_**

&emsp;&emsp;A boolean indicator for if the punt was blocked.

&emsp;**`distance`: _float_**

&emsp;&emsp;The punt distance in yards.

&emsp;**`touchback`: _bool_**

&emsp;&emsp;A boolean indicator for if the punt was downed in the endzone.

&emsp;**`time`: _float_**

&emsp;&emsp;The used for the punt.

## Punt Return Decision Model

`model_pntrd()`

### Parameters:

### Returns:

&emsp;**`_return`: _bool_**

&emsp;&emsp;A boolean indicator for if the punt was returned.

## Punt Return Fumble Model

### Parameters

### Returns

&emsp;**`yards`: _float_**

&emsp;&emsp;The net yards on the punt return fumble.

&emsp;**`td`: _bool_**

&emsp;&emsp;A boolean indicator for if the punt return fumble resulted in a touchdown.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used on the punt return fumble play.

## Punt Return Yards Model

`model_pntry()`

### Parameters

### Returns

&emsp;**`yards`: _float_**

&emsp;&emsp;The yards returned on the punt.

&emsp;**`fumble`: _bool_**

&emsp;&emsp;A boolean indicator for if the punt return resulted in a fumble lost.

&emsp;**`time`: _float_**

&emsp;&emsp;The time used during the punt return play.

## Receiver YAC Model

`model_ryac()`

### Parameters

### Returns

