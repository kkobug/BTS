export default function Closure() {
  const test1 = () =>{
    var a = 0
    return () => {
      console.log(++a)
    };
  }

  var test3 = test1()
  

  return (
    <div>
      <button onClick={test3}>더하기</button>
    </div>
  );
}