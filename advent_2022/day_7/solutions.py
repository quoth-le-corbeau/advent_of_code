from collections import defaultdict
from pathlib import Path

from reusables import timer, INPUT_PATH

# decide on a data structure into which to parse the input
# base the decision on an appropriate algorithm to arrive at the solution
# assess if the data structure misses any edge cases (e.g - repeated dir names in nesting means flat won't work)
# assess if the algo misses edge cases
# proceed

example_tree = {
    "dir /": {"dir d", "dir a", "14848514 b.txt", "8504156 c.dat"},
    "dir /a": {"62596 h.lst", "29116 f", "2557 g", "dir e"},
    "dir /a/e": {"584 i"},
    "dir /d": {"8033020 d.log", "7214296 k", "5626152 d.ext", "4060174 j"},
}

real = {
    "/": {
        "dir gnpd",
        "dir jsv",
        "21980 rbq.hpj",
        "dir zhfl",
        "dir nljtr",
        "200058 hbnlqs",
        "dir rfwwwgr",
        "dir nwzp",
        "61949 qdswp.wfj",
        "dir mfhzl",
        "136762 zwg",
        "dir sbnhc",
        "187585 dgflmqwt.srm",
    },
    "gnpd": {
        "dir dcqq",
        "167581 ndwfr.pbv",
        "144703 sct",
        "dir sbnhc",
        "dir dnscfz",
        "dir lsrb",
        "dir dwqbhgc",
        "dir smfhldss",
        "dir pbgrdvmc",
    },
    "gnpd/dcqq": {
        "dir mhpqqq",
        "dir mpbpcv",
        "155230 mfhzl.bpw",
        "24140 mrrznmvr.mmz",
        "dir bfdng",
    },
    "gnpd/dcqq/bfdng": {"dir hjlch", "dir sbnhc"},
    "gnpd/dcqq/bfdng/hjlch": {"239759 sct"},
    "sbnhc": {
        "232949 dcqq.rnj",
        "dir sbq",
        "221334 hbnlqs",
        "dir vmslnrmc",
        "35956 nfqs.crt",
        "173163 vnlmlq",
        "299303 vtrfbw.dng",
        "dir dwvphbm",
        "89464 qvhvlcl.nzq",
        "245520 tjp.pml",
        "dir dbb",
        "156705 zwr.rtg",
        "334229 mfhzl",
        "dir hwtmwp",
        "265434 vnlmlq",
        "dir vvn",
    },
    "mhpqqq": {
        "dir qqhz",
        "250305 nfqs.crt",
        "64587 tbzlnq",
        "dir vnlmlq",
        "dir tcbgmw",
        "60892 rbq.hpj",
    },
    "mhpqqq/qqhz": {"148009 sct"},
    "tcbgmw": {"85006 sbnhc"},
    "vnlmlq": {
        "dir mdj",
        "212688 hbnlqs",
        "153953 dwvphbm",
        "dir mtg",
        "213882 sbnhc.dzl",
        "69495 vnlmlq.thv",
        "dir blggqt",
        "dir vnlmlq",
        "dir gfsj",
        "155333 mmhjscr.mrh",
        "5068 mnfdf",
        "dir lbh",
        "dir jgc",
        "dir dcqq",
        "dir vfdqq",
        "dir rdvq",
        "293720 nfqs.crt",
        "84544 sbnhc",
        "121146 nfqs.crt",
        "dir fpw",
        "dir qnv",
        "11669 gqhltqf",
        "237487 cqhdvmzp.npw",
        "dir dwvphbm",
        "dir btqsh",
        "117656 dcqq.vlg",
        "195879 gsb.dvw",
        "dir qwbnvzv",
        "21720 vsrrhvlt.qbs",
        "234450 rqlnhpc.qfd",
        "dir mfhzl",
        "8202 mlpl.tsp",
        "dir rhszw",
        "281200 vzdwr.tbl",
        "dir lrwt",
        "dir clhclcr",
        "91205 hbnlqs",
        "285614 bfrjhpv.dvn",
        "2798 vwwbhsnb.dms",
        "160920 zgnft",
        "226720 zgmtqvws",
        "dir vbrc",
    },
    "mpbpcv": {"146794 bdpld.ddm"},
    "dnscfz": {
        "248161 qjgzgm",
        "dir wwf",
        "dir zjdhldlq",
        "dir vnlmlq",
        "276175 mfhzl.ndh",
    },
    "dnscfz/vnlmlq": {"130051 ftjnfc"},
    "wwf": {"166550 dwvphbm.jtd"},
    "zjdhldlq": {"345090 hbnlqs"},
    "dwqbhgc": {
        "139174 sct",
        "48014 nfqs.crt",
        "333356 rwb.njl",
        "dir vjcl",
        "157686 hbnlqs",
        "dir sbnhc",
        "310228 dwvphbm",
    },
    "dwqbhgc/sbnhc": {
        "51605 bfqw.cjd",
        "267184 fjvmbpf",
        "243630 sbnhc",
        "169122 mfhzl.jrp",
    },
    "vjcl": {"dir mfhzl"},
    "vjcl/mfhzl": {"302243 dcqq.djc"},
    "lsrb": {"311814 dcqq.prd", "200118 rbq.hpj"},
    "pbgrdvmc": {
        "204425 pddmq",
        "dir rqmhwhc",
        "dir jlcqmq",
        "338348 vnlmlq",
        "119324 cqhdvmzp.npw",
        "257084 sbnhc",
        "277930 jhlrpmqg",
    },
    "pbgrdvmc/jlcqmq": {"24876 mfhzl"},
    "rqmhwhc": {"36575 dlft.dtp"},
    "sbnhc/sbq": {"15689 hpzgsl.svb"},
    "vmslnrmc": {"29838 sbnhc", "dir lcqpws", "136481 nfqs.crt"},
    "vmslnrmc/lcqpws": {"322264 jmtwr.fzj", "18732 sct", "168866 dcqq.pdp"},
    "smfhldss": {"dir wfbssqj"},
    "smfhldss/wfbssqj": {"134050 tgghrp.hjq"},
    "jsv": {"dir bwc", "dir dcqq", "dir vnlmlq", "260913 lzcqm.wzr", "dir rhstw"},
    "jsv/bwc": {
        "dir dcqq",
        "dir gdgh",
        "dir jwrhclh",
        "dir nbwfdvsv",
        "221975 bdv.mfq",
        "101246 gqcfrzmn",
        "dir sbnhc",
        "dir crbnzrtw",
        "dir qnwhfv",
        "dir gsst",
    },
    "jsv/bwc/crbnzrtw": {
        "dir jdh",
        "dir wmjgmd",
        "dir mpgdhg",
        "302165 scpq.gpd",
        "204859 dwvphbm.csz",
        "dir shfhmdw",
        "202360 nfqs.crt",
        "dir sbnhc",
        "dir dmmpcrz",
    },
    "jsv/bwc/crbnzrtw/dmmpcrz": {"dir mfhzl"},
    "jsv/bwc/crbnzrtw/dmmpcrz/mfhzl": {"121861 hbnlqs"},
    "jdh": {"dir dwvphbm"},
    "jdh/dwvphbm": {"8977 ntdtdq"},
    "mpgdhg": {"48235 dcqq"},
    "sbnhc/dbb": {
        "275648 gcsdd.pdw",
        "dir rbbgrtm",
        "111336 sbnhc.qrn",
        "dir rmlm",
        "153146 sct",
    },
    "sbnhc/dbb/rbbgrtm": {"304685 rbq.hpj"},
    "rmlm": {"dir wfr"},
    "rmlm/wfr": {"197220 dhjjr.dqq"},
    "shfhmdw": {"221308 mhnfzmz.gqp"},
    "wmjgmd": {"dir zrtpgbg", "dir psrshrws"},
    "wmjgmd/psrshrws": {"202052 twgfblm"},
    "zrtpgbg": {"48134 hsnzvhvm.gnp"},
    "dcqq": {
        "146747 ltp",
        "90096 wgq.lrm",
        "63600 tlclsj.pvg",
        "181384 tzjn",
        "217679 hbnlqs",
    },
    "gdgh": {"78450 hrcdgnpv.ctz"},
    "gsst": {"199259 sct", "345240 nfqs.crt"},
    "jwrhclh": {
        "dir ftjcr",
        "dir vnlmlq",
        "dir wqjnwgpj",
        "177499 nhdh.bbn",
        "dir sbnhc",
    },
    "jwrhclh/ftjcr": {
        "236133 wdmwgzvs.jnw",
        "dir zwrmjlh",
        "121761 gqp",
        "36602 lcgfmtf.zct",
        "dir rrrrgbqv",
        "dir mfhzl",
        "dir glfptjpb",
    },
    "jwrhclh/ftjcr/glfptjpb": {
        "dir gdphvds",
        "dir fdnppcr",
        "98000 gqhv",
        "dir gchhnd",
    },
    "jwrhclh/ftjcr/glfptjpb/fdnppcr": {"dir dwvphbm", "dir ngsgrgp"},
    "jwrhclh/ftjcr/glfptjpb/fdnppcr/dwvphbm": {"dir wrg"},
    "jwrhclh/ftjcr/glfptjpb/fdnppcr/dwvphbm/wrg": {
        "265022 cqhdvmzp.npw",
        "316916 nfqs.crt",
    },
    "ngsgrgp": {"110198 sct"},
    "gchhnd": {"39462 mfhzl", "253836 hbnlqs", "211458 nfqs.crt"},
    "gdphvds": {"dir dpdb"},
    "gdphvds/dpdb": {"342610 vnlmlq"},
    "mfhzl": {
        "dir cptj",
        "dir cpcczt",
        "dir zdv",
        "dir dcqq",
        "dir dwvphbm",
        "dir pccldwf",
        "dir vnlmlq",
        "47767 nzzcn.qhp",
        "33994 splscqn.tqz",
        "154477 nbphv.pjc",
        "dir qpnncj",
        "166015 jrcqvgf.jdg",
    },
    "mfhzl/cptj": {"100729 nvctqj.gjw"},
    "rrrrgbqv": {"166055 dwvphbm.rvb", "303762 hbnlqs", "277411 wzr.rgz"},
    "zwrmjlh": {"32583 dvfnw"},
    "sbnhc/hwtmwp": {"dir zjmrr"},
    "sbnhc/hwtmwp/zjmrr": {"279103 cqhdvmzp.npw"},
    "vnlmlq/btqsh": {"dir lgh", "34333 rbq.hpj", "dir ljrjpg", "15387 vzldp.ffs"},
    "vnlmlq/btqsh/lgh": {"176966 vnlmlq"},
    "ljrjpg": {
        "180447 sbnhc",
        "dir dwvphbm",
        "251554 rdrbn.clr",
        "dir mfhzl",
        "231230 cqhdvmzp.npw",
    },
    "ljrjpg/dwvphbm": {"dir vghvsmq"},
    "ljrjpg/dwvphbm/vghvsmq": {"dir jqmgn", "132209 cqhdvmzp.npw"},
    "ljrjpg/dwvphbm/vghvsmq/jqmgn": {"95992 clbvg.bmr"},
    "mfhzl/dcqq": {"dir vjhl"},
    "mfhzl/dcqq/vjhl": {"dir nbhmzl"},
    "mfhzl/dcqq/vjhl/nbhmzl": {"155454 sbnhc.flh"},
    "clhclcr": {"268077 njcmcfl.ctm", "dir jwqwhq"},
    "clhclcr/jwqwhq": {"256988 rbq.hpj"},
    "qwbnvzv": {
        "147232 zlmgttpl",
        "131149 lsc.tjj",
        "dir mzhwwrtp",
        "dir hpwpm",
        "dir mfhzl",
        "167852 dln.zrn",
        "201277 sbnhc.pfh",
    },
    "qwbnvzv/hpwpm": {"135194 jpzt.fjn"},
    "mzhwwrtp": {"121846 dwvphbm.lvp", "231983 dgrvfdmp"},
    "vbrc": {"320029 wbhs.mpd"},
    "vfdqq": {
        "dir zfdhthfn",
        "dir qzgwglhc",
        "dir vnlmlq",
        "277998 nfqs.crt",
        "68520 wsc.vhz",
    },
    "vfdqq/qzgwglhc": {"25046 cqhdvmzp.npw", "250876 dwvphbm"},
    "zfdhthfn": {"233242 dstb.hrs", "269387 nfqs.crt"},
    "wqjnwgpj": {"dir vbf", "dir rtlw", "dir hfd", "dir lbft"},
    "wqjnwgpj/hfd": {"224694 cqhdvmzp.npw", "100103 dbmwn.tqz"},
    "lbft": {"60107 hbnlqs"},
    "rtlw": {"dir ntpb"},
    "rtlw/ntpb": {"341166 mfhzl.pvj"},
    "vbf": {"54177 ghrscj.tlh"},
    "nbwfdvsv": {"107273 mptw.qmn"},
    "qnwhfv": {"55633 hbnlqs"},
    "rhstw": {
        "dir clh",
        "dir qrjgl",
        "dir grz",
        "dir tzgrs",
        "dir ntjtzr",
        "dir zrdh",
        "dir rzqp",
    },
    "rhstw/clh": {"212153 cqhdvmzp.npw"},
    "grz": {"346002 cqhdvmzp.npw"},
    "ntjtzr": {"308693 sbnhc.zrv", "271549 rbq.hpj"},
    "qrjgl": {"119344 jfshwj"},
    "rzqp": {"210282 hlmnv.jph", "327891 dcqq", "118199 nfqs.crt", "dir rwh"},
    "rzqp/rwh": {"285057 rmvrnb"},
    "tzgrs": {"23830 cjqrr"},
    "zrdh": {"dir vpnzs", "dir dwvphbm", "dir dcqq", "188911 rbq.hpj"},
    "zrdh/dcqq": {"dir jnncgzgm", "277454 hbnlqs"},
    "zrdh/dcqq/jnncgzgm": {"199664 dcqq.tgm"},
    "dwvphbm": {
        "dir pftcdtd",
        "221700 fgnznr.dhf",
        "340073 sbnhc",
        "108321 qtqhqwnt",
        "337932 sct",
        "224321 hbnlqs",
        "58807 cdbdnrqh.fgq",
        "2613 vdc.nwz",
    },
    "vpnzs": {"254459 fvcf.zcj"},
    "vnlmlq/gfsj": {"dir hddvr"},
    "vnlmlq/gfsj/hddvr": {"dir mqmnzb"},
    "vnlmlq/gfsj/hddvr/mqmnzb": {"341835 jjjh"},
    "mfhzl/pccldwf": {"126977 nvcw", "318605 rljpfnc.dzd"},
    "nljtr": {"dir slztzqd"},
    "nljtr/slztzqd": {
        "dir vnlmlq",
        "55754 bpwghjpg.bfq",
        "319151 vdlmjj.mmn",
        "205753 pfplh",
    },
    "nljtr/slztzqd/vnlmlq": {"dir zpj", "338081 zhjrrs", "dir mfhzl"},
    "nljtr/slztzqd/vnlmlq/mfhzl": {
        "dir dcqq",
        "dir lgfb",
        "343125 vnlmlq.zpr",
        "dir rjbprpnl",
    },
    "nljtr/slztzqd/vnlmlq/mfhzl/dcqq": {"288030 rbq.hpj"},
    "lgfb": {"22119 cqhdvmzp.npw", "238775 wbmnzgt.vnl"},
    "rjbprpnl": {"244896 lvgg.jvz"},
    "zpj": {"339679 dcqq"},
    "nwzp": {"dir vnlmlq", "dir mfhzl"},
    "nwzp/mfhzl": {"107297 dwvphbm.nvb"},
    "vnlmlq/mdj": {"87553 dbtct.nws"},
    "rfwwwgr": {"287719 flpwrp", "74896 mfhzl"},
    "sbnhc/dwvphbm": {"21955 pcqbfbv.bfg"},
    "zhfl": {"180619 wcd.jsr", "dir jvnlhq", "dir vnlmlq"},
    "zhfl/jvnlhq": {
        "dir sdrrzp",
        "20692 clp.vmd",
        "192374 vnlmlq.lvj",
        "91389 jqbp.zss",
        "dir njmdrb",
        "dir sbnhc",
        "dir dbn",
    },
    "zhfl/jvnlhq/dbn": {"293401 dcqq"},
    "njmdrb": {
        "219739 hsdg.rss",
        "dir mllvdccz",
        "270463 dvzbtnbb.vth",
        "285584 mhq",
        "dir mfhzl",
        "dir gdvtg",
        "234503 nfqs.crt",
    },
    "njmdrb/gdvtg": {"27407 rws.vqt", "294243 dllnh"},
    "mfhzl/dwvphbm": {"87960 sct"},
    "qpnncj": {"182692 lqbbz"},
    "mllvdccz": {
        "8251 rbq.hpj",
        "184878 bsjzsmw.pwt",
        "243546 dwvphbm.rdw",
        "184061 dcqq.bbm",
        "dir ftmrszgl",
        "dir tgvchzn",
    },
    "mllvdccz/ftmrszgl": {"257447 npcrg.gjn", "267439 bdrn.gfb"},
    "tgvchzn": {"227775 lqbftlg.scr"},
    "sdrrzp": {"dir dcqq", "7894 gstzs", "dir rnjcrjj", "dir sbnhc"},
    "sdrrzp/dcqq": {"340987 sjb.nss"},
    "rnjcrjj": {"67782 rbq.hpj"},
    "vnlmlq/dwvphbm": {"257972 zccsn.bdr"},
    "jgc": {
        "dir ntz",
        "dir fnvjv",
        "49760 grsw",
        "249818 rgzqq.tlr",
        "85911 cqhdvmzp.npw",
    },
    "jgc/fnvjv": {"288935 dcqq.bsq", "dir nwlbbwtq", "264238 tcwwzs.zwg"},
    "jgc/fnvjv/nwlbbwtq": {"dir qcm", "318151 sbnhc.lwr", "322077 stb.cqj"},
    "jgc/fnvjv/nwlbbwtq/qcm": {
        "147721 crrdn",
        "59476 rbq.hpj",
        "dir gctnt",
        "dir sbnhc",
    },
    "jgc/fnvjv/nwlbbwtq/qcm/gctnt": {"328909 dwvphbm", "82536 rjnz"},
    "sbnhc/vvn": {"79030 vnlmlq", "119247 fztlb.qch"},
    "ntz": {"234879 mfhzl"},
    "lbh": {"dir dwvphbm", "24310 jgsp.ggs", "dir lft"},
    "lbh/dwvphbm": {"295434 rbq.hpj"},
    "lft": {"dir dwvphbm", "dir dcqq", "123657 mfhzl.nhq"},
    "lft/dcqq": {"dir tgp"},
    "lft/dcqq/tgp": {"271647 gmmq.tmp"},
    "dwvphbm/pftcdtd": {"28073 hwqzcr.zcp"},
    "lrwt": {"38953 hzhzfw.tpv", "59885 vnlmlq"},
    "rhszw": {
        "20071 rhdbms",
        "dir hsfbh",
        "dir mmflqvsd",
        "dir vnlmlq",
        "162563 rpjjld",
    },
    "rhszw/hsfbh": {
        "255050 lglw.jvw",
        "99814 pzvw",
        "dir wnwztl",
        "28443 sbct.hng",
        "168934 sbnhc.fnt",
    },
    "rhszw/hsfbh/wnwztl": {
        "215806 dcqq",
        "dir brwhjj",
        "214967 mqhv.wwq",
        "82998 vcm.mhc",
    },
    "rhszw/hsfbh/wnwztl/brwhjj": {"171935 rbq.hpj"},
    "mmflqvsd": {"109141 dcqq.mdc"},
    "vnlmlq/blggqt": {"195700 ntv.zjn"},
    "fpw": {"143105 sct"},
    "mfhzl/cpcczt": {"209755 vnlmlq.lbw"},
    "zdv": {"335546 sbnhc.ccg"},
    "mtg": {"dir zdtnqtcw", "240873 tpvqthc.ljw", "244632 dcqq.frr"},
    "mtg/zdtnqtcw": {"80980 nfqs.crt"},
    "vnlmlq/dcqq": {"142227 cqhdvmzp.npw", "199798 twqppvs"},
    "qnv": {
        "240044 nfqs.crt",
        "49861 pwsgmlq.hcw",
        "273687 jhqt.glz",
        "244311 cqhdvmzp.npw",
        "dir mnrh",
        "dir rdrs",
        "126195 vnlmlq.frr",
    },
    "qnv/mnrh": {"276125 hbnlqs"},
    "rdrs": {
        "116081 nfqs.crt",
        "213018 dwvphbm",
        "13785 hbnlqs",
        "154367 rbq.hpj",
        "dir dqgw",
        "dir lbpjczw",
        "77634 sct",
    },
    "rdrs/dqgw": {"dir rpcfdr"},
    "rdrs/dqgw/rpcfdr": {"dir swvlhbg"},
    "rdrs/dqgw/rpcfdr/swvlhbg": {"309244 sct"},
    "lbpjczw": {"69436 rbq.hpj"},
    "rdvq": {
        "128806 dcqq.qzr",
        "dir hht",
        "165359 jzj.rqv",
        "dir sbnhc",
        "64132 dcqq.vgc",
    },
    "rdvq/hht": {"dir vnlmlq"},
    "rdvq/hht/vnlmlq": {"49895 wct"},
}


