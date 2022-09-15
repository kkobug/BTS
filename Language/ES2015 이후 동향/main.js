var someone = {
	name: 'sunghyun',
    whoAmI : function() {
        console.log(this);
    }
};

someone.whoAmI();

//someone.whoAmI(); 얘가 호출


// #1
var myWhoAmI = someone.whoAmI;
myWhoAmI();

//myWhoAmI(); 얘가 호출


// #2
// var btn = document.getElementById('btn');
// btn.addEventListener('click', someone.whoAmI);
// btn.addEventListener('click', myWhoAmI);

// btn 이 호출


// 호출한 놈 === this

// #3
//bind 해보자

// var bindedWhoAmI = myWhoAmI.bind(someone);

// var btn = document.getElementById('btn');
// btn.addEventListener('click', bindedWhoAmI);




// #4
// const ssafy = {
//   location: '부울경',
//   func1: function () {
//     console.log(this.location)
//   }
// };

// ssafy.func1();

// #5
const ssafy = {
  location: '부울경',
  func1: function () {
    const func2 = function () {
      console.log(this.location)
    }
    func2();
  }
};

ssafy.func1();

// #6
// const ssafy = {
//   location: '부울경',
//   func1: function () {
//     const func2 = () => {
//       console.log(this.location)
//     }
//     func2();
//   }
// };

// ssafy.func1();

