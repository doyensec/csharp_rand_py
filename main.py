
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

    # that loop is put here, unwound
    for i in range(1, 56):
        m = 1 + (i + 30) % 55
        print("SeedArray[%d] -= SeedArray[%d]" % (i, m))
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


test_sampel_seed_4()
