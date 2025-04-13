import csv

def konverter_fil(inndata):
    ny_header = '"Date";"Name";"Amount";"Currency";"Explanation"\n'
    
    nye_linjer = []

    reader = csv.reader(inndata.splitlines(), delimiter=',', quotechar='"')

    for index, verdier in enumerate(reader):
        if index == 0:
            continue

        id = verdier[0]
        date = verdier[1]
        native_amount = verdier[2]
        converted_amount = verdier[6]
        currency = verdier[4]
        fee = verdier[11]
        status = verdier[14]
        taxes_on_fee = verdier[16]
        card_id = verdier[17]
        email = verdier[20]

        if converted_amount == "":
            continue

        received_amount = (
            float(converted_amount.replace(",", ".").replace(" ", "")) -
            float(fee.replace(",", ".").replace(" ", "")) -
            float(taxes_on_fee.replace(",", ".").replace(" ", ""))
        )

        print({
            "id": id,
            "date": date,
            "native_amount": native_amount,
            "converted_amount": converted_amount,
            "currency": currency,
            "fee": fee,
            "status": status,
            "taxes_on_fee": taxes_on_fee,
            "card_id": card_id,
            "email": email
        })
        
        date = date.split(' ')[0]
        date = ".".join(date.split('-')[::-1])
        print(fee)
        if status != "Paid":
            continue

        nye_linjer.append(f'{date};"{email if email != "" else card_id}";"{round(received_amount,2)}";"NOK";"{id} / {native_amount} {currency} = {converted_amount} NOK - {fee} NOK fee - {taxes_on_fee} NOK taxes"')
    
    return ny_header + '\n'.join(nye_linjer)

inndata = open("in.txt", "r", encoding="utf-8").read()

resultat = konverter_fil(inndata)
print(resultat)

with open("out.txt", "w", encoding="utf-8") as fil:
    fil.write(resultat)