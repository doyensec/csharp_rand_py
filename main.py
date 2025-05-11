
MSEED = 161803398
Int32MinValue = -2147483648
Int32MaxValue = 2147483647
MBIG = Int32MaxValue


def sampel_seed_1(seed):
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)
    mj = MSEED - subtraction
    SeedArray = [0 for i in range(56)]
    SeedArray[55] = mj
    mk = 1

    for i in range(1, 55):
        ii = (21 * i) % 55
        SeedArray[ii] = mk
        mk = mj - mk
        if mk < 0:
            mk += MBIG
        mj = SeedArray[ii]

    for k in range(1, 5):
        for i in range(1, 56):
            m = 1 + (i + 30) % 55
            SeedArray[i] -= SeedArray[m]
            if SeedArray[i] < 0:
                SeedArray[i] += MBIG
    inext = 0
    inextp = 21
    Seed = 1

    locINext = inext + 1
    locINextp = inextp + 1

    if locINext >= 56:
        locINext = 1

    if locINextp >= 56:
        locINextp = 1

    retVal = SeedArray[locINext]-SeedArray[locINextp]

    if retVal == MBIG:
        retVal -= 1

    if retVal < 0:
        retVal += MBIG

    SeedArray[locINext] = retVal

    inext = locINext
    inextp = locINextp
    return retVal

def test_sampel_seed_1():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        r = rands[0]
        my_r = sampel_seed_1(seed)
        # print("sample(%d) == %d should be %d" % (seed, my_r, r))
        if my_r != r:
            raise Exception("sample_seed_1 test failed on\n    sample(%d) == %d should be %d" % (seed, my_r, r))


def sampel_seed_2(seed):
    # same as 1 but returns array
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)
    mj = MSEED - subtraction
    SeedArray = [0 for i in range(56)]
    SeedArray[55] = mj
    mk = 1

    for i in range(1, 55):
        ii = (21 * i) % 55
        SeedArray[ii] = mk
        mk = mj - mk
        if mk < 0:
            mk += MBIG
        mj = SeedArray[ii]

    for k in range(1, 5):
        for i in range(1, 56):
            m = 1 + (i + 30) % 55
            SeedArray[i] -= SeedArray[m]
            if SeedArray[i] < 0:
                SeedArray[i] += MBIG
    inext = 0
    inextp = 21

    ret_array = []
    for i in range(34):
        locINext = inext + 1
        locINextp = inextp + 1

        if locINext >= 56 or locINextp >= 56:
            raise Exception("Shouldn't ever wrap")

        retVal = SeedArray[locINext] - SeedArray[locINextp]

        if retVal == MBIG:
            retVal -= 1

        if retVal < 0:
            retVal += MBIG

        SeedArray[locINext] = retVal
        ret_array.append(retVal)

        inext = locINext
        inextp = locINextp

    return ret_array


def test_sampel_seed_2():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        my_rands = sampel_seed_2(seed)
        for ri, my_r in enumerate(my_rands):
            r = rands[ri]
            # print("sample(%d) == %d should be %d" % (seed, my_r, r))
            if my_r != r:
                raise Exception("sample_seed_1 test failed on\n    sample(%d)[%d] == %d should be %d" % (seed, ri, my_r, r))


