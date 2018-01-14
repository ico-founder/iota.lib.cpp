#!/usr/bin/python
from iota import Iota
from iota import Address, ProposedTransaction, Tag, Transaction
from iota import TryteString

accounts = [
    {
        'seed': 'SXDHBTSTV9YHWKFFAZBHQXJTQHTO9HJMDBZHOJDKV9MMAODELRICQAQMEOCZXZKO9USMBUAKJCAYTF9TM',
        'fund': 977894,
        'addresses': [
            'FWPSSVXWSJRZLKWYKSVJIURDU9IKBAVPBJVTAXDJTYCJHSRUTKLVWKIN9AEEFNMONNDKVAIAXVRKLQSLCHZRXZWU9C',
            'QJJMMRENGJTHSSFIUAPVUACXPABAECWFMDWECLI9HZKNFQQWUMYIFFKXLTTVUAUQAYVHBQQAKXPFRGKCZF99CJTY99',
            'FSRCBZVWJOEAEPYMNRRWIIFZFVTENUMEBCEX9NWVORKIYZTFXNEQMEDGJUTUULI9DXWILJQEICIRCLOBYRRANTIJMC',
            'DOAOO9S9OWLSFYSTDARTDP9GWEXXMSYZTSXVCRPGQPOJGQKEJVNLOATQGPJGTUUN9PNPRYQYWMG9LZMWYLPHTZPHWX',
            'ZUITLIUCMVPG9EXNBXBFLZFNVWTNYHISHGUPQEWBNFEARKYQUCEFFOSAXQYTKNPCIUAFVOSWKUPHLRGWWPHZ9DXHAX',
            'WPJZKUFAFCEWEX9KKQUCCNO9KNRC9A9WOXABYX9UPMKKMZQWLVGOFQLFAROLCDZG9ZENZVFAEBWKEQDACJPRKXVEKX'
        ]
    },
    {
        'seed': 'S9YOBZWUIHQFGHQCUOFCKHFR99IJMSZNNHUDXRAGDZKLGEBGPNDWROALSUODRJNMFFQHDVNISRMVMPVNE',
        'fund': 251682,
        'addresses': [
            'JTJXWTWPREDKKWOWQLSHGTHXEXIWPRAQIZGWDZTAENBXYDNJEZMMQSJVNBVDVNDRA9KPYWPMMUCAINHYZOOHISFHVD',
            'O9N9SOKTMGUKMPRNOR9EFQNISGVUR9DJ9RGXREOLKEJFO9BMMC9MRSLJS9IWBREGSVUXUC9W9EEM9Y9ABOZCVZIPVC',
            'RYIKD9MLZ9YZCOCJLJHMVOQVNHHP9RUFONHMKMNJAWDUEZUGQZADSUBNSFLQLWJGYKGKRQDVINIUAQXVZWWAYVEHZC',
            'EMWMJXCUOSHAVZAJOT9LS9C9WSZRXVXINVAIZOYDZMOHAALJBJXYQHRYWADZB9JISEIGTQB9CUGPSVIJCXIBZXVIRD'
        ]
    },
    {
        'seed': 'UYMUEUOCKNROIJPNFFDLBP9GCQUJFRLIBQ9SMICMHSHSOXUZLOWHFJDPEEPUESUXJEAJFTICCEGPMMHKO',
        'fund': 26529296,
        'addresses': [
            'E9LVPMKJIAGCIPVKMUOYTQMSYAUQDUMEYUUCLXRQUWJJ9JXRDXQNGIOUPQVIMIWHFIRXD9QSYOP9KG9BWARSINOJ9W',
            'WCFQQNYYJHY9DCY9K9EDQNGBDGHQDHFNKUVIIPTHFJPTTVFUFNRKSZEPKTCPIKNOFBMSNMBUQNAWVNPCXXDCKBCMTA',
            'VFWUE9BDKNEBHCBCXDFVFPHXFTYFGSTTEYFYWRYLIOTFUAUEHCBGITXZJCBLVAPWFBIN9BGEKJO9GBQABEQKFF9Y9D',
            'SRDPEFFDWFNTNRKIIYFSVUYTSBAERXCALHQQVSIACNGGZMPCOURRAWEKCAKVVGUKGXJFKJDPWSJDJYHNXNBSBOSLS9',
            'ENDBGFTOKLSKSRYEIKYNB9RSSCVTWLEFQDNICDTC9ZGKEGNJAJTKQMPALXLWVLUSQIDABWRGPVDJQFQNWJNQEWHKWC',
            'SNJKTSZPAOWGFSOXNXKKKRYRTJXDJQ9SMGBVXNYBMNNOOYVDFNTUCKTPYSAGYDJIRXWOZGF9TDGZTULBWOYBQOCPTC',
            'LXJIDOAASJGMNQDXFIAYGBJRRKUWH9WTPRCF99IZXPUROIEOZRBUH9KLTRTQJRMKJJNIWPKSHRNDNXKAAHLPTEGCYB',
            'ZSQDZHAZEHINWPZXVQFZNCBNEXEXXUJVWCECPZMOAHSWQUHXAOLOYUCAGVYKCFYNUPUDJRJOFLHWDQAXXVGTNH9EEX',
            'HKIRNFIXFUDUDUUUVAXONNYE9YNUTMPXUQAUWENTHQVJBOHCYU9WLWHHCIFQZZPGNYDFKYFXMRK9DZR9CHSPFJTAK9'
        ]
    },
    {
        'seed': 'NG9VUE9RBOLTPNAHFVWBPF9QELYLBNX9ZNIKYJZKWASZWJCMXZ9QIXNMAYDO9DJAZ9EBUBKDEFCUVQFXG',
        'fund': 42,
        'addresses': [
            'EHMKBYQAFTPVBKQYDKTWWDKHXKHUALIDEBBIXABI9PJWHFBXY9MPRSJCWKJTDPGHBKAL9MYEFM9TXVCE9NWZSSZIDW'
        ]
    },
    {
        'seed': 'UYXMZDTITKOAPKPFCAZYB9DTPJ9VARFKCWVSYIOZROLBSUJECBLBZA99TTBFJTPUXEYN9PETLVENOHRKJ',
        'fund': 2779530255518847,
        'addresses': [
            'YCXCVQDFGWUKPUABPYNMVPAQUGUHYYLMWZQWRUIDIXGTDAOJKOUGRWDJUUOWGOHMVYLTZHGEZCZHBTMT9RM9XGRJUW'
        ]
    }
]

for account in accounts:
    # fetch seed
    seed  = account['seed']
    fund  = account['fund']
    addrs = account['addresses']
    # log
    print '[%s] Start' % (seed)
    # setup iota client
    api = Iota('http://localhost:14265', seed)
    # attach each address
    for address in addrs:
        # prepare trx
        trx = ProposedTransaction(
            address = Address(address),
            message = TryteString.from_string("MSG%s%s" % (seed[:5], address[:5])),
            tag     = Tag("TAG%s%s" % (seed[:5], address[:5])),
            value   = 0)
        # attach
        api.send_transfer(1, [trx])
    # ensure we can get the expected amount of funding for that account now
    api_fund = api.get_account_data(0)['balance']
    if api_fund == fund:
        print '[%s] Success' % (seed)
    else:
        print '[%s] Fail: expected %d IOTA, got %d IOTA' % (seed, fund, api_fund)
