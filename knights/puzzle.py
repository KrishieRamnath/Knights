from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),                # A must be either a knight or a knave, not both
    Not(And(AKnight, AKnave)),          # A cannot be both a knight and a knave
    Implication(AKnight, And(AKnight, AKnave))  # If A is a knight, then the statement "I am both" must be true
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a knight, they both must be knaves
    Implication(AKnave, Or(AKnight, BKnight))   # If A is a knave, at least one is a knight
)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    # A and B are either both knights or both knaves
    Biconditional(AKnight, BKnight),

    # If A is a knight, then they are the same kind as B (which A claims)
    Implication(AKnight, Biconditional(AKnight, BKnight)),

    # If B is a knight, then A and B are of different kinds (which B claims)
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),

    # A and B cannot both be knights or both be knaves due to contradiction
    Or(And(AKnight, BKnave), And(AKnave, BKnight))
)





# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Each character is either a knight or a knave, not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnight),
    Not(And(CKnight, CKnight)),

    # A makes an ambiguous statement, so no strong assertion here
    # B claims A said "I am a knave", implying:
    Implication(BKnight, Biconditional(AKnight, AKnave)),

    # B says "C is a knave"
    Implication(BKnight, CKnave),

    # C claims "A is a knight"
    Implication(CKnight, AKnight)
)






def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
