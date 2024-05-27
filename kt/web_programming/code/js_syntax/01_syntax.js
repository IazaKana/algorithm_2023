// Javascript
// 웹브라우저에서 이벤트를 처리하는 문법

var data1 = 10;
var data2 = "js";

var data3 = 20,
  data4 = "node";
var data3 = 20,
  data4 = "node";

var data5 = (data6 = "web");

console.log(data1, data2, data3, data4, data5, data6);

// 2. 데이터타입
// number, string, boolean, function, object
// 동적타이핑 : 데이터타입 선언 없이 자동으로 데이터타입 정의
var data1 = 1;
var data2 = "js";
var data3 = true;
var data4 = function () {
  console.log("js");
};
var data5 = { key: "js" };

// let, const

console.log(typeof data1, typeof data2, typeof data3);
console.log(typeof data4, typeof data5);

// 데이터가 없음
// undefined : 선언은 되었으나 데이터가 할당 X
// null : 선언은 되었으나 데이터 없음이 할당
// NaN : Number 데이터 타입에서 undefined
var data1 = undefined;
var data2 = null;
var data3 = NaN;
console.log(typeof data1, data1);
console.log(typeof data2, data2);
console.log(typeof data3, data3);

console.log(NaN == NaN);

// 데이터 타입의 형변환
// Number(), String(), Boolean()
var data1 = "1";
var data2 = 2;
console.log(typeof data1, typeof Number(data1));
console.log(data1 + data2);
console.log(Number(data1) + data2);
console.log(data1 + String(data2));

// 묵시적 형변환 : 서로 다른 데이터타입을 연산할 때 데이터 타입을 변경
var data1 = "1";
var data2 = 2;
console.log(typeof data1, typeof (data1 - 0));
console.log(typeof data2, typeof ("" + data2));

// 3. 연산자 : operator
// 산술 : 데이터 + 데이터 = 데이터 : +, -, *, /, %, **, ++, --
// 비교 : 데이터 + 데이터 = 논리값 : 조건 1개 : ==, !=, >, <, >=, <=, ===, !== -> 3개 짜리는 데이터 타입까지 비교
// 논리 : 논리값(조건1) + 논리값(조건2) = 논리값 : 조건 2개 이상 : !(not), &&(and), ||(or)
// 할당 : 변수 <산술>=데이터 : 누적해서 연산
// 삼항 : true if condition else false (python) : condition ? true : false (javascript)

// 산술
var data1 = 11,
  data2 = 4;
console.log(data1 / data2, data1 % data2, data2 ** 3);
// ++data1 : +1 하고 데이터 대입

// data1++ : 데이터 대입하고 +1

// 비교연산자 : ===(데이터, 데이터타입까지 비교), ==(데이터만비교)

// 논리연산자 : !, &&(and: T and T = T), ||(or: F or F = F)
console.log(true && false, true || false);

// 비교 : 조건 1개
// 논리 : 조건 2개 이상
// 예금잔고에서 예금인출이 가능하면 true, 아니면 false
// 조건 1 : 예금잔고 >= 인출금액
var balance = 10000;
var amount = 6000;
console.log(balance >= amount);

// 조건 2 : 최대 인출금액 5000원
var balance = 10000;
var amount = 6000;
console.log(balance >= amount, amount <= 5000);
console.log(balance >= amount && amount <= 5000);

// 할당연산자
var data1 = 10;
data1 += 20;
console.log(data1);

// 삼항연산자 : 조건 ? 참 : 거짓
var balance = 10000,
  amount = 16000;
var msg = balance >= amount ? "인출가능" : "인출불가";
console.log(msg);

// 실수하기 쉬운 코드 : 부동소수점 에러 -> 주로 반올림을 해서 처리
var data1 = 0.1,
  data2 = 0.2;
console.log(data1 + data2 === 0.3);
console.log(data1 + data2);
console.log(Math.round((data1 + data2) * 10) / 10 === 0.3);

// 4. 조건문
// if, else if, else
var balance = 10000,
  amount = 16000;
if (balance < amount) {
  console.log("인출불가");
} else {
  console.log("인출가능");
}

function showLotto(count) {
  var lotto = "";
  for (var i = 0; i < count; i++) {
    var rnum = Math.floor(Math.random() * 50) + 1;
    lotto = lotto + rnum + " ";
  }
  console.log(lotto);
}
console.log(typeof showLotto);

// 함수선언 방법 1 : 선언식
function plus1(n1, n2) {
  console.log(n1 + n2);
}
plus1(1, 2);

// 함수선언 방법 2 : 표현식
var plus2 = function (n1, n2) {
  console.log(n1 + n2);
};
plus2(2, 3);

// 표현식은 함수를 선언해야 함수 호출이 가능

// 선언식은 함수를 호출하고 선언해서 사용 가능 : 호이스팅

// 스코프
// 함수안 : 지역영역 : 지역변수 : local
// 함수밖 : 전역영역 : 전역변수 : global

var data = 10;
function change() {
  data = 20; // var 사용하지 않으면 global 변수
}
change();
console.log(data);

// return
function plus1(n1, n2) {
  console.log("plus1", n1 + n2);
  return n1 + n2;
}
function plus2(n1, n2) {
  console.log("plus2", n1 + n2);
}
result1 = plus1(2, 3);
result2 = plus2(2, 3);
console.log(result1, result2);

// 익명함수 : 선언과 동시에 호출하는 함수
// 자바스크립트 코드를 웹서비스 사용자가 사용할 수 없도록 하기 위해 사용
function plus1(n1, n2) {
  console.log(n1 + n2);
}
plus1(2, 3);

(function plus1(n1, n2) {
  console.log(n1 + n2);
})(2, 3);
plus1(2, 3);

// default parameter 설정
var plus = function (n1, n2) {
  console.log(n1, n2);
  n2 = n2 || 10; // 결측 데이터면 뒤의 숫자를 사용 아니면 앞의 것을 사용
  return n1 + n2;
};
result = plus(1, 2);
console.log(result);

// 7. 객체 : object
// Array : 배열
var data = [1, 2, 3, "A", "B"];
console.log(typeof data, data);
// 데이터추가 : push()
data.push("C");
console.log(data);
console.log(data[3]);
for (var i = 0; i < data.length; i++) {
  console.log(i, data[i]);
}

// 객체 생성 1(선호)
var data = {
  name: "andy",
  plus: function (n1, n2) {
    return n1 + n2;
  },
};
console.log(typeof data, data);
console.log(data.name, data["name"]);

// 객체 생성 2
function Person(name) {
  this.name = name;
}
var person = new Person("andy");
console.log(typeof person, person);

// 변수 추가
var data = {};
data.name = "alice";
data["age"] = 23;
console.log(data);
delete data.age;
console.log(data);

// json object : 웹에서 데이터를 주고 받는 용도로 사용되는 데이터 포멧
// 웹에서는 객체 자제사용이 불가능
// 클라이언트에서 서버로 데이터를 보낼때 str형식으로 바뀌어서 보내지기 때문에
// json object > str
var data = { name: "peter", age: 29, skills: ["code", "read"] };
var json_str = JSON.stringify(data);
console.log(typeof data, typeof json_str);
console.log(data, json_str);
// str > json object
var json_obj = JSON.parse(json_str);
console.log(typeof json_obj, json_obj, json_obj.name);

// 웹브라우저 객체
// window   : 전역객체 : 모든 변수와 함수와 객체를 저장하는 객체
// location : URL 데이터를 저장하는 객체
// document : 페이지 문서(HTML)에 대한 데이터를 저장하는 객체
