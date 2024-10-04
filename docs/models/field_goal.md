# Contents

- [Contents](#contents)
- [Field Goal Models](#field-goal-models)
  - [PRNG](#prng)
    - [Build](#build)
      - [Parameters](#parameters)
      - [Note](#note)
    - [Sample](#sample)
      - [Return](#return)

# Field Goal Models

## PRNG

```python
nflsim.model.field_goal.PRNG()
```

Field goal model that determines outcomes randomly according to a set of given weights.

### Build

```python
nflsim.model.field_goal.PRNG.build(self, w_made: float, w_miss: float, w_block: float w_recover: float, min_yrec: int, max_yrec: int) -> None
```

Build the PRNG field goal model.

#### Parameters

**w_made** : _float_

Weight assigned to a field goal make.

**w_miss** : _float_
    
Weight assigned to a field goal miss.

**w_block** : _float_
    
Weight assigned to a field goal block.

**w_recover** : _float_
    
Weight assigned to a field goal recovery.

**min_yrec** : _int_

Minimum yards returned possible.

**max_yrec** : _int_

Maximum yards returned possible.

#### Note

`w_make`, `w_miss`, `w_block`, `w_recover` are all mutually exclusive (i.e.
`w_any_missed_fg = w_miss + w_block + w_recover`)

### Sample

```python
nflsim.model.field_goal.PRNG.sample(self) -> dict
```

Randomly sample from the model.

#### Return

```python
{
    "made" : bool,
    "missed" : bool,
    "blocked" : bool,
    "recovered" : bool,
    "yards_returned" : int
}
```

