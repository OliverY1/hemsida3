import base64
import streamlit as st
import random
from streamlit_option_menu import option_menu as op

st.set_page_config(page_title="Youness", page_icon="random", layout="centered", initial_sidebar_state="auto", menu_items={
    "Get help": "https://www.pornhub.com"
},)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def motivation():
    peppande_meningar = [
    "Drömmar är som stjärnor på himlen - låt dem guida dig till ditt öde.",
    "Varje steg mot dina drömmar är ett steg mot din självförverkligande.",
    "Du är kaptenen av ditt eget skepp, styr det mot dina drömmars horisont.",
    "Tro på din förmåga att förvandla drömmar till verklighet.",
    "Världen väntar på att se din potential blomma ut.",
    "Ingenting kan stoppa dig när du brinner för din passion.",
    "Var envis som en myra och stark som en björn när du förföljer dina mål.",
    "Varje misslyckande är bara ett tillfälligt hinder på vägen till framgång.",
    "När du känner dig svag, kom ihåg varför du började.",
    "Ditt mål är värt varje svett dropp och tår.",
    "Du är född för att skina, låt ingen slockna din glöd.",
    "Livet belönar dem som vågar drömma stort och handla modigt.",
    "Vägen till framgång är ibland krokig, men det är värt resan.",
    "Ingenting är omöjligt för den som är fast besluten och villig att arbeta hårt.",
    "Se varje dag som en möjlighet att närma dig dina drömmar.",
    "Ditt liv är din konstverk - måla det med färger av ambition och mod.",
    "Låt dina drömmar vara starkare än dina rädslor.",
    "Framgång kommer till dem som inte ger upp när det blir tufft.",
    "Ge aldrig upp på dig själv - du är starkare än du tror.",
    "Det är aldrig för sent att börja jaga dina drömmar.",
    "Om du kan drömma det, kan du uppnå det med hårt arbete och uthållighet.",
    "Var din egen hjälte och skapa ditt eget sagoslut.",
    "Du är en stjärna som förtjänar att lysa på din egen himmel.",
    "När du når dina drömmar kommer du att inspirera andra att följa sina.",
    "Varje dag är en ny chans att göra ditt liv extraordinärt.",
    "Ditt liv är en bok - skriv ett kapitel fyllt av äventyr och framgång.",
    "Det är inte viktigt hur långsamt du går, så länge du inte stannar.",
    "Ge allt du har, och då kommer livet att ge tillbaka till dig tiofalt.",
    "Du är mer kapabel än du någonsin kunnat föreställa dig.",
    "Drömmar är inte bara för att fantisera om - de är för att förverkligas."
    ]
    h = random.randint(0, 29)
    return peppande_meningar[h]


def fun():
    fun_facts_lista = [
    "Bananer är bär, men jordgubbar är inte det!",
    "Polarisstjärnan, även känd som Polstjärnan, förändrar inte positionen på himlen trots jordens rotation på grund av dess närhet till jordens rotationsaxel.",
    "Honungsbin har ett dansspråk som de använder för att kommunicera med varandra om viktiga platser som matkällor.",
    "Din näsa kan skilja mellan mer än 1 biljon olika lukter!",
    "Havsglasögonen, även kända som maneter, har funnits på jorden i mer än 500 miljoner år, vilket gör dem äldre än dinosaurierna.",
    "Koalor sover i genomsnitt 18 timmar om dagen på grund av deras kost med lågt näringsvärde.",
    "De flesta svalor sover medan de flyger.",
    "Krokodiler är nära släkt med fåglar, inte med ödlor.",
    "Sniglar kan sova i flera år åt gången.",
    "Nästan alla pandor i världen ägs av Kina; till och med de som finns i utlandet lånas bara ut för en begränsad tid.",
    "Vulkaner kan även producera blå lavastötar, vilket beror på närvaron av svavel i magma.",
    "Det finns fler träd på jorden än stjärnor i Vintergatan.",
    "Huggormar kan inte bita under sin sömn.",
    "Den största snöflingan som någonsin registrerats var 38 centimeter bred och 20 centimeter tjock!",
    "Människans tår kan producera ungefär en liter svett per dag.",
    "En vuxen människas kropp består av cirka 7 oktillioner (7 med 27 nollor) atomer.",
    "Flodhästar är faktiskt närmare släkt med valar än med hästar.",
    "Isbjörnar är vänsterhänta.",
    "Man tror att floddelfiner kan använda ekolokalisering för att hitta mat, liknande sättet som valar gör.",
    "Det finns fler än 1500 aktiva vulkaner på jorden.",
    "På månen är det omöjligt att göra ett hål i marken eftersom det inte finns någon atmosfär för att bära bort stoftet och skapa ett hål.",
    "Ormar kan inte bita sin tunga.",
    "Kameleontögon kan rotera oberoende av varandra och fokusera på två olika saker samtidigt.",
    "Koalor har fingeravtryck som liknar mänskliga fingeravtryck.",
    "Ett träd kan producera cirka 260 pund syre per år.",
    "En bläckfisk har tre hjärnor!",
    "På grund av gravitationen på Jupiter skulle du kunna hoppa upp till tre gånger högre än på jorden.",
    "Den kortaste kriget någonsin var mellan Storbritannien och Zanzibar den 27 augusti 1896. Zanzibar gav upp efter 38 minuter.",
    "När du blundar ser du färger och mönster som kallas för \"färg och mönster\" hallucinationer.",
    ]
    v = random.randint(0, 28)
    return(fun_facts_lista[v])



