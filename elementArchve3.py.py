
# %%
import threading


#Group is the y axis on the periodic table and determines the patterns and extra fe4eatures of each element dragon

class Group:
    def __init__(self, features, pattern):
        self.features = features
        self.pattern = pattern


#Period is the x axis on the periodic table and determines the number of horns each element dragon has

class Period:
    def __init__(self, horns):
        self.horns = horns


class Dragon:
    def __init__(self, name):
        self.name = name
        #self.period = period

# %%

        #The listed features and patterns
       
        group_specs = {
            "one":      (["Mane Spikes", "Talons", "Ankle Spurs"], "Stripes"),
            "two":      (["Talons", "Ankle Spurs"], "Diamonds"),
            "three":    (["Devil Tail", "Ankle Spurs"], "Dorsal Stripe 1"),
            "four":     (["Devil Tail", "Spines"], "Dorsal Stripe 2"),
            "five":     (["Devil Tail", "Breast Plate", "Spines"], "Dorsal Stripe 3"),
            "six":      (["Breast Plate", "Spines"], "Dorsal Stripe 4"),
            "seven":    (["Breast Plate", "Spines"], "Dorsal Stripe 5"),
            "eight":    (["Talons", "Breast Plate", "Spines"], "Dorsal Stripe 6"),
            "nine":     (["Talons", "Mane Spikes", "Breast Plate"], "Dorsal Stripe 7"),
            "ten":      (["Talons", "Mane Spikes", "Breast Plate"], "Dorsal Stripe 8"),
            "eleven":   (["Talons", "Mane Spikes", "Breast Plate"], "Dorsal Stripe 9"),
            "twelve":   (["Talons", "Mane Spikes", "Breast Plate"], "Dorsal Stripe 10"),
            "thirteen": (["Mane Spikes", "Fur Tufts"], "Toes"),
            "fourteen": (["Talons", "Mane Spikes", "Fur Tufts"], "Freckles"),
            "fifteen":  (["Talons", "Fur Tufts"], "Spots"),
            "sixteen":  (["Mane", "Fur Tufts"], "Tipped"),
            "seventeen":(["Feathers", "Mane", "Breast Plate"], "Cheeks"),
            "eighteen": (["Feathers", "Mane"], "Goggles"),
        }

        for name, (features, pattern) in group_specs.items():
            setattr(self, name, Group(features, pattern))


def show_hint():
    # Only PRINT a hint; do not call input() here
    print("\n(For example: H, Hydrogen, or 1)")

# Arm a one-shot 5s timer to print the hint while we wait for input
timer = threading.Timer(5.0, show_hint)
timer.start()

#This directs the input to enter the element the user is retreiving information about, inside a loop for repeating inputs

while True:
        element = input("Enter the element name, symbol, or atomic number: ")        

        if element == "exit" or element == "quit":                
                break


            # could give examples of what to write
            # Examples: "H", "He", "Hydrogen", "Helium", "1", "2", maybe with a delay
            #could make a user interface, tkinter


# %%

