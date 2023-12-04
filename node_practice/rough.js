my_object = [{hello: "hey"}]
// console.log(my_object["hello"]);
if ("hello" in my_object){
    console.log("bye exists in my object");
}
else {
    console.log("bye does not exist in my object");
}