def ragg():
    raggningsrepliker = [
    "Är du en kamera? För varje gång jag ser dig ler jag.",
    "Finns det en flygplats i närheten? För mina fjärilar i magen är på väg att lyfta.",
    "Har du en karta? Jag har gått vilse i dina ögon.",
    "Tror du på kärlek vid första ögonkastet eller ska jag gå förbi igen?",
    "Kan jag få ditt telefonnummer? Jag verkar ha tappat mitt.",
    "Du måste vara trött för du har sprungit runt i mina tankar hela dagen.",
    "Om skönhet var ett brott skulle du vara livstidsdömd.",
    "Kan jag få låna din mobil? Jag måste ringa min mamma och säga att jag har träffat min drömtjej.",
    "Har du feber? För du är het!",
    "Har du ett plåster? För jag skrapade just mitt knä när jag föll för dig.",
    "Tror du på ödet? För jag tror just att jag har träffat mitt.",
    "Är du trött? För du har sprungit runt i mina drömmar hela natten.",
    "Om du var ett ord skulle du vara 'VACKER' i ordboken.",
    "Om skönhet var tid skulle du vara en evighet.",
    "Förlorade du din telefonnummer? Nej? Det är konstigt, för jag trodde du föll från himlen.",
    "Ursäkta mig, men jag tror jag förlorade mitt telefonnummer. Kan jag få ditt?",
    "Vet du vad som skulle se bra ut på dig? Jag.",
    "Förutom att vara vacker, vad gör du för skojigt?",
    "Jag tror du har något i dina ögon... Vänta, det är bara gnistan från hur du ser på mig.",
    "Är du en trollkarl? För när jag ser dig försvinner allt annat.",
    "Finns det en flygplats i närheten? För varje gång jag ser dig känns det som om jag lyfter.",
    "Är du trött? För du har sprungit runt i mina tankar hela natten.",
    "Om skönhet var en stjärna skulle du lysa starkast.",
    "Har du en karta? För jag har gått vilse i dina ögon.",
    "Är du en alien? För du har precis kidnappat mitt hjärta.",
    "Jag är inte en fotograf, men jag kan definitivt föreviga oss tillsammans.",
    "Är du en parkeringsbiljett? För du har 'finaste' skrivet över hela dig.",
    "Om jag var en katt skulle jag spendera alla mina liv med dig.",
    "Jag är inte en tjuv, men jag skulle gärna stjäla ditt hjärta.",
    "Finns det en spegel i din ficka? För jag kan se mig själv i dina byxor.",
    "Har du en solskensdag? För du får min dag att lysa upp."
    ]
    i = random.randint(0, 28)
    return raggningsrepliker[i]

def komplimang():
    komplimang_lista = [
    "Du har en strålande personlighet!",
    "Ditt leende lyser upp hela rummet!",
    "Du är otroligt intelligent!",
    "Din optimism är smittsam!",
    "Din kreativitet är inspirerande!",
    "Du har en fantastisk humor!",
    "Du är väldigt omtänksam och empatisk!",
    "Din styrka och uthållighet är beundransvärd!",
    "Ditt självförtroende är inspirerande!",
    "Du är en fantastisk lyssnare!",
    "Din närvaro gör alltid dagen bättre!",
    "Du är så charmig!",
    "Ditt mod imponerar mig!",
    "Du är så begåvad!",
    "Din vänlighet värmer hjärtat!",
    "Din energi är smittande!",
    "Du är en förebild för många!",
    "Din passion är beundransvärd!",
    "Din generositet känner inga gränser!",
    "Du har en magnetisk personlighet!",
    "Ditt engagemang är enastående!",
    "Du är så pålitlig!",
    "Din entusiasm är inspirerande!",
    "Din karisma är otrolig!",
    "Du är en sådan glädjespridare!",
    "Din positiva attityd är smittsam!",
    "Din empati gör världen till en bättre plats!",
    "Din ödmjukhet är beundransvärd!",
    "Du har en förmåga att göra andra känna sig sedda och uppskattade!",
    "Du är otroligt vacker, både inuti och utanpå!"
    ]
    c = random.randint(0, 28)
    return(komplimang_lista[c])



