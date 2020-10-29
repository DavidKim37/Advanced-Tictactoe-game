from movepiece1 import *
from printboard import *

board = {
    "Aa3": "   ", "Ab3": "   ", "Ac3": "   ", "Ba3": "   ", "Bb3": "   ", "Bc3": "   ",
    "Ca3": "   ", "Cb3": "   ", "Cc3": "   ",
    "Aa2": "   ", "Ab2": " A ", "Ac2": "   ", "Ba2": "   ", "Bb2": " B ", "Bc2": "   ",
    "Ca2": "   ", "Cb2": " C ", "Cc2": "   ",
    "Aa1": "   ", "Ab1": "   ", "Ac1": "   ", "Ba1": "   ", "Bb1": "   ", "Bc1": "   ",
    "Ca1": "   ", "Cb1": "   ", "Cc1": "   ",
    "Da3": "   ", "Db3": "   ", "Dc3": "   ", "Ea3": "   ", "Eb3": "   ", "Ec3": "   ",
    "Fa3": "   ", "Fb3": "   ", "Fc3": "   ",
    "Da2": "   ", "Db2": " D ", "Dc2": "   ", "Ea2": "   ", "Eb2": " E ", "Ec2": "   ",
    "Fa2": "   ", "Fb2": " F ", "Fc2": "   ",
    "Da1": "   ", "Db1": "   ", "Dc1": "   ", "Ea1": "   ", "Eb1": "   ", "Ec1": "   ",
    "Fa1": "   ", "Fb1": "   ", "Fc1": "   ",
    "Ga3": "   ", "Gb3": "   ", "Gc3": "   ", "Ha3": "   ", "Hb3": "   ", "Hc3": "   ",
    "Ia3": "   ", "Ib3": "   ", "Ic3": "   ",
    "Ga2": "   ", "Gb2": " G ", "Gc2": "   ", "Ha2": "   ", "Hb2": " H ", "Hc2": "   ",
    "Ia2": "   ", "Ib2": " I ", "Ic2": "   ",
    "Ga1": "   ", "Gb1": "   ", "Gc1": "   ", "Ha1": "   ", "Hb1": "   ", "Hc1": "   ",
    "Ia1": "   ", "Ib1": "   ", "Ic1": "   ",
}

boardA = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardB = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardC = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardD = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardE = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardF = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardG = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardH = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boardI = {"a3": " ", "b3": " ", "c3": " ", "a2": " ", "b2": " ", "c2": " ", "a1": " ", "b1": " ", "c1": " "}
boards = [boardA, boardB, boardC, boardD, boardE, boardF, boardG, boardH, boardI]
dictionary = {"a3": "A", "b3": "B", "c3": "C", "a2": "D", "b2": "E", "c2": "F", "a1": "G", "b1": "H", "c1": "I"}

gameend = False
player = "X"
playboard = "0"
validmove1 = False
currentblock = ""
dictio = {"a3": "A", "b3": "B", "c3": "C", "a2": "D", "b2": "E", "c2": "F", "a1": "G", "b1": "H", "c1": "I"}
dead = []

# for letter in open(rules.txt)

start = input("Press Enter to start")

exec(open("printboard.py").read())
printboard(board, "", [])
exec(open("movepiece1.py").read())
movepiece(currentblock, dead, board, player, dictio, boards, "\u001B[41m")
