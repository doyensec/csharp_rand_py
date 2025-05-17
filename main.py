

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

    # this is what the seed array will be
    # sa3__1 = (1421239448 + 33173928 * subtraction) % MBIG
    # sa3__2 = (1690538477 + 865455699 * subtraction) % MBIG
    # sa3__3 = (375638254 + 1028859030 * subtraction) % MBIG
    # sa3__4 = (2000099944 + 1284994575 * subtraction) % MBIG
    # sa3__5 = (1824227375 + 500080187 * subtraction) % MBIG
    # sa3__6 = (1827648813 + 1809347561 * subtraction) % MBIG
    # sa3__7 = (1074261432 + 326699238 * subtraction) % MBIG
    # sa3__8 = (756537524 + 416727394 * subtraction) % MBIG
    # sa3__9 = (1452186574 + 127074781 * subtraction) % MBIG
    # sa3_10 = (832354089 + 729461717 * subtraction) % MBIG
    # sa3_11 = (1599697867 + 1666899315 * subtraction) % MBIG
    # sa3_12 = (1840554554 + 2015209127 * subtraction) % MBIG
    # sa3_13 = (1945466017 + 280234821 * subtraction) % MBIG
    # sa3_14 = (26876081 + 1220209853 * subtraction) % MBIG
    # sa3_15 = (1651586209 + 1372849741 * subtraction) % MBIG
    # sa3_16 = (725122553 + 1783379287 * subtraction) % MBIG
    # sa3_17 = (2061339384 + 997579958 * subtraction) % MBIG
    # sa3_18 = (1364770206 + 1717477203 * subtraction) % MBIG
    # sa3_19 = (2021440089 + 1924825977 * subtraction) % MBIG
    # sa3_20 = (1844539912 + 1149294787 * subtraction) % MBIG
    # sa3_21 = (1086044294 + 859749576 * subtraction) % MBIG
    # sa3_22 = (86045080 + 1563220509 * subtraction) % MBIG
    # sa3_23 = (1492869096 + 1253593430 * subtraction) % MBIG
    # sa3_24 = (310631935 + 829551692 * subtraction) % MBIG
    # sa3_25 = (1358980938 + 478857727 * subtraction) % MBIG
    # sa3_26 = (1830701958 + 1321119334 * subtraction) % MBIG
    # sa3_27 = (1847676564 + 1520389438 * subtraction) % MBIG
    # sa3_28 = (723229640 + 837683034 * subtraction) % MBIG
    # sa3_29 = (1075103056 + 333384825 * subtraction) % MBIG
    # sa3_30 = (1660386044 + 1313147514 * subtraction) % MBIG
    # sa3_31 = (1339647823 + 655428663 * subtraction) % MBIG
    # sa3_32 = (2128185620 + 1185029587 * subtraction) % MBIG
    # sa3_33 = (925210790 + 984987374 * subtraction) % MBIG
    # sa3_34 = (376385315 + 358199081 * subtraction) % MBIG
    # sa3_35 = (883014450 + 1343399633 * subtraction) % MBIG
    # sa3_36 = (316400275 + 237354582 * subtraction) % MBIG
    # sa3_37 = (926512878 + 1230420470 * subtraction) % MBIG
    # sa3_38 = (1669922625 + 615900362 * subtraction) % MBIG
    # sa3_39 = (239691816 + 1416192770 * subtraction) % MBIG
    # sa3_40 = (741148003 + 1274658414 * subtraction) % MBIG
    # sa3_41 = (456752873 + 1140428625 * subtraction) % MBIG
    # sa3_42 = (1508977629 + 47771238 * subtraction) % MBIG
    # sa3_43 = (622831658 + 353550263 * subtraction) % MBIG
    # sa3_44 = (586056905 + 182262572 * subtraction) % MBIG
    # sa3_45 = (373796435 + 378698614 * subtraction) % MBIG
    # sa3_46 = (443755075 + 1293975888 * subtraction) % MBIG
    # sa3_47 = (1092806171 + 1457266301 * subtraction) % MBIG
    # sa3_48 = (340054249 + 320476606 * subtraction) % MBIG
    # sa3_49 = (195417944 + 1196203517 * subtraction) % MBIG
    # sa3_50 = (1605856671 + 918147337 * subtraction) % MBIG
    # sa3_51 = (286007796 + 2001937008 * subtraction) % MBIG
    # sa3_52 = (1139606199 + 1047914716 * subtraction) % MBIG
    # sa3_53 = (205103151 + 1689492340 * subtraction) % MBIG
    # sa3_54 = (335250606 + 2003236788 * subtraction) % MBIG
    # sa3_55 = (1960695162 + 1659957022 * subtraction) % MBIG

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

    for seed in range(4096 * 16):
        for i in range(34):
            r = sample_seed(seed, i)
            inv_r = invert_sample(r, i)
            if  inv_r != seed:
                raise Exception("Inversion test failed on seed: %d rand: %d i: %d inv: %d" % (seed, r, i, inv_r))

test_sampel_seed()

