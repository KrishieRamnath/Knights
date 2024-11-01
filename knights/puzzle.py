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
    # A can only be a knight or a knave
    Or(AKnight, AKnave),
    
    # B can only be a knight or a knave
    Or(BKnight, BKnave),
    
    # C can only be a knight or a knave
    Or(CKnight, CKnave),
    
    # Ensure that A cannot be both a knight and a knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    
    # B says "A said 'I am a knave'"
    Implication(BKnight, AKnave),  # If B is a knight, then A must be a knave
    Implication(BKnave, AKnight),   # If B is a knave, then A cannot be a knave (hence must be a knight)
    
    # B also says "C is a knave"
    Implication(BKnight, CKnave),   # If B is a knight, then C must be a knave
    Implication(BKnave, CKnight),    # If B is a knave, then C cannot be a knave (hence must be a knight)
    
    # C says "A is a knight"
    Implication(CKnight, AKnight),   # If C is a knight, then A must be a knight
    Implication(CKnave, AKnave)      # If C is a knave, then A cannot be a knight
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
