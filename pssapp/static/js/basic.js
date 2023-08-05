$('.nav-item.dropdown').mouseover(function(){
    $(this).find('.dropdown-menu').css("display","block")
})
$('.nav-item.dropdown').mouseout(function(){
    $(this).find('.dropdown-menu').css("display","none")
})
$('#GoToContactButton').click(function(){
    window.location.href = '/pssapp/contact/';
})