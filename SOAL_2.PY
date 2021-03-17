def timeConverter(seconds):
    if seconds > 359999 or seconds < 0:
        print('Invalid Input!')
    elif type(seconds) != int:
        print('Invalid Input!')
    elif seconds <= 359999:
        HH = seconds // 3600
        MM = (seconds % 3600) // 60
        SS = (seconds % 3600) % 60
        print('%d : %d : %d' % (HH, MM, SS))
        return HH and MM and SS

seconds = int(input('Masukkan detik : '))
print(timeConverter(seconds))