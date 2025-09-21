# simple fill-in-the-gap quiz

quiz = {
    "Blockchain is a ______ ledger.": "distributed",
    "Ethereum’s native token is called ______.": "ether",
    "A collection of NFTs is often stored on ______.": "ipfs",
}

print("🧩 Fill in the Gap Quiz!")
print("Type your answer (lowercase). Let's begin!\n")

for question, answer in quiz.items():
    print(question)
    user_input = input("Your answer: ").strip().lower()
    
    if user_input == answer:
        print("✅ Correct! Revealing: 🎉 You unlocked the clue!\n")
    else:
        print(f"❌ Oops! The correct answer was '{answer}'.\n")

print("Game Over! Thanks for playing ✨")
