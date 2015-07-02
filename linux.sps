#city() = [alexandra] | [ashburton] | [auckland] | [blenheim] | [chatham island] | [christchurch] | [dannevirke] | [dargaville] | [dunedin] | [franz josef] | [gisborne] | [greymouth] | [hamilton] | [hastings] | [hokitika] | [invercargill] | [kaikoura] | [kaitaia] | [kerikeri] | [lake tekapo] | [levin] | [masterton] | [motueka] | [murchison] | [mystery creek] | [napier] | [nelson] | [new plymouth] | [oamaru] | [palmerston north] | [paraparaumu] | [queenstown] | [reefton] | [rotorua] | [stewart island] | [stratford] | [taupo] | [tauranga] | [te kuiti] | [thames] | [timaru] | [turangi] | [wellington] | [westport] | [whakatane] | [whanganui] | [whangarei] | [whitianga];
@results
    0 { 'alexandra' }
    1 { 'ashburton' }
    2 { 'auckland' }
    3 { 'blenheim' }
    4 { 'chatham island' }
    5 { 'christchurch' }
    6 { 'dannevirke' }
    7 { 'dargaville' }
    8 { 'dunedin' }
    9 { 'franz josef' }
    10 { 'gisborne' }
    11 { 'greymouth' }
    12 { 'hamilton' }
    13 { 'hastings' }
    14 { 'hokitika' }
    15 { 'invercargill' }
    16 { 'kaikoura' }
    17 { 'kaitaia' }
    18 { 'kerikeri' }
    19 { 'lake tekapo' }
    20 { 'levin' }
    21 { 'masterton' }
    22 { 'motueka' }
    23 { 'murchison' }
    24 { 'mystery creek' }
    25 { 'napier' }
    26 { 'nelson' }
    27 { 'new plymouth' }
    28 { 'oamaru' }
    29 { 'palmerston north' }
    30 { 'paraparaumu' }
    31 { 'queenstown' }
    32 { 'reefton' }
    33 { 'rotorua' }
    34 { 'stewart island' }
    35 { 'stratford' }
    36 { 'taupo' }
    37 { 'tauranga' }
    38 { 'te kuiti' }
    39 { 'thames' }
    40 { 'timaru' }
    41 { 'turangi' }
    42 { 'wellington' }
    43 { 'westport' }
    44 { 'whakatane' }
    45 { 'whanganui' }
    46 { 'whangarei' }
    47 { 'whitianga' }
@

(give me | show me | how is | what is) the weather (in | at) #city;
@results
	#city { 'weather("' #city '");' }
@
