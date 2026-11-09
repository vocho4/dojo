import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lessons")
os.makedirs(OUT, exist_ok=True)

def ch(q, o, a, e="", big=None):
    d = {"t": "choice", "q": q, "o": o, "a": a, "e": e}
    if big: d["big"] = big
    return d

def ty(q, a, e="", big=None):
    d = {"t": "type", "q": q, "a": a, "e": e}
    if big: d["big"] = big
    return d

def mt(q, p, e=""):
    return {"t": "match", "q": q, "p": p, "e": e}

def kana(t, r, c):
    return {"t": t, "r": r, "c": c, "lang": "ja-JP"}

def en(t, c):
    return {"t": t, "r": "", "c": c, "lang": "en-US"}

L = []

L.append({
 "id": "l001", "day": 1, "date": "2026-11-08", "lang": "ja", "xp": 30,
 "title": "Pět samohlásek: あいうえお",
 "hook": "V mangách typu Dragon Ball je nad složitými znaky malé hiragana (furigana). Když ho umíš číst, přečteš i je.",
 "intro": "Hiragana je japonské písmo, kterým se píše většina základních slov. Každý znak je jedna slabika. Dnes pět nejjednodušších, a ty znáš z češtiny: a, i, u, e, o.\n\nSlova z dnešních znaků: あい (ai) = láska, いえ (ie) = dům, うえ (ue) = nahoře, あお (ao) = modrá. Modrý je třeba Sonic.",
 "vocab": [kana("あ","a","jako v „auto“"), kana("い","i","jako v „iglú“"), kana("う","u","rty uvolněné"), kana("え","e","jako v „ten“"), kana("お","o","jako v „okno“"),
          kana("あい","ai","láska"), kana("いえ","ie","dům"), kana("うえ","ue","nahoře"), kana("あお","ao","modrá")],
 "exercises": [
  ch("Jak se čte tohle písmeno?", ["a","i","u","e"], 0, "あ = a.", "あ"),
  ch("Jak se čte tohle písmeno?", ["o","i","e","u"], 1, "い = i.", "い"),
  ch("Jak se čte tohle písmeno?", ["u","a","i","o"], 0, "う = u. Rty drž uvolněně.", "う"),
  ch("Jak se čte tohle písmeno?", ["e","o","a","i"], 0, "え = e.", "え"),
  ch("Jak se čte tohle písmeno?", ["u","o","a","e"], 1, "お = o.", "お"),
  mt("Spoj písmeno s hláskou.", [["あ","a"],["い","i"],["う","u"],["え","e"],["お","o"]]),
  ty("Přepiš do romaji (latinkou).", ["ai"], "あい (ai) = láska.", "あい"),
  ch("Co znamená slovo いえ (ie)?", ["dům","láska","modrá","nahoře"], 0, "いえ = dům.", "いえ"),
  ch("Které slovo je „ao“ (modrá)?", ["あお","あい","いえ","うえ"], 0, "あ + お = ao."),
  ty("Přepiš do romaji. Znamená „nahoře“.", ["ue"], "うえ = ue.", "うえ"),
 ]})

L.append({
 "id": "l002", "day": 2, "date": "2026-11-09", "lang": "en", "xp": 30,
 "title": "Letiště: Level 1",
 "hook": "Cesta do Japonska je jako hra o Mariovi: několik levelů za sebou. Dnes level 1, letiště.",
 "intro": "Po přistání potkáš pasovou kontrolu, výdej zavazadel a celnici. Úředníci mluví jednoduše a otázky se opakují. Dnes se naučíš ty nejdůležitější věty. Slova z kartiček si můžeš nechat přečíst.",
 "vocab": [en("passport","pas"), en("boarding pass","palubní vstupenka"), en("luggage","zavazadla"), en("gate","nástupní brána"), en("customs","celnice"), en("baggage claim","výdej zavazadel"), en("holiday","dovolená"), en("Excuse me","promiňte")],
 "exercises": [
  mt("Spoj anglické slovo s českým.", [["passport","pas"],["luggage","zavazadla"],["ticket","letenka"],["gate","nástupní brána"],["customs","celnice"]]),
  ch("Chceš se zeptat, kde je gate 12. Co řekneš?", ["Excuse me, where is gate 12?","Excuse me, what is gate 12?","Sorry, who is gate 12?","Please, gate 12 is where?"], 0, "Where is …? je základní otázka na místo."),
  ty("Doplň: I ___ from the Czech Republic.", ["am"], "I am = I'm."),
  ch("Celník se zeptá: „What is the purpose of your visit?“ Nejlepší odpověď:", ["I am here on holiday with my family.","I am fine, thank you.","Yes, please.","It is Monday."], 0, "Purpose of your visit = důvod návštěvy."),
  ty("Napiš anglicky: Jsem tady na dovolené.", ["i am here on holiday","i am on holiday","i'm here on holiday","i'm on holiday","i am here on vacation","i'm here on vacation","i am on vacation","i'm on vacation"], "Holiday a vacation jsou obě správně."),
  ch("Co znamená „How long are you staying?“", ["Jak dlouho zůstaneš?","Kdy odlétáš?","Kolik ti je let?","Kde bydlíš?"], 0, ""),
  ty("Doplň: We are staying for three ___.", ["weeks"], "Množné číslo: week → weeks."),
  ch("Co znamená „baggage claim“?", ["výdej zavazadel","odlety","pasová kontrola","směnárna"], 0, "Tam si po přistání vyzvedneš kufry."),
 ]})