def sampel_seed_3(seed):
    # same as 2 but unrapping the sample section
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)
    mj = MSEED - subtraction
    SeedArray = [0 for i in range(56)]
    SeedArray[55] = mj
    mk = 1

    for i in range(1, 55):
        ii = (21 * i) % 55
        SeedArray[ii] = mk
        mk = mj - mk
        if mk < 0:
            mk += MBIG
        mj = SeedArray[ii]

    for k in range(1, 5):
        for i in range(1, 56):
            m = 1 + (i + 30) % 55
            SeedArray[i] -= SeedArray[m]
            if SeedArray[i] < 0:
                SeedArray[i] += MBIG
    """
    SAMPLE Section
    """
    ret_0 = (SeedArray[1] - SeedArray[22]) % MBIG
    ret_1 = (SeedArray[2] - SeedArray[23]) % MBIG
    ret_2 = (SeedArray[3] - SeedArray[24]) % MBIG
    ret_3 = (SeedArray[4] - SeedArray[25]) % MBIG
    ret_4 = (SeedArray[5] - SeedArray[26]) % MBIG
    ret_5 = (SeedArray[6] - SeedArray[27]) % MBIG
    ret_6 = (SeedArray[7] - SeedArray[28]) % MBIG
    ret_7 = (SeedArray[8] - SeedArray[29]) % MBIG
    ret_8 = (SeedArray[9] - SeedArray[30]) % MBIG
    ret_9 = (SeedArray[10] - SeedArray[31]) % MBIG
    ret10 = (SeedArray[11] - SeedArray[32]) % MBIG
    ret11 = (SeedArray[12] - SeedArray[33]) % MBIG
    ret12 = (SeedArray[13] - SeedArray[34]) % MBIG
    ret13 = (SeedArray[14] - SeedArray[35]) % MBIG
    ret14 = (SeedArray[15] - SeedArray[36]) % MBIG
    ret15 = (SeedArray[16] - SeedArray[37]) % MBIG
    ret16 = (SeedArray[17] - SeedArray[38]) % MBIG
    ret17 = (SeedArray[18] - SeedArray[39]) % MBIG
    ret18 = (SeedArray[19] - SeedArray[40]) % MBIG
    ret19 = (SeedArray[20] - SeedArray[41]) % MBIG
    ret20 = (SeedArray[21] - SeedArray[42]) % MBIG
    ret21 = (SeedArray[22] - SeedArray[43]) % MBIG
    ret22 = (SeedArray[23] - SeedArray[44]) % MBIG
    ret23 = (SeedArray[24] - SeedArray[45]) % MBIG
    ret24 = (SeedArray[25] - SeedArray[46]) % MBIG
    ret25 = (SeedArray[26] - SeedArray[47]) % MBIG
    ret26 = (SeedArray[27] - SeedArray[48]) % MBIG
    ret27 = (SeedArray[28] - SeedArray[49]) % MBIG
    ret28 = (SeedArray[29] - SeedArray[50]) % MBIG
    ret29 = (SeedArray[30] - SeedArray[51]) % MBIG
    ret30 = (SeedArray[31] - SeedArray[52]) % MBIG
    ret31 = (SeedArray[32] - SeedArray[53]) % MBIG
    ret32 = (SeedArray[33] - SeedArray[54]) % MBIG
    ret33 = (SeedArray[34] - SeedArray[55]) % MBIG

    return [ret_0, ret_1, ret_2, ret_3, ret_4, ret_5, ret_6, ret_7, ret_8,
            ret_9, ret10, ret11, ret12, ret13, ret14, ret15, ret16, ret17,
            ret18, ret19, ret20, ret21, ret22, ret23, ret24, ret25, ret26,
            ret27, ret28, ret29, ret30, ret31, ret32, ret33]

def test_sampel_seed_3():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        my_rands = sampel_seed_3(seed)
        for ri, my_r in enumerate(my_rands):
            r = rands[ri]
            # print("sample(%d) == %d should be %d" % (seed, my_r, r))
            if my_r != r:
                raise Exception("sample_seed_1 test failed on\n    sample(%d)[%d] == %d should be %d" % (seed, ri, my_r, r))

