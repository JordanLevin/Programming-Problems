import System.IO
import Data.List

data Board = Board 
            ((Char, Char, Char),
            (Char, Char, Char),
            (Char, Char, Char))

main = do
    let board = Board ((' ',' ',' '),(' ',' ',' '),(' ',' ',' '))
    turn board

turn :: Board -> Int -> Board
turn board count= do
    putStrLn "Enter coordinates"
    x <- getLine
    y <- getLine
    board

    