L.append({
 "id": "l003", "day": 3, "date": "2026-11-10", "lang": "ja", "xp": 30,
 "title": "Řada K: かきくけこ",
 "hook": "Magikarp se v japonštině jmenuje podle kapra „koi“. A dnes se naučíš napsat こい.",
 "intro": "Včera jsi uměl a, i, u, e, o. Dnes přidáš stejné samohlásky s písmenem K před sebou: ka, ki, ku, ke, ko. Až je znáš, přečteš už i slova jako あか (aka, červená) nebo かお (kao, obličej).\n\nPozdrav こんにちは (konnichiwa) znamená „dobrý den“. Začíná znakem こ (ko), tedy dnešním písmenem.",
 "vocab": [kana("か","ka",""), kana("き","ki",""), kana("く","ku",""), kana("け","ke",""), kana("こ","ko",""),
          kana("こい","koi","kapr"), kana("あか","aka","červená"), kana("かお","kao","obličej"), kana("いけ","ike","rybník"), kana("こんにちは","konnichiwa","dobrý den")],
 "exercises": [
  ch("Jak se čte tohle písmeno?", ["ka","ki","ku","ke"], 0, "か = ka.", "か"),
  ch("Jak se čte tohle písmeno?", ["ko","ki","ke","ka"], 1, "き = ki.", "き"),
  ch("Jak se čte tohle písmeno?", ["ke","ku","ko","ka"], 1, "く = ku.", "く"),
  ch("Jak se čte tohle písmeno?", ["ko","ki","ke","ku"], 2, "け = ke.", "け"),
  ch("Jak se čte tohle písmeno?", ["ka","ko","ku","ki"], 1, "こ = ko.", "こ"),
  mt("Spoj písmeno s hláskou.", [["か","ka"],["き","ki"],["く","ku"],["け","ke"],["こ","ko"]]),
  ty("Přepiš do romaji. Znamená „kapr“.", ["koi"], "Magikarp je podle koi.", "こい"),
  ch("Jak se čte slovo あか? Znamená „červená“.", ["aka","ika","uka","eka"], 0, "あ (a) + か (ka).", "あか"),
  ty("Přepiš do romaji. Znamená „obličej“.", ["kao"], "か (ka) + お (o).", "かお"),
  ch("Co znamená いけ (ike)?", ["rybník","dům","obličej","modrá"], 0, "Kapři koi žijí v rybníku.", "いけ"),
  ch("Co znamená こんにちは (konnichiwa)?", ["dobrý den","na shledanou","děkuji","dobrou noc"], 0, ""),
 ]})

L.append({
 "id": "l004", "day": 4, "date": "2026-11-11", "lang": "en", "xp": 30,
 "title": "Restaurace a vegetariáni",
 "hook": "Naruto by měl ramen na každý den. V Japonsku je ale v ramenu často vepřový nebo rybí vývar, takže se vyplatí umět se zeptat.",
 "intro": "Skoro každá japonská polévka se vaří z rybího vývaru dashi. Táta je vegetarián, proto se hodí věta „Is there fish in this?“. Dnes se naučíš objednat, zeptat se na složení a zaplatit.",
 "vocab": [en("rice","rýže"), en("water","voda"), en("noodles","nudle"), en("meat","maso"), en("fish","ryba"), en("vegetables","zelenina"), en("vegetarian","vegetarián"), en("the bill","účet")],
 "exercises": [
  mt("Spoj anglické slovo s českým.", [["rice","rýže"],["water","voda"],["noodles","nudle"],["meat","maso"],["fish","ryba"],["vegetables","zelenina"]]),
  ch("Chceš objednat nudle. Jak to řekneš zdvořile?", ["I would like noodles, please.","Give me noodles.","Noodles now.","I want noodles you."], 0, "I would like … je zdvořilé."),
  ty("Doplň: I would ___ a glass of water, please.", ["like"], ""),
  ch("Chceš vědět, jestli je v jídle ryba. Co řekneš?", ["Is there fish in this?","Is fish this in?","Are fish there?","There fish is?"], 0, "Rybí vývar dashi je v Japonsku skoro všude."),
  ty("Táta je vegetarián. Doplň, co řekne: I am ___. I don't eat meat or fish.", ["vegetarian"], ""),
  ch("Chceš zaplatit. Co řekneš?", ["Could we have the bill, please?","We bill you now.","Bill, go here.","Pay is please?"], 0, ""),
  ty("Napiš anglicky: Voda, prosím.", ["water please","a water please","some water please"], "Please říká zdvořilost."),
  ch("Co znamená „No meat, no fish, please.“?", ["Bez masa a bez ryby, prosím.","Maso a ryby, prosím.","Žádné prosím nechci.","Moc masa, prosím."], 0, ""),
 ]})

