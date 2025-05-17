
Int32MinValue = -2147483648
Int32MaxValue = 2147483647
MBIG = Int32MaxValue

def sample_seed(seed):
    # same as 5 but last loops unwound
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)

    # this is what the seed array will be
    # sa3__1 = 1421239448 + 33173928 * subtraction
    # sa3__2 = 1690538477 + 865455699 * subtraction
    # sa3__3 = 375638254 + 1028859030 * subtraction
    # sa3__4 = 2000099944 + 1284994575 * subtraction
    # sa3__5 = 1824227375 + 500080187 * subtraction
    # sa3__6 = 1827648813 + 1809347561 * subtraction
    # sa3__7 = 1074261432 + 326699238 * subtraction
    # sa3__8 = 756537524 + 416727394 * subtraction
    # sa3__9 = 1452186574 + 127074781 * subtraction
    # sa3_10 = 832354089 + 729461717 * subtraction
    # sa3_11 = 1599697867 + 1666899315 * subtraction
    # sa3_12 = 1840554554 + 2015209127 * subtraction
    # sa3_13 = 1945466017 + 280234821 * subtraction
    # sa3_14 = 26876081 + 1220209853 * subtraction
    # sa3_15 = 1651586209 + 1372849741 * subtraction
    # sa3_16 = 725122553 + 1783379287 * subtraction
    # sa3_17 = 2061339384 + 997579958 * subtraction
    # sa3_18 = 1364770206 + 1717477203 * subtraction
    # sa3_19 = 2021440089 + 1924825977 * subtraction
    # sa3_20 = 1844539912 + 1149294787 * subtraction
    # sa3_21 = 1086044294 + 859749576 * subtraction
    # sa3_22 = 86045080 + 1563220509 * subtraction
    # sa3_23 = 1492869096 + 1253593430 * subtraction
    # sa3_24 = 310631935 + 829551692 * subtraction
    # sa3_25 = 1358980938 + 478857727 * subtraction
    # sa3_26 = 1830701958 + 1321119334 * subtraction
    # sa3_27 = 1847676564 + 1520389438 * subtraction
    # sa3_28 = 723229640 + 837683034 * subtraction
    # sa3_29 = 1075103056 + 333384825 * subtraction
    # sa3_30 = 1660386044 + 1313147514 * subtraction
    # sa3_31 = 1339647823 + 655428663 * subtraction
    # sa3_32 = 2128185620 + 1185029587 * subtraction
    # sa3_33 = 925210790 + 984987374 * subtraction
    # sa3_34 = 376385315 + 358199081 * subtraction
    # sa3_35 = 883014450 + 1343399633 * subtraction
    # sa3_36 = 316400275 + 237354582 * subtraction
    # sa3_37 = 926512878 + 1230420470 * subtraction
    # sa3_38 = 1669922625 + 615900362 * subtraction
    # sa3_39 = 239691816 + 1416192770 * subtraction
    # sa3_40 = 741148003 + 1274658414 * subtraction
    # sa3_41 = 456752873 + 1140428625 * subtraction
    # sa3_42 = 1508977629 + 47771238 * subtraction
    # sa3_43 = 622831658 + 353550263 * subtraction
    # sa3_44 = 586056905 + 182262572 * subtraction
    # sa3_45 = 373796435 + 378698614 * subtraction
    # sa3_46 = 443755075 + 1293975888 * subtraction
    # sa3_47 = 1092806171 + 1457266301 * subtraction
    # sa3_48 = 340054249 + 320476606 * subtraction
    # sa3_49 = 195417944 + 1196203517 * subtraction
    # sa3_50 = 1605856671 + 918147337 * subtraction
    # sa3_51 = 286007796 + 2001937008 * subtraction
    # sa3_52 = 1139606199 + 1047914716 * subtraction
    # sa3_53 = 205103151 + 1689492340 * subtraction
    # sa3_54 = 335250606 + 2003236788 * subtraction
    # sa3_55 = 1960695162 + 1659957022 * subtraction

    # first 33 results from the PRNG
    ret_0 = (1559595546 + 1121899819 * subtraction) % MBIG
    ret_1 = (1755192844 + 630111683  * subtraction) % MBIG
    ret_2 = (1649316166 + 1501065279 * subtraction) % MBIG
    ret_3 = (1198642031 + 458365203  * subtraction) % MBIG
    ret_4 = (442452829  + 969558243  * subtraction) % MBIG
    ret_5 = (1200195957 + 1876681249 * subtraction) % MBIG
    ret_6 = (1945678308 + 962194431  * subtraction) % MBIG
    ret_7 = (949569752  + 1077359051 * subtraction) % MBIG
    ret_8 = (2099272109 + 265679591  * subtraction) % MBIG
    ret_9 = (587775847  + 791886952  * subtraction) % MBIG
    ret10 = (626863973  + 1582116761 * subtraction) % MBIG
    ret11 = (1003550677 + 1676571504 * subtraction) % MBIG
    ret12 = (1358625013 + 1476289907 * subtraction) % MBIG
    ret13 = (1008269081 + 1117239683 * subtraction) % MBIG
    ret14 = (2109153755 + 1503178135 * subtraction) % MBIG
    ret15 = (65212616   + 1341148412 * subtraction) % MBIG
    ret16 = (1851925803 + 902714229  * subtraction) % MBIG
    ret17 = (2137491580 + 1331438416 * subtraction) % MBIG
    ret18 = (1454235444 + 58133212   * subtraction) % MBIG
    ret19 = (675580731  + 831516153  * subtraction) % MBIG
    ret20 = (1754296375 + 285337308  * subtraction) % MBIG
    ret21 = (1821177336 + 526856546  * subtraction) % MBIG
    ret22 = (2130093701 + 362935496  * subtraction) % MBIG
    ret23 = (70062080   + 750214563  * subtraction) % MBIG
    ret24 = (1503113964 + 210465667  * subtraction) % MBIG
    ret25 = (1130186590 + 1381224997 * subtraction) % MBIG
    ret26 = (2005789796 + 1846331200 * subtraction) % MBIG
    ret27 = (1476653312 + 1330597961 * subtraction) % MBIG
    ret28 = (1174277203 + 593162892  * subtraction) % MBIG
    ret29 = (174182291  + 1729496551 * subtraction) % MBIG
    ret30 = (401846963  + 792803163  * subtraction) % MBIG
    ret31 = (973512717  + 565661843  * subtraction) % MBIG
    ret32 = (638171722  + 863554642  * subtraction) % MBIG
    ret33 = (2122881600 + 53838754   * subtraction) % MBIG

    return [ret_0, ret_1, ret_2, ret_3, ret_4, ret_5, ret_6, ret_7, ret_8,
            ret_9, ret10, ret11, ret12, ret13, ret14, ret15, ret16, ret17,
            ret18, ret19, ret20, ret21, ret22, ret23, ret24, ret25, ret26,
            ret27, ret28, ret29, ret30, ret31, ret32, ret33]

def test_sampel_seed():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        my_rands = sample_seed(seed)
        for ri, my_r in enumerate(my_rands):
            r = rands[ri]
            # print("sample(%d) == %d should be %d" % (seed, my_r, r))
            if my_r != r:
                raise Exception("sample_seed test failed on\n    sample(%d)[%d] == %d should be %d" % (seed, ri, my_r, r))

test_sampel_seed()
