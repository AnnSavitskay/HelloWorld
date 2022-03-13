import re

st = input().split()
shab = ""
answer = []
for j in st[0]:
    if j == "1":
        shab = shab + "[б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ, ъ, ь]"
    if j == "0":
        shab = shab + "[а, е, ё, и, о, у, ы, э, ю, я]"
    if j == "?":
        shab = shab + "[б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, " \
                      "х, ц, ч, ш, щ, ъ, ь, а, е, ё, и, о, у, ы, э, ю, я]{1}"
    if j == "*":
        shab = shab + "[б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, " \
                      "х, ц, ч, ш, щ, ъ, ь, а, е, ё, и, о, у, ы, э, ю, я]*"

for i in st:
    if re.fullmatch(shab, i):
        answer.append(i)

if not answer:
    print("Есть нечего, значить!")
else:
    print(answer)