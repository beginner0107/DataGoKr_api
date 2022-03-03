// JSON 데이터 객체와 문자열로 변환하기
// JSON.parse() - JSON 데이터를 객체로, 문자열로 되어 있는 JSON데이터를 받아 객체로
// JSON.stringify() --> classify : 분류하다, 구분하다. 객체를 문자열로 변환

// [1] : JSON.parse(jsonText) --> JSON 형식의 텍스트 --> 자바스크립트 객체로 변환
 let jsonText='{"name":"홍길동","age":20,"nationality":"대한민국"}';

// console.log("변환전-->" + typeof jsonText); // string

// let jsonText={"name":"홍길동","age":20,"nationality":"대한민국"};

console.log("변환전-->" + typeof jsonText); // String
const jsonObj=JSON.parse(jsonText);
console.log("변환후-->" + typeof jsonObj); // Object

console.log('----------------------------------------');
// console.log(jsonObj.name); // 홍길동
// console.log(jsonObj.age); // 20
// console.log(jsonObj.nationality); // 대한민국

// console.log(jsonObj.name+""+jsonObj.age+""+jsonObj.nationality);
console.log(`이름과 나이는 ${jsonObj.name}(${jsonObj.age})이며 국적은 ${jsonObj.nationality}이다`);

// [2] : JSON.stringify(dataObj) --> 데이터 객체를 --> JSON 형식의 텍스트로 변환.
console.log('-----------------------------------------------');
const jsonStr=JSON.stringify(jsonObj); //객체를 JSON 형식의 텍스트로 변환

console.log(jsonStr);
console.log(typeof jsonStr); //string