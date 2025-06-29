import tweepy
import random
import emoji

# Twitter credentials (fill in your own)
consumer_key = 'm6Zl3vxkHhcLPp2T9agVeQUOn'
consumer_secret = 'lYN0DgHux8fFtHyGWUxwFccAIfbY6jYEoG6WpbNRFqdMy1d7Z3'
access_token = '1853549000906952704-GS0x8hI4jHalztQZ2zhg8SOx4ITJKZ'
access_token_secret = 'HY6CyPraep8GbPkgzGDctRwPHgo6JWyeOXoXbBo8ru6eG'

# Initialize Tweepy Client (v2)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def generate_staircase(left_emoji, right_emoji, height=10):
    lines = []
    for i in range(1, height + 1):
        # Each line alternates left and right emojis i times
        line = ""
        for j in range(i):
            line += left_emoji if j % 2 == 0 else right_emoji
        lines.append(line)
    return "\n".join(lines)

def get_all_emojis():
    # Return a list of all emoji characters supported by emoji package
    return [char for char in emoji.EMOJI_DATA.keys()]

def get_emoji_name(em):
    # Gets emoji name without colons, wrapped in double quotes
    name = emoji.demojize(em).strip(":")
    return f'"{name}"'

def main():
    all_emojis = get_all_emojis()
    left = random.choice(all_emojis)
    right = random.choice(all_emojis)
    while right == left:
        right = random.choice(all_emojis)

    left_name = get_emoji_name(left)
    right_name = get_emoji_name(right)

    staircase = generate_staircase(left, right)

    tweet_text = f"{right_name} and {left_name} staircase\n\n{staircase}"

    try:
        response = client.create_tweet(text=tweet_text)
        print(f"✅ Tweeted:\n{tweet_text}\n🆔 Tweet ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print("❌ Error tweeting:", e)

if __name__ == '__main__':
    main()



