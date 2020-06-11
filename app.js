'use strict';
//argv[2]なのは標準入力の値が2から入るため
const number = process.argv[2] || 0;
let sum = 0;
for (let i = 1; i <= number; i++) {
  sum = sum + i;
}
console.log(sum);
//0 番には node コマンドのファイルのパス
console.log(process.argv[0]);
//1 番には実行しているプログラムのファイルのパス
console.log(process.argv[1]);