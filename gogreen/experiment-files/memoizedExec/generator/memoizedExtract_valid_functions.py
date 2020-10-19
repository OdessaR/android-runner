import os
import json
res_gen = """
{"0":"Failed","1":"Failed","2":"Failed","3":"Failed","4":"Failed","5":"Failed","6":"Ok","7":"Failed","8":"Failed","9":"Failed","10":"Failed","11":"Failed","12":"Failed","13":"Failed","14":"Failed","15":"Failed","16":"Failed","17":"Failed","18":"Failed","19":"Failed","20":"Ok","21":"Failed","22":"Failed","23":"Failed","24":"Failed","25":"Failed","26":"Failed","27":"Failed","28":"Failed","29":"Failed","30":"Failed","31":"Failed","32":"Failed","33":"Failed","34":"Failed","35":"Failed","36":"Failed","37":"Failed","38":"Failed","39":"Failed","40":"Failed","41":"Failed","42":"Failed","43":"Failed","44":"Failed","45":"Failed","46":"Failed","47":"Failed","48":"Failed","49":"Failed","50":"Failed","51":"Failed","52":"Failed","53":"Failed","54":"Failed","55":"Failed","56":"Failed","57":"Failed","58":"Failed","59":"Failed","60":"Failed","61":"Failed","62":"Failed","63":"Failed","64":"Failed","65":"Failed","66":"Failed","67":"Failed","68":"Failed","69":"Failed","70":"Failed","71":"Failed","72":"Failed","73":"Failed","74":"Failed","75":"Failed","76":"Failed","77":"Failed","78":"Failed","79":"Failed","80":"Failed","81":"Failed","82":"Failed","83":"Failed","84":"Failed","85":"Failed","86":"Failed","87":"Failed","88":"Failed","89":"Failed","90":"Failed","91":"Failed","92":"Failed","93":"Failed","94":"Failed","95":"Failed","96":"Failed","97":"Failed","98":"Failed","99":"Failed","100":"Failed","101":"Failed","102":"Failed","103":"Failed","104":"Failed","105":"Failed","106":"Failed","107":"Failed","108":"Failed","109":"Failed","110":"Failed","111":"Failed","112":"Failed","113":"Failed","114":"Failed","115":"Failed","116":"Failed","117":"Failed","118":"Failed","119":"Failed","120":"Failed","121":"Failed","122":"Failed","123":"Failed","124":"Failed","125":"Failed","126":"Failed","127":"Failed","128":"Failed","129":"Failed","130":"Failed","131":"Failed","132":"Failed","133":"Failed","134":"Failed","135":"Failed","136":"Failed","137":"Failed","138":"Failed","139":"Failed","140":"Failed","141":"Failed","142":"Failed","143":"Failed","144":"Failed","145":"Failed","146":"Failed","147":"Failed","148":"Failed","149":"Failed","150":"Failed","151":"Failed","152":"Failed","153":"Failed","154":"Failed","155":"Failed","156":"Failed","157":"Failed","158":"Failed","159":"Failed","160":"Failed","161":"Failed","162":"Failed","163":"Failed","164":"Failed","165":"Failed","166":"Failed","167":"Failed","168":"Failed","169":"Failed","170":"Failed","171":"Failed","172":"Failed","173":"Failed","174":"Failed","175":"Failed","176":"Failed","177":"Failed","178":"Failed","179":"Ok","180":"Failed","181":"Failed","182":"Failed","183":"Failed","184":"Failed","185":"Failed","186":"Failed","187":"Failed","188":"Failed","189":"Failed","190":"Failed","191":"Failed","192":"Failed","193":"Failed","194":"Failed","195":"Failed","196":"Ok","197":"Failed","198":"Failed","199":"Failed","200":"Failed","201":"Failed","202":"Failed","203":"Failed","204":"Failed","205":"Failed","206":"Failed","207":"Failed","208":"Failed","209":"Failed","210":"Failed","211":"Failed","212":"Failed","213":"Failed","214":"Failed","215":"Failed","216":"Failed","217":"Failed","218":"Failed","219":"Failed","220":"Failed","221":"Failed","222":"Failed","223":"Failed","224":"Failed","225":"Failed","226":"Failed","227":"Failed","228":"Failed","229":"Failed","230":"Failed","231":"Failed","232":"Failed","233":"Failed","234":"Failed","235":"Failed","236":"Failed","237":"Failed","238":"Failed","239":"Failed","240":"Failed","241":"Failed","242":"Failed","243":"Failed","244":"Failed","245":"Failed","246":"Failed","247":"Failed","248":"Failed","249":"Failed","250":"Failed","251":"Failed","252":"Failed","253":"Failed","254":"Failed","255":"Failed","256":"Failed","257":"Failed","258":"Failed","259":"Failed","260":"Failed","261":"Failed","262":"Failed","263":"Failed","264":"Failed","265":"Failed","266":"Failed","267":"Failed","268":"Failed","269":"Failed","270":"Failed","271":"Failed","272":"Failed","273":"Failed","274":"Failed","275":"Failed","276":"Failed","277":"Failed","278":"Failed","279":"Failed","280":"Failed","281":"Failed","282":"Failed","283":"Failed","284":"Failed","285":"Failed","286":"Failed","287":"Failed","288":"Failed","289":"Failed","290":"Failed","291":"Failed","292":"Failed","293":"Failed","294":"Failed","295":"Failed","296":"Failed","297":"Failed","298":"Failed","299":"Failed","300":"Failed","301":"Failed","302":"Failed","303":"Failed","304":"Failed","305":"Failed","306":"Failed","307":"Failed","308":"Failed","309":"Failed","310":"Failed","311":"Failed","312":"Failed","313":"Failed","314":"Ok","315":"Failed","316":"Failed","317":"Failed","318":"Failed","319":"Failed","320":"Failed","321":"Failed","322":"Ok","323":"Failed","324":"Failed","325":"Failed","326":"Failed","327":"Failed","328":"Failed","329":"Failed","330":"Failed","331":"Failed","332":"Failed","333":"Failed","334":"Failed","335":"Failed","336":"Failed","337":"Failed","338":"Failed","339":"Failed","340":"Failed","341":"Failed","342":"Failed","343":"Failed","344":"Failed","345":"Failed","346":"Failed","347":"Failed","348":"Failed","349":"Failed","350":"Failed","351":"Failed","352":"Failed","353":"Failed","354":"Failed","355":"Failed","356":"Failed","357":"Failed","358":"Ok","359":"Failed","360":"Failed","361":"Failed","362":"Failed","363":"Failed","364":"Failed","365":"Failed","366":"Failed","367":"Failed","368":"Failed","369":"Failed","370":"Failed","371":"Failed","372":"Failed","373":"Failed","374":"Failed","375":"Failed","376":"Failed","377":"Failed","378":"Failed","379":"Failed","380":"Failed","381":"Failed","382":"Failed","383":"Failed","384":"Failed","385":"Failed","386":"Failed","387":"Failed","388":"Failed","389":"Failed","390":"Failed","391":"Failed","392":"Failed","393":"Failed","394":"Failed","395":"Failed","396":"Failed","397":"Failed","398":"Failed","399":"Failed","400":"Failed","401":"Failed","402":"Failed","403":"Failed","404":"Failed","405":"Failed","406":"Failed","407":"Failed","408":"Failed","409":"Failed","410":"Failed","411":"Failed","412":"Failed","413":"Failed","414":"Failed","415":"Failed","416":"Failed","417":"Failed","418":"Failed","419":"Failed","420":"Failed","421":"Failed","422":"Failed","423":"Failed","424":"Failed","425":"Failed","426":"Failed","427":"Failed","428":"Failed","429":"Failed","430":"Failed","431":"Failed","432":"Failed","433":"Ok","434":"Failed","435":"Failed","436":"Failed","437":"Failed","438":"Failed","439":"Failed","440":"Failed","441":"Failed","442":"Failed","443":"Failed","444":"Failed","445":"Failed","446":"Failed","447":"Failed","448":"Failed","449":"Failed","450":"Failed","451":"Failed","452":"Failed","453":"Failed","454":"Failed","455":"Failed","456":"Failed","457":"Failed","458":"Failed","459":"Failed","460":"Failed","461":"Failed","462":"Failed","463":"Failed","464":"Failed","465":"Failed","466":"Failed","467":"Failed","468":"Failed","469":"Failed","470":"Failed","471":"Failed","472":"Failed","473":"Failed","474":"Failed","475":"Failed","476":"Failed","477":"Failed","478":"Failed","479":"Failed","480":"Failed","481":"Failed","482":"Failed","483":"Failed","484":"Failed","485":"Failed","486":"Failed","487":"Failed","488":"Failed","489":"Failed","490":"Failed","491":"Failed","492":"Failed","493":"Failed","494":"Failed","495":"Failed","496":"Failed","497":"Failed","498":"Failed","499":"Failed","500":"Failed","501":"Failed","502":"Failed","503":"Failed","504":"Failed","505":"Failed","506":"Failed","507":"Failed","508":"Failed","509":"Failed","510":"Failed","511":"Failed","512":"Failed","513":"Failed","514":"Failed","515":"Failed","516":"Ok","517":"Failed","518":"Failed","519":"Failed","520":"Failed","521":"Failed","522":"Failed","523":"Failed","524":"Failed","525":"Failed","526":"Failed","527":"Failed","528":"Failed","529":"Ok","530":"Failed","531":"Failed","532":"Failed","533":"Failed","534":"Failed","535":"Failed","536":"Failed","537":"Failed","538":"Failed","539":"Failed","540":"Failed","541":"Failed","542":"Ok","543":"Failed","544":"Failed","545":"Failed","546":"Failed","547":"Failed","548":"Failed","549":"Failed","550":"Failed","551":"Failed","552":"Failed","553":"Failed","554":"Failed","555":"Failed","556":"Failed","557":"Failed","558":"Failed","559":"Failed","560":"Failed","561":"Failed","562":"Failed","563":"Failed","564":"Failed","565":"Failed","566":"Failed","567":"Failed","568":"Failed","569":"Failed","570":"Failed","571":"Failed","572":"Failed","573":"Failed","574":"Failed","575":"Failed","576":"Failed","577":"Failed","578":"Failed","579":"Failed","580":"Failed","581":"Failed","582":"Failed","583":"Failed","584":"Failed","585":"Failed","586":"Failed","587":"Failed","588":"Failed","589":"Failed","590":"Failed","591":"Failed","592":"Failed","593":"Failed","594":"Failed","595":"Failed","596":"Failed","597":"Failed","598":"Failed","599":"Failed","600":"Failed","601":"Failed","602":"Failed","603":"Failed","604":"Failed","605":"Failed","606":"Failed","607":"Failed","608":"Failed","609":"Failed","610":"Failed","611":"Failed","612":"Failed","613":"Failed","614":"Failed","615":"Failed","616":"Failed","617":"Failed","618":"Failed","619":"Ok","620":"Failed","621":"Failed","622":"Failed","623":"Failed","624":"Failed","625":"Failed","626":"Failed","627":"Failed","628":"Failed","629":"Failed","630":"Failed","631":"Failed","632":"Failed","633":"Failed","634":"Failed","635":"Failed","636":"Failed","637":"Failed","639":"Failed","640":"Failed","641":"Failed","642":"Failed","643":"Failed","644":"Failed","646":"Failed","647":"Failed","648":"Failed","649":"Failed","650":"Failed","651":"Ok","652":"Failed","653":"Failed","654":"Failed","655":"Failed","656":"Failed","657":"Failed","658":"Failed","659":"Failed","660":"Failed","661":"Failed","662":"Failed","663":"Failed","664":"Failed","665":"Failed","666":"Failed","667":"Failed","668":"Failed","669":"Failed","670":"Failed","671":"Failed","672":"Failed","673":"Failed","674":"Failed","675":"Failed","676":"Failed","677":"Failed","678":"Failed","679":"Failed","680":"Failed","681":"Failed","682":"Failed","683":"Failed","684":"Failed","685":"Failed","686":"Failed","687":"Failed","688":"Failed","689":"Failed","690":"Failed","691":"Failed","692":"Failed","693":"Ok","694":"Failed","695":"Failed","696":"Failed","697":"Failed","698":"Failed","699":"Failed","700":"Failed","701":"Failed","702":"Failed","703":"Failed","704":"Failed","705":"Failed","706":"Failed","707":"Failed","708":"Failed","709":"Failed","710":"Failed","711":"Failed","712":"Failed","713":"Failed","714":"Failed","715":"Failed","716":"Failed","717":"Failed","718":"Failed","719":"Failed","720":"Failed","721":"Failed","722":"Failed","723":"Failed","724":"Failed","725":"Failed","726":"Failed","727":"Failed","728":"Failed","729":"Failed","730":"Failed","731":"Ok","732":"Failed","733":"Failed","734":"Failed","735":"Failed","736":"Failed","737":"Failed","738":"Failed","739":"Failed","740":"Failed","741":"Failed","742":"Failed","743":"Failed"}
"""
res_gen_anon = """
{"0":"Failed","1":"Failed","2":"Ok","3":"Failed","4":"Failed","5":"Failed","6":"Failed","7":"Failed","8":"Failed","9":"Failed","10":"Failed","11":"Ok","12":"Ok","13":"Failed","14":"Failed","15":"Failed","16":"Failed","17":"Failed","18":"Ok","19":"Failed","20":"Failed","21":"Failed","22":"Failed","23":"Failed","24":"Failed","25":"Failed","26":"Failed","27":"Failed","28":"Failed","29":"Failed","30":"Ok","31":"Failed","32":"Failed","33":"Failed","34":"Failed","35":"Failed","36":"Failed","37":"Failed","38":"Failed","39":"Failed","40":"Failed","41":"Failed","42":"Failed","43":"Failed","44":"Failed","45":"Failed","46":"Failed","47":"Failed","48":"Failed","49":"Failed","50":"Failed","51":"Failed","52":"Failed","53":"Failed","54":"Failed","55":"Ok","56":"Failed","57":"Failed","58":"Failed","59":"Ok","60":"Failed","61":"Failed","62":"Failed","63":"Failed","64":"Failed","65":"Failed","66":"Failed","67":"Failed","68":"Failed","69":"Failed","70":"Failed","71":"Failed","72":"Failed","73":"Failed","74":"Failed","75":"Failed","76":"Failed","77":"Failed","78":"Failed","79":"Failed","80":"Failed","81":"Failed","82":"Failed","83":"Failed","84":"Failed","85":"Failed","86":"Failed","87":"Ok","88":"Failed","89":"Failed","90":"Failed","91":"Failed","92":"Failed","93":"Failed","94":"Failed","95":"Failed","96":"Failed","97":"Failed","98":"Failed","99":"Failed","100":"Failed","101":"Ok","102":"Failed","103":"Failed","104":"Failed","105":"Failed","106":"Failed","107":"Failed","108":"Failed","109":"Failed","110":"Failed","111":"Failed","112":"Failed","113":"Failed","114":"Failed","115":"Ok","116":"Ok","117":"Ok","118":"Ok","119":"Failed","120":"Failed","121":"Failed","122":"Failed","123":"Failed","124":"Failed","125":"Failed","126":"Failed","127":"Failed","128":"Failed","129":"Failed","130":"Failed","131":"Failed","132":"Failed","133":"Failed","134":"Failed","135":"Ok","136":"Failed","137":"Failed","138":"Ok","139":"Failed","140":"Failed","141":"Failed","142":"Failed","143":"Failed","144":"Failed","145":"Failed","146":"Failed","147":"Failed","148":"Failed","149":"Failed","150":"Ok","151":"Failed","152":"Failed","153":"Failed","154":"Failed","155":"Failed","156":"Failed","157":"Ok","158":"Failed","159":"Failed","160":"Failed","161":"Failed","162":"Ok","163":"Failed","164":"Ok","165":"Failed","166":"Ok","167":"Failed","168":"Failed","169":"Failed","170":"Failed","171":"Failed","172":"Ok","173":"Failed","174":"Failed","175":"Ok","176":"Failed","177":"Ok","178":"Failed","179":"Failed","180":"Failed","181":"Failed","182":"Failed","183":"Failed","184":"Failed","185":"Failed","186":"Failed","187":"Failed","188":"Ok","189":"Failed","190":"Failed","191":"Ok","192":"Ok","193":"Failed","194":"Failed","195":"Failed","196":"Failed","197":"Failed","198":"Failed","199":"Failed","200":"Failed","201":"Failed","202":"Failed","203":"Failed","204":"Ok","205":"Ok","206":"Failed","207":"Failed","208":"Failed","209":"Ok","210":"Failed","211":"Failed","212":"Failed","213":"Failed","214":"Failed","215":"Failed","216":"Failed","217":"Failed","218":"Failed","219":"Failed","220":"Ok","221":"Failed","222":"Failed","223":"Failed","224":"Failed","225":"Failed","226":"Failed","227":"Failed","228":"Failed","229":"Failed","230":"Failed","231":"Failed","232":"Failed","233":"Failed","234":"Failed","235":"Failed","236":"Failed","237":"Failed","238":"Failed","239":"Failed","240":"Failed","241":"Failed","242":"Failed","243":"Failed","244":"Failed","245":"Failed","246":"Failed","247":"Failed","248":"Failed","249":"Failed","250":"Failed","251":"Failed","252":"Ok","253":"Failed","254":"Failed","255":"Failed","256":"Failed","257":"Failed","258":"Failed","259":"Failed","260":"Failed","261":"Failed","262":"Failed","263":"Failed","264":"Failed","265":"Failed","266":"Ok","267":"Failed","268":"Failed","269":"Failed","270":"Failed","271":"Failed","272":"Failed","273":"Failed","274":"Failed","275":"Failed","276":"Failed","277":"Failed","278":"Failed","279":"Failed","280":"Failed","281":"Failed","282":"Failed","283":"Failed","284":"Failed","285":"Failed","286":"Failed","287":"Failed","288":"Failed","289":"Failed","290":"Failed","291":"Failed","292":"Failed","293":"Failed","294":"Failed","295":"Ok","296":"Failed","297":"Failed","298":"Ok","299":"Failed","300":"Failed","301":"Failed","302":"Failed","303":"Failed","304":"Failed","305":"Failed","306":"Failed","307":"Failed","308":"Failed","309":"Failed","310":"Failed","311":"Failed","312":"Failed","313":"Failed","314":"Failed","315":"Failed","316":"Failed","317":"Failed","318":"Failed","319":"Failed","320":"Failed","321":"Failed","322":"Failed","323":"Failed","324":"Failed","325":"Failed","326":"Failed","327":"Failed","328":"Failed","329":"Failed","330":"Failed","331":"Ok","332":"Failed","333":"Failed","334":"Failed","335":"Failed","336":"Ok","337":"Failed","338":"Failed","339":"Failed","340":"Failed","341":"Failed","342":"Failed","343":"Failed","344":"Failed","345":"Failed","346":"Failed","347":"Failed","348":"Failed","349":"Failed","350":"Failed","351":"Failed","352":"Failed","353":"Failed","354":"Failed","355":"Failed","356":"Failed","357":"Failed","358":"Failed","359":"Failed","360":"Failed","361":"Failed","362":"Failed","363":"Failed","364":"Failed","365":"Failed","366":"Failed","367":"Failed","368":"Failed","369":"Failed","370":"Failed","371":"Failed","372":"Failed","373":"Failed","374":"Failed","375":"Failed","376":"Failed","377":"Failed","378":"Failed","379":"Failed","380":"Failed","381":"Failed","382":"Failed","383":"Failed","384":"Failed","385":"Failed","386":"Failed","387":"Failed","388":"Failed","389":"Failed","390":"Failed","391":"Failed","392":"Failed","393":"Failed","394":"Failed","395":"Failed","396":"Failed","397":"Failed","398":"Failed","399":"Failed","400":"Failed","401":"Ok","402":"Failed","403":"Failed","404":"Failed","405":"Failed","406":"Failed","407":"Failed","408":"Failed","409":"Failed","410":"Failed","411":"Failed","412":"Failed","413":"Failed","414":"Failed","415":"Failed","416":"Failed","417":"Failed","418":"Failed","419":"Failed","420":"Failed","421":"Failed","422":"Failed","423":"Failed","424":"Failed","425":"Failed","426":"Failed","427":"Failed","428":"Ok","429":"Failed","430":"Failed","431":"Failed","432":"Failed","433":"Failed","434":"Failed","435":"Failed","436":"Failed","437":"Failed","438":"Failed","439":"Failed","440":"Ok","441":"Failed","442":"Failed","443":"Failed","444":"Failed","445":"Failed","446":"Failed","447":"Failed","448":"Failed","449":"Failed","450":"Ok","451":"Ok","452":"Ok","453":"Failed","454":"Failed","455":"Failed","456":"Failed","457":"Failed","458":"Failed","459":"Ok","460":"Ok","461":"Failed","462":"Failed","463":"Failed","464":"Failed","465":"Failed","466":"Failed","467":"Failed","468":"Failed","469":"Failed","470":"Failed","471":"Failed","472":"Failed","473":"Ok","474":"Failed","475":"Failed","476":"Failed","477":"Ok","478":"Failed","479":"Ok","480":"Failed","481":"Failed","482":"Failed","483":"Failed","484":"Failed","485":"Failed","486":"Failed","487":"Failed","488":"Failed","489":"Failed","490":"Failed","491":"Failed","492":"Failed","493":"Failed","494":"Failed","495":"Ok","496":"Ok","497":"Failed","498":"Failed","499":"Failed","500":"Failed","501":"Failed","502":"Failed","503":"Failed","504":"Failed","505":"Failed","506":"Failed","507":"Failed","508":"Ok","509":"Failed","510":"Failed","511":"Failed","512":"Failed","513":"Failed","514":"Failed","515":"Failed","516":"Failed","517":"Failed","518":"Failed","519":"Failed","520":"Ok","521":"Failed","522":"Failed","523":"Ok","524":"Ok","525":"Ok","526":"Failed","527":"Failed","528":"Failed","529":"Failed","530":"Failed","531":"Failed","532":"Failed","533":"Failed","534":"Failed","535":"Failed","536":"Failed","537":"Failed","538":"Ok","539":"Failed","540":"Failed","541":"Failed","542":"Failed","543":"Ok","544":"Failed","545":"Failed","546":"Failed","547":"Failed","548":"Failed","549":"Failed","550":"Failed","551":"Failed","552":"Failed","553":"Failed","554":"Failed","555":"Failed","556":"Failed","557":"Failed","558":"Ok","559":"Failed","560":"Failed","561":"Failed","562":"Failed","563":"Failed","564":"Failed","565":"Failed","566":"Failed","567":"Failed","568":"Failed","569":"Failed","570":"Failed","571":"Ok","572":"Failed","573":"Failed","574":"Failed","575":"Failed","576":"Failed","577":"Failed","578":"Failed","579":"Failed","580":"Failed","581":"Failed","582":"Failed","583":"Failed","584":"Failed","585":"Failed","586":"Failed","587":"Failed","588":"Failed","589":"Failed","590":"Failed","591":"Failed","592":"Failed","593":"Failed","594":"Failed","595":"Failed","596":"Ok","597":"Failed","598":"Ok","599":"Failed","600":"Failed","601":"Failed","602":"Failed","603":"Failed","604":"Failed","605":"Failed","606":"Failed","607":"Failed","608":"Ok","609":"Ok","610":"Ok","611":"Ok","612":"Failed","613":"Failed","614":"Failed","615":"Failed","616":"Failed","617":"Failed","618":"Failed","619":"Failed","620":"Ok","621":"Ok","622":"Failed","623":"Failed","624":"Failed","625":"Ok","626":"Failed","627":"Ok","628":"Failed","629":"Ok","630":"Failed","631":"Ok","632":"Failed","633":"Ok","634":"Failed","635":"Failed","636":"Ok","637":"Failed","638":"Failed","639":"Failed","640":"Failed","641":"Failed","642":"Failed","643":"Failed","644":"Failed","645":"Failed","646":"Ok","647":"Failed","648":"Failed","649":"Failed","650":"Failed","651":"Ok","652":"Failed","653":"Failed","654":"Failed","655":"Failed","656":"Failed","657":"Failed","658":"Failed","659":"Failed","660":"Failed","661":"Failed","662":"Failed","663":"Failed","664":"Failed","665":"Ok","666":"Failed","667":"Failed","668":"Failed","669":"Failed","670":"Failed","671":"Failed","672":"Ok","673":"Failed","674":"Failed","675":"Failed","676":"Failed","677":"Failed","678":"Failed","679":"Failed","680":"Failed","681":"Failed","682":"Ok","683":"Failed","684":"Failed","685":"Failed","686":"Failed","687":"Failed","688":"Failed","689":"Failed","690":"Failed","691":"Failed","692":"Failed","693":"Failed","694":"Failed","695":"Failed","696":"Failed","697":"Failed","698":"Failed","699":"Failed","700":"Failed","701":"Ok","702":"Failed","703":"Failed","704":"Failed","705":"Ok","706":"Failed","707":"Ok","708":"Failed","709":"Failed","710":"Failed","711":"Failed","712":"Failed","713":"Failed","714":"Failed","715":"Failed","716":"Failed","717":"Ok","718":"Failed","719":"Failed","720":"Failed","721":"Failed","722":"Failed","723":"Failed","724":"Failed","725":"Failed","726":"Ok","727":"Failed","728":"Failed","729":"Failed","730":"Failed","731":"Failed","732":"Failed","733":"Failed","734":"Failed","735":"Failed","736":"Ok","737":"Ok","738":"Failed","739":"Failed","740":"Failed","741":"Failed","742":"Ok","743":"Ok","744":"Failed","745":"Failed","746":"Failed","747":"Failed","748":"Ok","749":"Failed","750":"Failed","751":"Failed","752":"Failed","753":"Failed","754":"Ok","755":"Failed","756":"Failed","757":"Failed","758":"Failed","759":"Failed","760":"Ok","761":"Failed","762":"Failed","763":"Failed","764":"Failed","765":"Failed","766":"Failed","767":"Failed","768":"Failed","769":"Failed","770":"Failed","771":"Ok","772":"Failed","773":"Failed"}
"""


