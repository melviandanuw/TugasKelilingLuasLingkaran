import math;

print("""
█▀▄▀█ █▀▀ █░░ █░█ █ ▄▀█ █▄░█   █▀▄ ▄▀█ █▄░█ █░█   █░█░█ █ ░░█ ▄▀█ █▄█ ▄▀█
█░▀░█ ██▄ █▄▄ ▀▄▀ █ █▀█ █░▀█   █▄▀ █▀█ █░▀█ █▄█   ▀▄▀▄▀ █ █▄█ █▀█ ░█░ █▀█

▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄
░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n""");

jari = int(input('Masukan jari-jari:\n'));

rumusKeliling = 2 * math.pi * jari;
rumusLuas = jari ** 2 * math.pi;

print('Keliling Lingkaran adalah ', rumusKeliling);
print('Luas Lingkaran adalah ', rumusLuas);