def _dfs(tree: dict[str, set[str]], node: str, size_map: dict[str, int]):
    size = 0
    if node in tree:
        for child in tree[node]:
            if child.split(" ")[0] == "dir":
                if node == "/":
                    new_node = child.split(" ")[1]
                else:
                    new_node = node + "/" + child.split(" ")[1]
                s, _ = _dfs(tree, new_node, size_map)
                size += s
            else:
                size += int(child.split(" ")[0])
        size_map[node] = size
    return size, size_map


def _parse_terminal_output(file_path: Path) -> dict:
    with open(file_path, "r") as puzzle_input:
        lines = puzzle_input.read().strip().splitlines()
        current_dir_name = ""
        tree = defaultdict(set)
        path = []
        for line in lines:
            parts = line.split(" ")
            if parts == ["$", "ls"]:
                continue
            elif parts == ["$", "cd", ".."]:
                current_dir_name = path[:1].pop()
            elif parts[0] == "$" and parts[1] == "cd" and parts[2] != "..":
                prev_dir_name = current_dir_name
                current_dir_name = parts[2]
                if current_dir_name != "/" and prev_dir_name != "/":
                    current_dir_name = prev_dir_name + "/" + current_dir_name
                path.append(current_dir_name)
            else:
                tree[current_dir_name].add(" ".join(parts))
        return dict(tree)


@timer
def part_one(file: str, day: int = 7, year: int = 2022) -> int:
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    tree = _parse_terminal_output(file_path=input_file_path)
    size_map = {dir_name: 0 for dir_name in tree}
    root_dir_size, size_map = _dfs(tree=tree, node="/", size_map=size_map)
    print(f"{root_dir_size=}")
    print(f"{size_map=}")
    total = 0
    for dir_name, dir_size in size_map.items():
        if dir_size <= 100000:
            total += dir_size
    return total


part_one(file="eg")
part_one(file="input")


@timer
def part_two(file: str, day: int = 7, year: int = 2022):
    input_file_path: Path = Path(__file__).resolve().parents[2] / INPUT_PATH.format(
        year=year, day=day, file=file
    )
    return _parse_terminal_output(file_path=input_file_path)


# part_two(file="eg")
# part_two(file="input")
