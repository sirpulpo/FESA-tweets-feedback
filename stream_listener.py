from tweepy import StreamListener


class FiniteStreamListener(StreamListener):
    
    def __init__(self, number_of_tweets):
        self.number_of_tweets = number_of_tweets
        self.tweets = []
        super().__init__()
        
    # aquí se define la lógica que ocurrira cada que se reciba un nuevo tweet.
    # aquí mismo se podría implementar la limpieza de los datos.
    def on_status(self, status):
        if len(self.tweets) < self.number_of_tweets:
            self.tweets.append(status.text)
        else:
            return False
