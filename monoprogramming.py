
#Nama Anggota Kelompok 
# 5200411188 - Tarsono
# 5200411187 - Arib Naufal 
# 5200411184 - Way Lilo Tandang Trengginas



RAM = int(input("Berapa RAM Anda (GB): "))
OS = int(input("Berapa OS Anda: (GB)"))
aplikasi = int(input("Aplikasi (GB): "))

# memory os
s = 4056

# Konvert GB to Mbps
mb = 1024

ram = RAM * mb
oes = OS * mb
apk = aplikasi * mb

terpakai = ram - (s + apk)

# Konvert Kbps to GB
convert = terpakai / mb

print("kapasitas tersisa = ",convert,"GB")