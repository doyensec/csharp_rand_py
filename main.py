

class rand_vec:
    p = 2147483647
    def __init__(self, mul, add):
        self.mul = mul % self.p # multiplicitive componenet
        self.add = add % self.p  # additive component

    def __add__(self, other):
        return rand_vec(self.mul + other.mul, self.add + other.add)

    def __sub__(self, other):
        return rand_vec(self.mul - other.mul, self.add - other.add)

    def resolve(self, seed) -> int:
        return (self.mul * seed + self.add) % self.p

    def __str__(self):
        return f"seed * {self.mul} + {self.add}"

    def invert(self):
        inv_mul = pow(self.mul, self.p - 2, self.p)
        inv_add = (-1 * self.add * inv_mul) % self.p
        return rand_vec(inv_mul, inv_add)

    def __call__(self, vec):
        mul = self.mul * vec.mul
        add = self.mul * vec.add + self.add
        return rand_vec(mul, add)

class csharp_rand:
    sa = {
        -55:  rand_vec(995627988, 1440537475),
        -54:  rand_vec(2027951972, 765327687),
        -53:  rand_vec(670659949, 2146736586),
        -52:  rand_vec(2089078589, 1117085494),
        -51:  rand_vec(262725605, 1507827100),
        -50:  rand_vec(578927091, 901135935),
        -49:  rand_vec(1858282523, 1551822454),
        -48:  rand_vec(1148018271, 516845708),
        -47:  rand_vec(999900014, 711038571),
        -46: rand_vec(1736516739, 375601216),
        -45: rand_vec(1619128077, 90720238),
        -44: rand_vec(1661658864, 1217722896),
        -43: rand_vec(97972249, 1359409112),
        -42: rand_vec(841511239, 1800563293),
        -41: rand_vec(78873853, 1207831134),
        -40: rand_vec(326112986, 1779800029),
        -39: rand_vec(677103352, 1721285135),
        -38: rand_vec(521273686, 1169352262),
        -37: rand_vec(1006678640, 415583418),
        -36: rand_vec(1294841426, 1558532116),
        -35: rand_vec(1959318507, 2093921742),
        -34: rand_vec(2021211816, 2028425576),
        -33: rand_vec(1397840289, 1157618490),
        -32: rand_vec(1317078317, 497420420),
        -31: rand_vec(1630713386, 2065927110),
        -30: rand_vec(1440651009, 1065374271),
        -29: rand_vec(849729489, 1848423625),
        -28: rand_vec(896088092, 1753627793),
        -27: rand_vec(70659220, 1714759603),
        -26: rand_vec(734220423, 759250109),
        -25: rand_vec(944629787, 1935309016),
        -24: rand_vec(37011316, 1611339912),
        -23: rand_vec(2132571007, 214172219),
        -22: rand_vec(769165989, 784099),
        -21: rand_vec(1871755203, 792294212),
        -20: rand_vec(723179365, 1246161026),
        -19: rand_vec(1132448221, 1714587413),
        -18: rand_vec(1921872770, 2016842979),
        -17: rand_vec(1337318917, 1179344329),
        -16: rand_vec(948545428, 1108831621),
        -15: rand_vec(463325273, 882951385),
        -14: rand_vec(1673981199, 339625367),
        -13: rand_vec(1494355270, 207248240),
        -12: rand_vec(1034904793, 1175008436),
        -11: rand_vec(566863754, 427358340),
        -10: rand_vec(1420247719, 562813146),
        -9: rand_vec(59426012, 2082671328),
        -8: rand_vec(1150881936, 1990117476),
        -7: rand_vec(1712973778, 276974481),
        -6: rand_vec(1624979975, 540482400),
        -5: rand_vec(1152207519, 585067818),
        -4: rand_vec(151826624, 1533462053),
        -3: rand_vec(1618833120, 637827195),
        -2: rand_vec(1269016365, 1723484144),
        -1: rand_vec(715327235, 25386146),
    }

    def sample_equation(self, rand_i: int) -> rand_vec:
        """
        What constants are needed to produce the `i`th PRNG from Random?
        """
        if ret := self.sa.get(rand_i, None):  # try from cache
            return ret

        a = self.sample_equation(rand_i - 55)
        b = self.sample_equation(rand_i - 34)  # ie: SeedArray[rand_i + 21]
        ret = a - b
        if rand_i > 0:
            self.sa[rand_i] = ret  # cache for later
        return ret

    def sample(self, seed, i) -> int:
        return self.sample_equation(i).resolve(seed)

    def inv(self, rand, i) -> int:
        return self.sample_equation(i).invert().resolve(rand)


def test_rand():
    import json
    rc = csharp_rand()
    with open("tests.json") as fp:
        for test in json.load(fp):
            seed = test["seed"]

            z = rc.sample_equation(0)           # returns zero element given seed
            f = rc.sample_equation(5).invert()  # given 5th element, returns seed
            five_to_zero = z(f)                 # given 5th element returns 0th element
            for i, rand in enumerate(test["values"]):
                my_rand = rc.sample(seed, i)
                if my_rand != rand:
                    raise Exception("Missed one: my_rand: %d != %d (seed: %d, i:%d)" % (my_rand, rand, seed, i))
                if seed != rc.inv(my_rand, i):
                    raise Exception("Inversion failed: my_rand: %d != %d (seed: %d, i:%d)" % (my_rand, rand, seed, i))

                if i == 5: # got the 5th output
                    zero = five_to_zero.resolve(rand)  # obtain the 0th aoutput
                    t = test["values"][0]
                    if zero != t:
                        raise Exception(f"Failed to get item 0 from 5 using inversoin + composition of functions\n\tseed: {seed}, rand[5]: {rand}, rand[0]: {t} myzero: {zero}")

test_rand()
