import chess
import chess.engine

def play_chess():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Enter your move: ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move. Try again.")
                continue
        else:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            print(f"Computer plays: {result.move}")
    
    print("Game over!")
    print("Result: ", board.result())
    engine.quit()

if __name__ == "__main__":
    play_chess()
