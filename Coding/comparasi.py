 #----0++++5----8++++11----
 #Tugas1
inputUser = float(input("masukkan angka yang berada diantara 0 dan 5 atau diantara 8 dan 11 : "))

# detect angka lebih dari 0
isLebihDari5 = (inputUser > 5)
print ("isLebihDari 5=", isLebihDari5)
# detect angka kurang dari 5
isKurangDari0 = (inputUser < 0)
print ("isKurangDari 0=", isKurangDari0)
# detect angka kurang dari 8
isKurangDari8 = (inputUser <8)
print ("isKurangDari 8=", isKurangDari8)

# detect angka lebih dari 11
isLebihDari11 = (inputUser > 11)
print ("isLebihDari 11=", isLebihDari11)

#hasil
isCorrect = isLebihDari5 and isKurangDari0 or isKurangDari8 and isLebihDari11
print ("angka yang anda masukkan :", isCorrect)

#tugas2
# ++++0----5++++8----11++++
inputUser = float(input("masukan angka sebelum 0 , diantara 5 dan 8, atau setelah 11 "))

iskurangdari0 =  (inputUser <0)
print ("iskurangdari0=", iskurangdari0)

islebihdari5 = (inputUser <5)
print ("iskurangdari5=", islebihdari5)

iskurangdari8 = (inputUser <8)
print ("iskutangdari8=", iskurangdari8)

islebihdari11 = (inputUser >11)
print ("islebihdari11=", islebihdari11)

#hasil
isCorrect = iskurangdari0 and islebihdari5 or iskurangdari8 and islebihdari11
print ("angka yang ada masukkan: ", isCorrect )