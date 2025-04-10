def konverter_fil(inndata):
    # Lag ny header-linje med ønskede kolonnenavn
    ny_header = '"Date";"Explanation";"Rentdate";"Amount"\n'
    
    # Behandle hver linje i inndata
    nye_linjer = []
    for linje in inndata.split('\n'):
        # Hopp over header-linjen
        if linje.startswith('"Dato"'):
            continue
            
        # Del opp linjen i verdier
        verdier = linje.split(';')
        
        # Velg ut ønskede kolonner og håndter beløp
        dato = verdier[0]
        forklaring = verdier[1].replace('Reservert transaksjon ', '')
        rentedato = verdier[2]
        
        # Finn beløpet - sjekk både "Ut fra konto" og "Inn på konto"
        belop = ''
        if verdier[3] != '""':
            belop = '-' + str(verdier[3])
        elif verdier[4]:  # Sjekk "Inn på konto"
            belop = str(verdier[4])
        
        # Lag ny linje med ønsket format
        nye_linjer.append(f'{dato};{forklaring};{rentedato};"{belop}"')
    
    # Kombiner header og alle linjer
    return ny_header + '\n'.join(nye_linjer)

# Eksempel på bruk
inndata = open("dnb.txt", "r", encoding="utf-8").read()

resultat = konverter_fil(inndata)
print(resultat)

with open("out.txt", "w", encoding="utf-8") as fil:
    fil.write(resultat)