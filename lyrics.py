
import lyr


with open('song-titles.txt', 'r') as file:
    titles_list = file.read().split('\n')
    for title in titles_list:



        lyrics = lyr.lyrics(title)
        if lyrics == None:
            lyrics = ''
        print(titles_list.index(title) , title)

        with open('train.txt', 'a') as train:
             train.write(lyrics)



















