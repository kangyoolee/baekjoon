#Julka zaskoczyła wczoraj w przedszkolu swoją wychowawczynię rozwiązując następującą zagadkę:

# Klaudia i Natalia mają razem 10 jabłek, ale Klaudia ma o 2 jabłka więcej niż Natalia. Ile jabłek ma każda z dziewczynek?
# Julka odpowiedziała bez namysłu: Klaudia ma sześć jabłek, natomiast Natalia ma cztery jabłka.

# Wychowywaczyni postanowiła sprawdzić, czy odpowiedź Julki nie była przypadkowa i powtarzała zagadkę, za każdym razem zwiększając liczby jabłek w zadaniu. Julka zawsze odpowiadała prawidłowo. Zaskoczona wychowawczyni chciała kontynuować ,,badanie'' Julki, ale przy bardzo dużych liczbach sama nie potrafiła szybko rozwiązać zagadki. Pomóż pani przedszkolance i napisz program, który będzie podpowiadał jej rozwiązania.

# Napisz program, który:

# wczyta (ze standardowego wejścia) liczbę jabłek, które mają razem obie dziewczynki oraz o ile więcej jabłek ma Klaudia,
# obliczy, ile jabłek ma Klaudia i ile jabłek ma Natalia,
# wypisze wynik (na standardowe wyjście).

a = int(input())
b = int(input())

sum1 = (a+b)//2
sum2 = a-sum1
print(sum1)
print(sum2)

