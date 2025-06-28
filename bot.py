import tweepy
import random
import emoji

# Twitter credentials (fill in your own)
consumer_key = 'sK7YeAis3LbNSK2wRzqMFEXCK'
consumer_secret = 'kTLn8HSHwMBdAO6PFArcJDRrDHgzxMK1fJ1RgPtsIuiJq1t5TL'
access_token = '1938981766104072192-5aIFTs7EdXNEYMPMFVXSiDeRjVR366'
access_token_secret = 'CE7KbykD8W9msVe8Brp16gIyKqCeuOrstfMLTqhgKNvET'

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