tests = json.loads(res_gen)
tests_anon = json.loads(res_gen_anon)

succes_tests = []

for number in tests:
    if tests[number] == "Ok": succes_tests.append({"number":number,"folder":"tests"})

for number in tests_anon:
    if tests_anon[number] == "Ok": succes_tests.append({"number":number,"folder":"tests_anon"})

i = 0
for test in succes_tests:
    path = os.path.sep.join([test["folder"], test["number"] + ".html"])
    if test["folder"] == "tests_anon":
        test["fn_name"] = "testFunc"
        test["anonymous"] = True
        
        head = True
        scan = True
        def_lines = []
        with open(path, "r") as f:
            for line in f.readlines():
                if head:
                    if line.startswith("</head>"): head = False
                    if scan:
                        if line.startswith("<script>"):
                            scan = False
                    else:
                        if line.startswith("</script>"):
                            scan = True
                        else:
                            def_lines.append(line)
                else:
                    break
        succes_tests[i]["def_lines"] = def_lines
    else:
        test["anonymous"] = False
        with open(path, "r") as f:
            next_line = False
            for line in f.readlines():
                if line.startswith("<script src=\"../../websites/"):
                    test["src"] = line[13:].split("\"")[0][3:]

                if next_line:
                    test["fn_name"] = line
                    next_line = False

                if line.startswith("try"):
                    next_line = True


    succes_tests[i] = test
    i += 1


