# Contents

- [Contents](#contents)
- [Game Progression](#game-progression)
  - [Play Decision](#play-decision)
  - [Kickoff](#kickoff)
  - [Punt](#punt)
  - [Field Goal](#field-goal)
  - [Pass](#pass)
  - [Rush](#rush)

# Game Progression

Models are stylized in all lowercase with underscores in a square box.

```mermaid
flowchart TD
A[this_is_a_model]
```

Independent flow paths are stylized with leading capitals and a round box.

```mermaid
flowchart TD
A(Independent Flow Path)
```

The end of play state is stylized in all caps with a diamond box.

```mermaid
flowchart TD
A{END PLAY}
```

## Play Decision

```mermaid
flowchart TD
A[play_decision] --> |punt| B(Punt)
B --> C{END PLAY}
A --> |field goal| D(Field Goal)
D --> C
A --> |pass| E(Pass)
E --> C
A --> |rush| F(Rush)
F --> C
A --> |QB kneel| G[qb_kneel]
G --> C
A --> |QB spike| H[qb_spike]
H --> C
```

## Kickoff

```mermaid
flowchart TD
A[kickoff]
A --> |returned| B[kick_return]
A --> |not returned| C{END PLAY}
A --> |recovered by kicking team| D[kick_recovery]
D --> C
B --> C
```

## Punt

```mermaid
flowchart TD
A[punt]
A --> |blocked| B{END PLAY}
A --> |returned| C[punt_return]
A --> |not returned| B
A --> |recovered by punting team| D[punt_recovery]
D --> B
C --> B
```

## Field Goal

```mermaid
flowchart TD
A[field_goal] --> B{END PLAY}
A --> |recovered| C[field_goal_return]
C --> B
```

## Pass

```mermaid
flowchart TD
A[pass] --> |sack| B{END PLAY}
A --> |scramble| E[qb_scramble]
E --> |fumble| C
E --> B
A --> |fumble| C[turnover_return]
C --> B
A --> |complete| D[reception]
A --> |incomplete| B
D --> |fumble| C
D --> B
A --> |interception| C
```

## Rush

```mermaid
flowchart TD
A[rush] --> B{END PLAY}
A --> |fumble| C[turnover_return]
C --> B
```
