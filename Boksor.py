class Boksor:
    def __init__(self, ad, guc, saglik, siklet, kacinmaOrani):
        self.ad = ad
        self.guc = guc
        self.saglik = saglik
        self.siklet = siklet
        self.kacinmaOrani = kacinmaOrani

    def hit(self, rakip):
        print("------------")
        print(self.ad, "=>", rakip.ad, self.guc, "hasar vurdu.")
        if self.kacinma():
            print(rakip.ad, "gelen hasarı savurdu.")
            return rakip.saglik
        if rakip.saglik - self.guc < 0:
            return 0
        return rakip.saglik - self.guc

    def kacinma(self):
        import random
        rastgeleDeger = random.random() * 100  # 0.0 to 99.9
        return rastgeleDeger <= self.kacinmaOrani
