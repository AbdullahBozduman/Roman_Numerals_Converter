from flask import Flask, render_template, request

# flask bir python kütüphanesidir. Flask ise bir sınıftır.
# render_template ve request birer modüldür.

app = Flask(__name__)

# Flask modülünü başlatır. Modülün adı "name" dir.

# decimal_num//i, sonucu tam sayı olarak verir.
# decimal_num %= i, bölme işleminden kalanı decimal_num a atar.

# diyelim ki girilen sayı 3241.
# roman.keys, sözlükteki anahtar değerlerdir.

# ilk döngüyü yapalım
# for i in roman.keys(1000)
#       num_to_roman += roman[1000]*(3241//1000) -M*3-
#       3241 %= 1000 -241-
#   return num_to_roman -MMM olur-

# ikinci döngüyü yapalım
# for i in roman.keys(900)
#       num_to_roman += roman[900]*(241//900) -CM*0-
#       241 %= 900 -241-
#   return num_to_roman "DEĞER ALMAZ"

# n inci döngüyü yapalım
# for i in roman.keys(100)
#       num_to_roman += roman[100]*(241//100) -C*2-
#       241 %= 100 -41-
#   return num_to_roman CC

# n+.. inci döngüyü yapalım
# for i in roman.keys(40)
#       num_to_roman += roman[40]*(41//40) -XL*1-
#       41 %= 40 -1-
#   return num_to_roman XL

# n+.. inci döngüyü yapalım
# for i in roman.keys(1)
#       num_to_roman += roman[1]*(1//1) -I*1-
#       1 %= 1 
#   return num_to_roman I

# @app.route('/', methods=['POST', 'GET'])
# def main_post():
# main_post() fonksiyonu ile yapılan işlem 
# '/' sayfasında görüntülenecektir.
# reuest.method post ise (ki metot post)
# girilen sayı alpha'ya atanır.
# alpha numerik değilse index.html'e gidilir, developer ismi girilir, not valid=True olduğu için paragraf yazdırılır.
# girilen sayı integer yapılır ve number değerine atanır.
# 0 < sayı < 4000 değilse index.html'e gidilir, developer ismi girilir, not valid=True olduğu için paragraf yazdırılır.
# girilen sayı şartları sağlıyorsa result html e gidilir ve değişkenler yerlerine atanarak sayfa gösterilir.
# eğer metod post değilse index.html sayfası görüntülenir ama hata yazısı gösterilmez.


