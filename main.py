
MSEED = 161803398
Int32MinValue = -2147483648
Int32MaxValue = 2147483647
MBIG = Int32MaxValue

def sample_seed(seed):
    # same as 5 but last loops unwound
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)
    mj = MSEED - subtraction

    sa3__1 = (993617469 + 2114309719 * mj)
    sa3__2 = (460395812 + 1282027948 * mj)
    sa3__3 = (274338781 + 1118624617 * mj)
    sa3__4 = (1572212774 + 862489072 * mj)
    sa3__5 = (1942726144 + 1647403460 * mj)
    sa3__6 = (1702582758 + 338136086 * mj)
    sa3__7 = (1348876235 + 1820784409 * mj)
    sa3__8 = (2121172134 + 1730756253 * mj)
    sa3__9 = (1247767031 + 2020408866 * mj)
    sa3_10 = (1180293850 + 1418021930 * mj)
    sa3_11 = (355977619 + 480584332 * mj)
    sa3_12 = (1306831694 + 132274520 * mj)
    sa3_13 = (1393370390 + 1867248826 * mj)
    sa3_14 = (960436776 + 927273794 * mj)
    sa3_15 = (1908003901 + 774633906 * mj)
    sa3_16 = (1392963411 + 364104360 * mj)
    sa3_17 = (286900388 + 1149903689 * mj)
    sa3_18 = (631452842 + 430006444 * mj)
    sa3_19 = (2054817766 + 222657670 * mj)
    sa3_20 = (1313603331 + 998188860 * mj)
    sa3_21 = (1704417679 + 1287734071 * mj)
    sa3_22 = (1783041471 + 584263138 * mj)
    sa3_23 = (120223455 + 893890217 * mj)
    sa3_24 = (835290707 + 1317931955 * mj)
    sa3_25 = (341819273 + 1668625920 * mj)
    sa3_26 = (1123711743 + 826364313 * mj)
    sa3_27 = (1766120454 + 627094209 * mj)
    sa3_28 = (535133861 + 1309800613 * mj)
    sa3_29 = (106439175 + 1814098822 * mj)
    sa3_30 = (114369196 + 834336133 * mj)
    sa3_31 = (1060505853 + 1492054984 * mj)
    sa3_32 = (1991381466 + 962454060 * mj)
    sa3_33 = (164310374 + 1162496273 * mj)
    sa3_34 = (431651654 + 1789284566 * mj)
    sa3_35 = (219821103 + 804084014 * mj)
    sa3_36 = (1010675065 + 1910129065 * mj)
    sa3_37 = (1529621864 + 917063177 * mj)
    sa3_38 = (2010451958 + 1531583285 * mj)
    sa3_39 = (1784495915 + 731290877 * mj)
    sa3_40 = (245731003 + 872825233 * mj)
    sa3_41 = (1845252285 + 1007055022 * mj)
    sa3_42 = (584247609 + 2099712409 * mj)
    sa3_43 = (931081829 + 1793933384 * mj)
    sa3_44 = (481876248 + 1965221075 * mj)
    sa3_45 = (806385705 + 1768785033 * mj)
    sa3_46 = (498877285 + 853507759 * mj)
    sa3_47 = (404061238 + 690217346 * mj)
    sa3_48 = (1025494172 + 1827007041 * mj)
    sa3_49 = (534316748 + 951280130 * mj)
    sa3_50 = (278050876 + 1229336310 * mj)
    sa3_51 = (856489986 + 145546639 * mj)
    sa3_52 = (368343740 + 1099568931 * mj)
    sa3_53 = (124932105 + 457991307 * mj)
    sa3_54 = (210383585 + 144246859 * mj)
    sa3_55 = (538383237 + 487526625 * mj)
    ret_0 = ((sa3__1 - sa3_32) - (sa3_22 - sa3_53)) % MBIG
    ret_1 = ((sa3__2 - sa3_33) - (sa3_23 - sa3_54)) % MBIG
    ret_2 = ((sa3__3 - sa3_34) - (sa3_24 - sa3_55)) % MBIG
    ret_3 = ((sa3__4 - sa3_35) - (sa3_25 - (sa3__1 - sa3_32))) % MBIG
    ret_4 = ((sa3__5 - sa3_36) - (sa3_26 - (sa3__2 - sa3_33))) % MBIG
    ret_5 = ((sa3__6 - sa3_37) - (sa3_27 - (sa3__3 - sa3_34))) % MBIG
    ret_6 = ((sa3__7 - sa3_38) - (sa3_28 - (sa3__4 - sa3_35))) % MBIG
    ret_7 = ((sa3__8 - sa3_39) - (sa3_29 - (sa3__5 - sa3_36))) % MBIG
    ret_8 = ((sa3__9 - sa3_40) - (sa3_30 - (sa3__6 - sa3_37))) % MBIG
    ret_9 = ((sa3_10 - sa3_41) - (sa3_31 - (sa3__7 - sa3_38))) % MBIG
    ret10 = ((sa3_11 - sa3_42) - (sa3_32 - (sa3__8 - sa3_39))) % MBIG
    ret11 = ((sa3_12 - sa3_43) - (sa3_33 - (sa3__9 - sa3_40))) % MBIG
    ret12 = ((sa3_13 - sa3_44) - (sa3_34 - (sa3_10 - sa3_41))) % MBIG
    ret13 = ((sa3_14 - sa3_45) - (sa3_35 - (sa3_11 - sa3_42))) % MBIG
    ret14 = ((sa3_15 - sa3_46) - (sa3_36 - (sa3_12 - sa3_43))) % MBIG
    ret15 = ((sa3_16 - sa3_47) - (sa3_37 - (sa3_13 - sa3_44))) % MBIG
    ret16 = ((sa3_17 - sa3_48) - (sa3_38 - (sa3_14 - sa3_45))) % MBIG
    ret17 = ((sa3_18 - sa3_49) - (sa3_39 - (sa3_15 - sa3_46))) % MBIG
    ret18 = ((sa3_19 - sa3_50) - (sa3_40 - (sa3_16 - sa3_47))) % MBIG
    ret19 = ((sa3_20 - sa3_51) - (sa3_41 - (sa3_17 - sa3_48))) % MBIG
    ret20 = ((sa3_21 - sa3_52) - (sa3_42 - (sa3_18 - sa3_49))) % MBIG
    ret21 = ((sa3_22 - sa3_53) - (sa3_43 - (sa3_19 - sa3_50))) % MBIG
    ret22 = ((sa3_23 - sa3_54) - (sa3_44 - (sa3_20 - sa3_51))) % MBIG
    ret23 = ((sa3_24 - sa3_55) - (sa3_45 - (sa3_21 - sa3_52))) % MBIG
    ret24 = ((sa3_25 - (sa3__1 - sa3_32)) - (sa3_46 - (sa3_22 - sa3_53))) % MBIG
    ret25 = ((sa3_26 - (sa3__2 - sa3_33)) - (sa3_47 - (sa3_23 - sa3_54))) % MBIG
    ret26 = ((sa3_27 - (sa3__3 - sa3_34)) - (sa3_48 - (sa3_24 - sa3_55))) % MBIG
    ret27 = ((sa3_28 - (sa3__4 - sa3_35)) - (sa3_49 - (sa3_25 - (sa3__1 - sa3_32)))) % MBIG
    ret28 = ((sa3_29 - (sa3__5 - sa3_36)) - (sa3_50 - (sa3_26 - (sa3__2 - sa3_33)))) % MBIG
    ret29 = ((sa3_30 - (sa3__6 - sa3_37)) - (sa3_51 - (sa3_27 - (sa3__3 - sa3_34)))) % MBIG
    ret30 = ((sa3_31 - (sa3__7 - sa3_38)) - (sa3_52 - (sa3_28 - (sa3__4 - sa3_35)))) % MBIG
    ret31 = ((sa3_32 - (sa3__8 - sa3_39)) - (sa3_53 - (sa3_29 - (sa3__5 - sa3_36)))) % MBIG
    ret32 = ((sa3_33 - (sa3__9 - sa3_40)) - (sa3_54 - (sa3_30 - (sa3__6 - sa3_37)))) % MBIG
    ret33 = ((sa3_34 - (sa3_10 - sa3_41)) - (sa3_55 - (sa3_31 - (sa3__7 - sa3_38)))) % MBIG

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
