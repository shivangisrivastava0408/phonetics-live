var numberOfDrumButtons = document.querySelectorAll(".drum").length;

for (var i = 0; i < numberOfDrumButtons; i++) {

  document.querySelectorAll(".drum")[i].addEventListener("click", function() {

    var buttonInnerHTML = this.innerHTML;

    makeSound(buttonInnerHTML);

    buttonAnimation(buttonInnerHTML);

  });

}

document.addEventListener("keypress", function(event) {

  makeSound(event.key);

  buttonAnimation(event.key);

});


function makeSound(key) {

  switch (key) {
    case "a":
      var a = new Audio("sounds/a.mp3");
      a.play();
      break;

    case "b":
      var b = new Audio("sounds/b.mp3");
      b.play();
      break;

    case "c":
      var c = new Audio('sounds/c.mp3');
      c.play();
      break;

    case "d":
      var d = new Audio('sounds/d.mp3');
      d.play();
      break;

    case "e":
      var e = new Audio('sounds/e.mp3');
      e.play();
      break;

    case "f":
      var f = new Audio('sounds/f.mp3');
      f.play();
      break;

    case "g":
      var g = new Audio('sounds/g.mp3');
      g.play();
      break;

    case "h":
      var h = new Audio('sounds/h.mp3');
      h.play();
      break;

    case "i":
      var i = new Audio('sounds/i.mp3');
      i.play();
      break;

    case "j":
      var j = new Audio('sounds/j.mp3');
      j.play();
      break;

    case "k":
      var k = new Audio('sounds/k.mp3');
      k.play();
      break;

    case "l":
      var l = new Audio('sounds/l.mp3');
      l.play();
      break;

    case "m":
      var m = new Audio('sounds/m.mp3');
      m.play();
      break;

    case "n":
      var n = new Audio('sounds/n.mp3');
      n.play();
      break;

    case "o":
      var o = new Audio('sounds/o.mp3');
      o.play();
      break;

    case "p":
      var p = new Audio('sounds/p.mp3');
      p.play();
      break;

    case "q":
      var q = new Audio('sounds/q.mp3');
      q.play();
      break;

    case "r":
      var r = new Audio('sounds/r.mp3');
      r.play();
      break;

    case "s":
      var s = new Audio('sounds/s.mp3');
      s.play();
      break;

    case "t":
      var t = new Audio('sounds/t.mp3');
      t.play();
      break;

    case "u":
      var u = new Audio('sounds/u.mp3');
      u.play();
      break;

    case "v":
      var v = new Audio('sounds/v.mp3');
      v.play();
      break;

    case "w":
      var w = new Audio('sounds/w.mp3');
      w.play();
      break;

    case "x":
      var x = new Audio('sounds/x.mp3');
      x.play();
      break;

    case "y":
      var y = new Audio('sounds/y.mp3');
      y.play();
      break;

    case "z":
      var z = new Audio('sounds/z.mp3');
      z.play();
      break;

    default: console.log(key);

  }
}


function buttonAnimation(currentKey) {

  var activeButton = document.querySelector("." + currentKey);

  activeButton.classList.add("pressed");

  setTimeout(function() {
    activeButton.classList.remove("pressed");
  }, 100);

}
