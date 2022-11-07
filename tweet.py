import tweepy


#credenciales
auth= tweepy.OAuthHandler("27Wl8ZNkK9XBVsigy2In7OwZ2","XnGG6mdmOxQJSRgWhl4idfUirk1BUAIUI385A6hZwrv73Wrop6")

auth.set_access_token("52285980-I1vRpGSv0atRmJub7ZT5hUqzwiPIHRYjrXp1xPpYI","kK7q9y27seFi8ThXnZzAin3HMI7xp6NZaaTXlKqk39sAL")
apiTweeter=tweepy.API(auth)

#tweet
status = "#salvandoRedes2022IC grupoCarlosMoi"

apiTweeter.update_status(status)