def sampel_seed_4(seed):
    # same as 2 but unrapping the sample section
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)
    mj = MSEED - subtraction
    SeedArray = [0 for i in range(56)]
    SeedArray[55] = mj
    mk = 1

    for i in range(1, 55):
        ii = (21 * i) % 55
        SeedArray[ii] = mk
        mk = mj - mk
        if mk < 0:
            mk += MBIG
        mj = SeedArray[ii]

    for k in range(1, 4):  # <-- one less loop then sampel_seed_3
        for i in range(1, 56):
            m = 1 + (i + 30) % 55
            SeedArray[i] -= SeedArray[m]
            if SeedArray[i] < 0:
                SeedArray[i] += MBIG

    # the removed outer loop above is placed here unwound, with custom variables
    sa4__1 = (SeedArray[1]  - SeedArray[32]) % MBIG
    sa4__2 = (SeedArray[2]  - SeedArray[33]) % MBIG
    sa4__3 = (SeedArray[3]  - SeedArray[34]) % MBIG
    sa4__4 = (SeedArray[4]  - SeedArray[35]) % MBIG
    sa4__5 = (SeedArray[5]  - SeedArray[36]) % MBIG
    sa4__6 = (SeedArray[6]  - SeedArray[37]) % MBIG
    sa4__7 = (SeedArray[7]  - SeedArray[38]) % MBIG
    sa4__8 = (SeedArray[8]  - SeedArray[39]) % MBIG
    sa4__9 = (SeedArray[9]  - SeedArray[40]) % MBIG
    sa4_10 = (SeedArray[10] - SeedArray[41]) % MBIG
    sa4_11 = (SeedArray[11] - SeedArray[42]) % MBIG
    sa4_12 = (SeedArray[12] - SeedArray[43]) % MBIG
    sa4_13 = (SeedArray[13] - SeedArray[44]) % MBIG
    sa4_14 = (SeedArray[14] - SeedArray[45]) % MBIG
    sa4_15 = (SeedArray[15] - SeedArray[46]) % MBIG
    sa4_16 = (SeedArray[16] - SeedArray[47]) % MBIG
    sa4_17 = (SeedArray[17] - SeedArray[48]) % MBIG
    sa4_18 = (SeedArray[18] - SeedArray[49]) % MBIG
    sa4_19 = (SeedArray[19] - SeedArray[50]) % MBIG
    sa4_20 = (SeedArray[20] - SeedArray[51]) % MBIG
    sa4_21 = (SeedArray[21] - SeedArray[52]) % MBIG
    sa4_22 = (SeedArray[22] - SeedArray[53]) % MBIG
    sa4_23 = (SeedArray[23] - SeedArray[54]) % MBIG
    sa4_24 = (SeedArray[24] - SeedArray[55]) % MBIG
    sa4_25 = (SeedArray[25] - sa4__1) % MBIG
    sa4_26 = (SeedArray[26] - sa4__2) % MBIG
    sa4_27 = (SeedArray[27] - sa4__3) % MBIG
    sa4_28 = (SeedArray[28] - sa4__4) % MBIG
    sa4_29 = (SeedArray[29] - sa4__5) % MBIG
    sa4_30 = (SeedArray[30] - sa4__6) % MBIG
    sa4_31 = (SeedArray[31] - sa4__7) % MBIG
    sa4_32 = (SeedArray[32] - sa4__8) % MBIG
    sa4_33 = (SeedArray[33] - sa4__9) % MBIG
    sa4_34 = (SeedArray[34] - sa4_10) % MBIG
    sa4_35 = (SeedArray[35] - sa4_11) % MBIG
    sa4_36 = (SeedArray[36] - sa4_12) % MBIG
    sa4_37 = (SeedArray[37] - sa4_13) % MBIG
    sa4_38 = (SeedArray[38] - sa4_14) % MBIG
    sa4_39 = (SeedArray[39] - sa4_15) % MBIG
    sa4_40 = (SeedArray[40] - sa4_16) % MBIG
    sa4_41 = (SeedArray[41] - sa4_17) % MBIG
    sa4_42 = (SeedArray[42] - sa4_18) % MBIG
    sa4_43 = (SeedArray[43] - sa4_19) % MBIG
    sa4_44 = (SeedArray[44] - sa4_20) % MBIG
    sa4_45 = (SeedArray[45] - sa4_21) % MBIG
    sa4_46 = (SeedArray[46] - sa4_22) % MBIG
    sa4_47 = (SeedArray[47] - sa4_23) % MBIG
    sa4_48 = (SeedArray[48] - sa4_24) % MBIG
    sa4_49 = (SeedArray[49] - sa4_25) % MBIG
    sa4_50 = (SeedArray[50] - sa4_26) % MBIG
    sa4_51 = (SeedArray[51] - sa4_27) % MBIG
    sa4_52 = (SeedArray[52] - sa4_28) % MBIG
    sa4_53 = (SeedArray[53] - sa4_29) % MBIG
    sa4_54 = (SeedArray[54] - sa4_30) % MBIG
    sa4_55 = (SeedArray[55] - sa4_31) % MBIG

    """
    SAMPLE Section
    """
    ret_0 = (sa4__1 - sa4_22) % MBIG
    ret_1 = (sa4__2 - sa4_23) % MBIG
    ret_2 = (sa4__3 - sa4_24) % MBIG
    ret_3 = (sa4__4 - sa4_25) % MBIG
    ret_4 = (sa4__5 - sa4_26) % MBIG
    ret_5 = (sa4__6 - sa4_27) % MBIG
    ret_6 = (sa4__7 - sa4_28) % MBIG
    ret_7 = (sa4__8 - sa4_29) % MBIG
    ret_8 = (sa4__9 - sa4_30) % MBIG
    ret_9 = (sa4_10 - sa4_31) % MBIG
    ret10 = (sa4_11 - sa4_32) % MBIG
    ret11 = (sa4_12 - sa4_33) % MBIG
    ret12 = (sa4_13 - sa4_34) % MBIG
    ret13 = (sa4_14 - sa4_35) % MBIG
    ret14 = (sa4_15 - sa4_36) % MBIG
    ret15 = (sa4_16 - sa4_37) % MBIG
    ret16 = (sa4_17 - sa4_38) % MBIG
    ret17 = (sa4_18 - sa4_39) % MBIG
    ret18 = (sa4_19 - sa4_40) % MBIG
    ret19 = (sa4_20 - sa4_41) % MBIG
    ret20 = (sa4_21 - sa4_42) % MBIG
    ret21 = (sa4_22 - sa4_43) % MBIG
    ret22 = (sa4_23 - sa4_44) % MBIG
    ret23 = (sa4_24 - sa4_45) % MBIG
    ret24 = (sa4_25 - sa4_46) % MBIG
    ret25 = (sa4_26 - sa4_47) % MBIG
    ret26 = (sa4_27 - sa4_48) % MBIG
    ret27 = (sa4_28 - sa4_49) % MBIG
    ret28 = (sa4_29 - sa4_50) % MBIG
    ret29 = (sa4_30 - sa4_51) % MBIG
    ret30 = (sa4_31 - sa4_52) % MBIG
    ret31 = (sa4_32 - sa4_53) % MBIG
    ret32 = (sa4_33 - sa4_54) % MBIG
    ret33 = (sa4_34 - sa4_55) % MBIG

    return [ret_0, ret_1, ret_2, ret_3, ret_4, ret_5, ret_6, ret_7, ret_8,
            ret_9, ret10, ret11, ret12, ret13, ret14, ret15, ret16, ret17,
            ret18, ret19, ret20, ret21, ret22, ret23, ret24, ret25, ret26,
            ret27, ret28, ret29, ret30, ret31, ret32, ret33]

