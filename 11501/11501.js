const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let t = input[0] * 1;
  for (let i = 0; i < t; i++) {
    let n = input[2 * i + 1] * 1;
    let arr = input[2 * (i + 1)].split(" ").map((e) => e * 1);
    let result = 0;

    let maxPrice = arr[arr.length - 1];
    for (let j = arr.length - 1; j >= 0; j--) {
      if (arr[j] >= maxPrice) {
        maxPrice = arr[j];
      } else if (arr[j] < maxPrice) {
        result += maxPrice - arr[j];
      }
    }
    console.log(result);
    // 원래 이렇게 풀었다가 시간 초과 나서 맨뒤에서 부터 계산하는 방식으러 바꿈
    // while (arr[0]) {
    //   if (arr[0] === Math.max(...arr) || arr.length === 1) {
    //     result += arr[0] * stock_num;
    //     stock_num = 0;
    //   } else if (arr[0] < Math.max(...arr)) {
    //     result -= arr[0];
    //     stock_num += 1;
    //   }
    //   arr.splice(0, 1);
    //   //   console.log(arr, result, stock_num);
    // }
    // result > 0 ? console.log(result) : console.log(0);
  }
}
