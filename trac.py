import prodotti as p

def trac(prodotto):
    print("Righi:", str(len(prodotto.keys())))
    print("")
    for key, value in prodotto.items():
        print(key + "\t" + value)
    print("\n")

oggi = [p.taralli_bianco, p.taralli_biologico]

for x in oggi:
    trac(x)