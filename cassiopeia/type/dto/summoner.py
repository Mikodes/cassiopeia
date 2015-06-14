import cassiopeia.type.dto.common

class RunePages(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # list<RunePage> # Collection of rune pages associated with the summoner.
        self.pages = [(RunePage(p) if not isinstance(p, RunePage) else p) for p in dictionary.get("pages", []) if p]

        # int # Summoner ID.
        self.summonerId = dictionary.get("summonerId", 0)

    @property
    def rune_ids(self):
        ids = set()
        for p in self.pages:
            ids = ids | p.rune_ids
        return ids


class RunePage(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # bool # Indicates if the page is the current page.
        self.current = dictionary.get("current", False)

        # int # Rune page ID.
        self.id = dictionary.get("id", 0)

        # str # Rune page name.
        self.name = dictionary.get("name", "")

        # list<RuneSlot> # Collection of rune slots associated with the rune page.
        self.slots = [(RuneSlot(s) if not isinstance(s, RuneSlot) else s) for s in dictionary.get("slots", []) if s]

    @property
    def rune_ids(self):
        ids = set()
        for s in self.slots:
            if(s.runeId):
                ids = ids.add(s.runeId)
        return ids


class RuneSlot(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Rune ID associated with the rune slot. For static information correlating to rune IDs, please refer to the LoL Static Data API.
        self.runeId = dictionary.get("runeId", 0)

        # int # Rune slot ID.
        self.runeSlotId = dictionary.get("runeSlotId", 0)


class MasteryPages(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # list<MasteryPage> # Collection of mastery pages associated with the summoner.
        self.pages = [(MasteryPage(p) if not isinstance(p, MasteryPage) else p) for p in dictionary.get("pages", []) if p]

        # int # Summoner ID.
        self.summonerId = dictionary.get("summonerId", 0)

    @property
    def mastery_ids(self):
        ids = set()
        for p in self.pages:
            ids = ids | p.mastery_ids
        return ids


class MasteryPage(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # bool # Indicates if the mastery page is the current mastery page.
        self.current = dictionary.get("current", False)

        # int # Mastery page ID.
        self.id = dictionary.get("id", 0)

        # list<MasteryDto> # Collection of masteries associated with the mastery page.
        self.masteries = dictionary.get("masteries", [])

        # str # Mastery page name.
        self.name = dictionary.get("name", "")

    @property
    def mastery_ids(self):
        ids = set()
        for m in self.masteries:
            if(m.id):
                ids.add(m.id)
        return ids


class Mastery(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Mastery ID. For static information correlating to masteries, please refer to the LoL Static Data API.
        self.id = dictionary.get("id", 0)

        # int # Mastery rank (i.e., the number of points put into this mastery).
        self.rank = dictionary.get("rank", 0)


class Summoner(cassiopeia.type.dto.common.CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Summoner ID.
        self.id = dictionary.get("id", 0)

        # str # Summoner name.
        self.name = dictionary.get("name", "")

        # int # ID of the summoner icon associated with the summoner.
        self.profileIconId = dictionary.get("profileIconId", 0)

        # int # Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change
        self.revisionDate = dictionary.get("revisionDate", 0)

        # int # Summoner level associated with the summoner.
        self.summonerLevel = dictionary.get("summonerLevel", 0)