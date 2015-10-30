import guesses
import songs
import loader


def print_first_lines(collection, amount):
    for i in range(amount):
        print(collection[i])


def shuffle_and_print_first_lines(song):
    print()
    print_first_lines(songs.get_shifted_lyrics(song), 2)
    print()


def print_song_artist_and_title(song):
    print("That was", song.title, "by", song.artist + ".")


def check_if_user_wants_to_play():
    positive_answers = ("y", "Y") #changed to simple Y/N answers
    negative_answers = ("n", "N")
    while True:
        answer = input("Do you want to play again? [Y/N] ") #Added hint for input
        if answer in positive_answers:
            return True
        elif answer in negative_answers:
            answer = input("Are you sure you want to quit? [Y/N]") #Added double check for quitting
            if answer in positive_answers:
                return False
            else:
                return True
        else:
            print("I don't understand that. Please use one of the following:")
            print(" ", " ".join(positive_answers + negative_answers))


def ask_for_guesses():
    title = input("Guess the song's title: ")
    artist = input("Guess the song's artist: ")
    return guesses.Guess(title, artist)


def mainloop():
    while True:
        random_song = songs.Song(**loader.get_random_song())
        shuffle_and_print_first_lines(random_song)
        user_guesses = ask_for_guesses()
        if user_guesses.check_title(random_song) and user_guesses.check_artist(random_song):
            print("You got everything right.")
        elif user_guesses.check_title(random_song):
            print("You only got the title right.")
        elif user_guesses.check_artist(random_song):
            print("You only got the artist right.")
        else:
            print("You are wrong.")
        print_song_artist_and_title(random_song)
        if not check_if_user_wants_to_play():
            break


if __name__ == '__main__':
    mainloop()