def skamt():
    skamt_lista = [
    "Varför kunde cykeln inte stå upp själv? För att den var tvåhjulskapabel!",
    "Vad sa en penna till en annan penna? Du skriver så bra!",
    "Varför delar inte astronauter sina skämt? För de landar inte.",
    "Vad sa den ena vågen till den andra vågen? Ingenting, de bara viftade.",
    "Varför blev solen så arg? För att den hade fått solsting.",
    "Vad gjorde en fågel när den var sjuk? Den gick till en flygande doktor.",
    "Varför kan inte bananer vara ensamma? För att de kommer i klungor.",
    "Vad sa den ena ballongen till den andra? Känner du dig uppblåst?",
    "Varför gick pappret till doktorn? För att det var skrivet på.",
    "Vad gjorde havet när det blev argt? Det drog en våg till stranden.",
    "Varför blev bilden arresterad? För att den hängde sig själv.",
    "Vad sa den ena kudden till den andra? Sov gott!",
    "Varför grävde grodan ett hål i golvet? För att den ville komma till underjorden.",
    "Vad kallar man en sovande tjur? En oxcillator.",
    "Varför var toalettpapperet argt? För att det kändes utnyttjat.",
    "Vad sa den ena lampan till den andra? Du lyser upp mitt liv.",
    "Varför var boken så nervös? För att den skulle bli uppläst.",
    "Vad sa ett berg till ett annat berg? Du är klippig!",
    "Varför kan inte dinosaurier dansa? För att de är utdöda.",
    "Vad sa den ena ägget till den andra? Du kläcks mig upp!",
    "Varför delar inte skelett sina hemligheter? För att de har ingen kropp att prata med.",
    "Vad gjorde musen på klockan? Den sprang runt som en tickande bomb.",
    "Varför gick inte nöten över gatan? För att den var rädd för att bli krossad.",
    "Vad gjorde ett träd när det blev hungrigt? Det åt lite lövsmörgås.",
    "Varför gillar inte cyklister att stå stilla? För att de blir upphakade.",
    "Vad sa den ena örat till det andra? Jag är allvarligt bekymrad för dig, du hör inte på mig.",
    "Varför var matematikboken ledsen? För att den hade för många problem.",
    "Vad gjorde den ena skjortan till den andra? Häng mig inte ute att torka!",
    "Varför var pianot så tyst? För att det inte hade några nycklar.",
    "Vad sa den ena skon till den andra? Vad är uppdraget? Vi har gått igenom det tillsammans!",
    ]
    x = random.randint(0,28)
    return(skamt_lista[x])

def sidebar_bg(side_bg):

   side_bg_ext = 'sideback.jpg'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
   
side_bg = 'sideback.jpg'
sidebar_bg(side_bg)