L.append({
 "id": "l005", "day": 5, "date": "2026-11-12", "lang": "ja", "xp": 30,
 "title": "Řada S: さしすせそ",
 "hook": "Naruto miluje ramen. Dnes se naučíš napsat すき (suki, mít rád) a すし (sushi).",
 "intro": "Tři dny jsi uměl samohlásky a řadu K. Dnes přidáš řadu S: sa, shi, su, se, so. Pozor: し se čte shi, ne si.\n\nS těmito znaky přečteš すし (sushi), すき (suki, mít rád), そら (sora, obloha), あさ (asa, ráno) a うし (ushi, kráva). Ve slově すき je znak き z lekce 3.",
 "vocab": [kana("さ","sa",""), kana("し","shi","ne si"), kana("す","su",""), kana("せ","se",""), kana("そ","so",""),
          kana("すし","sushi",""), kana("すき","suki","mít rád"), kana("そら","sora","obloha"), kana("あさ","asa","ráno"), kana("うし","ushi","kráva")],
 "exercises": [
  ch("Jak se čte tohle písmeno?", ["sa","su","so","se"], 0, "さ = sa.", "さ"),
  ch("Jak se čte tohle písmeno?", ["si","shi","su","sa"], 1, "し = shi.", "し"),
  ch("Jak se čte tohle písmeno?", ["se","so","su","sa"], 2, "す = su.", "す"),
  ch("Jak se čte tohle písmeno?", ["se","so","su","sa"], 0, "せ = se.", "せ"),
  ch("Jak se čte tohle písmeno?", ["sa","so","shi","se"], 1, "そ = so.", "そ"),
  mt("Spoj písmeno s hláskou.", [["さ","sa"],["し","shi"],["す","su"],["せ","se"],["そ","so"]]),
  ty("Přepiš do romaji. Slavné japonské jídlo.", ["sushi"], "す (su) + し (shi).", "すし"),
  ch("Co znamená すき (suki)?", ["mít rád","nahoře","ráno","kráva"], 0, "す + き. Díky tomu přečteš: Naruto suki.", "すき"),
  ty("Přepiš do romaji. Znamená „obloha“.", ["sora"], "", "そら"),
  ch("Co znamená あさ (asa)?", ["ráno","kapr","dům","modrá"], 0, "", "あさ"),
  ch("Co je うし (ushi)?", ["kráva","obloha","ryba","dům"], 0, "", "うし"),
 ]})

L.append({
 "id": "l006", "day": 6, "date": "2026-11-13", "lang": "en", "xp": 30,
 "title": "Vlaky a cesta městem",
 "hook": "Tokijské metro je jako velké bludiště, ale s pravidly je to jako redstone v Minecraftu: když je znáš, funguje to.",
 "intro": "V Tokiju budeš jezdit hlavně vlakem a metrem. Dnes se naučíš zeptat se na cestu, na nástupiště a na jízdenku, a rozumět pokynům vlevo, vpravo, rovně.",
 "vocab": [en("platform","nástupiště"), en("station","stanice"), en("ticket","jízdenka"), en("left","vlevo"), en("right","vpravo"), en("straight","rovně"), en("delay","zpoždění"), en("Which platform?","Které nástupiště?")],
 "exercises": [
  mt("Spoj anglické slovo s českým.", [["platform","nástupiště"],["station","stanice"],["ticket","jízdenka"],["left","vlevo"],["right","vpravo"],["straight","rovně"]]),
  ch("Co znamená „Does this train go to Shinjuku?“", ["Jede tenhle vlak do Šindžuku?","Kdy jede vlak do Šindžuku?","Kde je Šindžuku?","Kolik stojí Šindžuku?"], 0, ""),
  ty("Doplň: Turn ___ at the station. (vlevo)", ["left"], ""),
  ch("Které je správně: „Jdi rovně a odboč vpravo.“", ["Go straight and turn right.","Go right and turn straight.","Walk left and turn straight.","Turn straight go right."], 0, ""),
  ty("Napiš anglicky: Kde je stanice?", ["where is the station","where is the train station","wheres the station","where is the station please"], "Where is …? se hodí všude."),
  ch("Co znamená „Which platform?“", ["Které nástupiště?","Která stanice?","Jaký vlak?","Kolik stojí?"], 0, ""),
  ch("Vlak má „delay“. Co to je?", ["zpoždění","odjezd","přestup","jízdenka"], 0, ""),
  ty("Doplň: One ticket to Kyoto, ___.", ["please"], ""),
 ]})

files = []
for l in L:
    fn = l["id"] + ".json"
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(l, f, ensure_ascii=False, indent=1)
    files.append(fn)
with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as f:
    json.dump(files, f)
# kontrola: správná odpověď existuje
for l in L:
    for e in l["exercises"]:
        if e["t"] == "choice":
            assert 0 <= e["a"] < len(e["o"]), (l["id"], e["q"])
        if e["t"] == "type":
            assert e["a"], (l["id"], e["q"])
print("OK", len(files), "lekcí")
