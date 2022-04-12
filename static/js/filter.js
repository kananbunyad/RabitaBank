function resetfunc() {
  var element = document.getElementsByClassName("test");
  for (let i = 0; i < element.length; i++) {
    element[i].classList.remove("active")
    // console.log(element[i])
  }
}



$('#all').click(function(){
    $('.cardlist').hide().show()
    resetfunc()
    $('#all').addClass("active")
  })
  
  $('#kredit').click(function(){
    $('.cardlist').hide()
    $('.kredit').show()
    resetfunc()
    $('#kredit').addClass("active")
  })
  
  $('#emanet').click(function(){
    $('.cardlist').hide()
    $('.emanet').show()
    resetfunc()
    $('#emanet').addClass("active")
  })
  
  $('#emlak').click(function(){
    $('.cardlist').hide()
    $('.emlak').show()
    resetfunc()
    $('#emlak').addClass("active")
  })
  
  $('#biznes').click(function(){
    $('.cardlist').hide()
    $('.biznes').show()
    resetfunc()
    $('#biznes').addClass("active")
  })
  
  $('#tikinti').click(function(){
    $('.cardlist').hide()
    $('.tikinti').show()
    resetfunc()
    $('#tikinti').addClass("active")
  })
  
  $('#neqliyyat').click(function(){
    $('.cardlist').hide()
    $('.neqliyyat').show()
    resetfunc()
    $('#neqliyyat').addClass("active")
  })
  
  $('#kart').click(function(){
    $('.cardlist').hide()
    $('.kart').show()
    resetfunc()
    $('#kart').addClass("active")
  })

