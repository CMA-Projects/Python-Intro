score = int(input("Enter your test score (0 to 100): "))

passed = score >= 70
got_perfect = score == 100

if passed:
    print("✅ You passed the test!")
else:
    print("❌ You did not pass. Keep practicing!")

if got_perfect:
    print("🌟 Wow! You got a perfect score!")