def dep():
    ledsamma_fakta_lista = [
    "Varje dag dör tusentals barn av svält runt om i världen.",
    "Många djurarter riskerar att bli utrotade på grund av människans aktiviteter.",
    "Miljontals människor lever i extrem fattigdom utan tillgång till rent vatten eller tillräcklig näring.",
    "Många människor lider av kroniska sjukdomar och smärtsamma tillstånd utan tillgång till adekvat vård.",
    "Barn över hela världen tvingas arbeta under farliga och exploaterande förhållanden istället för att gå i skolan.",
    "Många människor lever under förtryckande regimer utan möjlighet att uttrycka sig fritt eller leva sina liv i frihet.",
    "Miljoner människor är tvungna att fly från sina hem på grund av krig, konflikter och naturkatastrofer, och många av dem lever i flyktingläger under svåra förhållanden.",
    "Många människor lider av psykisk ohälsa och kämpar dagligen med ångest, depression och andra svåra tillstånd.",
    "Många barn växer upp i dysfunktionella familjer och lider av misshandel, försummelse och andra former av trauma.",
    "Många människor kämpar dagligen för att överleva i en värld som ofta känns orättvis och oberäknelig.",
    "Många äldre människor lever i ensamhet och isolering utan tillräckligt stöd från samhället.",
    "Många människor känner sig ensamma och isolerade, även i en värld där vi är mer uppkopplade än någonsin tidigare.",
    "Många människor kämpar med självhat och självförtroende, och känner sig otillräckliga eller värdelösa.",
    "Många människor lever i ständig rädsla för att bli utnyttjade, övergivna eller förlorade.",
    "Många människor lever i områden som drabbas av krig, konflikter och våld, och tvingas leva sina liv under ständig hotbild.",
    "Många människor har förlorat sina nära och kära till sjukdomar, olyckor eller våldsamheter, och kämpar med sorgen och smärtan av deras förlust.",
    "Många människor känner sig fångade i sina egna tankar och känslor och vet inte hur de ska ta sig ur sin ångest och depression.",
    "Många människor kämpar med missbruk av alkohol, droger eller andra substanser och kämpar för att bryta sig loss från sina beroenden.",
    "Många människor lever i permanent fattigdom och har ingen möjlighet att förbättra sina livsvillkor eller skapa en bättre framtid för sig själva eller sina familjer.",
    "Många människor kämpar med att acceptera sig själva för den de är och känner sig aldrig tillräckligt bra eller värdefulla.",
    "Många människor kämpar med att hitta mening och syfte i sina liv och känner sig vilse och förvirrade i en värld som ibland kan kännas meningslös och tom.",
    "Många människor kämpar med att hantera sina känslor av ilska, hat och förbittring mot sig själva eller andra och kämpar för att förlåta och släppa taget om det förflutna.",
    "Många människor kämpar med att känna sig älskade och uppskattade och känner sig ensamma och övergivna i en värld som ibland kan vara kall och oberörd.",
    "Många människor kämpar med att hitta hopp och tro på en bättre framtid för sig själva och sina nära och kära och känner sig nedslagna och förtvivlade inför framtiden.",
    "Många människor kämpar med att hitta mening och lycka i sina liv och känner sig otillfredsställda och tomma trots materiell framgång och yttre framgångar.",
    "Många människor kämpar med att känna sig accepterade och förstådda av andra och känner sig utfrysta och ensamma i en värld där det kan vara svårt att passa in.",
    "Många människor kämpar med att finna frid och ro i sina liv och känner sig ständigt stressade och överväldigade av krav och förväntningar från andra och sig själva.",
    "Många människor kämpar med att känna sig trygga och säkra i sina liv och känner sig rädda och osäkra i en värld som ibland kan vara farlig och hotfull.",
    "Många människor kämpar med att övervinna sina rädslor och osäkerheter och känner sig fast i sina egna begränsande tankar och beteenden.",
    "Många människor kämpar med att hitta meningen med livet och döden och känner sig vilsna och förvirrade i en värld som ibland kan kännas meningslös och absurd."
    ]

    f = random.randint(0, 28)
    return(ledsamma_fakta_lista[f])



with st.sidebar:
    selected = op(
        menu_title="Meny",
        options=["Hem", "Om oss", "Generator", "Blogg"],
        icons=["house-door-fill", "people-fill", "robot", "journal-text"],
        menu_icon="list",
        default_index=0,
    )

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


col1, col2, col3 = st.columns([4, 4, 4])

if selected == "Hem":
    set_background("bckg.png")
    st.title("Oliver Youness")

    with col1:
        st.image("karim.jpg")
        if st.button("Karim"):
            st.write("Min favorit Karim. Karim är den klantigaste av dem alla. Han har en förmåga att kliva rakt in i situationer utan att tänka och orsakar oavsiktliga skador och olyckor vart han än går. Hans närvaro är som en ticking time bomb av klumpighet.")
    
            
    with col2:
        st.image("meron.jpg")
        if st.button("Meron"):
            st.write("Min favorit apa. Meron är den drömmande idealisten i gruppen. Han har alltid sitt huvud i molnen och tror på det bästa i alla människor. Tyvärr gör hans naivitet honom till ett lätt byte för luriga typer.") 


    with col3:
        st.image("jawsef.jpg")
        if st.button("Jawsef"):
            st.write("Min favorit vattentank. Jawsef är den klumpiga medlemmen av gruppen. Han är ökänd för att ständigt stöta till saker, spilla saker och allmänt orsaka kaos runt omkring sig.")

if selected == "Om oss":
    set_background("bckg.png")
    st.title("Om oss")
    st.write("I en dold by, insvept i skogens tysta sånger och månens sken, samlas fyra själar – Oliver, Karim, Meron och jawsef. Deras liv flätas samman av en gåtfull ödets tråd. Oliver bär en nyckel smidd av månens ljus, Karim har en gåva från jorden, Meron bär solens strålar och Jawsef bär gryningens nyckel. Deras gemensamma sökande tar dem genom dimmiga skogspassager och tätt lövverk, på jakt efter sanningen som vilar i det förlorade arvets skuggor.")

if selected == "Generator":
    set_background("bckg.png")
    st.title("Generera olika saker")
    
    if st.button("Raggningsreplik"):
        st.write(ragg())

    if st.button("Skämt"):
        st.write(skamt())

    if st.button("Komplimang"):
        st.write(komplimang())

    if st.button("Fun fact"):
        st.write(fun())

    if st.button("Depressing fact"):
        st.write(dep())

    if st.button("Motivation"):
        st.write(motivation())

if selected == "Blogg":
    set_background("note.jpg")
    st.title("Blogg")
    st.write("__________________________")
    st.subheader("2024-04-13")
    st.write("Idag har hemsidan lanserats!")
