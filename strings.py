example = "atsizatabeg development zone"

print(len(example)) #Kaç kelime olduğunu sayar
print(example[0:12]) #Girilen karakter sayısında bulunan yazıyı gösterir.
print(example[:12]) #Sıfır ile girdiğiniz karakter sayısında bulunan yazıyı gösterir.
print(example.title()) #Her kelimenin baş harfini büyütür.
print(example.upper()) #Bütün yazıyı büyük harf ile yazar.
print(example.lower())  #Bütün yazıları küçük harf ile yazar.
print(example.count('x')) #Hangi harfi girerseniz o harften kaç adet olduğunu gösterir.
print(example.find("n")) #Hangi harfi girerseniz o harfin kaçıncı karakter olduğunu gösterir. Yoksa -1
print(example.replace("zone", "bölgesi")) #Girdiğiniz yazıyı başka yazı ile değiştirir.
print(dir(example)) #String ile ilgili kullanabileceğiniz metodları gösterir.
print(help(str)) #String ile ilgili yardım dökümanlarını gösterir.