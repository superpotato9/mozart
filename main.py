with open('data.txt', "r") as input:
    for item in input.readlines():
        print(item)
        with open('song-titles.txt', 'r+' ) as output:
            if item not in output.readlines():
                output.write(item)




