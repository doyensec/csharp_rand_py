

MBIG = 2147483647
# return the ith prng value with seed=seed
# ie sample_seed(42, 2) is like `r = new Random(42); r.Next(); r.Next(); return r.Next()`
def sample_seed(seed, i):
    Int32MinValue = -2147483648
    # same as 5 but last loops unwound
    if seed == Int32MinValue:
        subtraction = MBIG
    else:
        subtraction = abs(seed)

    # first 33 results from the PRNG
    ret_nums = [
      (1121899819, 1559595546),
      (630111683, 1755192844),
      (1501065279, 1649316166),
      (458365203, 1198642031),
      (969558243, 442452829),
      (1876681249, 1200195957),
      (962194431, 1945678308),
      (1077359051, 949569752),
      (265679591, 2099272109),
      (791886952, 587775847),
      (1582116761, 626863973),
      (1676571504, 1003550677),
      (1476289907, 1358625013),
      (1117239683, 1008269081),
      (1503178135, 2109153755),
      (1341148412, 65212616),
      (902714229, 1851925803),
      (1331438416, 2137491580),
      (58133212, 1454235444),
      (831516153, 675580731),
      (285337308, 1754296375),
      (526856546, 1821177336),
      (362935496, 2130093701),
      (750214563, 70062080),
      (210465667, 1503113964),
      (1381224997, 1130186590),
      (1846331200, 2005789796),
      (1330597961, 1476653312),
      (593162892, 1174277203),
      (1729496551, 174182291),
      (792803163, 401846963),
      (565661843, 973512717),
      (863554642, 638171722),
      (53838754, 2122881600),
    ]
    mul, add = ret_nums[i]
    return (add + mul * subtraction) % MBIG

# invert prng, ie: invert_sample(sample_seed(seed, n), n) == x
def invert_sample(rand, i):
    ret_nums = [
        (1796695496, 1821612595),
        (1891800662, 1409645351),
        (1610885040, 587487227),
        (1696684875, 1455237719),
        (2130791390, 767595827),
        (1929834895, 129867698),
        (2121031305, 1742476897),
        (883591791, 2106280948),
        (648963137, 1348178552),
        (795631511, 1633747307),
        (796601229, 1716765365),
        (816410995, 1096882805),
        (1918475170, 1559029571),
        (381881470, 1466324819),
        (641551938, 297465690),
        (316080314, 75192552),
        (270400817, 1823883914),
        (1585239219, 729323790),
        (2120325298, 2118823669),
        (230186630, 726040245),
        (547167837, 1241601023),
        (2138164393, 2086904121),
        (213491428, 315710936),
        (729980750, 468302249),
        (1512126699, 1259943578),
        (1739690517, 1712653821),
        (918222596, 653087170),
        (157253577, 2061948226),
        (970904747, 309988906),
        (1801285644, 1451072879),
        (584087765, 1485089530),
        (1256192415, 888247729),
        (1100808447, 2137905013),
        (1705889883, 643403504),
    ]
    mul, add = ret_nums[i]
    return (add + mul * rand) % MBIG

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

