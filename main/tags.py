class Tags:

    rawstyle = False
    euphoric = False
    fairy = False
    karneval = False
    top18 = False
    klassik = False
    hardcore = False
    verschwoerung = False

    def set(self, key, value):
        setattr(self, key, value)
