print("Siemka powiedz mi gdzie najtaniej kupię jabłka")

lidl_input=float(input("Ile kosztują jabłka w Lidlu?"))
biedronka_input=float(input("Ile kosztują jabłka w Biedrze?"))
zabka_input=float(input("Ile kosztują jabłka w Żabce?"))

lower_price=min(lidl_input,biedronka_input,zabka_input)

print("Najtańsze jabłka kosztuja", lower_price)


