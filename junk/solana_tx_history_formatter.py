def konverter_solana_transaksjoner(inndata):
    # Lag ny header-linje med ønskede kolonnenavn, inkludert "Signature"
    ny_header = '"Signature";"Date";"Explanation";"Amount";"Currency"\n'
    
    # Liste for å lagre de konverterte linjene
    nye_linjer = []
    
    # Gå gjennom hver linje i inndata
    for linje in inndata.split('\n'):
        # Hopp over header-linjen
        if linje.startswith('Signature'):
            continue
            
        # Del opp linjen i verdier
        verdier = linje.split(',')
        
        # Hent nødvendige verdier
        signature = verdier[0]  # Hent signaturen fra første kolonne
        tid = verdier[1]
        belop = int(verdier[5])  # Konverter fra string til integer
        flyt = verdier[6]
        fra_adresse = verdier[3]
        til_adresse = verdier[4]
        
        # Konverter Unix-tid til DD.MM.YYYY format
        import datetime
        dato = datetime.datetime.fromtimestamp(int(tid))
        dato_str = dato.strftime('%d.%m.%Y')
        
        # Konverter beløp til desimalformat (USDC har 6 desimaler)
        belop_desimal = belop / (10 ** 6)
        
        # Sett riktig fortegn basert på flyt
        if flyt == 'out':
            belop_desimal = -belop_desimal
            
        # Lag forklaring basert på flyt
        if flyt == 'out':
            forklaring = f"Transfer to {til_adresse}"
        else:
            forklaring = f"Transfer from {fra_adresse}"
            
        # Lag ny linje med ønsket format
        nye_linjer.append(f'"{signature}";"{dato_str}";"{forklaring}";"{belop_desimal:.2f}";"USD"')
    
    # Kombiner header og alle konverterte linjer
    return ny_header + '\n'.join(nye_linjer)

# Eksempel på bruk
inndata = open("in.txt", "r", encoding="utf-8").read()

resultat = konverter_solana_transaksjoner(inndata)
print(resultat)

# Skriver resultatet til utfilen
with open("out.txt", "w", encoding="utf-8") as fil:
    fil.write(resultat)