#The following code retreives the information about the element dragon based on the input

        if element == "hydrogen" or element == "Hydrogen" or element == "H" or element == "1":
                H = Dragon("Hydrogen")
                print("Pattern:", H.one.pattern)       # Stripes
                print("Features:", H.one.features)      # ['Mane Spikes', 'Talons', 'Ankle Spurs']
                print("Horns:", 1)

        elif element == "helium" or element == "Helium" or element == "He" or element == "2":
                He = Dragon("Helium")
                print("Pattern:",He.eighteen.pattern)   # Goggles
                print("Features:", He.eighteen.features)  # ['Feathers', 'Mane']
                print("Horns:", 1)

        elif element == "lithium" or element == "Lithium" or element == "Li" or element == "3":
                Li = Dragon("Lithium")
                print("Pattern:", Li.one.pattern)       # Stripes
                print("Features:", Li.one.features)      # ['Mane Spikes', 'Talons', 'Ankle Spurs']
                print("Horns:", 2)

        elif element == "beryllium" or element == "Beryllium" or element == "Be" or element == "4":
                Be = Dragon("Beryllium")
                print("Pattern:", Be.two.pattern)      
                print("Features:", Be.two.features)    
                print("Horns:", 2)

        elif element == "boron" or element == "Boron" or element == "B" or element == "5":
                B = Dragon("Boron")
                print("Pattern:", B.thirteen.pattern)  
                print("Features:", B.thirteen.features)  
                print("Horns:", 3)

        elif element == "carbon" or element == "Carbon" or element == "C" or element == "6":
                C = Dragon("Carbon")
                print("Pattern:", C.fourteen.pattern)    
                print("Features:", C.fourteen.features)   
                print("Horns:", 2)

        elif element == "nitrogen" or element == "Nitrogen" or element == "N" or element == "7":
                N = Dragon("Nitrogen")
                print("Pattern:", N.fifteen.pattern)   
                print("Features:", N.fifteen.features)  
                print("Horns:", 2)

        elif element == "oxygen" or element == "Oxygen" or element == "O" or element == "8":
                O = Dragon("Oxygen")
                print("Pattern:", O.sixteen.pattern)   
                print("Features:", O.sixteen.features) 
                print("Horns:", 2)

        elif element == "fluorine" or element == "Fluorine" or element == "F" or element == "9":
                F = Dragon("Fluorine")
                print("Pattern:", F.seventeen.pattern)   
                print("Features:", F.seventeen.features)  
                print("Horns:", 2)

        elif element == "neon" or element == "Neon" or element == "Ne" or element == "10":
                Ne = Dragon("Neon")
                print("Pattern:", Ne.eighteen.pattern)   
                print("Features:", Ne.eighteen.features)  
                print("Horns:", 2)

        elif element == "sodium" or element == "Sodium" or element == "Na" or element == "11":
                Na = Dragon("Sodium")
                print("Pattern:", Na.one.pattern)      
                print("Features:", Na.one.features)     
                print("Horns:", 3)

        elif element == "magnesium" or element == "Magnesium" or element == "Mg" or element == "12":
                Mg = Dragon("Magnesium")
                print("Pattern:", Mg.two.pattern)    
                print("Features:", Mg.two.features)     
                print("Horns:", 3)

        elif element == "aluminum" or element == "Aluminum" or element == "Al" or element == "13":
                Al = Dragon("Aluminum")
                print("Pattern:", Al.thirteen.pattern)   
                print("Features:", Al.thirteen.features)  
                print("Horns:", 3)

        elif element == "silicon" or element == "Silicon" or element == "Si" or element == "14":
                Si = Dragon("Silicon")
                print("Pattern:", Si.fourteen.pattern)    
                print("Features:", Si.fourteen.features)  
                print("Horns:", 3)

        elif element == "phosphorus" or element == "Phosphorus" or element == "P" or element == "15":
                P = Dragon("Phosphorus")
                print("Pattern:", P.fifteen.pattern)  
                print("Features:", P.fifteen.features)  
                print("Horns:", 3)

        elif element == "sulfur" or element == "Sulfur" or element == "S" or element == "16":
                S = Dragon("Sulfur")
                print("Pattern:", S.sixteen.pattern)   
                print("Features:", S.sixteen.features)  
                print("Horns:", 3)

        elif element == "chlorine" or element == "Chlorine" or element == "Cl" or element == "17":
                Cl = Dragon("Chlorine")
                print("Pattern:", Cl.seventeen.pattern)   
                print("Features:", Cl.seventeen.features) 
                print("Horns:", 3)

        elif element == "argon" or element == "Argon" or element == "Ar" or element == "18":
                Ar = Dragon("Argon")
                print("Pattern:", Ar.eighteen.pattern)   
                print("Features:", Ar.eighteen.features)  
                print("Horns:", 3)

        elif element == "potassium" or element == "Potassium" or element == "K" or element == "19":
                K = Dragon("Potassium")
                print("Pattern:", K.one.pattern)      
                print("Features:", K.one.features)      
                print("Horns:", 4)

        elif element == "calcium" or element == "Calcium" or element == "Ca" or element == "20":
                Ca = Dragon("Calcium")
                print("Pattern:", Ca.two.pattern)      
                print("Features:", Ca.two.features)    
                print("Horns:", 4)

        elif element == "scandium" or element == "Scandium" or element == "Sc" or element == "21":
                Sc = Dragon("Scandium")
                print("Pattern:", Sc.three.pattern)   
                print("Features:", Sc.three.features)  
                print("Horns:", 4)

        elif element == "titanium" or element == "Titanium" or element == "Ti" or element == "22":
                Ti = Dragon("Titanium")
                print("Pattern:", Ti.four.pattern)    
                print("Features:", Ti.four.features)  
                print("Horns:", 4)

        elif element == "vanadium" or element == "Vanadium" or element == "V" or element == "23":
                V = Dragon("Vanadium")
                print("Pattern:", V.five.pattern)   
                print("Features:", V.five.features)  
                print("Horns:", 4)

        elif element == "chromium" or element == "Chromium" or element == "Cr" or element == "24":
                Cr = Dragon("Chromium")
                print("Pattern:", Cr.six.pattern)   
                print("Features:", Cr.six.features)  
                print("Horns:", 4)

        elif element == "manganese" or element == "Manganese" or element == "Mn" or element == "25":
                Mn = Dragon("Manganese")
                print("Pattern:", Mn.seven.pattern)   
                print("Features:", Mn.seven.features)  
                print("Horns:", 4)

        elif element == "iron" or element == "Iron" or element == "Fe" or element == "26":
                Fe = Dragon("Iron")
                print("Pattern:", Fe.eight.pattern)   
                print("Features:", Fe.eight.features)  
                print("Horns:", 4)

        elif element == "cobalt" or element == "Cobalt" or element == "Co" or element == "27":
                Co = Dragon("Cobalt")
                print("Pattern:", Co.nine.pattern)       
                print("Features:", Co.nine.features)      
                print("Horns:", 4)

        elif element == "nickel" or element == "Nickel" or element == "Ni" or element == "28":
                Ni = Dragon("Nickel")
                print("Pattern:", Ni.ten.pattern)       
                print("Features:", Ni.ten.features)      
                print("Horns:", 4)

        elif element == "copper" or element == "Copper" or element == "Cu" or element == "29":
                Cu = Dragon("Copper")
                print("Pattern:", Cu.eleven.pattern)   
                print("Features:", Cu.eleven.features)  
                print("Horns:", 4)

        elif element == "zinc" or element == "Zinc" or element == "Zn" or element == "30":
                Zn = Dragon("Zinc")
                print("Pattern:", Zn.twelve.pattern)    
                print("Features:", Zn.twelve.features)   
                print("Horns:", 4)

        elif element == "gallium" or element == "Gallium" or element == "Ga" or element == "31":
                Ga = Dragon("Gallium")
                print("Pattern:", Ga.thirteen.pattern)   
                print("Features:", Ga.thirteen.features) 
                print("Horns:", 4)

        elif element == "germanium" or element == "Germanium" or element == "Ge" or element == "32":
                Ge = Dragon("Germanium")
                print("Pattern:", Ge.fourteen.pattern)   
                print("Features:", Ge.fourteen.features)  
                print("Horns:", 4)

        elif element == "arsenic" or element == "Arsenic" or element == "As" or element == "33":
                As = Dragon("Arsenic")
                print("Pattern:", As.fifteen.pattern)   
                print("Features:", As.fifteen.features)  
                print("Horns:", 4)

        elif element == "selenium" or element == "Selenium" or element == "Se" or element == "34":
                Se = Dragon("Selenium")
                print("Pattern:", Se.sixteen.pattern)   
                print("Features:", Se.sixteen.features)  
                print("Horns:", 4)

        elif element == "bromine" or element == "Bromine" or element == "Br" or element == "35":
                Br = Dragon("Bromine")
                print("Pattern:", Br.seventeen.pattern)   
                print("Features:", Br.seventeen.features)  
                print("Horns:", 4)

        elif element == "krypton" or element == "Krypton" or element == "Kr" or element == "36":
                Kr = Dragon("Krypton")
                print("Pattern:", Kr.eighteen.pattern)   
                print("Features:", Kr.eighteen.features)  
                print("Horns:", 4)

        elif element == "rubidium" or element == "Rubidium" or element == "Rb" or element == "37":
                Rb = Dragon("Rubidium")
                print("Pattern:", Rb.one.pattern)       
                print("Features:", Rb.one.features)      
                print("Horns:", 5)

        elif element == "strontium" or element == "Strontium" or element == "Sr" or element == "38":
                Sr = Dragon("Strontium")
                print("Pattern:", Sr.two.pattern)      
                print("Features:", Sr.two.features)      
                print("Horns:", 5)

        elif element == "yttrium" or element == "Yttrium" or element == "Y" or element == "39":
                Y = Dragon("Yttrium")
                print("Pattern:", Y.three.pattern)   
                print("Features:", Y.three.features)  
                print("Horns:", 5)

        elif element == "zirconium" or element == "Zirconium" or element == "Zr" or element == "40":
                Zr = Dragon("Zirconium")
                print("Pattern:", Zr.four.pattern)
                print("Features:", Zr.four.features)
                print("Horns:", 5)

        elif element == "niobium" or element == "Niobium" or element == "Nb" or element == "41":
                Nb = Dragon("Niobium")
                print("Pattern:", Nb.five.pattern)   
                print("Features:", Nb.five.features)  
                print("Horns:", 5)

        elif element == "molybdenum" or element == "Molybdenum" or element == "Mo" or element == "42":
                Mo = Dragon("Molybdenum")
                print("Pattern:", Mo.six.pattern)   
                print("Features:", Mo.six.features)
                print("Horns:", 5)

        elif element == "technetium" or element == "Technetium" or element == "Tc" or element == "43":
                Tc = Dragon("Technetium")
                print("Pattern:", Tc.seven.pattern)  
                print("Features:", Tc.seven.features)
                print("Horns:", 5)

        elif element == "ruthenium" or element == "Ruthenium" or element == "Ru" or element == "44":
                Ru = Dragon("Ruthenium")
                print("Pattern:", Ru.eight.pattern)   
                print("Features:", Ru.eight.features) 
                print("Horns:", 5)

        elif element == "rhodium" or element == "Rhodium" or element == "Rh" or element == "45":
                Rh = Dragon("Rhodium")
                print("Pattern:", Rh.nine.pattern)       
                print("Features:", Rh.nine.features)     
                print("Horns:", 5)

        elif element == "palladium" or element == "Palladium" or element == "Pd" or element == "46":
                Pd = Dragon("Palladium")
                print("Pattern:", Pd.ten.pattern)       
                print("Features:", Pd.ten.features)      
                print("Horns:", 5)

        elif element == "silver" or element == "Silver" or element == "Ag" or element == "47":
                Ag = Dragon("Silver")
                print("Pattern:", Ag.eleven.pattern)   
                print("Features:", Ag.eleven.features)  
                print("Horns:", 5)

        elif element == "cadmium" or element == "Cadmium" or element == "Cd" or element == "48":
                Cd = Dragon("Cadmium")
                print("Pattern:", Cd.twelve.pattern)    
                print("Features:", Cd.twelve.features)   
                print("Horns:", 5)

        elif element == "indium" or element == "Indium" or element == "In" or element == "49":
                In = Dragon("Indium")
                print("Pattern:", In.thirteen.pattern)   
                print("Features:", In.thirteen.features)  
                print("Horns:", 5)  

        elif element == "tin" or element == "Tin" or element == "Sn" or element == "50":
                Sn = Dragon("Tin")
                print("Pattern:", Sn.fourteen.pattern)   
                print("Features:", Sn.fourteen.features)  
                print("Horns:", 5)  

        elif element == "antimony" or element == "Antimony" or element == "Sb" or element == "51":
                Sb = Dragon("Antimony")
                print("Pattern:", Sb.fifteen.pattern)   
                print("Features:", Sb.fifteen.features)  
                print("Horns:", 5)

        elif element == "tellurium" or element == "Tellurium" or element == "Te" or element == "52":
                Te = Dragon("Tellurium")
                print("Pattern:", Te.sixteen.pattern)   
                print("Features:", Te.sixteen.features)  
                print("Horns:", 5)

        elif element == "iodine" or element == "Iodine" or element == "I" or element == "53":
                I = Dragon("Iodine")
                print("Pattern:", I.seventeen.pattern)   
                print("Features:", I.seventeen.features)  
                print("Horns:", 5)

        elif element == "xenon" or element == "Xenon" or element == "Xe" or element == "54":
                Xe = Dragon("Xenon")
                print("Pattern:", Xe.eighteen.pattern)   
                print("Features:", Xe.eighteen.features)  
                print("Horns:", 5)

        elif element == "cesium" or element == "Cesium" or element == "Cs" or element == "55":
                Cs = Dragon("Cesium")
                print("Pattern:", Cs.one.pattern)       
                print("Features:", Cs.one.features)      
                print("Horns:", 6)

        elif element == "barium" or element == "Barium" or element == "Ba" or element == "56":
                Ba = Dragon("Barium")
                print("Pattern:", Ba.two.pattern)      
                print("Features:", Ba.two.features)     
                print("Horns:", 6)  

        elif element == "lanthanum" or element == "Lanthanum" or element == "La" or element == "57":
                La = Dragon("Lanthanum")
                print("Pattern:", La.three.pattern)   
                print("Features:", La.three.features)  
                print("Horns:", 6)

        elif element == "cerium" or element == "Cerium" or element == "Ce" or element == "58":
                Ce = Dragon("Cerium")
                print("Pattern:", Ce.four.pattern)    
                print("Features:", Ce.four.features)  
                print("Horns:", 6)

        elif element == "praseodymium" or element == "Praseodymium" or element == "Pr" or element == "59":
                Pr = Dragon("Praseodymium")
                print("Pattern:", Pr.five.pattern)   
                print("Features:", Pr.five.features)  
                print("Horns:", 6)

        elif element == "neodymium" or element == "Neodymium" or element == "Nd" or element == "60":
                Nd = Dragon("Neodymium")
                print("Pattern:", Nd.six.pattern)   
                print("Features:", Nd.six.features)  
                print("Horns:", 6)

        elif element == "promethium" or element == "Promethium" or element == "Pm" or element == "61":
                Pm = Dragon("Promethium")
                print("Pattern:", Pm.seven.pattern)  
                print("Features:", Pm.seven.features) 
                print("Horns:", 6)

        elif element == "samarium" or element == "Samarium" or element == "Sm" or element == "62":
                Sm = Dragon("Samarium")
                print("Pattern:", Sm.eight.pattern)   
                print("Features:", Sm.eight.features)  
                print("Horns:", 6)

        elif element == "europium" or element == "Europium" or element == "Eu" or element == "63":
                Eu = Dragon("Europium")
                print("Pattern:", Eu.nine.pattern)       
                print("Features:", Eu.nine.features)      
                print("Horns:", 6)

        elif element == "gadolinium" or element == "Gadolinium" or element == "Gd" or element == "64":
                Gd = Dragon("Gadolinium")
                print("Pattern:", Gd.ten.pattern)       
                print("Features:", Gd.ten.features)      
                print("Horns:", 6)

        elif element == "terbium" or element == "Terbium" or element == "Tb" or element == "65":
                Tb = Dragon("Terbium")
                print("Pattern:", Tb.eleven.pattern)   
                print("Features:", Tb.eleven.features)  
                print("Horns:", 6)

        elif element == "dysprosium" or element == "Dysprosium" or element == "Dy" or element == "66":
                Dy = Dragon("Dysprosium")
                print("Pattern:", Dy.twelve.pattern)    
                print("Features:", Dy.twelve.features)   
                print("Horns:", 6)

        elif element == "holmium" or element == "Holmium" or element == "Ho" or element == "67":
                Ho = Dragon("Holmium")
                print("Pattern:", Ho.thirteen.pattern)   
                print("Features:", Ho.thirteen.features)  
                print("Horns:", 6)

        elif element == "erbium" or element == "Erbium" or element == "Er" or element == "68":
                Er = Dragon("Erbium")
                print("Pattern:", Er.fourteen.pattern)   
                print("Features:", Er.fourteen.features)  
                print("Horns:", 6)

        elif element == "thulium" or element == "Thulium" or element == "Tm" or element == "69":
                Tm = Dragon("Thulium")
                print("Pattern:", Tm.fifteen.pattern)   
                print("Features:", Tm.fifteen.features)  
                print("Horns:", 6)

        elif element == "ytterbium" or element == "Ytterbium" or element == "Yb" or element == "70":
                Yb = Dragon("Ytterbium")
                print("Pattern:", Yb.sixteen.pattern)   
                print("Features:", Yb.sixteen.features)  
                print("Horns:", 6)

        elif element == "lutetium" or element == "Lutetium" or element == "Lu" or element == "71":
                Lu = Dragon("Lutetium")
                print("Pattern:", Lu.seventeen.pattern)   
                print("Features:", Lu.seventeen.features)  
                print("Horns:", 6)

        elif element == "hafnium" or element == "Hafnium" or element == "Hf" or element == "72":
                Hf = Dragon("Hafnium")
                print("Pattern:", Hf.four.pattern)   
                print("Features:", Hf.four.features)  
                print("Horns:", 6)

        elif element == "tantalum" or element == "Tantalum" or element == "Ta" or element == "73":
                Ta = Dragon("Tantalum")
                print("Pattern:", Ta.five.pattern)   
                print("Features:", Ta.five.features)  
                print("Horns:", 6)

        elif element == "tungsten" or element == "Tungsten" or element == "W" or element == "74":
                W = Dragon("Tungsten")
                print("Pattern:", W.six.pattern)   
                print("Features:", W.six.features)  
                print("Horns:", 6)

        elif element == "rhenium" or element == "Rhenium" or element == "Re" or element == "75":
                Re = Dragon("Rhenium")
                print("Pattern:", Re.seven.pattern)  
                print("Features:", Re.seven.features) 
                print("Horns:", 6)

        elif element == "osmium" or element == "Osmium" or element == "Os" or element == "76":
                Os = Dragon("Osmium")
                print("Pattern:", Os.eight.pattern)   
                print("Features:", Os.eight.features)  
                print("Horns:", 6)

        elif element == "iridium" or element == "Iridium" or element == "Ir" or element == "77":
                Ir = Dragon("Iridium")
                print("Pattern:", Ir.nine.pattern)       
                print("Features:", Ir.nine.features)     
                print("Horns:", 6)

        elif element == "platinum" or element == "Platinum" or element == "Pt" or element == "78":
                Pt = Dragon("Platinum")
                print("Pattern:", Pt.ten.pattern)       
                print("Features:", Pt.ten.features)      
                print("Horns:", 6)

        elif element == "gold" or element == "Gold" or element == "Au" or element == "79":
                Au = Dragon("Gold")
                print("Pattern:", Au.eleven.pattern)   
                print("Features:", Au.eleven.features)  
                print("Horns:", 6)

        elif element == "mercury" or element == "Mercury" or element == "Hg" or element == "80":
                Hg = Dragon("Mercury")
                print("Pattern:", Hg.twelve.pattern)    
                print("Features:", Hg.twelve.features)   
                print("Horns:", 6)

        elif element == "thallium" or element == "Thallium" or element == "Tl" or element == "81":
                Tl = Dragon("Thallium")
                print("Pattern:", Tl.thirteen.pattern)   
                print("Features:", Tl.thirteen.features)  
                print("Horns:", 6)

        elif element == "lead" or element == "Lead" or element == "Pb" or element == "82":
                Pb = Dragon("Lead")
                print("Pattern:", Pb.fourteen.pattern)   
                print("Features:", Pb.fourteen.features)  
                print("Horns:", 6)

        elif element == "bismuth" or element == "Bismuth" or element == "Bi" or element == "83":
                Bi = Dragon("Bismuth")
                print("Pattern:", Bi.fifteen.pattern)   
                print("Features:", Bi.fifteen.features)  
                print("Horns:", 6)

        elif element == "polonium" or element == "Polonium" or element == "Po" or element == "84":
                Po = Dragon("Polonium")
                print("Pattern:", Po.sixteen.pattern)   
                print("Features:", Po.sixteen.features)  
                print("Horns:", 6)

        elif element == "astatine" or element == "Astatine" or element == "At" or element == "85":
                At = Dragon("Astatine")
                print("Pattern:", At.seventeen.pattern)   
                print("Features:", At.seventeen.features)  
                print("Horns:", 6)

        elif element == "radon" or element == "Radon" or element == "Rn" or element == "86":
                Rn = Dragon("Radon")
                print("Pattern:", Rn.eighteen.pattern)   
                print("Features:", Rn.eighteen.features)  
                print("Horns:", 6)

        elif element == "francium" or element == "Francium" or element == "Fr" or element == "87":
                Fr = Dragon("Francium")
                print("Pattern:", Fr.one.pattern)       
                print("Features:", Fr.one.features)      
                print("Horns:", 7)

        elif element == "radium" or element == "Radium" or element == "Ra" or element == "88":
                Ra = Dragon("Radium")
                print("Pattern:", Ra.two.pattern)      
                print("Features:", Ra.two.features)     
                print("Horns:", 7)

        elif element == "actinium" or element == "Actinium" or element == "Ac" or element == "89":
                Ac = Dragon("Actinium")
                print("Pattern:", Ac.three.pattern)   
                print("Features:", Ac.three.features)  
                print("Horns:", 7)

        elif element == "thorium" or element == "Thorium" or element == "Th" or element == "90":
                Th = Dragon("Thorium")
                print("Pattern:", Th.four.pattern)    
                print("Features:", Th.four.features)  
                print("Horns:", 7)

        elif element == "protactinium" or element == "Protactinium" or element == "Pa" or element == "91":
                Pa = Dragon("Protactinium")
                print("Pattern:", Pa.five.pattern)   
                print("Features:", Pa.five.features)  
                print("Horns:", 7)

        elif element == "uranium" or element == "Uranium" or element == "U" or element == "92":
                U = Dragon("Uranium")
                print("Pattern:", U.six.pattern)   
                print("Features:", U.six.features)  
                print("Horns:", 7)

        elif element == "neptunium" or element == "Neptunium" or element == "Np" or element == "93":
                Np = Dragon("Neptunium")
                print("Pattern:", Np.seven.pattern)  
                print("Features:", Np.seven.features) 
                print("Horns:", 7)

        elif element == "plutonium" or element == "Plutonium" or element == "Pu" or element == "94":
                Pu = Dragon("Plutonium")
                print("Pattern:", Pu.eight.pattern)   
                print("Features:", Pu.eight.features)  
                print("Horns:", 7)

        elif element == "americium" or element == "Americium" or element == "Am" or element == "95":
                Am = Dragon("Americium")
                print("Pattern:", Am.nine.pattern)       
                print("Features:", Am.nine.features)     
                print("Horns:", 7)

        elif element == "curium" or element == "Curium" or element == "Cm" or element == "96":
                Cm = Dragon("Curium")
                print("Pattern:", Cm.ten.pattern)       
                print("Features:", Cm.ten.features)      
                print("Horns:", 7)

        elif element == "berkelium" or element == "Berkelium" or element == "Bk" or element == "97":
                Bk = Dragon("Berkelium")
                print("Pattern:", Bk.eleven.pattern)   
                print("Features:", Bk.eleven.features)  
                print("Horns:", 7)

        elif element == "californium" or element == "Californium" or element == "Cf" or element == "98":
                Cf = Dragon("Californium")
                print("Pattern:", Cf.twelve.pattern)    
                print("Features:", Cf.twelve.features)   
                print("Horns:", 7)

        elif element == "einsteinium" or element == "Einsteinium" or element == "Es" or element == "99":
                Es = Dragon("Einsteinium")
                print("Pattern:", Es.thirteen.pattern)   
                print("Features:", Es.thirteen.features)  
                print("Horns:", 7)

        elif element == "fermium" or element == "Fermium" or element == "Fm" or element == "100":
                Fm = Dragon("Fermium")
                print("Pattern:", Fm.fourteen.pattern)   
                print("Features:", Fm.fourteen.features)  
                print("Horns:", 7)

        elif element == "mendelevium" or element == "Mendelevium" or element == "Md" or element == "101":
                Md = Dragon("Mendelevium")
                print("Pattern:", Md.fifteen.pattern)   
                print("Features:", Md.fifteen.features)  
                print("Horns:", 7)

        elif element == "nobelium" or element == "Nobelium" or element == "No" or element == "102":
                No = Dragon("Nobelium")
                print("Pattern:", No.sixteen.pattern)   
                print("Features:", No.sixteen.features)  
                print("Horns:", 7)

        elif element == "lawrencium" or element == "Lawrencium" or element == "Lr" or element == "103":
                Lr = Dragon("Lawrencium")
                print("Pattern:", Lr.seventeen.pattern)   
                print("Features:", Lr.seventeen.features)  
                print("Horns:", 7)

        elif element == "rutherfordium" or element == "Rutherfordium" or element == "Rf" or element == "104":
                Rf = Dragon("Rutherfordium")
                print("Pattern:", Rf.four.pattern)   
                print("Features:", Rf.four.features)  
                print("Horns:", 7)

        elif element == "dubnium" or element == "Dubnium" or element == "Db" or element == "105":
                Db = Dragon("Dubnium")
                print("Pattern:", Db.five.pattern)   
                print("Features:", Db.five.features)  
                print("Horns:", 7)
                
        elif element == "seaborgium" or element == "Seaborgium" or element == "Sg" or element == "106":
                Sg = Dragon("Seaborgium")
                print("Pattern:", Sg.six.pattern)   
                print("Features:", Sg.six.features)  
                print("Horns:", 7)

        elif element == "bohrium" or element == "Bohrium" or element == "Bh" or element == "107":
                Bh = Dragon("Bohrium")
                print("Pattern:", Bh.seven.pattern)  
                print("Features:", Bh.seven.features) 
                print("Horns:", 7)

        elif element == "hassium" or element == "Hassium" or element == "Hs" or element == "108":
                Hs = Dragon("Hassium")
                print("Pattern:", Hs.eight.pattern)   
                print("Features:", Hs.eight.features)  
                print("Horns:", 7)

        elif element == "meitnerium" or element == "Meitnerium" or element == "Mt" or element == "109":
                Mt = Dragon("Meitnerium")
                print("Pattern:", Mt.nine.pattern)       
                print("Features:", Mt.nine.features)     
                print("Horns:", 7)

        elif element == "darmstadtium" or element == "Darmstadtium" or element == "Ds" or element == "110":
                Ds = Dragon("Darmstadtium")
                print("Pattern:", Ds.ten.pattern)       
                print("Features:", Ds.ten.features)      
                print("Horns:", 7)

        elif element == "roentgenium" or element == "Roentgenium" or element == "Rg" or element == "111":
                Rg = Dragon("Roentgenium")
                print("Pattern:", Rg.eleven.pattern)   
                print("Features:", Rg.eleven.features)  
                print("Horns:", 7)

        elif element == "copernicium" or element == "Copernicium" or element == "Cn" or element == "112":
                Cn = Dragon("Copernicium")
                print("Pattern:", Cn.twelve.pattern)    
                print("Features:", Cn.twelve.features)   
                print("Horns:", 7)

        elif element == "nihonium" or element == "Nihonium" or element == "Nh" or element == "113":
                Nh = Dragon("Nihonium")
                print("Pattern:", Nh.thirteen.pattern)   
                print("Features:", Nh.thirteen.features)  
                print("Horns:", 7)

        elif element == "flerovium" or element == "Flerovium" or element == "Fl" or element == "114":
                Fl = Dragon("Flerovium")
                print("Pattern:", Fl.fourteen.pattern)   
                print("Features:", Fl.fourteen.features)  
                print("Horns:", 7)

        elif element == "moscovium" or element == "Moscovium" or element == "Mc" or element == "115":
                Mc = Dragon("Moscovium")
                print("Pattern:", Mc.fifteen.pattern)   
                print("Features:", Mc.fifteen.features)  
                print("Horns:", 7)

        elif element == "livermorium" or element == "Livermorium" or element == "Lv" or element == "116":
                Lv = Dragon("Livermorium")
                print("Pattern:", Lv.sixteen.pattern)   
                print("Features:", Lv.sixteen.features)  
                print("Horns:", 7)

        elif element == "tennessine" or element == "Tennessine" or element == "Ts" or element == "117": 
                Ts = Dragon("Tennessine")
                print("Pattern:", Ts.seventeen.pattern)   
                print("Features:", Ts.seventeen.features)  
                print("Horns:", 7)

        elif element == "oganesson" or element == "Oganesson" or element == "Og" or element == "118":
                Og = Dragon("Oganesson")
                print("Pattern:", Og.eighteen.pattern)   
                print("Features:", Og.eighteen.features)  
                print("Horns:", 7)


        #This if for incorrect inputs

        else:    
                print("Element not found.")


# If the user answered in time, stop the hint from firing (or stop future ones)
timer.cancel()