class fakerand:
    sa = {
        0: 42,
        # the zero element is never used?!?!?!
        # it's existence in the array from the original C# is wasted space
        # I include it here none the less, for solidarity
        1:  rand_vec(995627988, 1440537475),
        2:  rand_vec(2027951972, 765327687),
        3:  rand_vec(670659949, 2146736586),
        4:  rand_vec(2089078589, 1117085494),
        5:  rand_vec(262725605, 1507827100),
        6:  rand_vec(578927091, 901135935),
        7:  rand_vec(1858282523, 1551822454),
        8:  rand_vec(1148018271, 516845708),
        9:  rand_vec(999900014, 711038571),
        10: rand_vec(1736516739, 375601216),
        11: rand_vec(1619128077, 90720238),
        12: rand_vec(1661658864, 1217722896),
        13: rand_vec(97972249, 1359409112),
        14: rand_vec(841511239, 1800563293),
        15: rand_vec(78873853, 1207831134),
        16: rand_vec(326112986, 1779800029),
        17: rand_vec(677103352, 1721285135),
        18: rand_vec(521273686, 1169352262),
        19: rand_vec(1006678640, 415583418),
        20: rand_vec(1294841426, 1558532116),
        21: rand_vec(1959318507, 2093921742),
        22: rand_vec(2021211816, 2028425576),
        23: rand_vec(1397840289, 1157618490),
        24: rand_vec(1317078317, 497420420),
        25: rand_vec(1630713386, 2065927110),
        26: rand_vec(1440651009, 1065374271),
        27: rand_vec(849729489, 1848423625),
        28: rand_vec(896088092, 1753627793),
        29: rand_vec(70659220, 1714759603),
        30: rand_vec(734220423, 759250109),
        31: rand_vec(944629787, 1935309016),
        32: rand_vec(37011316, 1611339912),
        33: rand_vec(2132571007, 214172219),
        34: rand_vec(769165989, 784099),
        35: rand_vec(1871755203, 792294212),
        36: rand_vec(723179365, 1246161026),
        37: rand_vec(1132448221, 1714587413),
        38: rand_vec(1921872770, 2016842979),
        39: rand_vec(1337318917, 1179344329),
        40: rand_vec(948545428, 1108831621),
        41: rand_vec(463325273, 882951385),
        42: rand_vec(1673981199, 339625367),
        43: rand_vec(1494355270, 207248240),
        44: rand_vec(1034904793, 1175008436),
        45: rand_vec(566863754, 427358340),
        46: rand_vec(1420247719, 562813146),
        47: rand_vec(59426012, 2082671328),
        48: rand_vec(1150881936, 1990117476),
        49: rand_vec(1712973778, 276974481),
        50: rand_vec(1624979975, 540482400),
        51: rand_vec(1152207519, 585067818),
        52: rand_vec(151826624, 1533462053),
        53: rand_vec(1618833120, 637827195),
        54: rand_vec(1269016365, 1723484144),
        55: rand_vec(715327235, 25386146),
    }

    def sample_equation(self, rand_i: int) -> rand_vec:
        """
        What constants are needed to produce the `i`th PRNG from Random?
        """
        sa_indx = rand_i + 56
        if ret := self.sa.get(sa_indx, None):  # try from cache
            return ret

        a = self.sample_equation(rand_i - 55)
        b = self.sample_equation(rand_i - 34)  # ie: SeedArray[rand_i + 21]
        ret = a - b
        self.sa[sa_indx] = ret  # cache for later
        return ret

    def sample(self, seed, i) -> int:
        return self.sample_equation(i).resolve(seed)

    def inv(self, rand, i) -> int:
        return self.sample_equation(i).invert().resolve(rand)


def sample_all(seed):
    for i in range(34):
        yield sample_seed(seed, i)


def test_sampel_seed():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        for ri, my_r in enumerate(sample_all(seed)):
            r = rands[ri]
            # print("sample(%d) == %d should be %d" % (seed, my_r, r))
            if my_r != r:
                raise Exception("sample_seed test failed on\n    sample(%d)[%d] == %d should be %d" % (seed, ri, my_r, r))

    rc = fakerand()
    for seed in range(4096 * 16):
        for i in range(34):
            r = sample_seed(seed, i)
            inv_r = invert_sample(r, i)
            r2 = rc.sample(seed, i)
            if  inv_r != seed:
                raise Exception("Inversion test failed on seed: %d rand: %d i: %d inv: %d" % (seed, r, i, inv_r))
            elif r2 != r:
                raise Exception("big_sample_seed test failed on seed: %d rand: %d i: %d inv: %d" % (seed, r, i, inv_r))


def test_big_sample():
    import json
    rc = fakerand()
    with open("tests2.json") as fp:
        for test in json.load(fp):
            seed = test["seed"]
            for i, rand in enumerate(test["values"]):
                my_rand = rc.sample(seed, i)
                if my_rand != rand:
                    raise Exception("Missed one: my_rand: %d != %d (seed: %d, i:%d)" % (my_rand, rand, seed, i))
                # print("seed: %d i: %d good" % (seed, i))


# test_sampel_seed()

test_big_sample()
