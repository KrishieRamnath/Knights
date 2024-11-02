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
    # A and B are mutually exclusive in their knighthood/knavehood
    Or(And(AKnight, BKnave), And(AKnave, BKnight)),

    # A says "We are the same kind"
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),

    # B says "We are of different kinds"
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
    Implication(BKnave, Biconditional(AKnight, BKnight))
)






# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Each character is either a knight or a knave (not both)
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),

    # Statements from the puzzle:
    # A's ambiguous statement: "I am a knight or I am a knave." (we don’t know which)
    Biconditional(AKnight, Or(AKnight, AKnave)),  # This makes A consistent with a truthful statement

    # B's first statement: "A said 'I am a knave'"
    Implication(BKnight, AKnave),  # If B is a knight, then A said they are a knave
    Implication(BKnave, AKnight),  # If B is a knave, then A is actually a knight

    # B's second statement: "C is a knave"
    Implication(BKnight, CKnave),  # If B is a knight, then C is indeed a knave
    Implication(BKnave, CKnight),  # If B is a knave, then C must be a knight

    # C's statement: "A is a knight"
    Implication(CKnight, AKnight),  # If C is telling the truth, then A must be a knight
    Implication(CKnave, AKnave),    # If C is lying, then A is a knave

    # Cross-references to reinforce deductions
    # Ensures that if B's statement is true, it aligns with both B and C’s statements.
    Implication(And(BKnight, CKnave), AKnave),   # If B and C's statements align on A being a knave, enforce this
    Implication(And(CKnight, BKnave), AKnight)   # If C and B’s statements imply A is a knight, enforce this
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
