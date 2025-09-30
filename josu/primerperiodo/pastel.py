arroz=False
leche=True
canela=False

if arroz==True:
    print("Usted puede hacer el arroz con leche")
elif arroz==False:
    ans=input("Puede comprar el arroz?")
    if ans=="si":
        print("Ya tiene los ingredientes para hacer el arroz con leche")
    else:
        print("Ya no hay forma de hacer el arroz con leche")

else:
    print(f"Usted no puede hacer el arroz, le falta {arroz}")