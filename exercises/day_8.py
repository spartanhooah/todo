heads = 0
tails = 0

while True:
    result = input("Throw the coin and enter heads or tails here: ? ")

    match result.lower():
        case 'heads':
            heads += 1
        case 'tails':
            tails += 1

    print(f"Heads: {heads / (heads + tails) * 100}%")
