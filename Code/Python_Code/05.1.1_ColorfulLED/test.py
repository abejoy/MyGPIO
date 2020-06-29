from matplotlib import colors

while True:
    color_info = colors.to_rgba(input('type color: '))
    print(color_info)
    print(int(round(color_info[0]*100)))
