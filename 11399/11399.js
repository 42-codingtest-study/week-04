const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const n = input[0];
  let result = 0;
  const data = input[1]
    .split(" ")
    .map((v) => +v)
    .sort((a, b) => a - b);

  for (let i = 0; i < n; i++) {
    result += data[i] * (n - i);
  }
  console.log(result);
}
