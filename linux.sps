#editor() = [vim] | [nano];
@results
	0 { 'vim' }
	1 { 'nano' }
@

open #editor;
@results
	#editor { 'execute2(' #editor ');' }
@

#city() = [Alexandra] | [Ashburton] | [Auckland] | [Blenheim] | [Chatham Island] | [Christchurch] | [Dannevirke] | [Dargaville] | [Dunedin] | [Franz Josef] | [Gisborne] | [Greymouth] | [Hamilton] | [Hastings] | [Hokitika] | [Invercargill] | [Kaikoura] | [Kaitaia] | [Kerikeri] | [Lake Tekapo] | [Levin] | [Masterton] | [Motueka] | [Murchison] | [Mystery Creek] | [Napier] | [Nelson] | [New Plymouth] | [Oamaru] | [Palmerston North] | [Paraparaumu] | [Queenstown] | [Reefton] | [Rotorua] | [Stewart Island] | [Stratford] | [Taupo] | [Tauranga] | [Te Kuiti] | [Thames] | [Timaru] | [Turangi] | [Wellington] | [Westport] | [Whakatane] | [Whanganui] | [Whangarei] | [Whitianga];
@results
    0 { 'Alexandra' }
    1 { 'Ashburton' }
    2 { 'Auckland' }
    3 { 'Blenheim' }
    4 { 'Chatham Island' }
    5 { 'Christchurch' }
    6 { 'Dannevirke' }
    7 { 'Dargaville' }
    8 { 'Dunedin' }
    9 { 'Franz Josef' }
    10 { 'Gisborne' }
    11 { 'Greymouth' }
    12 { 'Hamilton' }
    13 { 'Hastings' }
    14 { 'Hokitika' }
    15 { 'Invercargill' }
    16 { 'Kaikoura' }
    17 { 'Kaitaia' }
    18 { 'Kerikeri' }
    19 { 'Lake Tekapo' }
    20 { 'Levin' }
    21 { 'Masterton' }
    22 { 'Motueka' }
    23 { 'Murchison' }
    24 { 'Mystery Creek' }
    25 { 'Napier' }
    26 { 'Nelson' }
    27 { 'New Plymouth' }
    28 { 'Oamaru' }
    29 { 'Palmerston North' }
    30 { 'Paraparaumu' }
    31 { 'Queenstown' }
    32 { 'Reefton' }
    33 { 'Rotorua' }
    34 { 'Stewart Island' }
    35 { 'Stratford' }
    36 { 'Taupo' }
    37 { 'Tauranga' }
    38 { 'Te Kuiti' }
    39 { 'Thames' }
    40 { 'Timaru' }
    41 { 'Turangi' }
    42 { 'Wellington' }
    43 { 'Westport' }
    44 { 'Whakatane' }
    45 { 'Whanganui' }
    46 { 'Whangarei' }
    47 { 'Whitianga' }
@

(give me | show me | how is | what is) the weather (in | at) #city;
@results
	#city { 'weather(' #city ');' }
@