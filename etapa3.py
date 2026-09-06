tempo_sequencial = float(input("Digite o tempo sequencial (T1): "))

tempo_2 = float(input("Digite o tempo com 2 processos: "))
tempo_4 = float(input("Digite o tempo com 4 processos: "))
tempo_8 = float(input("Digite o tempo com 8 processos: "))


speedup_2 = tempo_sequencial / tempo_2
eficiencia_2 = speedup_2 / 2

speedup_4 = tempo_sequencial / tempo_4
eficiencia_4 = speedup_4 / 4

speedup_8 = tempo_sequencial / tempo_8
eficiencia_8 = speedup_8 / 8


print("\nRESULTADOS")

print("\n2 processos")
print("Speedup:", speedup_2)
print("Eficiência:", eficiencia_2)

print("\n4 processos")
print("Speedup:", speedup_4)
print("Eficiência:", eficiencia_4)

print("\n8 processos")
print("Speedup:", speedup_8)
print("Eficiência:", eficiencia_8)