def generate_html_normal(test):
    return """<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">
</head>

<body>
    <!-- memoization lib -->
    <script src="../lib/memoization.js"></script>
    <!-- METADATA (JSON): %s -->
    <!-- ==> CONF: WEBSITE -->
    <script src="%s"></script>

    <!-- exectution -->
    <script type="text/javascript">
        /* ==> CONF: MEMOIZE FUNCTION */
        const memoFunc = memoizer(%s);
        while (true) {
            // memo
            memoFunc
        }
    </script>
</body>
</html>""" % (test, test["src"], test["fn_name"])


def generate_html_anon(test):
    return """<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">
</head>

<body>
    <!-- memoization lib -->
    <script src="../lib/memoization.js"></script>
    <!-- METADATA (JSON): %s -->
    <script>
        %s
    </script>
    <!-- ==> CONF: WEBSITE -->
    <script src="../websites/bitly.com/unauth.js"></script>

    <!-- exectution -->
    <script type="text/javascript">
        /* ==> CONF: MEMOIZE FUNCTION */
        const memoFunc = memoizer(%s);

        while (true) {
            // memo
            memoFunc()
        }
    </script>
</body>
</html>
    """ % (json.dumps(test), "".join(test["def_lines"]), test["fn_name"])


for test in succes_tests:
    dst_path = ".".join(["auto", test["folder"], test["number"], "html"])
    html = ""
    if test["folder"] == "tests_anon":
        html = generate_html_anon(test)
    else:
        html = generate_html_normal(test)
    
    with open(dst_path, "w") as f: f.writelines([html])