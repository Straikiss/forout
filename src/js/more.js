$(function(){
    $(".section-more").slice(0,16).show(),$("#load").click(function(e){
        e.preventDefault(),$(".section-more:hidden").slice(0,100).show(),0==$(".section-more:hidden").length&&$("#load").hide()
    })
});