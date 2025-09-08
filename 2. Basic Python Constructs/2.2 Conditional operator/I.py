fir_name = input()
sec_name = input()
thr_name = input()

if fir_name < sec_name and fir_name < thr_name:
    print(fir_name)
if sec_name < fir_name and sec_name < thr_name:
    print(sec_name)
if thr_name < fir_name and thr_name < sec_name:
    print(thr_name)