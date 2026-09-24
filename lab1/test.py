import os
print(os.getcwd())
startpath = "./lab1"

print("="*30, "Проверим работу сообщения подсказки", "="*30)
os.system(f"python {startpath}/mathtool.py")
os.system(f"python {startpath}/mathtool.py --help")
print("="*30, "Готово!", "="*30)

print("="*30, "Проверим работу основного модуля 'solve'", "="*30)
os.system(f"python {startpath}/mathtool.py da")
print("="*70)
os.system(f"python {startpath}/mathtool.py solve -a 1 -b 2")
print("="*70)
os.system(f"python {startpath}/mathtool.py solve")
print("="*70)
os.system(f"python {startpath}/mathtool.py solve -a 1 -b 2 -c 3")
print("="*70)
os.system(f"python {startpath}/mathtool.py solve -a 1 -b -3 -c 2")
print("="*30, "Готово!", "="*30)
print("="*30, "Все модули успешно простестированы", "="*30)