def test_sampel_seed_4():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        my_rands = sampel_seed_4(seed)
        for ri, my_r in enumerate(my_rands):
            r = rands[ri]
            # print("sample(%d) == %d should be %d" % (seed, my_r, r))
            if my_r != r:
                raise Exception("sample_seed_1 test failed on\n    sample(%d)[%d] == %d should be %d" % (seed, ri, my_r, r))


def sampel_seed_5(seed):
    # same as 5 but last loops unwound
    if seed == Int32MinValue:
        subtraction = Int32MinValue
    else:
        subtraction = abs(seed)
    mj = MSEED - subtraction
    SeedArray = [0 for i in range(56)]
    SeedArray[55] = mj
    mk = 1

    for i in range(1, 55):
        ii = (21 * i) % 55
        SeedArray[ii] = mk
        mk = mj - mk
        if mk < 0:
            mk += MBIG
        mj = SeedArray[ii]

    for k in range(1, 2):  # <-- 2 less loop then sampel_seed_3
        for i in range(1, 56):
            m = 1 + (i + 30) % 55
            SeedArray[i] -= SeedArray[m]
            if SeedArray[i] < 0:
                SeedArray[i] += MBIG

    sa2__1 = (SeedArray[1]  - SeedArray[32]) % MBIG
    sa2__2 = (SeedArray[2]  - SeedArray[33]) % MBIG
    sa2__3 = (SeedArray[3]  - SeedArray[34]) % MBIG
    sa2__4 = (SeedArray[4]  - SeedArray[35]) % MBIG
    sa2__5 = (SeedArray[5]  - SeedArray[36]) % MBIG
    sa2__6 = (SeedArray[6]  - SeedArray[37]) % MBIG
    sa2__7 = (SeedArray[7]  - SeedArray[38]) % MBIG
    sa2__8 = (SeedArray[8]  - SeedArray[39]) % MBIG
    sa2__9 = (SeedArray[9]  - SeedArray[40]) % MBIG
    sa2_10 = (SeedArray[10] - SeedArray[41]) % MBIG
    sa2_11 = (SeedArray[11] - SeedArray[42]) % MBIG
    sa2_12 = (SeedArray[12] - SeedArray[43]) % MBIG
    sa2_13 = (SeedArray[13] - SeedArray[44]) % MBIG
    sa2_14 = (SeedArray[14] - SeedArray[45]) % MBIG
    sa2_15 = (SeedArray[15] - SeedArray[46]) % MBIG
    sa2_16 = (SeedArray[16] - SeedArray[47]) % MBIG
    sa2_17 = (SeedArray[17] - SeedArray[48]) % MBIG
    sa2_18 = (SeedArray[18] - SeedArray[49]) % MBIG
    sa2_19 = (SeedArray[19] - SeedArray[50]) % MBIG
    sa2_20 = (SeedArray[20] - SeedArray[51]) % MBIG
    sa2_21 = (SeedArray[21] - SeedArray[52]) % MBIG
    sa2_22 = (SeedArray[22] - SeedArray[53]) % MBIG
    sa2_23 = (SeedArray[23] - SeedArray[54]) % MBIG
    sa2_24 = (SeedArray[24] - SeedArray[55]) % MBIG
    sa2_25 = (SeedArray[25] - sa2__1) % MBIG
    sa2_26 = (SeedArray[26] - sa2__2) % MBIG
    sa2_27 = (SeedArray[27] - sa2__3) % MBIG
    sa2_28 = (SeedArray[28] - sa2__4) % MBIG
    sa2_29 = (SeedArray[29] - sa2__5) % MBIG
    sa2_30 = (SeedArray[30] - sa2__6) % MBIG
    sa2_31 = (SeedArray[31] - sa2__7) % MBIG
    sa2_32 = (SeedArray[32] - sa2__8) % MBIG
    sa2_33 = (SeedArray[33] - sa2__9) % MBIG
    sa2_34 = (SeedArray[34] - sa2_10) % MBIG
    sa2_35 = (SeedArray[35] - sa2_11) % MBIG
    sa2_36 = (SeedArray[36] - sa2_12) % MBIG
    sa2_37 = (SeedArray[37] - sa2_13) % MBIG
    sa2_38 = (SeedArray[38] - sa2_14) % MBIG
    sa2_39 = (SeedArray[39] - sa2_15) % MBIG
    sa2_40 = (SeedArray[40] - sa2_16) % MBIG
    sa2_41 = (SeedArray[41] - sa2_17) % MBIG
    sa2_42 = (SeedArray[42] - sa2_18) % MBIG
    sa2_43 = (SeedArray[43] - sa2_19) % MBIG
    sa2_44 = (SeedArray[44] - sa2_20) % MBIG
    sa2_45 = (SeedArray[45] - sa2_21) % MBIG
    sa2_46 = (SeedArray[46] - sa2_22) % MBIG
    sa2_47 = (SeedArray[47] - sa2_23) % MBIG
    sa2_48 = (SeedArray[48] - sa2_24) % MBIG
    sa2_49 = (SeedArray[49] - sa2_25) % MBIG
    sa2_50 = (SeedArray[50] - sa2_26) % MBIG
    sa2_51 = (SeedArray[51] - sa2_27) % MBIG
    sa2_52 = (SeedArray[52] - sa2_28) % MBIG
    sa2_53 = (SeedArray[53] - sa2_29) % MBIG
    sa2_54 = (SeedArray[54] - sa2_30) % MBIG
    sa2_55 = (SeedArray[55] - sa2_31) % MBIG

    sa3__1 = (sa2__1  - sa2_32) % MBIG
    sa3__2 = (sa2__2  - sa2_33) % MBIG
    sa3__3 = (sa2__3  - sa2_34) % MBIG
    sa3__4 = (sa2__4  - sa2_35) % MBIG
    sa3__5 = (sa2__5  - sa2_36) % MBIG
    sa3__6 = (sa2__6  - sa2_37) % MBIG
    sa3__7 = (sa2__7  - sa2_38) % MBIG
    sa3__8 = (sa2__8  - sa2_39) % MBIG
    sa3__9 = (sa2__9  - sa2_40) % MBIG
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

    # the removed outer loop above is placed here unwound, with custom variables
    sa4__1 = (sa3__1  - sa3_32) % MBIG
    sa4__2 = (sa3__2  - sa3_33) % MBIG
    sa4__3 = (sa3__3  - sa3_34) % MBIG
    sa4__4 = (sa3__4  - sa3_35) % MBIG
    sa4__5 = (sa3__5  - sa3_36) % MBIG
    sa4__6 = (sa3__6  - sa3_37) % MBIG
    sa4__7 = (sa3__7  - sa3_38) % MBIG
    sa4__8 = (sa3__8  - sa3_39) % MBIG
    sa4__9 = (sa3__9  - sa3_40) % MBIG
    sa4_10 = (sa3_10 - sa3_41) % MBIG
    sa4_11 = (sa3_11 - sa3_42) % MBIG
    sa4_12 = (sa3_12 - sa3_43) % MBIG
    sa4_13 = (sa3_13 - sa3_44) % MBIG
    sa4_14 = (sa3_14 - sa3_45) % MBIG
    sa4_15 = (sa3_15 - sa3_46) % MBIG
    sa4_16 = (sa3_16 - sa3_47) % MBIG
    sa4_17 = (sa3_17 - sa3_48) % MBIG
    sa4_18 = (sa3_18 - sa3_49) % MBIG
    sa4_19 = (sa3_19 - sa3_50) % MBIG
    sa4_20 = (sa3_20 - sa3_51) % MBIG
    sa4_21 = (sa3_21 - sa3_52) % MBIG
    sa4_22 = (sa3_22 - sa3_53) % MBIG
    sa4_23 = (sa3_23 - sa3_54) % MBIG
    sa4_24 = (sa3_24 - sa3_55) % MBIG
    sa4_25 = (sa3_25 - sa4__1) % MBIG
    sa4_26 = (sa3_26 - sa4__2) % MBIG
    sa4_27 = (sa3_27 - sa4__3) % MBIG
    sa4_28 = (sa3_28 - sa4__4) % MBIG
    sa4_29 = (sa3_29 - sa4__5) % MBIG
    sa4_30 = (sa3_30 - sa4__6) % MBIG
    sa4_31 = (sa3_31 - sa4__7) % MBIG
    sa4_32 = (sa3_32 - sa4__8) % MBIG
    sa4_33 = (sa3_33 - sa4__9) % MBIG
    sa4_34 = (sa3_34 - sa4_10) % MBIG
    sa4_35 = (sa3_35 - sa4_11) % MBIG
    sa4_36 = (sa3_36 - sa4_12) % MBIG
    sa4_37 = (sa3_37 - sa4_13) % MBIG
    sa4_38 = (sa3_38 - sa4_14) % MBIG
    sa4_39 = (sa3_39 - sa4_15) % MBIG
    sa4_40 = (sa3_40 - sa4_16) % MBIG
    sa4_41 = (sa3_41 - sa4_17) % MBIG
    sa4_42 = (sa3_42 - sa4_18) % MBIG
    sa4_43 = (sa3_43 - sa4_19) % MBIG
    sa4_44 = (sa3_44 - sa4_20) % MBIG
    sa4_45 = (sa3_45 - sa4_21) % MBIG
    sa4_46 = (sa3_46 - sa4_22) % MBIG
    sa4_47 = (sa3_47 - sa4_23) % MBIG
    sa4_48 = (sa3_48 - sa4_24) % MBIG
    sa4_49 = (sa3_49 - sa4_25) % MBIG
    sa4_50 = (sa3_50 - sa4_26) % MBIG
    sa4_51 = (sa3_51 - sa4_27) % MBIG
    sa4_52 = (sa3_52 - sa4_28) % MBIG
    sa4_53 = (sa3_53 - sa4_29) % MBIG
    sa4_54 = (sa3_54 - sa4_30) % MBIG
    sa4_55 = (sa3_55 - sa4_31) % MBIG

    """
    SAMPLE Section
    """
    ret_0 = (sa4__1 - sa4_22) % MBIG
    ret_1 = (sa4__2 - sa4_23) % MBIG
    ret_2 = (sa4__3 - sa4_24) % MBIG
    ret_3 = (sa4__4 - sa4_25) % MBIG
    ret_4 = (sa4__5 - sa4_26) % MBIG
    ret_5 = (sa4__6 - sa4_27) % MBIG
    ret_6 = (sa4__7 - sa4_28) % MBIG
    ret_7 = (sa4__8 - sa4_29) % MBIG
    ret_8 = (sa4__9 - sa4_30) % MBIG
    ret_9 = (sa4_10 - sa4_31) % MBIG
    ret10 = (sa4_11 - sa4_32) % MBIG
    ret11 = (sa4_12 - sa4_33) % MBIG
    ret12 = (sa4_13 - sa4_34) % MBIG
    ret13 = (sa4_14 - sa4_35) % MBIG
    ret14 = (sa4_15 - sa4_36) % MBIG
    ret15 = (sa4_16 - sa4_37) % MBIG
    ret16 = (sa4_17 - sa4_38) % MBIG
    ret17 = (sa4_18 - sa4_39) % MBIG
    ret18 = (sa4_19 - sa4_40) % MBIG
    ret19 = (sa4_20 - sa4_41) % MBIG
    ret20 = (sa4_21 - sa4_42) % MBIG
    ret21 = (sa4_22 - sa4_43) % MBIG
    ret22 = (sa4_23 - sa4_44) % MBIG
    ret23 = (sa4_24 - sa4_45) % MBIG
    ret24 = (sa4_25 - sa4_46) % MBIG
    ret25 = (sa4_26 - sa4_47) % MBIG
    ret26 = (sa4_27 - sa4_48) % MBIG
    ret27 = (sa4_28 - sa4_49) % MBIG
    ret28 = (sa4_29 - sa4_50) % MBIG
    ret29 = (sa4_30 - sa4_51) % MBIG
    ret30 = (sa4_31 - sa4_52) % MBIG
    ret31 = (sa4_32 - sa4_53) % MBIG
    ret32 = (sa4_33 - sa4_54) % MBIG
    ret33 = (sa4_34 - sa4_55) % MBIG

    return [ret_0, ret_1, ret_2, ret_3, ret_4, ret_5, ret_6, ret_7, ret_8,
            ret_9, ret10, ret11, ret12, ret13, ret14, ret15, ret16, ret17,
            ret18, ret19, ret20, ret21, ret22, ret23, ret24, ret25, ret26,
            ret27, ret28, ret29, ret30, ret31, ret32, ret33]

def test_sampel_seed_5():
    import json
    with open("tests.json") as fp:
        test_data = json.load(fp)

    for _seed, rands in test_data.items():
        seed = int(_seed)
        my_rands = sampel_seed_5(seed)
        for ri, my_r in enumerate(my_rands):
            r = rands[ri]
            # print("sample(%d) == %d should be %d" % (seed, my_r, r))
            if my_r != r:
                raise Exception("sample_seed_1 test failed on\n    sample(%d)[%d] == %d should be %d" % (seed, ri, my_r, r))

test_sampel_seed_5()
