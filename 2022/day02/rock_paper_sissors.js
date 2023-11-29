const fs = require("fs");

fs.readFile("input.txt", "utf8", (err, data) => {
  let splitData = data.split("\r\n");

  scoreRounds(splitData);
  findShape(splitData);
});

// A = rock, B = paper, C = sissors
// X = loss, Y = tie,   Z = win
// rock = 1, paper = 2, sissors = 3

//part two
const findShape = (data) => {
  const roundScore = {
    loss: 0,
    tie: 3,
    win: 6,
  };
  const shapeScore = {
    rock: 1,
    paper: 2,
    sissors: 3,
  };
  // value returns an object containing:
  // the desired outcome: 'loss' | 'tie' | 'win'
  // and shape that fulfills the outcome 'rock' | 'paper' | 'sissors'
  const scoreSheet = {
    "A X": {outcome: "loss", shape: "sissors"},
    "A Y": {outcome: "tie", shape: "rock"},
    "A Z": {outcome: "win", shape: "paper"},
    "B X": {outcome: "loss", shape: "rock"},
    "B Y": {outcome: "tie", shape: "paper"},
    "B Z": {outcome: "win", shape: "sissors"},
    "C X": {outcome: "loss", shape: "paper"},
    "C Y": {outcome: "tie", shape: "sissors"},
    "C Z": {outcome: "win", shape: "rock"},
  };
  let sum = 0;
  // sum scores using a double dictionary map
  for (const round of data) {
    sum +=
      roundScore[scoreSheet[round].outcome] +
      shapeScore[scoreSheet[round].shape];
  }

  // get result
  console.log(sum);
};

// A, X = rock, B, Y = paper, C, Z = sissors
//    X = 1,       Y = 2,        Z = 3
// loss = 0,     tie = 3,      win = 6

// part one
const scoreRounds = (data) => {
  // dictionary of outcomes and scores
  const scoreSheet = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
  };

  let score = 0;
  // sum scores
  for (const round of data) {
    score += scoreSheet[round];
  }

  // get result
  console.log(`part 1 score: ${score}`);
};
