from nflsim.nfl_data_cols import *


class INITS:
    STANDINGS = {
        COLS.STANDINGS.NFL_TEAM: {},
        COLS.STANDINGS.W: {},
        COLS.STANDINGS.L: {},
        COLS.STANDINGS.T: {},
        COLS.STANDINGS.PCT: {},
        COLS.STANDINGS.PF: {},
        COLS.STANDINGS.PA: {},
        COLS.STANDINGS.NET_PTS: {},
        COLS.STANDINGS.HOME: {},
        COLS.STANDINGS.AWAY: {},
        COLS.STANDINGS.DIV: {},
        COLS.STANDINGS.CONF: {},
        COLS.STANDINGS.NON_CONF: {},
        COLS.STANDINGS.STRK: {},
    }

    STANDINGS_ROW = {
        COLS.STANDINGS.NFL_TEAM: "",
        COLS.STANDINGS.W: 0,
        COLS.STANDINGS.L: 0,
        COLS.STANDINGS.T: 0,
        COLS.STANDINGS.PCT: 0,
        COLS.STANDINGS.PF: 0,
        COLS.STANDINGS.PA: 0,
        COLS.STANDINGS.NET_PTS: 0,
        COLS.STANDINGS.HOME: "0-0-0",
        COLS.STANDINGS.AWAY: "0-0-0",
        COLS.STANDINGS.DIV: "0-0-0",
        COLS.STANDINGS.CONF: "0-0-0",
        COLS.STANDINGS.NON_CONF: "0-0-0",
        COLS.STANDINGS.STRK: "-",
    }

    STATS = {
        COLS.STAT_CATEGORIES.PASSING: {},
        COLS.STAT_CATEGORIES.RUSHING: {},
        COLS.STAT_CATEGORIES.RECEIVING: {},
        COLS.STAT_CATEGORIES.DEFENSE: {},
        COLS.STAT_CATEGORIES.SCORING: {},
        COLS.STAT_CATEGORIES.RETURNING: {},
        COLS.STAT_CATEGORIES.KICKING: {},
        COLS.STAT_CATEGORIES.PUNTING: {},
    }

    class STAT_TYPES:
        PASSING = {
            COLS.STAT_PASSING.GP: {},
            COLS.STAT_PASSING.CMP: {},
            COLS.STAT_PASSING.ATT: {},
            COLS.STAT_PASSING.CMPP: {},
            COLS.STAT_PASSING.YDS: {},
            COLS.STAT_PASSING.AVG: {},
            COLS.STAT_PASSING.TD: {},
            COLS.STAT_PASSING.INT: {},
            COLS.STAT_PASSING.LNG: {},
            COLS.STAT_PASSING.SACK: {},
        }

        PASSING_ROW = {
            COLS.STAT_PASSING.GP: 0,
            COLS.STAT_PASSING.CMP: 0,
            COLS.STAT_PASSING.ATT: 0,
            COLS.STAT_PASSING.CMPP: 0,
            COLS.STAT_PASSING.YDS: 0,
            COLS.STAT_PASSING.AVG: 0,
            COLS.STAT_PASSING.TD: 0,
            COLS.STAT_PASSING.INT: 0,
            COLS.STAT_PASSING.LNG: 0,
            COLS.STAT_PASSING.SACK: 0,
        }

        RUSHING = {
            COLS.STAT_RUSHING.GP: {},
            COLS.STAT_RUSHING.CAR: {},
            COLS.STAT_RUSHING.YDS: {},
            COLS.STAT_RUSHING.AVG: {},
            COLS.STAT_RUSHING.TD: {},
            COLS.STAT_RUSHING.LNG: {},
            COLS.STAT_RUSHING.FD: {},
            COLS.STAT_RUSHING.FUM: {},
            COLS.STAT_RUSHING.LST: {},
        }

        RUSHING_ROW = {
            COLS.STAT_RUSHING.GP: 0,
            COLS.STAT_RUSHING.CAR: 0,
            COLS.STAT_RUSHING.YDS: 0,
            COLS.STAT_RUSHING.AVG: 0,
            COLS.STAT_RUSHING.TD: 0,
            COLS.STAT_RUSHING.LNG: 0,
            COLS.STAT_RUSHING.FD: 0,
            COLS.STAT_RUSHING.FUM: 0,
            COLS.STAT_RUSHING.LST: 0,
        }

        RECEIVING = {
            COLS.STAT_RECEIVING.GP: {},
            COLS.STAT_RECEIVING.REC: {},
            COLS.STAT_RECEIVING.TGTS: {},
            COLS.STAT_RECEIVING.YDS: {},
            COLS.STAT_RECEIVING.AVG: {},
            COLS.STAT_RECEIVING.TD: {},
            COLS.STAT_RECEIVING.LNG: {},
            COLS.STAT_RECEIVING.FD: {},
            COLS.STAT_RECEIVING.FUM: {},
            COLS.STAT_RECEIVING.LST: {},
        }

        RECEIVING_ROW = {
            COLS.STAT_RECEIVING.GP: 0,
            COLS.STAT_RECEIVING.REC: 0,
            COLS.STAT_RECEIVING.TGTS: 0,
            COLS.STAT_RECEIVING.YDS: 0,
            COLS.STAT_RECEIVING.AVG: 0,
            COLS.STAT_RECEIVING.TD: 0,
            COLS.STAT_RECEIVING.LNG: 0,
            COLS.STAT_RECEIVING.FD: 0,
            COLS.STAT_RECEIVING.FUM: 0,
            COLS.STAT_RECEIVING.LST: 0,
        }

        DEFENSE = {
            COLS.STAT_DEFENSE.GP: {},
            COLS.STAT_DEFENSE.TOT: {},
            COLS.STAT_DEFENSE.SOLO: {},
            COLS.STAT_DEFENSE.AST: {},
            COLS.STAT_DEFENSE.SACK: {},
            COLS.STAT_DEFENSE.FF: {},
            COLS.STAT_DEFENSE.FR: {},
            COLS.STAT_DEFENSE.FYDS: {},
            COLS.STAT_DEFENSE.INT: {},
            COLS.STAT_DEFENSE.IYDS: {},
            COLS.STAT_DEFENSE.AVG: {},
            COLS.STAT_DEFENSE.TD: {},
            COLS.STAT_DEFENSE.LNG: {},
            COLS.STAT_DEFENSE.PD: {},
            COLS.STAT_DEFENSE.STF: {},
            COLS.STAT_DEFENSE.STFYDS: {},
            COLS.STAT_DEFENSE.KB: {},
        }

        DEFENSE_ROW = {
            COLS.STAT_DEFENSE.GP: 0,
            COLS.STAT_DEFENSE.TOT: 0,
            COLS.STAT_DEFENSE.SOLO: 0,
            COLS.STAT_DEFENSE.AST: 0,
            COLS.STAT_DEFENSE.SACK: 0,
            COLS.STAT_DEFENSE.FF: 0,
            COLS.STAT_DEFENSE.FR: 0,
            COLS.STAT_DEFENSE.FYDS: 0,
            COLS.STAT_DEFENSE.INT: 0,
            COLS.STAT_DEFENSE.IYDS: 0,
            COLS.STAT_DEFENSE.AVG: 0,
            COLS.STAT_DEFENSE.TD: 0,
            COLS.STAT_DEFENSE.LNG: 0,
            COLS.STAT_DEFENSE.PD: 0,
            COLS.STAT_DEFENSE.STF: 0,
            COLS.STAT_DEFENSE.STFYDS: 0,
            COLS.STAT_DEFENSE.KB: 0,
        }

        SCORING = {
            COLS.STAT_SCORING.GP: {},
            COLS.STAT_SCORING.PASS: {},
            COLS.STAT_SCORING.RUSH: {},
            COLS.STAT_SCORING.REC: {},
            COLS.STAT_SCORING.RET: {},
            COLS.STAT_SCORING.TD: {},
            COLS.STAT_SCORING.TWOPT: {},
            COLS.STAT_SCORING.PAT: {},
            COLS.STAT_SCORING.FG: {},
            COLS.STAT_SCORING.PTS: {},
        }

        SCORING_ROW = {
            COLS.STAT_SCORING.GP: 0,
            COLS.STAT_SCORING.PASS: 0,
            COLS.STAT_SCORING.RUSH: 0,
            COLS.STAT_SCORING.REC: 0,
            COLS.STAT_SCORING.RET: 0,
            COLS.STAT_SCORING.TD: 0,
            COLS.STAT_SCORING.TWOPT: 0,
            COLS.STAT_SCORING.PAT: 0,
            COLS.STAT_SCORING.FG: 0,
            COLS.STAT_SCORING.PTS: 0,
        }

        RETURNING = {
            COLS.STAT_RETURNING.GP: {},
            COLS.STAT_RETURNING.PATT: {},
            COLS.STAT_RETURNING.PYDS: {},
            COLS.STAT_RETURNING.PTD: {},
            COLS.STAT_RETURNING.PFC: {},
            COLS.STAT_RETURNING.PLNG: {},
            COLS.STAT_RETURNING.KATT: {},
            COLS.STAT_RETURNING.KYDS: {},
            COLS.STAT_RETURNING.KTD: {},
            COLS.STAT_RETURNING.KRFC: {},
            COLS.STAT_RETURNING.KLNG: {},
        }

        RETURNING_ROW = {
            COLS.STAT_RETURNING.GP: 0,
            COLS.STAT_RETURNING.PATT: 0,
            COLS.STAT_RETURNING.PYDS: 0,
            COLS.STAT_RETURNING.PTD: 0,
            COLS.STAT_RETURNING.PFC: 0,
            COLS.STAT_RETURNING.PLNG: 0,
            COLS.STAT_RETURNING.KATT: 0,
            COLS.STAT_RETURNING.KYDS: 0,
            COLS.STAT_RETURNING.KTD: 0,
            COLS.STAT_RETURNING.KRFC: 0,
            COLS.STAT_RETURNING.KLNG: 0,
        }

        KICKING = {
            COLS.STAT_KICKING.GP: {},
            COLS.STAT_KICKING.FG: {},
            COLS.STAT_KICKING.FGP: {},
            COLS.STAT_KICKING.Y01_19: {},
            COLS.STAT_KICKING.Y20_29: {},
            COLS.STAT_KICKING.Y30_39: {},
            COLS.STAT_KICKING.Y40_49: {},
            COLS.STAT_KICKING.Y50P: {},
            COLS.STAT_KICKING.LNG: {},
            COLS.STAT_KICKING.XPM: {},
            COLS.STAT_KICKING.XPA: {},
            COLS.STAT_KICKING.PTS: {},
        }

        KICKING_ROW = {
            COLS.STAT_KICKING.GP: 0,
            COLS.STAT_KICKING.FG: 0,
            COLS.STAT_KICKING.FGP: 0,
            COLS.STAT_KICKING.Y01_19: 0,
            COLS.STAT_KICKING.Y20_29: 0,
            COLS.STAT_KICKING.Y30_39: 0,
            COLS.STAT_KICKING.Y40_49: 0,
            COLS.STAT_KICKING.Y50P: 0,
            COLS.STAT_KICKING.LNG: 0,
            COLS.STAT_KICKING.XPM: 0,
            COLS.STAT_KICKING.XPA: 0,
            COLS.STAT_KICKING.PTS: 0,
        }

        PUNTING = {
            COLS.STAT_PUNTING.GP: {},
            COLS.STAT_PUNTING.PUNTS: {},
            COLS.STAT_PUNTING.AVG: {},
            COLS.STAT_PUNTING.LNG: {},
            COLS.STAT_PUNTING.YDS: {},
            COLS.STAT_PUNTING.TB: {},
            COLS.STAT_PUNTING.TBP: {},
            COLS.STAT_PUNTING.IN20: {},
            COLS.STAT_PUNTING.IN20P: {},
            COLS.STAT_PUNTING.ATT: {},
            COLS.STAT_PUNTING.RYDS: {},
            COLS.STAT_PUNTING.RAVG: {},
            COLS.STAT_PUNTING.NET: {},
        }

        PUNTING_ROW = {
            COLS.STAT_PUNTING.GP: 0,
            COLS.STAT_PUNTING.PUNTS: 0,
            COLS.STAT_PUNTING.AVG: 0,
            COLS.STAT_PUNTING.LNG: 0,
            COLS.STAT_PUNTING.YDS: 0,
            COLS.STAT_PUNTING.TB: 0,
            COLS.STAT_PUNTING.TBP: 0,
            COLS.STAT_PUNTING.IN20: 0,
            COLS.STAT_PUNTING.IN20P: 0,
            COLS.STAT_PUNTING.ATT: 0,
            COLS.STAT_PUNTING.RYDS: 0,
            COLS.STAT_PUNTING.RAVG: 0,
            COLS.STAT_PUNTING.NET: 0,
        }
