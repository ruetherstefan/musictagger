class Tags:

    rawstyle = False
    euphoric = False
    fairy = False
    karneval = False
    top18 = False
    klassik = False
    verschwoerung = False
    intro = False

    hardcore = False
    happyhardcore = False
    house = False
    hardtechno = False

    #rock, pop, rap

    def set(self, key, value):
        setattr(self, key, value)

    def create_id3(self):
        id3 = ""

        if self.rawstyle:
            id3 += "#rawstyle"
        if self.euphoric:
            id3 += "#euphoric"
        if self.fairy:
            id3 += "#fairy"
        if self.karneval:
            id3 += "#karneval"
        if self.top18:
            id3 += "#top18"
        if self.klassik:
            id3 += "#klassik"
        if self.verschwoerung:
            id3 += "#verschwoerung"
        if self.intro:
            id3 += "#intro"
        if self.hardcore:
            id3 += "#hardcore"
        if self.happyhardcore:
            id3 += "#happyhardcore"
        if self.house:
            id3 += "#house"
        if self.hardtechno:
            id3 += "#hardtechno"

        return id3
