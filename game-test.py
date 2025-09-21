# simple fill-in-the-gap quiz

import random

# ==============================
# QUIZ DATA
# ==============================
levels = {
    "Level 1": {
        "Blockchain is a ______ ledger.": "distributed",
        "Ethereum’s native token is called ______.": "ether",
        "A collection of NFTs is often stored on ______.": "ipfs",
    },
    "Level 2": {
        "The consensus mechanism Bitcoin uses is called ______ of Work.": "proof",
        "Smart contracts run on the ______ Virtual Machine.": "ethereum",
        "Gas fees on Polygon are paid in ______.": "matic",
    },
    "Level 3": {
        "Solana is famous for high ______ transactions per second.": "throughput",
        "Layer 2 solutions help Ethereum scale by reducing ______.": "congestion",
        "DAO stands for Decentralized ______ Organization.": "autonomous",
    }
}

# Hidden phrase to reveal (word by word)
secret_phrase = "Knowledge unlocks the future of Web3"

# Track revealed words
revealed_words = ["_" * len(word) for word in secret_phrase.split()]

# ==============================
# GAME LOOP
# ==============================
print("🧩 Welcome to the Web3 Fill-in-the-Gap Quiz!")
print("Answer correctly to reveal the hidden phrase:\n")

for level_name, questions in levels.items():
    print(f"\n🔓 {level_name} Unlocked! Answer the questions:\n")
    for q, ans in questions.items():
        print(q)
        user_input = input("Your answer: ").strip().lower()

        if user_input == ans:
            print("✅ Correct!")
            # Reveal one word of the secret phrase
            for i in range(len(revealed_words)):
                if "_" in revealed_words[i]:
                    revealed_words[i] = secret_phrase.split()[i]
                    break
            print("🔑 Revealed so far:", " ".join(revealed_words), "\n")
        else:
            print(f"❌ Wrong! The correct answer was '{ans}'.\n")

print("\n🎉 Game Over!")
print("✨ Final Secret Message:", secret_phrase)
