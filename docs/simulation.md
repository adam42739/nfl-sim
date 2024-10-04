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
A[play_decision]
B(Punt)
C(Field Goal)
D(Pass)
E(Rush)
F[qb_kneel]
G[qb_spike]
H{END PLAY}

A --> B
A --> C
A --> D
A --> E
A --> F
A --> G

B --> H
C --> H
D --> H
E --> H
F --> H
G --> H

```

## Kickoff

```mermaid
flowchart TD
A[kickoff]
B[kick_recovery]
C[kick_return]
D{END PLAY}

A --> |recovered by kicking team| B
A --> |returned| C
A --> |fair catch/touchback| D

B --> D
C --> D
```

## Punt

```mermaid
flowchart TD
A[punt]
B[punt_return]
C[punt_recovery]
D{END PLAY}

A --> |returned| B
A --> |recovery by punting team| C
A --> |fair catch/touchback|D

B --> D
C --> D
```

## Field Goal

```mermaid
flowchart TD
A[field_goal]
B[field_goal_return]
C{END PLAY}

A --> |recovered| B
B --> C
A --> |made/missed/blocked| C
```

## Pass

```mermaid
flowchart TD
A[pass]
B[turnover_return]
C[reception]
D[qb_scramble]
E{END PLAY}

A --> |interception/fumble| B
A --> |completion| C
A --> |scramble| D
A --> |incomplete/sack| E

C --> |fumble| B
D --> |fumble| B
C --> E
B --> E
D --> E
```

## Rush

```mermaid
flowchart TD
A[rush]
B[turnover_return]
C{END PLAY}

A --> |fumble| B
A --> C
B --> C
```
