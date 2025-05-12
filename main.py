
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

    sa1__1 = ((10946 + 2147476882*mj)  - (2147483503 + 89*mj)) % MBIG
    sa1__2 = ((1879569351 + 165580141*mj)  - (3524578 + 2145305338*mj)) % MBIG
    sa1__3 = ((2147483626 + 13*mj)  - (1779258255 + 1776683645*mj)) % MBIG
    sa1__4 = ((514229 + 2147165836*mj)  - (2147476882 + 4181*mj)) % MBIG
    sa1__5 = ((298632857 + 1336291108*mj)  - (165580141 + 2045149492*mj)) % MBIG
    sa1__6 = ((2147482660 + 610*mj)  - (13 + 2147483639*mj)) % MBIG
    sa1__7 = ((24157817 + 2132553295*mj)  - (2147165836 + 196418*mj)) % MBIG
    sa1__8 = ((1 - (mj - 1))  - (1336291108 + 1634923965*mj)) % MBIG
    sa1__9 = ((2147437279 + 28657*mj)  - (610 + 2147483270*mj)) % MBIG
    sa1_10 = ((1134903170 + 1446074914*mj) - (2132553295 + 9227465*mj)) % MBIG
    sa1_11 = ((89 + 2147483592*mj) - (mj - 1)) % MBIG
    sa1_12 = ((2145305338 + 1346269*mj) - (28657 + 2147465936*mj)) % MBIG
    sa1_13 = ((1776683645 + 1408458253*mj) - (1446074914 + 433494437*mj)) % MBIG
    sa1_14 = ((4181 + 2147481063*mj) - (2147483592 + 34*mj)) % MBIG
    sa1_15 = ((2045149492 + 63245986*mj) - (1346269 + 2146651607*mj)) % MBIG
    sa1_16 = ((2147483639 + 5*mj) - (1408458253 + 1037658251*mj)) % MBIG
    sa1_17 = ((196418 + 2147362254*mj) - (2147481063 + 1597*mj)) % MBIG
    sa1_18 = ((1634923965 + 823731426*mj) - (63245986 + 2108395478*mj)) % MBIG
    sa1_19 = ((2147483270 + 233*mj) - (5 - 3*mj)) % MBIG
    sa1_20 = ((9227465 + 2141780760*mj) - (2147362254 + 75025*mj)) % MBIG
    sa1_21 = (1 - (823731426 + 311171744*mj)) % MBIG
    sa1_22 = ((2147465936 + 10946*mj) - (233 + 2147483503*mj)) % MBIG
    sa1_23 = ((433494437 + 1879569351*mj) - (2141780760 + 3524578*mj)) % MBIG
    sa1_24 = ((34 + 2147483626*mj) - mj) % MBIG
    sa1_25 = ((2146651607 + 514229*mj) - sa1__1) % MBIG
    sa1_26 = ((1037658251 + 298632857*mj) - sa1__2) % MBIG
    sa1_27 = ((1597 + 2147482660*mj) - sa1__3) % MBIG
    sa1_28 = ((2108395478 + 24157817*mj) - sa1__4) % MBIG
    sa1_29 = ((2*mj - 3) - sa1__5) % MBIG
    sa1_30 = ((75025 + 2147437279*mj) - sa1__6) % MBIG
    sa1_31 = ((311171744 + 1134903170*mj) - sa1__7) % MBIG
    sa1_32 = ((2147483503 + 89*mj) - sa1__8) % MBIG
    sa1_33 = ((3524578 + 2145305338*mj) - sa1__9) % MBIG
    sa1_34 = ((1779258255 + 1776683645*mj) - sa1_10) % MBIG
    sa1_35 = ((2147476882 + 4181*mj) - sa1_11) % MBIG
    sa1_36 = ((165580141 + 2045149492*mj) - sa1_12) % MBIG
    sa1_37 = ((13 + 2147483639*mj) - sa1_13) % MBIG
    sa1_38 = ((2147165836 + 196418*mj) - sa1_14) % MBIG
    sa1_39 = ((1336291108 + 1634923965*mj) - sa1_15) % MBIG
    sa1_40 = ((610 + 2147483270*mj) - sa1_16) % MBIG
    sa1_41 = ((2132553295 + 9227465*mj) - sa1_17) % MBIG
    sa1_42 = ((mj - 1) - sa1_18) % MBIG
    sa1_43 = ((28657 + 2147465936*mj) - sa1_19) % MBIG
    sa1_44 = ((1446074914 + 433494437*mj) - sa1_20) % MBIG
    sa1_45 = ((2147483592 + 34*mj) - sa1_21) % MBIG
    sa1_46 = ((1346269 + 2146651607*mj) - sa1_22) % MBIG
    sa1_47 = ((1408458253 + 1037658251*mj) - sa1_23) % MBIG
    sa1_48 = ((2147481063 + 1597*mj) - sa1_24) % MBIG
    sa1_49 = ((63245986 + 2108395478*mj) - sa1_25) % MBIG
    sa1_50 = ((5 - 3*mj) - sa1_26) % MBIG
    sa1_51 = ((2147362254 + 75025*mj) - sa1_27) % MBIG
    sa1_52 = ((823731426 + 311171744*mj) - sa1_28) % MBIG
    sa1_53 = ((233 + 2147483503*mj) - sa1_29) % MBIG
    sa1_54 = ((2141780760 + 3524578*mj) - sa1_30) % MBIG
    sa1_55 = (mj - sa1_31) % MBIG

    sa2__1 = (sa1__1 - sa1_32) % MBIG
    sa2__2 = (sa1__2 - sa1_33) % MBIG
    sa2__3 = (sa1__3 - sa1_34) % MBIG
    sa2__4 = (sa1__4 - sa1_35) % MBIG
    sa2__5 = (sa1__5 - sa1_36) % MBIG
    sa2__6 = (sa1__6 - sa1_37) % MBIG
    sa2__7 = (sa1__7 - sa1_38) % MBIG
    sa2__8 = (sa1__8 - sa1_39) % MBIG
    sa2__9 = (sa1__9 - sa1_40) % MBIG
    sa2_10 = (sa1_10 - sa1_41) % MBIG
    sa2_11 = (sa1_11 - sa1_42) % MBIG
    sa2_12 = (sa1_12 - sa1_43) % MBIG
    sa2_13 = (sa1_13 - sa1_44) % MBIG
    sa2_14 = (sa1_14 - sa1_45) % MBIG
    sa2_15 = (sa1_15 - sa1_46) % MBIG
    sa2_16 = (sa1_16 - sa1_47) % MBIG
    sa2_17 = (sa1_17 - sa1_48) % MBIG
    sa2_18 = (sa1_18 - sa1_49) % MBIG
    sa2_19 = (sa1_19 - sa1_50) % MBIG
    sa2_20 = (sa1_20 - sa1_51) % MBIG
    sa2_21 = (sa1_21 - sa1_52) % MBIG
    sa2_22 = (sa1_22 - sa1_53) % MBIG
    sa2_23 = (sa1_23 - sa1_54) % MBIG
    sa2_24 = (sa1_24 - sa1_55) % MBIG
    sa2_25 = (sa1_25 - sa2__1) % MBIG
    sa2_26 = (sa1_26 - sa2__2) % MBIG
    sa2_27 = (sa1_27 - sa2__3) % MBIG
    sa2_28 = (sa1_28 - sa2__4) % MBIG
    sa2_29 = (sa1_29 - sa2__5) % MBIG
    sa2_30 = (sa1_30 - sa2__6) % MBIG
    sa2_31 = (sa1_31 - sa2__7) % MBIG
    sa2_32 = (sa1_32 - sa2__8) % MBIG
    sa2_33 = (sa1_33 - sa2__9) % MBIG
    sa2_34 = (sa1_34 - sa2_10) % MBIG
    sa2_35 = (sa1_35 - sa2_11) % MBIG
    sa2_36 = (sa1_36 - sa2_12) % MBIG
    sa2_37 = (sa1_37 - sa2_13) % MBIG
    sa2_38 = (sa1_38 - sa2_14) % MBIG
    sa2_39 = (sa1_39 - sa2_15) % MBIG
    sa2_40 = (sa1_40 - sa2_16) % MBIG
    sa2_41 = (sa1_41 - sa2_17) % MBIG
    sa2_42 = (sa1_42 - sa2_18) % MBIG
    sa2_43 = (sa1_43 - sa2_19) % MBIG
    sa2_44 = (sa1_44 - sa2_20) % MBIG
    sa2_45 = (sa1_45 - sa2_21) % MBIG
    sa2_46 = (sa1_46 - sa2_22) % MBIG
    sa2_47 = (sa1_47 - sa2_23) % MBIG
    sa2_48 = (sa1_48 - sa2_24) % MBIG
    sa2_49 = (sa1_49 - sa2_25) % MBIG
    sa2_50 = (sa1_50 - sa2_26) % MBIG
    sa2_51 = (sa1_51 - sa2_27) % MBIG
    sa2_52 = (sa1_52 - sa2_28) % MBIG
    sa2_53 = (sa1_53 - sa2_29) % MBIG
    sa2_54 = (sa1_54 - sa2_30) % MBIG
    sa2_55 = (sa1_55 - sa2_31) % MBIG

    sa3__1 = (sa2__1 - sa2_32) % MBIG
    sa3__2 = (sa2__2 - sa2_33) % MBIG
    sa3__3 = (sa2__3 - sa2_34) % MBIG
    sa3__4 = (sa2__4 - sa2_35) % MBIG
    sa3__5 = (sa2__5 - sa2_36) % MBIG
    sa3__6 = (sa2__6 - sa2_37) % MBIG
    sa3__7 = (sa2__7 - sa2_38) % MBIG
    sa3__8 = (sa2__8 - sa2_39) % MBIG
    sa3__9 = (sa2__9 - sa2_40) % MBIG
    sa3_10 = (sa2_10 - sa2_41) % MBIG
    sa3_11 = (sa2_11 - sa2_42) % MBIG
    sa3_12 = (sa2_12 - sa2_43) % MBIG
    sa3_13 = (sa2_13 - sa2_44) % MBIG
    sa3_14 = (sa2_14 - sa2_45) % MBIG
    sa3_15 = (sa2_15 - sa2_46) % MBIG
    sa3_16 = (sa2_16 - sa2_47) % MBIG
    sa3_17 = (sa2_17 - sa2_48) % MBIG
    sa3_18 = (sa2_18 - sa2_49) % MBIG
    sa3_19 = (sa2_19 - sa2_50) % MBIG
    sa3_20 = (sa2_20 - sa2_51) % MBIG
    sa3_21 = (sa2_21 - sa2_52) % MBIG
    sa3_22 = (sa2_22 - sa2_53) % MBIG
    sa3_23 = (sa2_23 - sa2_54) % MBIG
    sa3_24 = (sa2_24 - sa2_55) % MBIG
    sa3_25 = (sa2_25 - sa3__1) % MBIG
    sa3_26 = (sa2_26 - sa3__2) % MBIG
    sa3_27 = (sa2_27 - sa3__3) % MBIG
    sa3_28 = (sa2_28 - sa3__4) % MBIG
    sa3_29 = (sa2_29 - sa3__5) % MBIG
    sa3_30 = (sa2_30 - sa3__6) % MBIG
    sa3_31 = (sa2_31 - sa3__7) % MBIG
    sa3_32 = (sa2_32 - sa3__8) % MBIG
    sa3_33 = (sa2_33 - sa3__9) % MBIG
    sa3_34 = (sa2_34 - sa3_10) % MBIG
    sa3_35 = (sa2_35 - sa3_11) % MBIG
    sa3_36 = (sa2_36 - sa3_12) % MBIG
    sa3_37 = (sa2_37 - sa3_13) % MBIG
    sa3_38 = (sa2_38 - sa3_14) % MBIG
    sa3_39 = (sa2_39 - sa3_15) % MBIG
    sa3_40 = (sa2_40 - sa3_16) % MBIG
    sa3_41 = (sa2_41 - sa3_17) % MBIG
    sa3_42 = (sa2_42 - sa3_18) % MBIG
    sa3_43 = (sa2_43 - sa3_19) % MBIG
    sa3_44 = (sa2_44 - sa3_20) % MBIG
    sa3_45 = (sa2_45 - sa3_21) % MBIG
    sa3_46 = (sa2_46 - sa3_22) % MBIG
    sa3_47 = (sa2_47 - sa3_23) % MBIG
    sa3_48 = (sa2_48 - sa3_24) % MBIG
    sa3_49 = (sa2_49 - sa3_25) % MBIG
    sa3_50 = (sa2_50 - sa3_26) % MBIG
    sa3_51 = (sa2_51 - sa3_27) % MBIG
    sa3_52 = (sa2_52 - sa3_28) % MBIG
    sa3_53 = (sa2_53 - sa3_29) % MBIG
    sa3_54 = (sa2_54 - sa3_30) % MBIG
    sa3_55 = (sa2_55 - sa3_31) % MBIG


    """
    SAMPLE Section
    """
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
