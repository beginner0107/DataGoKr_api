//JSON 데이터를 다루기위한 JS 기본 사용법2

// [1] : 데이터
const person = [
	{"name":"홍길동","age":20,"nationality":"대한민국"},
	{"name":"이순신","age":30,"nationality":"미국"},
	{"name":"강감찬","age":40,"nationality":"영국"},
	{"name":"을지문덕","age":50,"nationality":"프랑스"},
];

console.log(typeof person[0]); //object 요소 체크

// [2] : 출력
console.log('------------------------------------');
console.log(person[0].name+" "+person[0].age+" "+person[0].nationality);

// [3] : 반복
console.log('------------------------------------전개 연산자');
const str1 = "korea";
console.log([...str1]); // _proto__ --> Array
console.log({...str1}); // _proto__ --> Object
// __proto__ : (부모가 누구니?, 너를 만들 수 있게 해준 원형이 누구니?)


console.log(...person); // 전개 연산자 (반복이 가능한 객체)
console.log({...person}); // _proto__ --> Object
console.log([...person]); // _proto__ --> Array

console.log([...person].length); // 4

console.log([...person][0].name); // 홍길동
console.log([...person][3].name); // 을지문덕

console.log([...person][3].age); // 50
console.log({...person}[1].name); // 이순신

// [4] : 반복 가능한 객체 --> for..of, ...(전개 연산자)
console.log('--------------------------------for ..of');
for(let ele of person){ // person --> iterable 즉, 반복 가능한 객체가 오면 된다.
	console.log(ele);
}

// [5] : 수정
console.log('--------------------------------역따옴표');
person[0].name='홍길자';
person[0].age=22;
console.log(`홍길동의 이름이 ${person[0].name}로 수정되었고, 나이는 ${person[0].age}살로 수정되었습니다.`);