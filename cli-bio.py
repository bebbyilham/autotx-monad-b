import pexpect

# Jalankan bot.py
child = pexpect.spawn('python3 bot.py', encoding='utf-8')

# Tunggu sampai muncul prompt input modul
child.expect('Masukkan nomor modul.*:')
child.sendline('3,5,7')  # pilih modul ke-1, misalnya

# Tunggu sampai muncul prompt input loop
child.expect('Berapa kali.*:')
child.sendline('50')  # jalankan 2 kali

# Tunggu hingga selesai
child.expect(pexpect.EOF)
print(child.before)
