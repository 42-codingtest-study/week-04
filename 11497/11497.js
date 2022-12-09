const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = input[0] * 1;
  for (let i = 0; i < n; i++) {
    let m = input[i * 2 + 1];
    const arr = input[i * 2 + 2]
      .split(" ")
      .map((e) => e * 1)
      .sort((a, b) => b - a);
    // console.log(arr);
    const resultArr = [];
    arr.forEach((e, idx) => {
      idx % 2 === 0 ? resultArr.push(e) : resultArr.splice(0, 0, e);
    });
    let result = resultArr[1] - resultArr[0];
    resultArr.forEach((e, idx) => {
      let temp;
      if (idx !== resultArr.length - 1) {
        e >= resultArr[idx + 1]
          ? (temp = e - resultArr[idx + 1])
          : (temp = resultArr[idx + 1] - e);
      } else {
        e >= resultArr[0]
          ? (temp = e - resultArr[0])
          : (temp = resultArr[0] - e);
      }
      if (temp > result) result = temp;
    });
    console.log(result);
  }
}
