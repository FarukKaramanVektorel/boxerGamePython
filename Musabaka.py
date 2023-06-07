class Musabaka:
    def __init__(self, boksor1, boksor2, minSiklet, maxSiklet):
        self.boksor1 = boksor1
        self.boksor2 = boksor2
        self.minSiklet = minSiklet
        self.maxSiklet = maxSiklet

    def roundBasla(self):
        raund = 1
        if self.sikletKontrolEt():
            while self.boksor1.saglik > 0 and self.boksor2.saglik > 0:
                if self.roundKontrol(raund):
                    break
                print("======== " + str(raund) + ". ROUND ===========")
                self.boksor2.saglik = self.boksor1.hit(self.boksor2)
                if self.kazanan():
                    break
                self.boksor1.saglik = self.boksor2.hit(self.boksor1)
                if self.kazanan():
                    break
                self.spiker()
                raund += 1

        else:
            print("Sporcuların ağırlıkları uyuşmuyor.")

    def sikletKontrolEt(self):
        return (self.boksor1.siklet >= self.minSiklet and self.boksor1.siklet <= self.maxSiklet) and (self.boksor2.siklet >= self.minSiklet and self.boksor2.siklet <= self.maxSiklet)

    def kazanan(self):
        if self.boksor1.saglik == 0:
            print("Maçı Kazanan: " + self.boksor2.ad)
            return True
        elif self.boksor2.saglik == 0:
            print("Maçı Kazanan: " + self.boksor1.ad)
            return True
        return False

    def roundKontrol(self, raund):
        if raund == 6:
            print("Toplamda oynanan round: " + str(raund))
            if self.boksor1.saglik < self.boksor2.saglik:
                print("Maçı Kazanan: " + self.boksor2.ad)
                return True
            elif self.boksor2.saglik < self.boksor1.saglik:
                print("Maçı Kazanan: " + self.boksor1.ad)
                return True
            else:
                print("Maç Berabere Bitti")
                return True

        return False

    def spiker(self):
        print("------------")
        print(self.boksor1.ad + " Kalan Can\t:" + str(self.boksor1.saglik))
        print(self.boksor2.ad + " Kalan Can\t:" + str(self.boksor2.saglik))
