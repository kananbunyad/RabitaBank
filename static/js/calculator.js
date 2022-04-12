function resetfunc() {
    var element = document.getElementsByClassName("test");
    for (let i = 0; i < element.length; i++) {
      element[i].classList.remove("active")
      // console.log(element[i])
    }
  }


$('#mehsul').click(function(){
    $('.sigorta').hide()
    $('.mehsul').show()
    resetfunc()
    $('#mehsul').addClass("active")
  })

$('#sigorta').click(function(){
    $('.mehsul').hide()
    $('.sigorta').show()
    resetfunc()
    $('#sigorta').addClass("active")
  })