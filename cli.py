import pexpect

# Jalankan program CLI yang akan diisi input
child = pexpect.spawn('python3 bot.py', encoding='utf-8')

# Tunggu muncul prompt, kirim "1"
child.expect('Pilih modul yang ingin dijalankan (pisahkan dengan koma, misal: 1,2,3).')
child.sendline('1,2,5')

# Tunggu prompt berikutnya, kirim "2"
child.expect('Masukkan pilihan:')
child.sendline('50')

# Tunggu program selesai
child.expect(pexpect.EOF)
print(child.before)  # Tampilkan hasil
